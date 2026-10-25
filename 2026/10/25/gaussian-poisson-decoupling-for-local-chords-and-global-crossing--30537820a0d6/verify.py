#!/usr/bin/env python3
"""Exact checks of local-chord deletion and the factorial marking identity.
Scientific scope: finite enumeration only, not a proof of limiting statements.
"""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from math import factorial

@lru_cache(None)
def pairings(vertices):
    if not vertices:
        return ((),)
    a, *rest = vertices
    out = []
    for j,b in enumerate(rest):
        for tail in pairings(tuple(rest[:j] + rest[j+1:])):
            out.append(((a,b),)+tail)
    return tuple(out)

def cross(a,b):
    x,y = sorted(a); u,v = sorted(b)
    return (x<u<y<v) or (u<x<v<y)

def crossings(m):
    return sum(cross(m[i],m[j]) for i in range(len(m)) for j in range(i+1,len(m)))

def shortlength(pair,m):
    x,y=sorted(pair)
    return min(y-x-1,m-y+x-1)

def falling(v,k):
    z=1
    for q in range(k): z*=v-q
    return z

def odd_product(m,k):
    out=1
    for i in range(k):out*=m-2*i-1
    return out

def count_ordered_adjacent(n,k):
    m=2*n
    return (m*factorial(m-k))//((m-k)*factorial(m-2*k))

states=0
for n in range(2,8):
    m=2*n
    allp=pairings(tuple(range(m)))
    states+=len(allp)
    joint=Counter((crossings(p),sum(shortlength(c,m)==0 for c in p)) for p in allp)
    for k in range(n+1):
        smaller=pairings(tuple(range(2*(n-k))))
        counter=Counter(crossings(p) for p in smaller)
        den=odd_product(m,k)
        num=count_ordered_adjacent(n,k)
        for x in set(counter)|set(a for a,_ in joint):
            left=sum(cnt*falling(s,k) for (xx,s),cnt in joint.items() if xx==x)
            # E[(S)_k 1_{X=x}]=num/den * P(X_{n-k}=x).
            # Clear denominators without fractional rounding.
            assert left*den*len(smaller)==len(allp)*num*counter[x],(n,k,x)
    for j in range(min(n-2,3)+1):
        for a in range(m):
            b=(a+j+1)%m
            wanted=frozenset((a,b))
            if a==b: continue
            remaining=tuple(x for x in range(m) if x not in wanted)
            for tail in pairings(remaining):
                extra=crossings((tuple(wanted),)+tail)-crossings(tail)
                assert 0<=extra<=j,(n,j,a,b,extra)
    print('EXHAUSTIVE_DELETE_AND_FACTORIAL_PASS',n,len(allp), 'k=0..'+str(n), 'j<=3')
print('VERIFY_OK total matchings',states)
