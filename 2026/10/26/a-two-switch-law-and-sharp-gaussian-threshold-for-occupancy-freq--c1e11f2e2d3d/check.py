#!/usr/bin/env python3
"""Reproduce finite multinomial cross-frequency covariance and likelihood-ratio checks."""
import itertools
import math
from fractions import Fraction
from math import comb

def probs(m, n, r, s):
    pr = Fraction(comb(n, r) * (m-1)**(n-r), m**n)
    ps = Fraction(comb(n, s) * (m-1)**(n-s), m**n)
    prs = (Fraction(comb(n, r)*comb(n-r, s)*(m-2)**(n-r-s),m**n)
           if r+s<=n else Fraction(0))
    return pr, ps, prs

def cross_cov(m, n, r, s):
    pr, ps, prs = probs(m, n, r, s)
    return m*(m-1)*prs-m*m*pr*ps

def q_exact(m,n,r,s):
    pr,ps,prs=probs(m,n,r,s)
    return Fraction(m-1,m)*prs/(pr*ps)

checks=0
for m,lo,hi in ((3,2,7),(4,2,7),(5,2,5)):
    for n in range(lo,hi+1):
        counter=[0]*(n+1)
        pair=[[0]*(n+1) for _ in range(n+1)]
        for balls in itertools.product(range(m), repeat=n):
            occ=[0]*m
            for ball in balls: occ[ball]+=1
            f=[0]*(n+1)
            for a in occ: f[a]+=1
            for r in range(n+1):
                counter[r]+=f[r]
                for s in range(n+1): pair[r][s]+=f[r]*f[s]
        total=m**n
        for r in range(n+1):
            for s in range(r+1,n+1):
                enumeration=Fraction(pair[r][s], total)-Fraction(counter[r]*counter[s],total**2)
                claimed=cross_cov(m,n,r,s)
                assert enumeration==claimed,(m,n,r,s,enumeration,claimed)
                checks+=1

# Finite unimodality follows from the exact adjacent-ratio identity.
for m in range(3,8):
    for n in range(3,30):
        for r in range(1,n):
            for s in range(n-r):
                a=q_exact(m,n,r,s)
                b=q_exact(m,n,r,s+1)
                assert b/a==Fraction((n-r-s)*(m-1),(n-s)*(m-2))
                checks+=1

# A substantive two-switch witness has all three bands feasible.
m,n,r=3,15,3
assert all(cross_cov(m,n,r,s)<0 for s in range(0,7))
assert all(cross_cov(m,n,r,s)>0 for s in range(7,12))
assert all(cross_cov(m,n,r,s)<0 for s in range(12,16))
checks+=16

# The central multinomial normal approximation gives the critical profile.
for m in (3,4,5):
    rho=-1/(m-1)
    a=(m-1)/m/math.sqrt(1-rho**2)
    n=100000
    scale=math.sqrt(n*(m-1)/m**2)
    for x in (-1.2,0,1.2):
        r=round(n/m+x*scale)
        s=round(n/m+(x/rho)*scale)
        logq=(math.log((m-1)/m)+math.lgamma(n-r+1)+math.lgamma(n-s+1)
              -math.lgamma(n+1)-math.lgamma(n-r-s+1)
              +(n-r-s)*math.log((m-2)/m)-(2*n-r-s)*math.log((m-1)/m))
        limit=math.log(a)+x*x/2
        assert abs(logq-limit)<0.055,(m,x,logq,limit)
        checks+=1

print('PASS',checks,'independent exact comparisons / algebraic ratios / asymptotic diagnostics')
