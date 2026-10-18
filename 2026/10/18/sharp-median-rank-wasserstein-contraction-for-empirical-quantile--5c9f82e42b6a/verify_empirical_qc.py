#!/usr/bin/env python3
"""Exact checks for the discrete-quantile clipping theorem.
No floating point numbers, dependencies or external input required.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement


def qclip(b, k, x):
    tau = sorted(abs(x-a) for a in b)[k-1]
    return [max(-tau, min(tau, x-a)) for a in b]


def segments(b):
    # Every ordering switch of absolute residuals occurs at a pair midpoint.
    v=sorted(set([F(a) for a in b]+[(F(a)+F(c))/2 for a in b for c in b]))
    return [(v[0]-1, v[0]), *((a,c) for a,c in zip(v,v[1:])), (v[-1],v[-1]+1)]

checks=0
for m in range(2,9):
    for raw in combinations_with_replacement(range(-2,4),m):
        b=tuple(map(F,raw))
        for k in range(1,m+1):
            beta=F(2*k-m,m)
            for a,c in segments(b):
                x=(2*a+c)/3; y=(a+2*c)/3; d=y-x
                u=qclip(b,k,x); v=qclip(b,k,y)
                diffs=[(vv-uu)/d for uu,vv in zip(u,v)]
                assert all(abs(z)<=1 for z in diffs),(m,b,k,a,c,diffs)
                avg=sum(diffs)/m
                assert beta<=avg<=1,(m,b,k,a,c,avg,beta)
                checks+=1
            # Also test at all kinks, a global 1-Lipschitz property.
            pts=sorted(set([F(t) for t in b]+[(F(a)+F(c))/2 for a in b for c in b]))
            for x,y in zip(pts,pts[1:]):
                u=qclip(b,k,x);v=qclip(b,k,y)
                assert all(abs(vv-uu)<=y-x for uu,vv in zip(u,v))
                assert sum(v)-sum(u)>=m*beta*(y-x)
                checks+=1

# The uniform factor is attained locally for every above-median rank.
sharp=0
for m in range(2,35):
 for k in range(m//2+1,m):
    b=(F(0),)*k+(F(10),)*(m-k)
    x=F(1);y=F(2);eta=F(1,5)
    u=qclip(b,k,x);v=qclip(b,k,y)
    q=1-2*eta*F(2*k-m,m)+eta*eta
    actual=sum(((y-eta*vv)-(x-eta*uu))**2 for uu,vv in zip(u,v))/m
    assert actual==q*(y-x)**2,(m,k,actual,q)
    sharp+=1

# Below (and at) the median rank, two different exact absorbing states exist.
absorbing=0
for m in range(2,35):
 for k in range(1,m//2+1):
    b=(F(0),)*k+(F(10),)*(m-k)
    assert all(v==0 for v in qclip(b,k,F(0)))
    assert all(v==0 for v in qclip(b,k,F(10)))
    absorbing+=1

print(f'PASS: {checks} exact rational slope/endpoint tests; {sharp} attained contraction factors; {absorbing} non-uniqueness examples.')
