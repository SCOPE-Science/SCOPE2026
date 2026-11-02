#!/usr/bin/env python3
"""Reproducibility checks for the flat Möbius band pointed-loop profile.

This checker uses exact rational arithmetic for deck transformations,
truncated moments and the sharp-deficit identity. Numerical quadrature
is an independent diagnostic, not a proof of the universal statements.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def deck_min_sq(L, y, bound=12):
    values = []
    for k in range(-bound, bound + 1):
        if k == 0:
            continue
        y_image = -y if k % 2 else y
        values.append((k * L)**2 + (y_image - y)**2)
    return min(values)


def exact_var_profile(r):
    # r = H/(sqrt(3)*L); q is uniform on [0,r]
    if r <= 1:
        m1 = r*r / 3
        m2 = r**4 / 5
    else:
        m1 = 1 - F(2, 3) / r
        m2 = 1 - F(4, 5) / r
    var = m2 - m1*m1
    area_normalized = 3*var / (r*r)
    formula = F(4, 15)*r*r if r <= 1 else F(8, 5)/r**3 - F(4, 3)/r**4
    assert area_normalized == formula
    return formula


samples = 0
for L in (F(1), F(3, 2), F(5, 3), F(7, 4)):
    for H in (F(1, 3), F(1), F(2), F(3), F(7, 2), F(5)):
        for k in range(-10, 11):
            y = H*F(k, 20)
            actual = deck_min_sq(L, y)
            expected = min(4*L*L, L*L+4*y*y)
            assert actual == expected, (L, H, y, actual, expected)
            samples += 1
print('EXACT_DECK_PARITY_AND_MINIMIZATION_PASSED', samples)

for r in (F(1, 9), F(2, 7), F(3, 4), F(1), F(11, 10),
          F(10, 9), F(4, 3), F(3, 2), F(2), F(3), F(7)):
    exact_var_profile(r)
print('EXACT_TRUNCATED_MOMENT_IDENTITIES_PASSED', 11)

# (9r-10)^2(27r^2+60r+100)=2187r^4-12000r+10000.
# Coefficients in ascending powers.
a = [F(100), F(-180), F(81)]
b = [F(100), F(60), F(27)]
c = [F(0)]*5
for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        c[i+j] += ai*bj
assert c == [F(10000), F(-12000), F(0), F(0), F(2187)]
assert exact_var_profile(F(10, 9)) == F(729, 2500)
assert F(4, 15) < F(729, 2500)
assert F(1)-F(1)/F(10, 9) == F(1, 10)
print('GLOBAL_SHARP_DEFICIT_FACTORIZATION_AND_ATOM_PASSED')

# Independent direct quadrature of the defining uniform q-law.
def simpson_mean(r, power, steps=10000):
    assert steps % 2 == 0
    h = r/steps
    def f(i):
        q = i*h
        return min(1., q*q)**power
    integral = f(0) + f(steps)
    integral += 4*sum(f(i) for i in range(1, steps, 2))
    integral += 2*sum(f(i) for i in range(2, steps-1, 2))
    return integral*h/(3*r)

for ratio in (0.24, 0.6, 0.99, 1.01, 1.12, 1.5, 2.3, 4.0):
    m1 = simpson_mean(ratio, 1)
    m2 = simpson_mean(ratio, 2)
    q = 3*(m2-m1*m1)/(ratio*ratio)
    expected = (4*ratio*ratio/15 if ratio <= 1 else
                8/(5*ratio**3)-4/(3*ratio**4))
    assert isclose(q, expected, abs_tol=2e-6), (ratio, q, expected)
print('INDEPENDENT_QUADRATURE_PROFILE_CHECKS_PASSED', 8)
print('ALL_CHECKS_PASSED')
