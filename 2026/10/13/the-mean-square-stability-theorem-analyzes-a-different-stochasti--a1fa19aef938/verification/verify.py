#!/usr/bin/env python3
from fractions import Fraction as F

# Representative positive equilibrium coordinates and noise intensities.
E = (F(2, 3), F(5, 4), F(7, 5))
alpha = (F(1, 10), F(3, 20), F(2, 25))
assert all(x > 0 for x in E)
assert all(a > 0 for a in alpha)

# After translating X = E + U, the original abundance-proportional
# diffusion alpha_i X_i has affine coefficients (alpha_i E_i, alpha_i).
orig_constant = tuple(a*x for a, x in zip(alpha, E))
orig_slope = alpha
center_constant = (F(0), F(0), F(0))
center_slope = alpha
assert all(c > 0 for c in orig_constant)
assert center_constant == (0, 0, 0)
assert orig_slope == center_slope

# Exact coordinatewise identity for several displacements.
for U in [
    (F(0), F(0), F(0)),
    (F(1, 7), F(-1, 8), F(2, 9)),
    (F(-1, 5), F(3, 11), F(-1, 13)),
]:
    original = tuple(a*(x+u) for a, x, u in zip(alpha, E, U))
    centered = tuple(a*u for a, u in zip(alpha, U))
    assert tuple(o-c for o, c in zip(original, centered)) == orig_constant

# Ito generator of ||X-E||^2 at X=E: the drift contribution vanishes
# at a deterministic drift equilibrium, leaving this strictly positive term.
short_time_coefficient = sum(c*c for c in orig_constant)
assert short_time_coefficient > 0
assert sum(c*c for c in center_constant) == 0

print('VERIFY_OK')
