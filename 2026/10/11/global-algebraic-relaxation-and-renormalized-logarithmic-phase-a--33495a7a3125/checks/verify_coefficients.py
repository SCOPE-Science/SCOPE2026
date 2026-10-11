#!/usr/bin/env python3
"""Exact one-turn coefficient checks for the cubic Liénard oscillator.
Requires Python 3 and SymPy. Finite symbolic identities do not replace the global analytic proof.
"""
import sympy as sp
x,y,mu=sp.symbols('x y mu',real=True,nonzero=True)
H=sp.exp(-2*mu*y)*x**2/sp.Integer(2)+(1-(1+2*mu*y)*sp.exp(-2*mu*y))/(4*mu**2)
xd=y-mu*x*x-x**3
yd=-x
assert sp.simplify(sp.diff(H,x)*xd+sp.diff(H,y)*yd+sp.exp(-2*mu*y)*x**4)==0
th=sp.symbols('th',real=True)
c=sp.cos(th); s=sp.sin(th)
u=-mu*(s-s**3/sp.Integer(3))
assert sp.simplify(sp.diff(u,th)+mu*c**3)==0
rad_cubic=sp.expand_trig(-2*mu*c**3*u+mu**2*c**5*s-c**4)
ret=sp.simplify(sp.integrate(rad_cubic,(th,0,2*sp.pi)))
assert sp.simplify(ret+3*sp.pi/sp.Integer(4))==0
per_second=-mu*c*c*s*u+mu**2*c**4*s*s-c**3*s
val=sp.simplify(sp.integrate(sp.expand_trig(per_second),(th,0,2*sp.pi)))
assert sp.simplify(val-sp.pi*mu**2/3)==0
assert sp.simplify(val/(2*(3*sp.pi/4))-2*mu**2/9)==0
print('CHECK_OK')
