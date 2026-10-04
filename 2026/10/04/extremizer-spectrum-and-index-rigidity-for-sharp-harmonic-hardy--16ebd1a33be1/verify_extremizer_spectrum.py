#!/usr/bin/env python3
import math

TAU = 2.0 * math.pi

def inv_gamma(x):
    if x <= 0 and abs(x-round(x)) < 1e-12:
        return 0.0
    return 1.0 / math.gamma(x)

def c_formula(r, m):
    return (2.0**(-r) * math.gamma(r+1.0) *
            inv_gamma((r+m+2.0)/2.0) * inv_gamma((r-m+2.0)/2.0))

def coeff_numeric(r, m, N=120000):
    s = 0.0
    for j in range(N):
        t = TAU * (j + 0.5) / N
        c = math.cos(t)
        phi = math.copysign(abs(c)**r, c)
        s += phi * math.cos(m*t)
    return s / N

max_err = 0.0
fourier_cases = 0
for r in (0.5, 1.0, 1.7, 3.0, 4.0):
    for m in (1, 3, 5, 7, 9):
        num = coeff_numeric(r, m)
        exact = c_formula(r, m)
        err = abs(num-exact)
        max_err = max(max_err, err)
        fourier_cases += 1
        if err > 8e-5:
            raise AssertionError((r, m, num, exact, err))

recurrence_cases = 0
for r in (0.3, 0.5, 1.0, 1.7, 3.0, 4.0, 5.0):
    for k in range(1, 6):
        left = (2*k + r + 1.0) * c_formula(r, 2*k+1)
        right = (r + 1.0 - 2*k) * c_formula(r, 2*k-1)
        if abs(left-right) > 2e-12 * max(1.0, abs(left), abs(right)):
            raise AssertionError((r, k, left, right))
        recurrence_cases += 1

truncation_cases = 0
for r in (1.0, 3.0, 5.0, 7.0):
    top = int(r)
    if abs(c_formula(r, top)) < 1e-14:
        raise AssertionError(('top vanished', r))
    for m in range(top+2, top+10, 2):
        if abs(c_formula(r, m)) > 1e-14:
            raise AssertionError(('tail nonzero', r, m, c_formula(r,m)))
        truncation_cases += 1

print('VERIFY_OK max_fourier_error={:.3e} fourier_cases={} recurrence_cases={} truncation_cases={}'.format(
    max_err, fourier_cases, recurrence_cases, truncation_cases))
