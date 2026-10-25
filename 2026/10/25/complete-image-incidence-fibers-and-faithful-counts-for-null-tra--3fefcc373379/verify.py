#!/usr/bin/env python3
"""Independent exhaustive check of image-incidence fibers for null transformation representations."""
from itertools import product
from collections import Counter
from math import factorial


def stirling(n,k):
    if k<0 or k>n: return 0
    r=[0]*(k+1);r[0]=1
    for _ in range(n):
        nxt=[0]*(k+1)
        for j in range(1,k+1):nxt[j]=j*r[j]+r[j-1]
        r=nxt
    return r[k]

def predicted2(n,m,profile):
    u=sum(profile)
    if u>n:return 0
    r=n-u
    a=[sum(profile[mask-1] for mask in range(1,1<<m) if mask&(1<<i)) for i in range(m)]
    if any(x>r for x in a):return 0
    numer=factorial(n)
    denom=factorial(r)
    for t in profile:denom*=factorial(t)
    v=numer//denom
    for x in a:v*=factorial(x)*stirling(r+1,x+1)
    return v

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for i in range(n+1):
            for tail in compositions(n-i,k-1):yield(i,)+tail

def total_formula(n,m):
    if m==0:return 1
    return sum(predicted2(n,m,profile) for r in range(n+1) for profile in compositions(n-r,(1<<m)-1))

def signed_stirling_first(n,k):
    vals=[1]
    for j in range(n):
        nxt=[0]*(len(vals)+1)
        for i,c in enumerate(vals):
            nxt[i]-=j*c
            nxt[i+1]+=c
        vals=nxt
    return vals[k]

def faithful_formula(n,m):
    return sum(signed_stirling_first(m+1,k)*total_formula(n,k-1) for k in range(1,m+2))

def check(n,m):
    X=list(range(n+1))
    maps=[(0,)+t for t in product(X,repeat=n)]
    valid=Counter()
    total=0
    faithful=0
    for fs in product(maps,repeat=m):
        images=[set(f) for f in fs]
        U=set().union(*images)-{0}
        if any(any(f[g[x]]!=0 for x in X) for f in fs for g in fs):
            continue
        profile=[0]*((1<<m)-1)
        for x in U:
            mask=sum((1<<i) for i,A in enumerate(images) if x in A)
            profile[mask-1]+=1
        valid[tuple(profile)]+=1
        total+=1
        if len(set(fs)|{(0,)*(n+1)})==m+1:faithful+=1
    assert faithful==faithful_formula(n,m),(n,m,faithful,faithful_formula(n,m))
    expected={profile:predicted2(n,m,profile) for r in range(n+1) for profile in compositions(n-r,(1<<m)-1)}
    expected={k:v for k,v in expected.items() if v}
    if expected!=dict(valid):
        missing={k:(expected.get(k,0),valid.get(k,0)) for k in set(expected)|set(valid) if expected.get(k,0)!=valid.get(k,0)}
        raise AssertionError((n,m,missing))
    print(f'PASS n={n} m={m} ordered_representations={total} realized_profiles={len(valid)} faithful={faithful}')

if __name__=='__main__':
    for n,m in [(0,1),(1,1),(2,1),(3,1),(4,1),(2,2),(3,2),(4,2),(2,3),(3,3)]:check(n,m)
    print('THEORETICAL_COUNTS')
    for n in range(1,6):
        print(n,[(m,total_formula(n,m),faithful_formula(n,m)) for m in range(1,4)])
    print('VERIFY_OK_NULL_TRANSFORMATION_IMAGE_INCIDENCE')
