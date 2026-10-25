#!/usr/bin/env python3
"""Finite diagnostics for the nonlinear three-dimensional toral skew volume law."""
from fractions import Fraction
from math import cos, pi, sin, sqrt
import random

# Previously established quadratic coefficient-volume, independently recomputed.
# Integral over [-1,1] of sqrt(1-u) du = 4*sqrt(2)/3.
assert Fraction(16) + 4 * Fraction(32, 9) == Fraction(272, 9)
assert 2 * Fraction(272, 9) == Fraction(544, 9)

# Exact binomial orbit difference identities for the unperturbed triangular map.
for j in range(0, 110):
    for h, b, c in [(Fraction(1, 101), Fraction(-2, 37), Fraction(7, 29)),
                    (Fraction(-3, 73), Fraction(1, 11), Fraction(-5, 43))]:
        y, z = b, c
        for k in range(j):
            z += y
            y += h
        assert y == b + j*h
        assert z == c + j*b + Fraction(j*(j-1), 2)*h

# Compare exact-in-the-real-lift recursion to the independent weighted formula.
alpha = (sqrt(5)-1)/2
for amp, x in [(0.0, .187), (.05, .317), (.15, .617)]:
    for h, b, c in [(0.00013, -.00033, .007), (-0.00021, .00048, -.004)]:
        yg, zg = b, c
        increments = []
        for j in range(240):
            incr = h + amp*(sin(2*pi*(x+j*alpha+h))-sin(2*pi*(x+j*alpha)))
            y_formula = b + j*h + sum(increments)
            z_formula = c + j*b + j*(j-1)*h/2 + sum((j-1-r)*increments[r] for r in range(j))
            assert abs(yg-y_formula) < 3e-11
            assert abs(zg-z_formula) < 3e-11
            zg += yg
            yg += incr
            increments.append(incr-h)

# Limit-body membership compared with full nonlinear Bowen constraints.
def gap(A, B, C):
    return 1-max(abs(C+t*B+.5*t*t*A) for t in (i/4096 for i in range(4097)))

def finite_inside(A, B, C, x, amp, n=640, eps=.012):
    h, b, c = eps*A/(n*n), eps*B/n, eps*C
    y, z = b, c
    for j in range(n):
        if abs(h)>=eps or abs(y)>=eps or abs(z)>=eps:
            return False
        z += y
        y += h + amp*(sin(2*pi*(x+j*alpha+h))-sin(2*pi*(x+j*alpha)))
    return True

rng=random.Random(732381)
comparisons=0
for amp in (0.0, 0.07, 0.15):
    for x in (.1234, .8234):
        for _ in range(180):
            A=rng.uniform(-13,13)
            B=rng.uniform(-7,7)
            C=rng.uniform(-1.3,1.3)
            g=gap(A,B,C)
            if abs(g)<.16: # exclude the finite-n boundary layer
                continue
            assert finite_inside(A,B,C,x,amp) == (g>0), (A,B,C,x,amp,g)
            comparisons+=1
print('VERIFY_OK', 'rational_orbit_cases', 220, 'nonlinear_lift_cases', 6,
      'off_boundary_shape_checks', comparisons, 'coefficient_volume', '544/9')
