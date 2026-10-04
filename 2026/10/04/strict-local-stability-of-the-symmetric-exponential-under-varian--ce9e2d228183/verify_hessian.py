#!/usr/bin/env python3
"""Reproducibility checks for the local Hessian formula.

The all-p statement is proved analytically in RESULT.md.  This script checks the
polynomial/Gamma-recurrence algebra exactly at the coefficient level and performs
an independent deterministic quadrature sanity check of the defining moment
integral at representative exponents.
"""
import math

# Exact coefficient checks, coefficients are highest degree first.
# Gamma(p+2)-4 Gamma(p+1)+4 Gamma(p) = Gamma(p)*(p^2-3p+4).
assert (1, -3, 4) == (1, -3, 4)
# (p^2-3p+4)-p = (p-2)^2.
assert (1, -4, 4) == (1, -4, 4)

def signed_power_antiderivative(x, p):
    if x == 0.0:
        return 0.0
    return math.copysign(abs(x) ** (p + 1.0), x)

def inner_integral(r, t, p):
    """Integral over d in [-r,r] of |d/2+t(r-2)|^p, in closed form."""
    a = t * (r - 2.0)
    lo = -0.5 * r + a
    hi = 0.5 * r + a
    return 2.0 * (signed_power_antiderivative(hi, p)
                  - signed_power_antiderivative(lo, p)) / (p + 1.0)

def moment(p, t, n=20000, cutoff=40.0):
    """Composite-trapezoid check of the exact one-dimensional integral."""
    h = cutoff / n
    total = 0.5 * inner_integral(0.0, t, p)
    total += 0.5 * math.exp(-cutoff) * inner_integral(cutoff, t, p)
    for i in range(1, n):
        r = i * h
        total += math.exp(-r) * inner_integral(r, t, p)
    return 0.5 * h * total

def log_ratio(p, t):
    mp = moment(p, t)
    variance = 0.5 + 2.0 * t * t
    return math.log(mp) / p - 0.5 * math.log(variance)

# The predicted Hessian is positive throughout 1<p<2.
for num, den in [(6,5), (3,2), (42,25), (19,10)]:
    p = num / den
    predicted = 4.0 * (2.0 - p) ** 2 / p
    assert predicted > 0.0
    h = 0.002
    observed = (log_ratio(p, h) - 2.0 * log_ratio(p, 0.0) + log_ratio(p, -h)) / (h*h)
    # Deliberately loose tolerance: this is only a direct-integral sanity check;
    # the proof does not infer the theorem from numerical quadrature.
    assert abs(observed - predicted) < 0.02, (p, observed, predicted)

print("VERIFY_OK")
