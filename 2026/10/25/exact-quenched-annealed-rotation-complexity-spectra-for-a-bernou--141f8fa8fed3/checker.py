#!/usr/bin/env python3
"""Exact finite-branch and asymptotic-shape diagnostics for a Bernoulli circle-map theorem.
All dependencies are in the Python standard library. Finite tests are not infinite proofs.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import exp, log

K = {'+': (0, 1, 1), '-': (-1, -1, 0)}

def inv(sign, branch, y):
    if sign == '+':
        return ((y / 3), ((y + 1) / 3), ((3 - y) / 3))[branch]
    return (((1 - y) / 3), ((y + 1) / 3), ((y + 2) / 3))[branch]

def full_lift(sign, x):
    integer = x.numerator // x.denominator
    y = x - integer
    if sign == '+':
        return integer + (3 * y if y < Fraction(2, 3) else 4 - 3 * y)
    return integer + (-3 * y if y < Fraction(1, 3) else 3 * y - 2)

def exact_poly(base):
    coef = Counter({0: 1})
    for sign in base:
        nex = Counter()
        for exponent, count in coef.items():
            for k in K[sign]:
                nex[exponent + k] += count
        coef = nex
    return coef

def annealed_poly(n, p):
    coef = {0: Fraction(1)}
    for _ in range(n):
        nex = {}
        for exponent, count in coef.items():
            for k, wt in [(-1, 2 * (1-p)), (0, Fraction(1)), (1, 2*p)]:
                nex[exponent+k] = nex.get(exponent+k, Fraction(0))+count*wt
        coef = nex
    return coef

branch_tests = 0
for n in range(1, 6):
    for base in [tuple('+' if (j % 2 == 0) else '-' for j in range(n)), tuple('-' for _ in range(n))]:
        symbolic = Counter()
        for branches in product(range(3), repeat=n):
            y = Fraction(1, 5)
            for sign, branch in reversed(list(zip(base, branches))):
                y = inv(sign, branch, y)
            x0 = y
            point = x0
            for sign in base:
                point = full_lift(sign, point)
            k = sum(K[s][b] for s, b in zip(base, branches))
            assert abs(point - x0 - k) < 1
            # The exact lift equals the branch sum plus endpoint displacement.
            assert point - x0 - k == Fraction(1,5) - x0
            symbolic[k] += 1
            branch_tests += 1
        assert symbolic == exact_poly(base)
        assert sum(symbolic.values()) == 3**n
p = Fraction(2,5)
annealed_tests = 0
for n in range(1, 7):
    exact_avg = Counter()
    for base in product('+-', repeat=n):
        weight = p**base.count('+') * (1-p)**base.count('-')
        for k, c in exact_poly(base).items():
            exact_avg[k] += weight*c
    assert dict(exact_avg) == annealed_poly(n, p)
    assert sum(exact_avg.values()) == 3**n
    annealed_tests += 1

def pq(lam, p):
    return p * log(1+2*exp(lam)) + (1-p)*log(1+2*exp(-lam))

def pa(lam, p):
    return log(1+2*p*exp(lam)+2*(1-p)*exp(-lam))

def dpq(lam,p):
    return p * (2/(2+exp(-lam))) - (1-p) * (2/(2+exp(lam)))

def dpa(lam,p):
    return (2*p*exp(lam)-2*(1-p)*exp(-lam))/(1+2*p*exp(lam)+2*(1-p)*exp(-lam))

def entropy(r,p,P,D):
    lo, hi = -45., 45.
    for i in range(140):
        t=(lo+hi)/2
        if D(t,p)<r:
            lo=t
        else:
            hi=t
    t=(lo+hi)/2
    return P(t,p)-t*r

gap_tests = 0
for p_float in [.2,.5,.8]:
    rt=(4*p_float-2)/3
    assert abs(pq(0,p_float)-log(3))<1e-12
    assert abs(pa(0,p_float)-log(3))<1e-12
    assert abs(dpq(0,p_float)-rt)<1e-12
    assert abs(dpa(0,p_float)-rt)<1e-12
    for r in [p_float-1+.03, rt-.05, rt+.05, p_float-.03]:
        if abs(r-rt) < 1e-9: continue
        hq=entropy(r,p_float,pq,dpq)
        ha=entropy(r,p_float,pa,dpa)
        assert ha-hq>1e-8, (p_float,r,hq,ha)
        gap_tests += 1
    assert abs(entropy(rt,p_float,pq,dpq)-log(3))<1e-10
    assert abs(entropy(rt,p_float,pa,dpa)-log(3))<1e-10

print('EXACT_LIFT_CODING_PASS', branch_tests)
print('ANNEALED_POLYNOMIAL_IDENTITIES_PASS', annealed_tests)
print('STRICT_GAP_SAMPLES_PASS', gap_tests)
print('DIAGNOSTICS_PASS')
