#!/usr/bin/env python3
import sympy as sp
x,y,z,w,a,b,c = sp.symbols("x y z w a b c", real=True)
F = sp.Matrix([a*z, b*w, -a*x + c*x*w, -b*y - c*x*z])
H = x*x + y*y + z*z + w*w
vars_ = (x,y,z,w)
Hdot = sp.expand(sum(sp.diff(H,v)*F[i] for i,v in enumerate(vars_)))
divF = sp.expand(sum(sp.diff(F[i],vars_[i]) for i in range(4)))
assert Hdot == 0
assert divF == 0
assert sp.simplify(F[2].subs({z:0,w:0})/(-a)) == x
assert sp.simplify(F[3].subs({z:0,w:0})/(-b)) == y
energy = sp.Rational(1)**2 + sp.Rational(11,10)**2 + sp.Rational(32,10)**2 + sp.Rational(33,10)**2
assert energy == sp.Rational(1167,50)
reported = [sp.Rational(4260,10**6), sp.Rational(5551,10**6), -sp.Rational(2850,10**6), -sp.Rational(6961,10**6)]
assert sum(reported) == 0
assert sum(1 for q in reported if q > 0) == 2
print("VERIFY_OK")
