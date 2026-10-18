#!/usr/bin/env python3
"""Independent finite-field spot/exhaustive checks for equal-power monomial CI automorphisms."""
from itertools import product
from math import prod
import random

def vectors(r,d): return list(product(range(d),repeat=r))

def powpoly(poly,n,r,d,p):
    zero=(0,)*r
    def multiply(a,b):
        out={}
        for aa,ca in a.items():
            for bb,cb in b.items():
                e=tuple(x+y for x,y in zip(aa,bb))
                if max(e)>=d: continue
                out[e]=(out.get(e,0)+ca*cb)%p
        return {e:c for e,c in out.items() if c}
    z={zero:1}; b=poly.copy()
    while n:
        if n&1: z=multiply(z,b)
        n//=2
        if n: b=multiply(b,b)
    return z

def formula(r,d,p,q):
    m=d
    if p:
        while m%p==0: m//=p
    gl=prod(q**r-q**i for i in range(r))
    if m==1: return gl*q**(r*(d**r-1-r))
    from math import factorial
    return factorial(r)*(q-1)**r*q**(r*(d**r-1-m**(r-1)))

def check_exhaustive(r,d,p):
    # prime field only: count valid images for each prescribed cotangent row.
    q=p; mons=vectors(r,d); high=[a for a in mons if sum(a)>=2]
    basis=[tuple(int(i==j) for i in range(r)) for j in range(r)]
    counts={}
    for row in product(range(p),repeat=r):
        if not any(row): continue
        cnt=0
        for coeffs in product(range(p),repeat=len(high)):
            f={basis[i]:a for i,a in enumerate(row) if a}
            f.update({a:c for a,c in zip(high,coeffs) if c})
            if not powpoly(f,d,r,d,p): cnt+=1
        counts[row]=cnt
    mats=product(list(counts),repeat=r)
    def inv(rows):
        a=[list(row) for row in rows]; rank=0
        for j in range(r):
            k=next((i for i in range(rank,r) if a[i][j]%p),None)
            if k is None: continue
            a[rank],a[k]=a[k],a[rank]
            inv=pow(a[rank][j],-1,p)
            a[rank]=[v*inv%p for v in a[rank]]
            for i in range(rank+1,r):
                t=a[i][j]%p
                a[i]=[(a[i][c]-t*a[rank][c])%p for c in range(r)]
            rank+=1
        return rank==r
    actual=sum(prod(counts[row] for row in rows) for rows in mats if inv(rows))
    expected=formula(r,d,p,p)
    assert actual==expected,(r,d,p,actual,expected,counts)
    print('EXHAUSTIVE',f'r={r} d={d} q={p}',actual,'MATCH')

# These exhaust all images of every possible generator, and all invertible linear rows.
check_exhaustive(2,2,2)
check_exhaustive(2,2,3)
check_exhaustive(2,3,2)
check_exhaustive(2,3,3)
check_exhaustive(3,2,2)
# Sparse independent direct multiplication checks at non-p-power modular d=6,p=3.
rng=random.Random(314159)
for r,d,p in [(3,6,3),(2,6,3),(3,4,2),(2,6,2)]:
    mons=vectors(r,d)
    for k in range(12):
        j=rng.randrange(r)
        unit=tuple(int(j==i) for i in range(r))
        f={unit:1}
        for a in rng.sample([a for a in mons if sum(a)>=2],min(14,d**r-1-r)):
            c=rng.randrange(p)
            if c:f[a]=c
        m=d
        while m%p==0:m//=p
        allowed=all(a[j]!=0 or any(v>=m for v in a) for a in f if a!=unit)
        assert (not powpoly(f,d,r,d,p))==allowed,(r,d,p,j,allowed,f)
    print('SAMPLED',f'r={r} d={d} q={p}',12,'MATCH')
print('VERIFY_OK')
