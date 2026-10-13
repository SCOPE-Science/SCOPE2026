#!/usr/bin/env python3
"""Direct finite-field checks for idempotent endomorphisms of bilinear-form Leibniz algebras."""
from itertools import product
from math import prod


def matmul(A,B,q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))%q for j in range(len(B[0]))) for i in range(len(A)))

def dotB(v,w,D,q):return sum(d*v[i]*w[i] for i,d in enumerate(D))%q

def rank(A,q):
    a=[list(r) for r in A];m=len(a);n=len(a[0]) if m else 0;r=0
    for j in range(n):
        t=next((i for i in range(r,m) if a[i][j]%q),None)
        if t is None:continue
        a[r],a[t]=a[t],a[r];fac=pow(a[r][j],-1,q)
        a[r]=[x*fac%q for x in a[r]]
        for i in range(m):
            if i!=r:
                c=a[i][j];a[i]=[(x-c*y)%q for x,y in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

def isotropic_subspace_counts(q,D):
    n=len(D);answer={0:1}
    vecs=list(product(range(q),repeat=n))
    for k in range(1,min(2,n)+1):
        spaces=set()
        for seq in product((v for v in vecs if any(v)),repeat=k):
            if rank(seq,q)<k:continue
            if any(dotB(v,w,D,q) for v in seq for w in seq):continue
            # canonical by listing members (safe for n<=4)
            S=frozenset(tuple(sum(c*seq[j][i] for j,c in enumerate(coeff))%q for i in range(n)) for coeff in product(range(q),repeat=k))
            spaces.add(S)
        answer[k]=len(spaces)
    return answer

def ortho_count(q,D):
    n=len(D);m=n//2;eps=1
    if n%2==0:
        d=prod(D)%q
        eps=1 if pow(((-1)**m*d)%q,(q-1)//2,q)==1 else -1
    w=m if n%2 or eps==1 else m-1
    I={0:1};v=1
    for k in range(1,w+1):
        dim=n-2*(k-1)
        if dim%2:ell=(q**(dim-1)-1)//(q-1)
        else:
            h=dim//2
            ell=((q**(h-1)+eps)*(q**h-eps))//(q-1)
        v=v*ell//((q**k-1)//(q-1))
        I[k]=v
    return I

def count_all_A(q,D):
    n=len(D);total=0;bands={}
    for z in product(range(q),repeat=n*n):
        A=tuple(tuple(z[i*n:(i+1)*n]) for i in range(n))
        if matmul(A,A,q)!=A:continue
        if any(dotB([A[i][a] for i in range(n)],[A[i][b] for i in range(n)],D,q) for a in range(n) for b in range(n)):continue
        r=rank(A,q)
        # fA=f has q^rank(A) solutions
        c=q**r;bands[r]=bands.get(r,0)+c;total+=c
    return total+1,bands

def brute_full(q,D):
    n=len(D);N=n+1;total=0
    for z in product(range(q),repeat=N*N):
        M=tuple(tuple(z[i*N:(i+1)*N]) for i in range(N))
        if matmul(M,M,q)!=M:continue
        if any(M[i][n] for i in range(n)):continue
        if any(dotB([M[i][a] for i in range(n)],[M[i][b] for i in range(n)],D,q)!=(M[n][n]*D[a] if a==b else 0)%q for a in range(n) for b in range(n)):continue
        total+=1
    return total

def check(q,D,full=False,subspace=False):
    n=len(D);I=ortho_count(q,D);formula=2+sum(c*q**(k*(n-k+1)) for k,c in I.items() if k)
    direct,bands=count_all_A(q,D)
    assert formula==direct,(q,D,formula,direct,bands)
    if full:assert formula==brute_full(q,D),(q,D,formula)
    if subspace:
        got=isotropic_subspace_counts(q,D)
        for k,c in I.items():assert got[k]==c,(q,D,k,got[k],c)
    print('CASE',q,D,'ISOTROPIC',I,'COUNT',formula,'DIRECT_BANDS',bands)

check(3,(1,1),full=True,subspace=True)  # anisotropic plane
check(3,(1,2),full=True,subspace=True)  # split plane
check(5,(1,1),subspace=True)             # split plane
check(5,(1,2),subspace=True)             # anisotropic plane
check(3,(1,1,1),subspace=True)           # parabolic 3-space
# 4-space: line/plane enumeration independent of formula, omit exhaustive matrices
for D in ((1,1,1,1),(1,1,1,2)):
    I=ortho_count(3,D); G=isotropic_subspace_counts(3,D)
    for k,c in I.items():assert c==G[k],(D,k,c,G[k])
    print('QUADRIC',3,D,I,'RETRACTIONS',2+sum(c*3**(k*(4-k+1)) for k,c in I.items() if k))
print('VERIFY_OK')
