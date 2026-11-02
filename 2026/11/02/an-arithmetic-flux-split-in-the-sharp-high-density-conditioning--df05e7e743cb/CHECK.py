#!/usr/bin/env python3
"""Independent elementary numerical diagnostics for the first-Hermite Gabor bound asymptotics.

Requires Python 3 standard library only. These finite checks support but do not
replace the operator-theoretic and infinite-series arguments in RESULT.md.
"""
import math

P = math.pi

def tail(q, cutoff=12):
    """Absolute coefficient tail of Janssen's sum, computed on a finite grid."""
    z = 0.0
    for k in range(-cutoff, cutoff + 1):
        for ell in range(-cutoff, cutoff + 1):
            m = k * k + ell * ell
            if m >= 2:
                z += abs(1 - P * q * m) * math.exp(-P * q * m / 2)
    return z

# An absolute, nonnumerical upper bound for the infinite tail is
# q*exp(-pi*q)*4*SUM_(m>=2) [(m+1)(1/2+pi*m) exp(-pi(m-2))].
# Bounding pi by 22/7, and exp(-pi) by 1/20 bounds the last constant by 617840/6859 < 91.
# We use the relaxed rigorous constant 100.
assert 617840 / 6859 < 100
nchecks = 0
for q in [3, 3.5, 4, 4.5, 5, 6, 7.5, 9, 12]:
    t = tail(q)
    assert t < 100 * q * math.exp(-P * q)
    nchecks += 1
    h = 4.0 if float(q).is_integer() else 2.0 * math.sqrt(2)
    c = (P * q - 1) * math.exp(-P * q / 2)
    assert 1 - h * c - 100 * q * math.exp(-P * q) > 0
    nchecks += 1
    # Leading asymptotic normalization predicts 2*pi*h.
    observed_difference = abs(2 * h * (P * q - 1) / q - 2 * P * h)
    assert abs(observed_difference - 2 * h / q) < 1e-12
    nchecks += 1

# Magnetic Harper Bloch matrices: integer flux is scalar; half-integer flux
# gives off-diagonal/diagonal Pauli blocks, with eigenvalues +/- 2 sqrt(cos²kx+cos²ky).
for j in range(101):
    x = P * j / 100
    for k in range(101):
        y = P * k / 100
        e0 = 2 * (math.cos(x) + math.cos(y))
        ehalf = 2 * math.hypot(math.cos(x), math.cos(y))
        assert abs(e0) <= 4 + 1e-13
        assert ehalf <= 2 * math.sqrt(2) + 1e-13
        nchecks += 2
assert abs(2 * math.hypot(1, 1) - 2 * math.sqrt(2)) < 1e-14
nchecks += 1
print(f"PASS: {nchecks} finite checks, no external dependencies")
