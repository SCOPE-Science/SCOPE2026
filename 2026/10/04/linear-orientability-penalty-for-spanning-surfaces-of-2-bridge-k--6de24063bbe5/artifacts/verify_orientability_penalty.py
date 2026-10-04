#!/usr/bin/env python3
"""Regression checks for the orientability-penalty deduction.

The topology inputs are the two published/preprint asymptotic formulas cited in
RESULT.md.  This script checks only the algebra of the deduction and the
probability inequality; it is not evidence for those topology inputs.
"""
from fractions import Fraction

# Constant and linear coefficients in 2*gbar - Gammabar.
g_lin = Fraction(1,4)
g_const = Fraction(1,12)
Gamma_lin = Fraction(1,3)
Gamma_const = Fraction(1,9)
assert 2*g_lin - Gamma_lin == Fraction(1,6)
assert 2*g_const - Gamma_const == Fraction(1,18)

# General density lower bound from X in [0,1] and E[X] -> 1/6.
def lower(delta):
    return (Fraction(1,6)-delta)/(1-delta)

assert lower(Fraction(1,12)) == Fraction(1,11)
for q in range(7,60):
    delta=Fraction(1,q)
    if delta < Fraction(1,6):
        b=lower(delta)
        assert 0 < b < 1
        # Extremal two-point distribution at delta and 1 attains the bound.
        mean = delta*(1-b) + b
        assert mean == Fraction(1,6)

print('VERIFY_OK mean_gap=c/6+1/18+o(1) threshold=c/12 density_lower_bound=1/11')
