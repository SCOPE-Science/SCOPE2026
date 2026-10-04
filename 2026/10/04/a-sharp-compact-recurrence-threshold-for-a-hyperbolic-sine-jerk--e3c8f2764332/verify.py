#!/usr/bin/env python3
import sympy as sp
x, y, z, a, b, c, d = sp.symbols("x y z a b c d", real=True)
xd = y
yd = z
zd = -a*x - b**2*y - c*z + d*sp.sinh(x)
P = x*z - sp.Rational(1,2)*y**2 + c*x*y + sp.Rational(1,2)*b**2*x**2
Pdot = sp.diff(P,x)*xd + sp.diff(P,y)*yd + sp.diff(P,z)*zd
expected = c*y**2 + (d-a)*x**2 + d*x*(sp.sinh(x)-x)
assert sp.simplify(Pdot - expected) == 0
assert sp.simplify(Pdot - (-a*x**2 + c*y**2 + d*x*sp.sinh(x))) == 0
# At y=z=0 and d*sinh(x)=a*x, the only nontrivial residual is zero by that relation.
residual = zd.subs({y:0,z:0})
assert sp.simplify(residual - (-a*x + d*sp.sinh(x))) == 0
# Derivative controlling strict monotonicity of sinh(x)/x.
h = x*sp.cosh(x)-sp.sinh(x)
assert sp.simplify(sp.diff(h,x) - x*sp.sinh(x)) == 0
print("VERIFY_OK")
