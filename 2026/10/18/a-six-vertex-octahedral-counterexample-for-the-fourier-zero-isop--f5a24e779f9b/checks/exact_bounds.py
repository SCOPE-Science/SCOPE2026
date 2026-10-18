"""Exact-rational sign and threshold certificate for a six-vertex Fourier example.

Only Python standard-library rational arithmetic is used.
"""
from fractions import Fraction
from math import factorial

x = Fraction(44935, 10000)
# G(t) = sin(t) - t*cos(t) has terms (-1)^(k+1) 2k*t^(2k+1)/(2k+1)!, k>=1.
# For k>=2, absolute term magnitudes strictly decrease at x; the k=10
# remainder immediately after the positive ninth term is negative.
S9 = sum(((-1)**(k+1))*Fraction(2*k, factorial(2*k+1))*x**(2*k+1)
         for k in range(1, 10))
assert S9 < -Fraction(3, 10000), (S9, float(S9))

# 24/17 < sqrt(2), since 24^2 < 2*17^2; and pi < 22/7.
assert 24**2 < 2*17**2
threshold_upper = Fraction(22,7) * x**3 / (2*Fraction(24,17))
assert threshold_upper < 101
print('OCTAHEDRAL_FOURIER_EXACT_CERTIFICATE_OK')
print('S9_upper:', S9)
print('threshold_upper:', threshold_upper)
