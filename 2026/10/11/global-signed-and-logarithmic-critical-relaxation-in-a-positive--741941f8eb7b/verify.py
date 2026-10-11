#!/usr/bin/env python3
"""Symbolic rational certificates and optional numerical sanity checks.

Requires Python 3 and SymPy. No network services or external files.
"""
import sympy as s
x,u=s.symbols('x u')
f=(2*x*x+x+8)/(8*x*x+3)
g=s.cancel(f.subs(x,f))
Q=224*x**4+32*x**3+408*x**2+128*x+539
assert s.cancel(f-1+(x-1)*(6*x+5)/(8*x*x+3))==0
assert s.cancel(g-x+56*(x-1)**3*(4*x*x+3*x+4)/Q)==0
assert s.cancel(g-1-(x-1)*(6*x+5)*(52*x*x+6*x+63)/Q)==0
v=s.cancel(g.subs(x,1+u)-1)
assert s.series(v,u,0,7).removeO().expand()==(u-s.Rational(56,121)*u**3+s.Rational(280,1331)*u**4+s.Rational(224,1331)*u**5-s.Rational(3136,14641)*u**6)
expr=s.cancel(1/v**2-1/u**2)
jet=s.series(expr,u,0,3).removeO().expand()
A=s.Rational(112,121); B=-s.Rational(560,1331); C=s.Rational(4480,14641)
assert jet==A+B*u+C*u*u
p=s.simplify(2*B/s.sqrt(A));q=s.simplify(C/A-(B/A)**2)
assert s.simplify(p+s.Rational(40,121)*s.sqrt(7))==0
assert q==s.Rational(15,121)
import math
for x0 in [0.3,2.0,8.0]:
    z=x0; sigma=1 if x0>1 else -1
    for j in range(1,2001):
        z=float((2*z*z+z+8)/(8*z*z+3))
        z=float((2*z*z+z+8)/(8*z*z+3))
    n=2000
    r=(z-1)**(-2)-float(A)*n-sigma*float(p)*math.sqrt(n)-float(q)*math.log(n)
    assert math.isfinite(r)
print('SYMBOLIC_EXACT_CHECK_OK; FINITE_SANITY_CHECK_OK')
