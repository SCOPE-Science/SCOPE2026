"""Finite and high-precision reproducibility checks for a Hardy approximation zero theorem.

Requires sympy, numpy, mpmath. These numerical checks are not proofs of the
all-degree assertions, which follow from binomial inequalities and Hurwitz's theorem.
"""
import math
import numpy as np
import sympy as sp
import mpmath as mp

z = sp.symbols('z')
exact_cases = 0
for m in range(3, 41):
    q = sum(sp.Rational(m-1-j, m) * z**j for j in range(m-1))
    numerator = sp.expand(m * (1-z)**2 * q - (z**m - m*z + (m-1)))
    assert numerator == 0, (m, numerator)
    exact_cases += 1

root_cases = 0
min_angle_deg = 180.0
for n in range(1, 17):
    coeffs = np.arange(1, n+2, dtype=float)
    roots = np.roots(coeffs)
    assert len(roots) == n
    angles = np.abs(np.degrees(np.angle(roots-1)))
    if np.min(angles) < min_angle_deg:
        min_angle_deg = float(np.min(angles))
    assert np.min(angles) > 45.0, (n, angles)
    root_cases += 1

mp.mp.dps = 75
w0 = mp.findroot(lambda w: mp.exp(w)-1-w,
                  (mp.mpc('2','7'), mp.mpc('2.3','7.6')))
assert abs(mp.exp(w0)-1-w0) < mp.mpf('1e-65')
assert mp.re(w0) > 0 and mp.im(w0) > 0
c = w0*(1+w0)/2
print('symbolic_polynomial_identities:', exact_cases, 'PASS')
print('numerical_roots_deg_1_to_16:', root_cases, 'PASS')
print('minimum_observed_absolute_angle_degrees:', f'{min_angle_deg:.9f}')
print('limit_root_w0:', mp.nstr(w0, 26))
print('first_correction_c:', mp.nstr(c, 26))
print('limit_root_absolute_angle_degrees:', mp.nstr(mp.arg(w0)*180/mp.pi, 17))
for m in (30, 60, 120, 240, 480):
    fm = lambda w: (1+w/mp.mpf(m))**m - 1 - w
    wm = mp.findroot(fm, (w0+c/m, w0+c/m+mp.mpc('.001','.001')),
                     solver='secant', tol=mp.mpf('1e-64'))
    assert abs(fm(wm)) < mp.mpf('1e-59')
    err = abs(wm - (w0+c/m))
    print('m=',m,'scaled_root=',mp.nstr(wm,18),
          'm2_expansion_error=',mp.nstr(m*m*err,14))
print('status: PASS (finite checks only; all-degree proof is separate)')
