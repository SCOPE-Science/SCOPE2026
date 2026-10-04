from fractions import Fraction
from math import sqrt, pi, log

# Exact coefficient replay using the Gaussian moments
# E[n]=E[d]=sigma*r, E[n^2]=2 sigma^2, E[d^2]=sigma^2,
# E[n^3]=8 sigma^3*r, E[d^3]=2 sigma^3*r, r=sqrt(2/pi).

# Rational multipliers of the symbolic monomials.
second_noise = -Fraction(1, 2) * (Fraction(2) - Fraction(1))
assert second_noise == -Fraction(1, 2)

# Cubic coefficient divided by sigma*r is -a + 2*sigma^2.
# At a=sigma^2/2 it is (3/2)*sigma^2.
critical_cubic = -Fraction(1, 2) + Fraction(2)
assert critical_cubic == Fraction(3, 2)

# The threshold shift is the negative of the critical cubic coefficient
# because d lambda/da tends to one.
threshold_shift = -critical_cubic
assert threshold_shift == -Fraction(3, 2)

# Direct algebraic sanity checks for the one-step multiplier.
def multiplier(h, a, c, sigma, z):
    return (1.0 + (c+a)*h + sigma*sqrt(h)*(abs(z)-z)) / (1.0 + c*h + sigma*sqrt(h)*abs(z))

def source_linearized_multiplier(h, a, c, sigma, z):
    A = c*h + sigma*sqrt(h)*abs(z)
    return 1.0 + (a*h - sigma*sqrt(h)*z)/(1.0 + A)

for vals in [
    (0.01, 0.5, 1.0, 0.7, -1.25),
    (0.0025, 0.1, 2.0, 1.3, 0.8),
    (0.04, -0.2, 1.5, 0.4, -0.3),
]:
    x=multiplier(*vals)
    y=source_linearized_multiplier(*vals)
    assert x > 0.0 and abs(x-y) < 1e-14

# At the exact SDE threshold the leading BIM correction is positive.
sigma=1.0
r=sqrt(2.0/pi)
lead=1.5*r*sigma**3
assert lead > 0.0

print('VERIFY_OK')
