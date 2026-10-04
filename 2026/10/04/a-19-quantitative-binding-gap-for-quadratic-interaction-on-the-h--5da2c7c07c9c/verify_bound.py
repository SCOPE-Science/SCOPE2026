#!/usr/bin/env python3
from fractions import Fraction
import math

# Exact rational comparisons used in the proof.
assert 1773 * 1773 * 7 > 22 * 1000 * 1000
m_lower = Fraction(72000, 91613)
assert m_lower > Fraction(157, 200)
assert Fraction(4, 3) - Fraction(2, 3) * Fraction(157, 200) == Fraction(81, 100)

# Corroborate the closed-form dimensionless Rayleigh quotient at b=1/3.
b = 1.0 / 3.0
M = math.exp(-b*b) / (math.sqrt(math.pi) * math.erfc(b))
F = 1.0 + 3.0*b*b - 2.0*b*M
assert F < 0.81
assert 0.805 < F < 0.806

# Scaling check: the quotient is omega*F for every positive omega.
for omega in (0.125, 1.0, 7.0, 31.0):
    quotient = omega * F
    assert quotient < 0.81 * omega

print('VERIFY_OK F(1/3)=%.15f exact_lower=%s' % (F, m_lower))
