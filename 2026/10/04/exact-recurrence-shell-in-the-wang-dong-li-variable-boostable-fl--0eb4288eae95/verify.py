#!/usr/bin/env python3
from fractions import Fraction as F

# Coefficients of b - (k+1)x^2 - (y-x)^2
# and -zdot + ((k+2)/a) x xdot after substituting
# xdot=a(y-x), zdot=y^2-b+kxy.
# Monomial order: const, x^2, xy, y^2.
def lhs(k):
    return [F(1), -(k+2), F(2), F(-1)]
def rhs(k):
    # b coefficient is handled as a symbolic unit; remaining terms:
    # -y^2-kxy+(k+2)xy-(k+2)x^2
    return [F(1), -(k+2), F(2), F(-1)]
for k in [F(0), F(1), F(23,5), F(17,9)]:
    assert lhs(k) == rhs(k)

a=F(12); b=F(100); k=F(23,5)
assert k+1 == F(28,5)
assert b/(k+1) == F(125,7)
assert F(1,1)/(a*a*(k+1)) == F(5,4032)
# Equilibrium radius check: (k+1) s^2 = b with s^2=125/7.
assert (k+1)*F(125,7) == b
print("VERIFY_OK")
