#!/usr/bin/env python3
"""Finite numerical checks for a disk Bergman boundary-chirp spectrum.

Dependencies: mpmath, scipy, numpy.  The proof of the infinite statements
is analytical; this program tests sample moments and counting scales only.
"""
import math
import numpy as np
import mpmath as mp
from scipy.integrate import quad

mp.mp.dps = 45
passed = 0

def check(test, message):
    global passed
    assert test, message
    passed += 1

def exact_eigenvalue(beta, s):
    a = mp.mpc(0, -1)
    return 2 * s * mp.im((a / s) ** ((1 - beta) / 2)
                          * mp.besselk(1 - beta, 2 * mp.sqrt(a * s)))

def leading_eigenvalue(beta, s):
    exponent = (2 * beta + 1) / 4
    return (mp.sqrt(mp.pi) * mp.power(s, exponent) *
            mp.exp(-mp.sqrt(2 * s)) *
            mp.sin(mp.sqrt(2 * s) + mp.pi * (2 * beta - 1) / 8))

# Bessel evaluation versus independent sine-weighted oscillatory quadrature.
for beta in (0.25, 0.5, 1.0, 1.5, 1.9):
    for s in (1, 2, 7, 20):
        def envelope(t):
            if t == 0:
                return 0.0
            return s * math.exp(-s / t) * t ** (beta - 2)
        integral, err = quad(envelope, 0.0, math.inf, weight='sin', wvar=1,
                             epsabs=1e-10, limit=400, limlst=400)
        value = float(exact_eigenvalue(beta, s))
        check(abs(integral - value) < 5e-9,
              f'oscillatory integral mismatch: beta={beta}, s={s}: {integral} vs {value}')
        check(err < 2e-8, f'quadrature error estimate: beta={beta}, s={s}')

# The half-integer modified Bessel function is elementary.
for beta in (0.5, 1.5):
    for s in (1, 2, 3, 7, 10, 20, 40, 100, 400, 1000):
        exact = exact_eigenvalue(beta, s)
        shortcut = leading_eigenvalue(beta, s)
        check(abs(exact - shortcut) < mp.mpf('1e-35') * max(1, abs(exact)),
              f'half-integer identity: beta={beta}, s={s}')

# Check absolute (not relative near roots) Bessel asymptotics.
for beta in (0.25, 0.75, 1.0, 1.9):
    for s in (100, 400, 1600):
        amplitude = mp.sqrt(mp.pi) * mp.power(s, (2*beta+1)/4) * mp.exp(-mp.sqrt(2*s))
        difference = abs(exact_eigenvalue(beta, s) - leading_eigenvalue(beta, s))
        check(difference / amplitude < 10 / mp.sqrt(s),
              f'nonuniform large-order approximation: beta={beta}, s={s}')

# Exact elementary spectrum for beta=3/2; signed and total counting laws.
upper = 15000
s = np.arange(1, upper+1, dtype=float)
values = np.sqrt(np.pi) * s * np.exp(-np.sqrt(2*s)) * np.sin(np.sqrt(2*s) + np.pi/4)
for L in (14., 18., 25., 35., 50., 70., 85.):
    threshold = math.exp(-L)
    pos = int(np.count_nonzero(values > threshold))
    neg = int(np.count_nonzero(values < -threshold))
    reference_total = 0.5*L*L + 2*L*math.log(L)
    reference_each = 0.25*L*L + L*math.log(L)
    check(abs(pos+neg-reference_total) <= 6*L, f'total two-term count: L={L}')
    check(abs(pos-reference_each) <= 6*L, f'positive two-term count: L={L}')
    check(abs(neg-reference_each) <= 6*L, f'negative two-term count: L={L}')
    print(f'L={L:g}: positive={pos}, negative={neg}, total={pos+neg}; '
          f'leading+second={reference_total:.4f}')

print(f'PASS: {passed} finite checks')
