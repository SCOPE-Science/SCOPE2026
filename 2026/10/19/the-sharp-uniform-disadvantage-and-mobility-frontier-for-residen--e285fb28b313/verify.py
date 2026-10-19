#!/usr/bin/env python3
"""Exact rational checks for the smooth one-dimensional invasion witness.

No numerical PDE simulation is treated as proof of any spectral limit.
"""
from fractions import Fraction as F
from math import comb

THETA = F(1, 4)
COST = F(1, 100)
DIFFUSION = F(1)


def cosine_average(power):
    """Integral of cos(x)**power on (0,pi), divided by pi."""
    if power % 2:
        return F(0)
    k = power // 2
    return F(comb(2*k, k), 4**k)


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai * bj
    return out


def avg_poly(coeff):
    return sum((v * cosine_average(i) for i, v in enumerate(coeff)), F(0))


# Set t = cos(x); Q = 1 + theta*t; Q*r = theta*t.
Q = [F(1), THETA]
W = Q[:]
W2 = poly_mul(W, W)
# Trial potential energy / pi = int(theta*t*W**2) / pi.
potential = avg_poly([F(0)] + [THETA * z for z in W2])
# Trial diffusion energy / pi = theta**2 * int(sin(x)**2) / pi.
gradient = THETA**2 * (1 - cosine_average(2))
# Trial denominator / pi = int(Q*W**2) / pi.
denominator = avg_poly(poly_mul(Q, W2))
ratio = (potential - DIFFUSION * gradient) / denominator
assert potential == F(1, 16)
assert gradient == F(1, 32)
assert denominator == F(35, 32)
assert ratio == F(1, 35)
assert ratio - COST == F(13, 700)

# Capacity as function of t is m(t) = 1+theta*t + theta*t/(1+theta*t).
# m'(t) = theta + theta/(1+theta*t)**2 > 0 on [-1,1].
minimum_resident = (1-THETA) - THETA/(1-THETA)
minimum_invader = minimum_resident - COST
assert minimum_resident == F(5, 12)
assert minimum_invader == F(61, 150)

# Resident stationary equation: Q'' = -theta*cos(x),
# Q*(m-Q) = theta*cos(x), so the PDE and Neumann ends cancel.
assert avg_poly([F(0), THETA]) == 0  # int Q*r = 0

# Neumann corrector h=theta*cos(x)-theta**2/2,
# hence -h''=theta*cos(x)=Q*r and int Q*h = 0.
h = [-THETA**2 / 2, THETA]
assert avg_poly(poly_mul(Q, h)) == 0
corrector_energy = THETA**2 * (1 - cosine_average(2))
C = corrector_energy / avg_poly(Q)
assert C == F(1, 32)
print('PASS: exact moments, capacity positivity, positive Rayleigh witness, corrector coefficient')
print('Rayleigh bound:', ratio, 'invasion bound:', ratio-COST, 'large-d constant:', C)
