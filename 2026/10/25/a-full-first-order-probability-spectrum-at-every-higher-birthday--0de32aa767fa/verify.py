#!/usr/bin/env python3
"""Exact occupancy factorial moments and finite critical-scale corroboration."""
from fractions import Fraction
from itertools import product
from math import comb, factorial
import math

def fall(n,r):
    z=1
    for j in range(r): z*=n-j
    return z

def exact_moment(n,m,j,r):
    if j*r>n or r>m: return Fraction(0)
    return Fraction(fall(m,r)*fall(n,j*r),factorial(j)**r*m**(j*r))*Fraction(m-r,m)**(n-j*r)

def exhaust(n,m,j,r):
    tot=0
    for f in product(range(m),repeat=n):
        counts=[f.count(i) for i in range(m)]
        z=sum(t==j for t in counts)
        tot+=fall(z,r)
    return Fraction(tot,m**n)

checks=0
for n in range(1,6):
    for m in range(1,5):
        for j in range(n+1):
            for r in (1,2):
                assert exhaust(n,m,j,r)==exact_moment(n,m,j,r),(n,m,j,r)
                checks+=1

for k in range(2,6):
    for c in (0.75,1,2):
        n=500
        m=round(c*n**(k/(k-1)))
        lam=1/(factorial(k)*c**(k-1))
        ex=float(exact_moment(n,m,k,1))
        assert abs(ex-lam)<.075, (k,c,ex,lam)
        exhigh=sum(float(exact_moment(n,m,j,1)) for j in range(k+1,min(n,k+8)+1))
        assert exhigh<.1, (k,c,exhigh)
        checks+=2

print("CRITICAL_STAR_OCCUPANCY_EXACT_OK",checks,"checks")
