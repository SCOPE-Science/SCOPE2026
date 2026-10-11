#!/usr/bin/env python3
import sympy as sp

s, x, y = sp.symbols("s x y", real=True)
F = (
    s**4*x**4 - s**4*x**2 + 2*s**3*x**3 - 2*s**3*x
    + 3*s**2*x**2 - 2*s**2 + 2*s*x + 1
)
Fx = sp.diff(F, x)
Q = s**6 - 4*s**4 + 23*s**2 - 9

assert sp.factor(F.subs(x, -1)) == (s-1)**2
assert sp.factor(F.subs(x, 1)) == (s+1)**2
assert sp.factor(sp.resultant(F, Fx/(2*s), x)) == -s**16*Q

# Q is strictly increasing for s>0 because 3 y^2-8 y+23 is positive.
assert sp.discriminant(3*y**2 - 8*y + 23, y) < 0
assert (3*y**2 - 8*y + 23).subs(y, 0) > 0
assert Q.subs(s, 0) < 0 and Q.subs(s, 1) > 0

lo = sp.Rational(646983632244827, 10**15)
hi = sp.Rational(646983632244828, 10**15)
assert Q.subs(s, lo) < 0 < Q.subs(s, hi)

P = y**3 - 4*y**2 + 23*y - 9
assert P.subs(y, sp.Rational(2,5)) < 0
assert P.subs(y, sp.Rational(1,2)) > 0

subs = sp.subresultants(F, Fx/(2*s), x)
linear = sp.factor(subs[-2] / (-s**12))
expected_linear = s**5*x + s**4 - 4*s**3*x - 11*s**2 - 3*s*x + 3
assert sp.expand(linear - expected_linear) == 0

N = y**2 - 11*y + 3
D = y**2 - 4*y - 3
margin = sp.rem(sp.expand(y*D**2 - N**2), P, domain=sp.QQ)
assert sp.factor(margin) == -23*y**2 + 283*y - 108
assert margin.subs(y, sp.Rational(2,5)) == sp.Rational(38,25)
assert sp.diff(margin,y).subs(y, sp.Rational(1,2)) > 0

rho = sp.sqrt(sp.RootOf(P, 0))
xrho = -(rho**4 - 11*rho**2 + 3)/(rho*(rho**4 - 4*rho**2 - 3))
assert -1 < sp.N(xrho, 50) < 0
assert abs(sp.N(F.subs({s:rho, x:xrho}), 60)) < sp.Float('1e-50')
assert abs(sp.N(Fx.subs({s:rho, x:xrho}), 60)) < sp.Float('1e-50')

print('VERIFY_OK')
print('rho =', sp.N(rho, 50))
print('x_rho =', sp.N(xrho, 50))
print('resultant =', sp.factor(sp.resultant(F, Fx/(2*s), x)))
