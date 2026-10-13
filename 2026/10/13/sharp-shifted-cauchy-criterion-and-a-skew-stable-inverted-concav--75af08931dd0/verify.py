#!/usr/bin/env python3
"""Finite algebraic and characteristic-function checks for a folded Cauchy--stable result.
These tests supplement, and do not replace, the analytical proof.
"""
from fractions import Fraction as Q
from math import atan, tan, pi, cos, sin, sqrt
from cmath import exp

checks = 0
for i in range(-16, 17):
    m = Q(i, 8)
    for j in range(1, 49):
        x = Q(j, 12)
        d_minus = 1 + (x-m)**2
        d_plus = 1 + (x+m)**2
        derivative = (2*x/d_minus - 2*x*x*(x-m)/d_minus**2
                      + 2*x/d_plus - 2*x*x*(x+m)/d_plus**2)
        polynomial = ((1-3*m*m)*x**4 + 2*(1+m*m)**2*x*x+(1+m*m)**3)
        closed_form = 4*x*polynomial/(d_minus**2*d_plus**2)
        assert derivative == closed_form
        checks += 1
        if 3*m*m <= 1:
            assert polynomial > 0
            checks += 1

for alpha in [0.09, 0.25, 0.5, 0.72, 0.95, 0.999]:
    bound = tan(pi*alpha/6)/tan(pi*alpha/2)
    assert 0 < bound < 1
    checks += 1
    for k in range(-10, 11):
        m = k/(10*sqrt(3))
        theta = atan(m)
        beta = tan(alpha*theta)/tan(pi*alpha/2)
        scalealpha = (1+m*m)**(alpha/2)*cos(alpha*theta)
        assert abs(beta) <= bound + 2e-15
        for t in [-4., -0.7, 0.3, 2.5]:
            left = exp(-complex(abs(t),-m*t)**alpha)
            right = exp(-scalealpha*abs(t)**alpha*(1-1j*beta*tan(pi*alpha/2)*(1 if t>0 else -1)))
            assert abs(left-right) < 4e-14
            checks += 1

# Exhibit loss of monotonicity beyond the exact shifted-Cauchy cutoff.
for m in [Q(3,5), Q(1,1), Q(2,1), Q(3,1)]:
    assert 3*m*m > 1
    # The negative leading coefficient dominates for sufficiently large x.
    x=Q(1)
    while True:
        polynomial=((1-3*m*m)*x**4+2*(1+m*m)**2*x*x+(1+m*m)**3)
        if polynomial < 0:
            break
        x *= 2
    checks+=1

print(f"PASS: {checks} exact-rational and finite complex-analytic identity checks")
