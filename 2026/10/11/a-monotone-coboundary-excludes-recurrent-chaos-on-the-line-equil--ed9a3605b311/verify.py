#!/usr/bin/env python3
from fractions import Fraction

# Monomials are keyed by exponents of (g, m, x, y).
def add(poly, key, coeff):
    poly[key] = poly.get(key, Fraction(0)) + Fraction(coeff)
    if poly[key] == 0:
        del poly[key]

p = {}

# zdot = g*m*x^2 - g*(1+m)*x*y
add(p, (1, 1, 2, 0), 1)
add(p, (1, 0, 1, 1), -1)
add(p, (1, 1, 1, 1), -1)

# (g(1+m)/r) x * xdot, with xdot = r(y-x)
add(p, (1, 0, 1, 1), 1)
add(p, (1, 1, 1, 1), 1)
add(p, (1, 0, 2, 0), -1)
add(p, (1, 1, 2, 0), -1)

expected = {(1, 0, 2, 0): Fraction(-1)}
assert p == expected, (p, expected)

m = Fraction(11, 10)
r = Fraction(61, 10)
g = Fraction(12, 1)
coef = g * (1 + m) / (2 * r)
assert coef == Fraction(126, 61), coef

# Published line-equilibrium parameters.
par = dict(m=m, r=r, g=g, k1=0, k2=g, k3=0, k4=0, k5=0, k6=-100)
x = y = z = u = v = Fraction(0)
xd = par["r"] * (y - x) + par["k1"] * u
yd = par["m"] * x - (1 + par["m"]) * y + x * z + v
zd = par["g"] * (par["m"] * x*x + 1 - (1 + par["m"]) * x*y) - par["k2"] - par["k3"] * z
ud = par["k4"] * x*y - par["k5"] * u
vd = par["k6"] * x + x*z - u
assert (xd, yd, zd, ud, vd) == (0, 0, 0, 0, 0)

print("VERIFY_OK")
