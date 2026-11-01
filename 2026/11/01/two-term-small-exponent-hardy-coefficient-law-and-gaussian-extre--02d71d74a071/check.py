#!/usr/bin/env python3
"""Finite algebra checks for normalized Hardy coefficient trial families.
These checks supplement an analytical proof; they do not certify global maxima.
"""
from math import comb, exp, factorial, sqrt

def binomial_coefficient(a, power, k):
    # Coefficient of z^k of a normalized polynomial raised to integer power.
    p = [0.0] * (k + 1)
    p[0] = 1.0
    for ell in range(1, k + 1):
        nxt = [0.0] * (k + 1)
        for i in range(k + 1):
            if p[i] == 0:
                continue
            for j in range(1, k - i + 1):
                nxt[i+j] += p[i] * a[j]
        p = nxt
        total = comb(power, ell) * a[0]**(power-ell) * p[k]
        if ell == 1:
            ans = total
        else:
            ans += total
    return ans

def trial(k, s):
    a = [0.0] * (k + 1)
    a[1] = sqrt(k / s)
    if k >= 2:
        a[2] = (k - 1) / s
    a[0] = sqrt(1 - sum(x*x for x in a[1:]))
    assert abs(sum(x*x for x in a) - 1.0) < 1e-13
    return binomial_coefficient(a, s, k)

for k in range(1, 7):
    s = 8000
    base = (k / exp(1))**(k/2) / factorial(k)
    val = trial(k, s) / s**(k/2)
    pred = base * (1 + ((k-1)**2+1)/(4*s))
    assert abs(val / base - pred / base) < 3e-5, (k, val, pred)
    if k == 1:
        exact = sqrt(s) * ((s-1)/s)**((s-1)/2)
        assert abs(trial(1, s) - exact) < 1e-10
print('CHECK_OK: six finite-index normalized coefficient expansions; exact first-coefficient control')
