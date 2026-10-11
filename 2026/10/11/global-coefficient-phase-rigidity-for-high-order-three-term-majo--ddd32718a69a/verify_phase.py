#!/usr/bin/env python3
"""Exact rational checks supporting the phase-rigidity estimates.

The analytic inequalities outside the rational substeps are proved in RESULT.md.
This script uses Python's standard library only.
"""
from fractions import Fraction as Q
from math import factorial

KAPPA = Q(29, 50)
C = Q(440, 9)  # strict upper bound for 80*sqrt(3)*pi/9

def B0(k):
    return Q(1, 2*k + 8) + Q(1, 2*k)

def U0(k):
    return Q(1) + Q(2, 2*k - 3)

def upper_R(k):
    return C * factorial(2*k + 2) * B0(k) * U0(k) * \
        Q(10000, 7569*(k+2)**2)**k

def exact_step(k):
    return Q((2*k+4)*(2*k+3), (k+3)**2) * Q(10000,7569) * \
           Q(k+2, k+3)**(2*k) * B0(k+1)/B0(k) * U0(k+1)/U0(k)

assert KAPPA*KAPPA == Q(841,2500)
base = upper_R(23)
assert base < Q(4,5), "base case not enclosed"
x = Q(23,13)
exp_lower = Q(1) + x + x*x/2 + x*x*x/6 + x*x*x*x/24
assert exp_lower > Q(800000,143811)
assert Q(40000,7569) / exp_lower < Q(19,20)
# Supplementary exact checks, not a substitute for the uniform ratio proof.
for k in range(23,124):
    assert exact_step(k) < Q(19,20)
    assert upper_R(k) < Q(4,5)*Q(19,20)**(k-23)
print('VERIFY_OK')
print('upper_R(23) strictly less than 4/5:', float(base))
print('rational exponential lower bound:', float(exp_lower))
print('uniform step upper bound:', float(Q(40000,7569)/exp_lower))
print('101 supplementary step and envelope checks passed')
