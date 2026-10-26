#!/usr/bin/env python3
"""Exact, independently enumerated degree-depth covariance checks."""
from itertools import product
from fractions import Fraction as Q
from math import sqrt

def exact(n,j):
    return Q(1,j)-sum((Q(1,t*t) for t in range(j,n)),Q(0))

def enumerate_joint(n):
    # Uniform over all (n-1)! parent arrays.
    count=0
    sd=0
    sx=[0]*(n+1)
    sxd=[0]*(n+1)
    for parents in product(*(range(1,t) for t in range(2,n+1))):
        depth=[0]*(n+1)
        degree=[0]*(n+1)
        for t,p in enumerate(parents,2):
            depth[t]=1+depth[p]
            degree[p]+=1
        count+=1
        sd+=depth[n]
        for j in range(1,n):
            sx[j]+=degree[j]
            sxd[j]+=degree[j]*depth[n]
    for j in range(1,n):
        cov=Q(sxd[j],count)-Q(sx[j]*sd,count*count)
        assert cov==exact(n,j), (n,j,cov,exact(n,j))
    return n-1

checks=sum(enumerate_joint(n) for n in range(3,10))
for n in range(3,100):
    cs=[exact(n,j) for j in range(1,n)]
    assert cs[0]<0 and cs[-1]>0
    for j in range(1,n-1):
        assert cs[j]-cs[j-1]==Q(1,j*j*(j+1))
        checks+=1
for n in (1000,10000,100000):
    jstar=next(j for j in range(1,n) if exact(n,j)>0) if n<10000 else None
    # Compute float signs economically for larger n.
    if jstar is None:
        import math
        tail=[0.]*(n+1)
        for t in range(n-1,0,-1): tail[t]=tail[t+1]+1/(t*t)
        jstar=next(j for j in range(1,n) if 1/j-tail[j]>0)
    assert abs(jstar/sqrt(n)-1/sqrt(2))<0.04,(n,jstar)
    checks+=1
print('PASS exact assertions',checks,'including independent exhaustive parent-array enumerations through n=9')
