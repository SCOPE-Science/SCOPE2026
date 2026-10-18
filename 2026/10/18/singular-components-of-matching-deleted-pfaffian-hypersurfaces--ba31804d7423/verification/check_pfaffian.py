#!/usr/bin/env python3
"""Deterministic exact finite-field checks for sparse alternating Pfaffian hypersurfaces."""
from functools import lru_cache
from random import Random

P=101
R=Random(20261013)

def rank(M):
    a=[[x%P for x in row] for row in M]
    if not a:return 0
    n=len(a);m=len(a[0]);t=0
    for c in range(m):
        pivot=next((i for i in range(t,n) if a[i][c]),None)
        if pivot is None:continue
        a[t],a[pivot]=a[pivot],a[t]
        u=pow(a[t][c],-1,P)
        a[t]=[(x*u)%P for x in a[t]]
        for i in range(n):
            if i!=t and a[i][c]:
                d=a[i][c]
                a[i]=[(v-d*w)%P for v,w in zip(a[i],a[t])]
        t+=1
        if t==n:break
    return t

def pfaff(M):
    n=len(M)
    if n==0:return 1
    s=0
    for j in range(1,n):
        if M[0][j]:
            ids=[i for i in range(1,n) if i!=j]
            A=[[M[i][h] for h in ids] for i in ids]
            s+=(-1)**(j+1)*M[0][j]*pfaff(A)
    return s%P

def entries(N,k):
    return [(i,j) for i in range(N) for j in range(i+1,N) if (i//2!=j//2 or i>=2*k or j!=i+1)]

def matrix(N,k):
    A=[[0]*N for _ in range(N)]
    for i,j in entries(N,k):
        a=R.randrange(P);A[i][j]=a;A[j][i]=(-a)%P
    return A

def gradients(A,E):
    N=len(A);v=[]
    for i,j in E:
        ids=[t for t in range(N) if t!=i and t!=j]
        m=[[A[x][y] for y in ids] for x in ids]
        v.append(((-1)**(i+j+1)*pfaff(m))%P)
    return v

def bilinear(a,b):
    return sum(a[2*i]*b[2*i+1]-a[2*i+1]*b[2*i] for i in range(len(a)//2))%P

def factor_matrix(N,r,k):
    for _ in range(1000):
        B=[[R.randrange(P) for _ in range(r)] for _ in range(N)]
        for i in range(k):
            u,v=B[2*i],B[2*i+1]
            index=next((j for j in range(r) if bilinear(u,[1 if h==j else 0 for h in range(r)])),None)
            if index is None:continue
            base=[1 if h==index else 0 for h in range(r)]
            c=bilinear(u,v)*pow(bilinear(u,base),-1,P)%P
            B[2*i+1]=[(v[j]-c*base[j])%P for j in range(r)]
        if rank(B)==r:break
    else:raise AssertionError('factorization sampling failed')
    A=[[bilinear(B[i],B[j]) for j in range(N)] for i in range(N)]
    assert all(A[2*i][2*i+1]==0 for i in range(k))
    assert rank(A)==r
    return A

def zero_pair_matrix(N,k,index):
    for _ in range(500):
        A=matrix(N,k)
        i=2*index;j=i+1
        for t in range(N):
            A[i][t]=A[t][i]=A[j][t]=A[t][j]=0
        if rank(A)==N-2:return A
    raise AssertionError('no zero-pair rank N-2 witness')

def transverse_hessian(A,E):
    # The Pfaffian is multiaffine in its independent edge variables.
    M=[x[:] for x in A]
    n=len(E)
    H=[[0]*n for _ in range(n)]
    for i,(a,b) in enumerate(E):
        M[a][b]=(M[a][b]+1)%P;M[b][a]=(M[b][a]-1)%P
        f1=gradients(M,[E[j] for j in range(i+1,n)])
        # delta_i of gradient_j = d^2 pf / (d x_i d x_j)
        M[a][b]=(M[a][b]-1)%P;M[b][a]=(M[b][a]+1)%P
        f0=gradients(M,[E[j] for j in range(i+1,n)])
        for j in range(i+1,n):H[i][j]=H[j][i]=(f1[j-i-1]-f0[j-i-1])%P
    return H

def run():
    count=0
    for N in (6,8):
        for k in range(1,N//2+1):
            E=entries(N,k)
            for _ in range(45):
                A=matrix(N,k)
                g=gradients(A,E)
                e=(rank(A)<=N-4 or any(all(A[t][v]==0 for v in range(N)) and all(A[t+1][v]==0 for v in range(N)) for t in range(0,2*k,2)))
                assert (not any(g))==e, ('random',N,k)
                count+=1
            for r in (N-4,N-2):
                for _ in range(13):
                    A=factor_matrix(N,r,k)
                    e=(r==N-4 or any(all(A[t][v]==0 and A[t+1][v]==0 for v in range(N)) for t in range(0,2*k,2)))
                    assert (not any(gradients(A,E)))==e, ('factor',N,k,r)
                    count+=1
            for idx in range(k):
                for _ in range(5):
                    A=zero_pair_matrix(N,k,idx)
                    assert not any(gradients(A,E))
                    count+=1
            A=factor_matrix(N,N-4,k)
            assert rank(transverse_hessian(A,E))==6,(N,k,'rank-4 normal Hessian')
            count+=1
            for idx in range(k):
                A=zero_pair_matrix(N,k,idx)
                assert rank(transverse_hessian(A,E))==2*(N-2),(N,k,idx,'zero-pair Hessian')
                count+=1
    print('VERIFY_OK',count,'gradient classifications; Hessian strata for N=6,8 all k')

if __name__=='__main__':run()
