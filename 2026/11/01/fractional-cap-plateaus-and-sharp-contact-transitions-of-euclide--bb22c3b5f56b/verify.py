#!/usr/bin/env python3
"""Exact-rational test of the circumball formula for uniform capped cubes."""
from fractions import Fraction as F
from itertools import combinations

def median(a,b,c):
    return sorted((a,b,c))[1]

def predicted(n,t):
    assert n>=2 and F(0)<=t<=n
    m=t.numerator//t.denominator
    delta=t-m
    c=F(1,2) if 2*m>=n else median(F(m,n),delta/2,t/n)
    center=(c,)*n
    radius2=n*c*c+max((F(j)*(1-2*c) for j in range(m+1)),default=F(0))
    if delta:radius2=max(radius2,n*c*c+m+delta*delta-2*t*c)
    return c,radius2

def vertices(n,t):
    m=t.numerator//t.denominator
    d=t-m
    for k in range(m+1):
        for I in combinations(range(n),k):
            v=[F(0)]*n
            for i in I:v[i]=F(1)
            yield tuple(v)
    if d and m<n:
        for I in combinations(range(n),m):
            for j in range(n):
                if j in I:continue
                v=[F(0)]*n
                for i in I:v[i]=F(1)
                v[j]=d
                yield tuple(v)

def checks():
    cases=0;dist=0;cert=0
    for n in range(2,11):
        for m in range(n+1):
            for delta in (F(0),F(1,9),F(1,3),F(1,2),F(3,4),F(8,9)):
                t=m+delta
                if t>n:continue
                c,r=predicted(n,t)
                v=list(vertices(n,t))
                vals=[sum((x-c)**2 for x in w) for w in v]
                assert max(vals)==r,(n,t,c,r,max(vals))
                # Exact certificate from a convex combination of contact vertices:
                contact=[w for w,x in zip(v,vals) if x==r]
                ranks=[sum(w) for w in contact]
                # Symmetrized contact orbits have means rank/n; interpolate two orbits.
                assert min(ranks)<=n*c<=max(ranks),(n,t,c,min(ranks),max(ranks))
                cases+=1;dist+=len(vals);cert+=len(contact)
    print('PASS',cases,'parameter cases,',dist,'exact vertex distances,',cert,'contact points')
if __name__=='__main__':checks()
