"""Independent exhaustive small-field verification of square-zero Smith strata over dual numbers.
Field elements are integers; F4 uses x^2+x+1. Python standard library only.
"""
from collections import Counter
from itertools import product
from math import prod


def gaussian(n,k,q):
    if k<0 or k>n:return 0
    if k==0 or k==n:return 1
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))


def gl(n,q):
    return prod(q**n-q**i for i in range(n))


def rank_matrices(n,r,q):
    return gaussian(n,r,q)**2*gl(r,q)


def predicted(n,q):
    d={}
    for r in range(n//2+1):
        s=n-2*r
        H=gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)
        for t in range(s+1):
            d[(r,t)]=H*q**(2*r*(n-r))*rank_matrices(s,t,q)
    return d


def gf_mul(a,b,q):
    if q!=4:return (a*b)%q
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return z

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def neg(a,q):
    return a if q==4 else (-a)%q

def mul(A,B,n,q):
    return tuple(sum((gf_mul(A[i*n+k],B[k*n+j],q) for k in range(n)),0)%q for i in range(n) for j in range(n)) if q!=4 else tuple(
        __import__('functools').reduce(int.__xor__, (gf_mul(A[i*n+k],B[k*n+j],q) for k in range(n)), 0)
        for i in range(n) for j in range(n))

def rank(A,n,m,q):
    A=[list(A[i*m:(i+1)*m]) for i in range(n)]
    r=0
    for j in range(m):
        k=next((k for k in range(r,n) if A[k][j]),None)
        if k is None:continue
        A[k],A[r]=A[r],A[k]
        inv=next(x for x in range(1,q) if gf_mul(x,A[r][j],q)==1)
        A[r]=[gf_mul(x,inv,q) for x in A[r]]
        for k in range(n):
            if k!=r and A[k][j]:
                v=A[k][j]
                A[k]=[add(x,neg(gf_mul(v,y,q),q),q) for x,y in zip(A[k],A[r])]
        r+=1
        if r==n:break
    return r


def smith_t(A,B,n,q,r):
    # Underlying field-linear map for X=A+eps B on R^n:
    # [A 0; B A], whose rank is 2r+t when the Smith form has
    # r unit entries and t entries associate to eps.
    C=[]
    for i in range(n):
        C.extend(A[i*n:(i+1)*n]);C.extend([0]*n)
    for i in range(n):
        C.extend(B[i*n:(i+1)*n]);C.extend(A[i*n:(i+1)*n])
    return rank(tuple(C),2*n,2*n,q)-2*r


def exhaustive(n,q):
    elems=list(product(range(q),repeat=n*n))
    sq=[(A,rank(A,n,n,q)) for A in elems if mul(A,A,n,q)==(0,)*(n*n)]
    obs=Counter()
    for A,r in sq:
        for B in elems:
            AB=mul(A,B,n,q); BA=mul(B,A,n,q)
            if all(add(x,y,q)==0 for x,y in zip(AB,BA)):
                t=smith_t(A,B,n,q,r)
                obs[r,t]+=1
    ex=predicted(n,q)
    assert dict(obs)==ex,(n,q,obs,ex)
    print('ALL_DUAL_SQUARE_ZERO_OK', 'n=',n,'q=',q,'total=',sum(obs.values()),
          'strata=',sorted(obs.items()))

exhaustive(2,2)
exhaustive(3,2)
exhaustive(2,3)
exhaustive(2,4)
for n in range(1,9):
 for q in (2,3,4,5,7,8,9):
  p=predicted(n,q)
  assert all(v>0 for v in p.values())
  assert sum(p.values())==sum(gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)*q**(n*n-2*r*(n-r)) for r in range(n//2+1))
print('VERIFY_OK')

# Unequal-characteristic rings: Z/4 and Z/9, checked independently
# of the equal-characteristic dual-number encoding above.
def exhaustive_mod_p2(p):
    modulus=p*p
    n=2
    obs=Counter()
    for X in product(range(modulus),repeat=4):
        square=tuple(sum(X[i*2+k]*X[k*2+j] for k in range(2))%modulus
                     for i in range(2) for j in range(2))
        if square!=(0,0,0,0): continue
        A=tuple(x%p for x in X)
        r=rank(A,2,2,p)
        im=set()
        for v0 in range(modulus):
            for v1 in range(modulus):
                im.add(((X[0]*v0+X[1]*v1)%modulus,
                        (X[2]*v0+X[3]*v1)%modulus))
        z=len(im)
        t=0
        while z>1:
            assert z%p==0
            z//=p;t+=1
        t-=2*r
        obs[r,t]+=1
    assert dict(obs)==predicted(2,p), (p,obs,predicted(2,p))
    print('CHAIN_RING_MIXED_CHARACTERISTIC_OK', 'ring=Z/'+str(modulus),
          'total=',sum(obs.values()),'strata=',sorted(obs.items()))

exhaustive_mod_p2(2)
exhaustive_mod_p2(3)
print('VERIFY_OK_CHAIN_RINGS')
