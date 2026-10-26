#!/usr/bin/env python3
"""Finite rational verification of exact harmonic-Bergman monomial Toeplitz identities.

All quantifiers over arbitrary dimension/weight and all infinite limits are proved in
RESULT.md; this script only checks finitely many rational parameters and truncations.
"""
from functools import lru_cache
from fractions import Fraction
from math import sqrt, log

@lru_cache(maxsize=None)
def moment(alpha: Fraction, j: int) -> Fraction:
    assert alpha > -1 and j >= 0
    if j == 0: return Fraction(1)
    return moment(alpha, j-1) * Fraction(j,1) / (Fraction(j,1)+alpha+1)

def weight2(alpha: Fraction, n: int, k: int) -> Fraction:
    m = lambda j: moment(alpha, j)
    if k >= 0:
        out = Fraction(1)
        for j in range(k+1,k+n+1): out *= Fraction(j,1)/(Fraction(j,1)+alpha+1)
        return out
    j = -k
    if j >= n:
        out = Fraction(1)
        for q in range(j-n+1,j+1): out *= Fraction(q,1)/(Fraction(q,1)+alpha+1)
        return out
    return m(n)**2/(m(j)*m(n-j))

def independent_gram_weight2(alpha: Fraction, n: int, k: int) -> Fraction:
    # <z^n e_k,e_{k+n}> obtained by angular/radial orthogonality.
    out = k+n
    M = lambda j: moment(alpha, j)
    integral = M((n+abs(k)+abs(out))//2)
    assert (n+abs(k)+abs(out)) % 2 == 0
    return integral**2/(M(abs(k))*M(abs(out)))

parameters=[Fraction(-3,4),Fraction(-1,2),Fraction(0),Fraction(1,3),Fraction(1),Fraction(2),Fraction(5)]
coefficient_checks=0
valley_checks=0
for alpha in parameters:
    for n in range(1,16):
        for k in range(-36,37):
            assert weight2(alpha,n,k)==independent_gram_weight2(alpha,n,k)
            coefficient_checks+=1
        rmin = [moment(alpha,n)**2/(moment(alpha,r)*moment(alpha,n-r)) for r in range(n)]
        for r in range(n):
            cells=[weight2(alpha,n,r+j*n) for j in range(-12,13)]
            assert min(cells)==rmin[r]
            valley_checks+=1
            # Difference signs around the canonical valley (allow one plateau for r=0).
            left=[weight2(alpha,n,r+j*n) for j in range(-12,0)]
            right=[weight2(alpha,n,r+j*n) for j in range(-1,13)]
            assert all(left[i]>=left[i+1] for i in range(len(left)-1))
            assert all(right[i]<=right[i+1] for i in range(len(right)-1))
        exact=2*sum(1-x for x in rmin)
        L=40
        truncated=sum(abs(weight2(alpha,n,k)-weight2(alpha,n,k-n)) for k in range(-L*n,L*n+1))
        assert truncated < exact and exact-truncated > 0

# exact unweighted formula
for n in range(1,61):
    a=Fraction(0)
    m=lambda j:moment(a,j)
    exact=2*sum(1-m(n)**2/(m(r)*m(n-r)) for r in range(n))
    assert exact==Fraction(n*(5*n+1),3*(n+1))

# positive/negative weak singular-value coefficient computed independently
for a in [Fraction(-1,2),Fraction(0),Fraction(1),Fraction(3)]:
    for n in (1,2,4,9):
        target=float((a+1)*n/2)
        for k in (100000,200000):
            pos=k*(1-sqrt(float(weight2(a,n,k))))
            neg=k*(1-sqrt(float(weight2(a,n,-k))))
            assert abs(pos-target)<.005 and abs(neg-target)<.005
print('PASS: %d exact radial-Gram comparisons; %d finite valleys; 60 exact unweighted rational trace norms; 32 weak-tail comparisons.' % (coefficient_checks,valley_checks))
