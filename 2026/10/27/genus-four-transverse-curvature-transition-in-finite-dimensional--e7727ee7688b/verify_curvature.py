#!/usr/bin/env python3
"""Standalone exact rational checks and independent high-precision diagnostics.
No claims about independent external mathematical validation are made.
"""
from fractions import Fraction as F
from math import log

# Positive-coefficient power series for the gamma-ratio logarithmic defect.
def coeff(k):
    assert k >= 3 and k % 2 == 1
    return F(2 * (2**k - 2) * (1 + 3**k - 2**(k+1)), k)

# The k=3 contribution is (48*zeta(3))*a**3.
assert coeff(3) == 48
assert all(coeff(k) > 0 for k in range(3, 32, 2))
low3 = sum(coeff(k) / (7**k) for k in (3, 5, 7, 9, 11))
assert low3 == F(865827184, 1977326743)
assert low3 > F(5, 12)
# For d>=4, a=1/(2d+1)<=1/9. Bounds zeta(3)<=5/4 and zeta(5)<=9/8.
up4 = F(60, 729) + F(2,5)*F(9,8)*F(2,3)**5/(1-F(2,3)**2)
assert up4 == F(1148, 6075) and up4 < F(2,5)
# Elementary strict logarithm comparisons, with an independently numeric diagnostic only.
assert log(1.5) < float(F(5,12))
assert log(1.5) > float(F(2,5))

try:
    import mpmath as mp
    mp.mp.dps = 45
    for d in (3, 4, 5, 6, 8, 16):
        m = 2*d + 1
        cs = []
        for j in range(3):
            a = mp.mpf(j+1) / m
            cs.append(mp.gamma(1-a)*mp.gamma(mp.mpf('.5')+a) / (mp.gamma(a)*mp.gamma(mp.mpf('.5')-a)))
        E = mp.log((mp.mpf(3)/4)*cs[1]**2/(cs[0]*cs[2]))
        kappa = 2 - 4*cs[0]*cs[2]/cs[1]**2
        assert E > 0 and ((d == 3 and kappa > 0) or (d >= 4 and kappa < 0))
        if d == 3: assert E > mp.mpf(low3.numerator) / low3.denominator
        if d >= 4: assert E < mp.mpf(up4.numerator) / up4.denominator
        print(f'd={d}: E={mp.nstr(E,18)}; normalized curvature={mp.nstr(kappa,18)}')
except ImportError:
    print('mpmath not installed; exact rational proof bounds verified, decimal diagnostics skipped')
print('PASS: exact genus-three and all-genus-four-plus bounds; polynomial-series coefficients; optional gamma diagnostics')
