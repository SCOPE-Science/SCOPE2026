#!/usr/bin/env python3
import sympy as sp

theta, eps = sp.symbols("theta eps", real=True)
c = sp.cos(theta)
f = 1 + eps*c**3
r = f**(-sp.Rational(1,3))

curvature_numerator = sp.simplify(
    (r**2 + 2*sp.diff(r,theta)**2 - r*sp.diff(r,theta,2))
    * f**(sp.Rational(8,3))
)
target = 1 + 2*eps*c - eps*c**3
assert sp.simplify(curvature_numerator-target) == 0

x = sp.symbols("x", real=True)
g = 2*x-x**3
assert sp.diff(g,x) == 2-3*x**2

c0 = -sp.sqrt(sp.Rational(2,3))
gmin = sp.simplify(g.subs(x,c0))
assert sp.simplify(gmin + 4*sp.sqrt(6)/9) == 0

estar = 3*sp.sqrt(6)/8
assert sp.simplify(1+estar*gmin) == 0
assert sp.simplify(estar-9/(4*sp.sqrt(6))) == 0

# Endpoint and nearby stress checks.
m091 = float((1+sp.Rational(91,100)*gmin).evalf(30))
m092 = float((1+sp.Rational(92,100)*gmin).evalf(30))
assert m091 > 0
assert m092 < 0

print("VERIFY_OK")
print("curvature_factorization = exact")
print("cubic_minimum = exact")
print("sharp_threshold = exact")
print("nearby_decimal_stress = passed")
