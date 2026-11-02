#!/usr/bin/env python3
"""Exact verification of the two-step fat-node punctual incidence Euler series.
Python 3 standard library only. This checks independent finite combinatorics;
the proof of the universal formula is in RESULT.md, not inferred from testing.
"""
from functools import lru_cache
from math import comb

N = 34

def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def mul(a,b):
    c=[0]*(N+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:N+1-i]):
                if y:c[i+j]+=x*y
    return c
def shift(a,k):return ([0]*k+a[:N+1-k]) if k<=N else [0]*(N+1)

def poly_P(k):
    if k<0:return [0]*(N+1)
    a=[1]+[0]*N
    for j in range(1,k+1):
        for i in range(j,N+1): a[i]+=a[i-j]
    return a

def poly_D(k):
    if k<0:return [0]*(N+1)
    a=[0]*(N+1)
    for j in range(1,k+1):a[j]+=1
    return mul(poly_P(k),a)

def poly_T(k):
    if k<0:return [0]*(N+1)
    a=[0]*(N+1)
    for i in range(1,k+1):
        for j in range(i+1,k+1):
            if i+j<=N:a[i+j]+=1
    for j in range(1,k+1):
        if 2*j<=N:a[2*j]+=1
    for j in range(2,k+1):
        if j<=N:a[j]+=1
        if 2*j-1<=N:a[2*j-1]-=1
    return mul(poly_P(k),a)

def formula(u,v):
    total=[0]*(N+1)
    for r in range(v+1):
        term=add(mul(sub(poly_T(r),poly_T(r-1)),poly_P(u)),
                 add(mul(sub(poly_P(r),poly_P(r-1)),poly_T(u)),
                     mul(sub(poly_D(r),poly_D(r-1)),poly_D(u))))
        total=add(total,shift(term,u*r))
    for r in range(1,v+1):
        total=add(total,shift(mul(poly_P(r-1),poly_P(u-1)),(u+1)*r))
    assert total[:2]==[0,0],(u,v,total[:2])
    return total[2:]+[0,0]

@lru_cache(None)
def partitions(n,upper):
    if n==0:return ((),)
    return tuple((a,)+p for a in range(min(n,upper),0,-1)
                 for p in partitions(n-a,a))

def inc(mu,lam):
    return len(mu)<=len(lam) and all(mu[i]<=lam[i] for i in range(len(mu)))

def allowed(lam,u,v):
    return len(lam)<=v or lam[v]<=u

def domino_stat(lam):
    vals=sorted(set(lam),reverse=True)
    d=len(vals)
    horiz=sum(vals[i]-(vals[i+1] if i+1<d else 0)>=2 for i in range(d))
    vert=sum(lam.count(a)>=2 for a in vals)
    return comb(d,2)+horiz+vert

def brute(u,v,maxn):
    vals=[]
    for n in range(maxn+1):
        c=0
        for lam in partitions(n+2,n+2):
            if not allowed(lam,u,v):continue
            c+=sum(inc(mu,lam) for mu in partitions(n,n))
        vals.append(c)
    return vals

for size in range(2,19):
    for lam in partitions(size,size):
        assert domino_stat(lam)==sum(inc(mu,lam) for mu in partitions(size-2,size-2)),lam

for u in range(1,5):
    for v in range(1,5):
        expected=formula(u,v)
        observed=brute(u,v,13)
        assert expected[:14]==observed,(u,v,expected[:14],observed)
        assert expected[:32]==formula(v,u)[:32]
        print('PASS',u,v,'n=0..13 independent pairs',observed)
assert formula(1,1)[:14]==[2]+[3*i for i in range(1,14)]
assert formula(2,2)[:11]==[2,3,8,13,25,39,66,97,149,207,294]
print('VERIFY_OK: 16 parameter pairs, 224 exact pair counts, all partitions of sizes 2..18, symmetric rational coefficient formula')
