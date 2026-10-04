#!/usr/bin/env python3

def rank_mod(rows,p):
    a=[list(map(lambda x:x%p,row)) for row in rows]
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        iv=pow(a[r][c],-1,p)
        a[r]=[(x*iv)%p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                f=a[i][c]; a[i]=[(a[i][j]-f*a[r][j])%p for j in range(n)]
        r+=1
    return r

def mm(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p for j in range(len(B[0]))] for i in range(len(A))]

def sub(A,B,p): return [[(A[i][j]-B[i][j])%p for j in range(len(A[0]))] for i in range(len(A))]

def block(A,C):
    Z=[[0]*3 for _ in range(3)]
    return [A[i]+C[i] for i in range(3)] + [Z[i]+A[i] for i in range(3)]

for p in (2,3,5,7):
    # Exhaust the canonical rank minimization in four effective Sylvester variables.
    for tau in range(p):
      for kap in range(p):
        best=3
        for u in range(p):
          for v in range(p):
            for w in range(p):
              for z in range(p):
                R=[[u,v,w],[0,(-u-tau)%p,0],[0,z,(-kap)%p]]
                best=min(best,rank_mod(R,p))
        expect=0 if tau==0 and kap==0 else (2 if tau and kap else 1)
        assert best==expect,(p,tau,kap,best,expect)
    # Verify the source-normalized rank-one intertwiner defect.
    A=[[0,1,0],[0,0,0],[0,0,0]]; C=[[1,0,0],[0,0,0],[0,0,1]]; Z=[[0]*3 for _ in range(3)]
    P=[[1,0,0,0,0,0],[0,1,0,1,0,0],[0,0,0,0,1,0],[0,0,1,0,0,0],[0,0,0,0,0,1],[0,1,0,0,0,0]]
    MC=block(A,C); M0=block(A,Z)
    D=sub(mm(P,MC,p),mm(M0,P,p),p)
    assert rank_mod(P,p)==6
    assert rank_mod(D,p)==1
print('VERIFY_OK primes=2,3,5,7')
