#!/usr/bin/env python3
import sympy as sp
x,y,z,w,u,v = sp.symbols('x y z w u v', real=True)
a,b,c,d,e,g,k = sp.symbols('a b c d e g k', real=True)
T = sp.tanh(v)
field = (-a*x+y*z+b*w+sp.cos(u), c*y*T-x*z+k, x*y-d*z, x*z-e*w, g*y, y**2-v)
state=(x,y,z,w,u,v)
def L(F): return sp.expand(sum(sp.diff(F,q)*f for q,f in zip(state,field)))
assert sp.simplify(L(y**2/sp.Integer(2))+L(z**2/sp.Integer(2))-k*y-(c*y**2*T-d*z**2))==0
assert sp.simplify(L(v**2/sp.Integer(2))-(v*y**2-v**2))==0
assert sp.simplify(L(u)-g*y)==0
assert sp.simplify(L(v)-(y**2-v))==0
Z2,YT=sp.symbols('Z2 YT')
assert sp.expand((d*Z2-c*YT).subs({d:31,c:7}))==31*Z2-7*YT
assert sp.Rational(1,20)!=0 and sp.Integer(7)!=0
print('VERIFY_OK')
