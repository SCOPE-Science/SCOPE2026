"""Exact finite-field verification of the rank formula for a memory cellular automaton."""
from itertools import product

def matmul(A,B,p):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][h]*B[h][j] for h in range(q))%p for j in range(m)] for i in range(n)]

def rank(A,p):
    A=[row[:] for row in A]; n=len(A); m=len(A[0]) if n else 0
    r=0
    for c in range(m):
        pivot=next((i for i in range(r,n) if A[i][c]%p),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(v*inv)%p for v in A[r]]
        for i in range(r+1,n):
            v=A[i][c]
            if v:
                A[i]=[(a-v*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==n:break
    return r

def make(p,a,k):
    L=p**a; N=k*L
    T=[[0]*L for _ in range(L)]
    for i in range(L):
        for t in range(p):T[i][(i-t)%L]=(T[i][(i-t)%L]+1)%p
    M=[[0]*N for _ in range(N)]
    for j in range(k):
        for i in range(L):
            for h in range(L):M[i][j*L+h]=T[i][h]
    for j in range(1,k):
        for i in range(L):M[j*L+i][(j-1)*L+i]=1
    return M

def verify(p,a,k):
    L=p**a; N=k*L
    ell=[(L-1-r)//(p-1)+1 for r in range(p-1)]
    M=make(p,a,k)
    P=[[int(i==j) for j in range(N)] for i in range(N)]
    for t in range(k*ell[0]+1):
        rr=rank(P,p)
        target=sum(max(k*v-t,0) for v in ell)
        assert rr==target,(p,a,k,t,rr,target)
        P=matmul(P,M,p)
    return k*ell[0]

def main():
    tests=[]
    for p,a,k in product((2,3,5),(1,2),(1,2,3)):
        if k*p**a>50:continue
        t=verify(p,a,k)
        tests.append((p,p**a,k,t))
    print('EXACT_RANK_PROFILE_PASS',len(tests))
    print('CASES',tests)
    p,a,k=3,2,2;L=p**a;ells=[(L-1-r)//(p-1)+1 for r in range(p-1)];
    print('EXAMPLE_p3_L9_k2', 'Jordan_sizes',tuple(k*e for e in ells),'nilpotency',k*ells[0],'upper_bound',k*L)
if __name__=='__main__':main()
