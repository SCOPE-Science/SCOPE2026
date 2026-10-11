#!/usr/bin/env python3
"""Standalone exact bracket and Schur-transform identity checks.

The infinite theorem is proved analytically in RESULT.md; finite arithmetic here
only checks the localization and the extremizing construction.
"""
from fractions import Fraction as Q
from math import factorial, sin, cos, tan

def alternating_interval(x, cosine=False, pairs=18):
    # Consecutive alternating partial sums, from a negative term to a positive term.
    # For 0 <= x <= 1 their respective remainders have the indicated signs.
    if cosine:
        terms = [(-1)**j * x**(2*j) / factorial(2*j) for j in range(2*pairs+1)]
    else:
        terms = [(-1)**j * x**(2*j+1) / factorial(2*j+1) for j in range(2*pairs+1)]
    lo = sum(terms[:2*pairs])
    hi = lo + terms[2*pairs]
    assert lo <= hi
    return lo, hi

def derivative_numerator_interval(x):
    sl, su = alternating_interval(x, False)
    cl, cu = alternating_interval(x, True)
    a = 1 - x*x
    lower = a*(1+sl) - 2*x*cu*(cu+1+su)
    upper = a*(1+su) - 2*x*cl*(cl+1+sl)
    return lower, upper

low=Q(27327758,100000000)
high=Q(27327760,100000000)
ll,lu=derivative_numerator_interval(low)
hl,hu=derivative_numerator_interval(high)
assert ll>0, 'lower bracket derivative not certified positive'
assert hu<0, 'upper bracket derivative not certified negative'
print('Exact rational root bracket:', str(low), '< r_* <', str(high))

# Independent float reproduction of the root and norm, not a proof of uniqueness.
left, right = float(low), float(high)
def h(r):
    u = 1/cos(r)+tan(r)
    return (1-r*r)*u/cos(r)-2*r*(1+u)
for _ in range(60):
    mid=(left+right)/2
    if h(mid)>0: left=mid
    else: right=mid
r=(left+right)/2
constant=(1-r*r)*(1+1/cos(r)+tan(r))
assert abs(h(r)) < 1e-13
assert 2.14565 < constant < 2.14567
print('Numerical root: %.15f; numerical sharp norm: %.15f'%(r,constant))

# Exact checks: beta_R(R)=-s/R^m and beta'_R(R) Schwarz-Pick equality.
# This is a finite algebraic check; the limit for arbitrary m is proved on paper.
for m in range(1,11):
    for numerator in [90, 95, 98, 99]:
        R=Q(numerator,100)
        s=Q(1,4)
        if not R**m > s: continue
        c=(R-s/R**m)/(1-s*R**(1-m))
        assert -1 < c < 1
        beta=(c-R)/(1-c*R)
        assert beta == -s/R**m
        derivative=-(1-c*c)/(1-c*R)**2
        assert derivative == -(1-beta*beta)/(1-R*R)
print('Exact Blaschke identities: passed for all 40 indicated cases')
