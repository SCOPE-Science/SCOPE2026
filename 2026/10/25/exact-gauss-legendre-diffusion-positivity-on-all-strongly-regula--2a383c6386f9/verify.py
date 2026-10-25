"""Independent exact checks of fourth-order Gauss endpoint diffusion on strongly regular graphs.

Run: python verify.py  (Python 3.9+, standard library only).
For the infinite family, use the mathematical proof in RESULT.md; finite examples are checks only.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def invert(A):
    n=len(A)
    B=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        piv=next(i for i in range(j,n) if B[i][j])
        B[j],B[piv]=B[piv],B[j]
        x=B[j][j]
        B[j]=[e/x for e in B[j]]
        for i in range(n):
            if i !=j and B[i][j]:
                x=B[i][j]
                B[i]=[u-x*v for u,v in zip(B[i],B[j])]
    return [row[n:] for row in B]

def adj_from(n,edges):
    A=[[0]*n for _ in range(n)]
    for u,v in edges:
        assert u!=v
        A[u][v]=A[v][u]=1
    return A

def c5():
    return adj_from(5,[(i,(i+1)%5) for i in range(5)])

def petersen():
    return adj_from(10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)])

def complement(A):
    n=len(A)
    return [[0 if i==j else 1-A[i][j] for j in range(n)] for i in range(n)]

def rook(q):
    return adj_from(q*q,[(i*q+j,k*q+l) for i in range(q) for j in range(q) for k in range(q) for l in range(q) if i*q+j < k*q+l and ((i==k)!=(j==l))])

def triangular(n):
    verts=list(combinations(range(n),2))
    return adj_from(len(verts),[(i,j) for i in range(len(verts)) for j in range(i+1,len(verts)) if len(set(verts[i]).intersection(verts[j]))==1])

def paley(q):
    assert q%4==1
    sq={i*i%q for i in range(1,q)}
    return adj_from(q,[(i,j) for i in range(q) for j in range(i+1,q) if (i-j)%q in sq])

def multipart(*sizes):
    n=sum(sizes); part=sum(([i]*m for i,m in enumerate(sizes)),[])
    return adj_from(n,[(i,j) for i in range(n) for j in range(i+1,n) if part[i]!=part[j]])

def srg_parameters(A):
    n=len(A)
    k=sum(A[0]);assert 0<k<n-1
    assert all(sum(row)==k for row in A)
    A2=matmul(A,A)
    sets=[{A2[i][j] for i in range(n) for j in range(i+1,n) if A[i][j]==t} for t in (0,1)]
    assert all(len(s)==1 for s in sets),sets
    mu,lam=[s.pop() for s in sets]
    assert mu>0
    return n,k,lam,mu

def pade(A,h):
    n=len(A);k=sum(A[0]);L=[[F(k*(i==j)-A[i][j]) for j in range(n)] for i in range(n)]
    L2=matmul(L,L)
    num=[[F(12*(i==j))-6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    den=[[F(12*(i==j))+6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    return matmul(num,invert(den))

def predicted(v,k,lam,mu,h,adj):
    S=2*k-lam+mu; delta=v-2*k+lam-mu
    D=(mu*v)**2*h**4+6*mu*v*S*h**3+12*(S*S+mu*v)*h*h+72*S*h+144
    if adj: return 12*h*(12+6*mu*h-mu*delta*h*h)/D
    return 12*mu*h*h*(6+S*h)/D

def check():
    graphs=[('C5',c5()),('Petersen',petersen()),('Petersen complement',complement(petersen())),('rook3',rook(3)),('rook4',rook(4)),('triangular5',triangular(5)),('triangular6',triangular(6)),('Paley5',paley(5)),('Paley13',paley(13)),('3x3 complete multipartite',multipart(3,3,3)),('4x4 complete multipartite',multipart(4,4))]
    entries=0; cases=0
    steps=[F(1,17),F(1,2),F(3,2),F(5,1),F(13,1)]
    for name,A in graphs:
        v,k,lam,mu=srg_parameters(A)
        delta=v-2*k+lam-mu
        if delta>0:
            p=12+6*mu*F(1,1000)-mu*delta*F(1,1000)**2
            assert p>0
            # The quadratic is negative at sufficiently large rational steps.
            assert 12+6*mu*F(10000)-mu*delta*F(10000)**2<0
        for h in steps:
            T=pade(A,h)
            for i in range(v):
                assert sum(T[i])==1,(name,h,i)
                for j in range(v):
                    if i !=j:
                        expect=predicted(v,k,lam,mu,h,A[i][j])
                        assert T[i][j]==expect,(name,v,k,lam,mu,h,i,j,T[i][j],expect)
                        entries+=1
            cases+=1
    print('VERIFY_OK: %d strongly regular graphs; %d exact rational Gauss matrices; %d exact off-diagonal identities; stochastic row sums; finite-cutoff signs'%(len(graphs),cases,entries))
if __name__=='__main__':check()
