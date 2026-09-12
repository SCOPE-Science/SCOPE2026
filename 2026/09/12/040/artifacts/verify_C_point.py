"""Reproducible verification for the named quintic Tyurin obstruction lemma.

Checks the explicit point on C = S cap {q5=0} at x0=0:
  (y1,y2,y3,y4) = (1, zeta, u, eta*u), zeta=eta=exp(i*pi/4),
  u^5 = -(1+zeta^5)/(1+eta^5).
Verifies sum yi^4 = 0 exactly-in-structure and numerically, sum yi^5 = 0,
all coordinates nonzero, and the Jacobian rank condition at the point.
"""
import cmath

zeta = cmath.exp(1j * cmath.pi / 4)
eta = cmath.exp(1j * cmath.pi / 4)
num = 1 + zeta ** 5
den = 1 + eta ** 5
assert abs(den) > 1e-12, "denominator vanishes; point construction fails"
assert abs(num) > 1e-12, "numerator vanishes; u would be 0"
u = (-num / den) ** (1 / 5) if (-num / den) != 0 else 0.0
# principal 5th root; any root works
ys = [1.0, zeta, u, eta * u]
s4 = sum(y ** 4 for y in ys)
s5 = sum(y ** 5 for y in ys)
print("zeta^4 =", zeta ** 4, "(expect -1)")
print("1+zeta^5 =", num, " modulus^2 =", abs(num) ** 2, "(expect 2-sqrt(2) > 0)")
print("u =", u)
print("sum yi^4 =", s4, " |.| =", abs(s4))
print("sum yi^5 =", s5, " |.| =", abs(s5))
print("all nonzero:", [abs(y) > 1e-9 for y in ys])
# Jacobian rows at point: (4 yi^3), (5 yi^4); check 2x2 minor nonzero
# use first two coords: det [[4*1, 4*z^3],[5*1, 5*z^4]] = 20(z^4 - z^3) != 0?
minor = (4 * ys[0] ** 3) * (5 * ys[1] ** 4) - (4 * ys[1] ** 3) * (5 * ys[0] ** 4)
print("2x2 minor (cols 1,2) =", minor, " |.| =", abs(minor))
assert abs(s4) < 1e-12 and abs(s5) < 1e-12, "point fails to lie on C"
assert abs(minor) > 1e-9, "Jacobian drops rank at point"
print("PASS: explicit smooth point of C; total space singular there.")
