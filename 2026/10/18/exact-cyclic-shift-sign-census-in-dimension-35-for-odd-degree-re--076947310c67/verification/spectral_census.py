#!/usr/bin/env python3
"""Exact rational interval certificate for cyclic real overlap signs in dimension 35."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, factorial

Q = 10**15
N = 22

def atan_recip(q):
    return sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(N)), F(0))

p = 16*atan_recip(5)-4*atan_recip(239)
p_error = 16*F(1,(2*N+1)*5**(2*N+1))+4*F(1,(2*N+1)*239**(2*N+1))
assert 3 < p-p_error and p+p_error < F(22,7)

def floor(f): return f.numerator//f.denominator

def ceil(f): return -floor(-f)

COS=[]
for t in range(18):
    x = F(2*t,35)*p
    term=F(1)
    approx=term
    for k in range(1,25):
        term *= -x*x/F((2*k-1)*(2*k))
        approx += term
    err=x**50/factorial(50) + F(2*t,35)*p_error
    # |sin|<=1 on R, hence pi input uncertainty bounded by its argument error.
    lo=floor(Q*(approx-err))
    hi=ceil(Q*(approx+err))
    assert lo<=hi and (hi-lo)<10000, (t,hi-lo)
    COS.append((lo,hi))

# For any k, sigma_{a} cos(2 pi k a/35) = sigma_{a} cos(2 pi r/35),
# r = min(ka mod 35, -ka mod 35) ∈{0,..17}.
POS=[]
for k in range(1,18):
    POS.append([min((k*a)%35,(-(k*a))%35) for a in range(1,18)])

survivors={}
worst_margin=None
min_certified_positive = None
for S in (-3,9):
    r=(17+S)//2
    viable=[]
    for plus in combinations(range(1,18),r):
        aset=set(plus)
        accepted=True
        for vec in POS:
            lower=3*Q
            upper=3*Q
            for a,b in enumerate(vec,1):
                lo,hi=COS[b]
                if a in aset:
                    lower+=lo;upper+=hi
                else:
                    lower-=hi;upper-=lo
            if upper<0:
                accepted=False
                break
            if lower<0:
                raise ArithmeticError(('ambiguous',S,plus,lower,upper))
        if accepted:
            for vec in POS:
                lower = 3*Q + sum((COS[b][0] if a in aset else -COS[b][1]) for a,b in enumerate(vec,1))
                assert lower > 0, (S,plus,lower)
                if min_certified_positive is None or lower < min_certified_positive:
                    min_certified_positive = lower
            viable.append(plus)
    survivors[S]=set(viable)
    print('S',S,'tested',len(list(combinations(range(1,18),r))),'positive-definite',len(viable))

reps=[(1,3,4,7,10,11,14),(1,5,6,7,8,13,14),(1,5,10,11,14,15,16)]
units=[u for u in range(1,35) if gcd(u,35)==1]
all_orbits=set()
for rep in reps:
    orbit={tuple(sorted(min((u*a)%35,(-(u*a))%35) for a in rep)) for u in units}
    assert orbit.isdisjoint(all_orbits)
    assert orbit <=survivors[-3]
    all_orbits |=orbit
    print('representative',rep,'orbit size',len(orbit))
assert all_orbits==survivors[-3]
assert len(survivors[9])==0
print('Certified minimum positive nonzero Fourier eigenvalue greater than',F(min_certified_positive,3*Q))
print('CERTIFIED: all 21828 sign vectors partitioned into 19 feasible and 21809 impossible; orbit sizes 12,3,4.')
print('pi interval and cosine grid certified using rational arithmetic; max grid width',max(hi-lo for lo,hi in COS))
