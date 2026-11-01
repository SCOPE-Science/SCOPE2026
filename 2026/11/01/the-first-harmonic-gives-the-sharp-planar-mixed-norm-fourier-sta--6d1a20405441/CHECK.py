#!/usr/bin/env python3
"""Exact rational certificates for the high-exponent Bessel-mode comparison.

Requires only the Python standard library. The proof of the analytic Bessel
estimates used with these identities appears in the cited references.
"""
from fractions import Fraction as F
from math import comb

# U(x) = x/8 - x^2/96 + x^3/3072 - x^4/184320 + x^5/17694720
power = [F(1,2),-F(2),F(8,3),-F(4,3),F(16,45),-F(8,135)]
N=20
bernstein=[sum(power[l]*F(comb(j,l),comb(N,l)) for l in range(min(5,j)+1)) for j in range(N+1)]
assert min(bernstein) == F(61,43605)
assert bernstein.index(min(bernstein)) == 11
assert min(bernstein) > 0
# At x = 16 the lower alternating series has positive factor Q(16) = 7/45.
assert 1-F(16,12)+F(16**2,384)-F(16**3,23040) == F(7,45)
# Its derivative multiplied by 7680 is -(x^2-40x+640),
# whose discriminant 40^2-4*640 is negative.
assert 40**2-4*640 < 0
# Concavity polynomial L''(r) is negative: discriminant in r^2.
assert 160**2 - 4*7*1152 < 0

def L(r):
    return r/2-r**3/16+r**5/384-r**7/18432
assert L(F(8,5)) > F(9,16)
assert L(F(21,10)) > F(9,16)
assert (F(21,10)**2-F(8,5)**2)/2 == F(37,40)
# The rational majorant of the uniform sixth moment is < 1/3.
assert 2*F(7,10)**6 + F(4,45) < F(1,3)
# Landau bound for k>=3 is below 1/2 (cube both positive sides).
assert F(7,5)**3 < 3
# At q=27, the lower first-mode bound beats all higher-mode ceilings.
assert F(37,40)*F(9,8)**27 > F(64,3)
print('PASS: all rational polynomial and threshold certificates')
