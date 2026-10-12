#!/usr/bin/env python3
"""Exact rational checks for an anonymous repeated-count identifiability theorem.

Run: python3 verify.py
No external dependencies. This checks formulas and finite certificates;
the general identifiability and nonidentifiability statements have analytic proofs.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def rising(x, k):
    y = F(1)
    for j in range(k):
        y *= x + j
    return y


def eq_moment(a, b, r):
    return rising(a, r) / rising(a+b, r)


def cross_cumulants(mu, a, b, xi, t):
    return [None] + [xi + mu*eq_moment(a,b,1) if j == 1
                     else mu*eq_moment(a,b,j) for j in range(1,t+1)]


def invert(c):
    c1,c2,c3,c4=c[1:5]
    r,h=c3/c2,c4/c3
    assert 0<r<h<3*r/(r+2)<1
    S=(1-3*h+2*r)/(h-r)
    a=r*(S+2)-2
    b=S-a
    mu=c2/eq_moment(a,b,2)
    xi=c1-mu*eq_moment(a,b,1)
    assert a>0 and b>0 and mu>0 and xi>=0
    return (mu,a,b,xi)


def mark_intensities(mu,a,b,xi,t):
    # Independent Poisson count from a mark pattern S, using beta moments.
    out={}
    for k in range(1,t+1):
        for sub in combinations(range(t),k):
            out[sub]=mu*rising(a,k)*rising(b,t-k)/rising(a+b,t)
            if k==1:out[sub]+=xi
    return out


witness_a=(F(10),F(2),F(3),F(2))
witness_b=(F(686,75),F(18,7),F(24,7),F(52,25))
ca=cross_cumulants(*witness_a,4)
cb=cross_cumulants(*witness_b,4)
assert ca[1:4]==cb[1:4]==[F(6), F(2), F(8,7)]
assert ca[4]==F(5,7) and cb[4]==F(104,147)
assert ca[4]-cb[4]==F(1,147)
assert mark_intensities(*witness_a,3)==mark_intensities(*witness_b,3)
assert mark_intensities(*witness_a,4)!=mark_intensities(*witness_b,4)

sample=[(F(10),F(2),F(3),F(2)),(F(686,75),F(18,7),F(24,7),F(52,25)),
        (F(7,3),F(1,2),F(3,5),F(0)),(F(9),F(4),F(2),F(1,7)),
        (F(1,10),F(11,13),F(17,19),F(2,15))]
count=0
for params in sample:
    coeffs=cross_cumulants(*params,4)
    assert invert(coeffs)==params
    for T in range(1,5):
        intensities=mark_intensities(*params,T)
        for r in range(1,T+1):
            # Marginal joint factorial cumulant is sum over all Poisson marks
            # containing any given r visits; here choose visits 0..r-1.
            observed=sum(z for S,z in intensities.items() if set(range(r)).issubset(S))
            assert observed==coeffs[r]
            count+=1
    assert coeffs[3]/coeffs[2]<coeffs[4]/coeffs[3]
    assert coeffs[4]/coeffs[3]< 3*(coeffs[3]/coeffs[2])/(coeffs[3]/coeffs[2]+2)

# Verify a continuum of distinct 3-visit parameterizations analytically via rational points.
# Keep c1,c2,c3 fixed at the witness values; vary S around the original S=5.
continuum=0
c1,c2,c3=ca[1:4]
r=c3/c2
for S in [F(9,2),F(19,4),F(21,4),F(11,2),F(23,4),F(6)]:
    a=r*(S+2)-2;b=S-a
    if a<=0 or b<=0:continue
    mu=c2/eq_moment(a,b,2);xi=c1-mu*eq_moment(a,b,1)
    if xi<=0:continue
    assert cross_cumulants(mu,a,b,xi,3)[1:]==ca[1:4]
    assert mark_intensities(mu,a,b,xi,3)==mark_intensities(*witness_a,3)
    continuum+=1
assert continuum>=3
print(f'VERIFY_OK inverted_parameter_sets={len(sample)} independent_mark_checks={count} '
      f'nonidentifiable_three_visit_profiles={continuum} fourth_order_difference={ca[4]-cb[4]}')
