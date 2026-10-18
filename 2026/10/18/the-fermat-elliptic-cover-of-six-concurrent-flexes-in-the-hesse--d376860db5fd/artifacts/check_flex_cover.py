#!/usr/bin/env python3
"""Exact symbolic checks for the flex-incidence morphism on a cubic."""
import sympy as s
X,Y,Z,g,t,z,w=s.symbols('X Y Z g t z w')
phi=X**3+Y**3+Z**3-3*g*X*Y*Z
F=s.expand(s.Rational(2,3)*(s.diff(phi,Z,2)*phi-s.Rational(1,2)*s.diff(phi,Z)**2))
assert s.expand(F-(4*Z*(X**3+Y**3)+Z**4-6*g*X*Y*Z**2-3*g**2*X**2*Y**2))==0
G=s.expand(F.subs({X:t,Y:1,Z:z}))
assert s.expand(G-(z**4-6*g*t*z**2+4*(t**3+1)*z-3*g**2*t**2))==0
assert s.expand(s.diff(G,z,2)-12*(z*z-g*t))==0
assert s.expand((s.diff(G,z)/4).subs(g,z**2/t)-(t**3+1-2*z**3))==0
assert s.factor(G.subs(g,z**2/t)-(z**4-6*z**4+4*(t**3+1)*z-3*z**4))==0
assert s.factor((z**4-6*z**4+4*(2*z**3)*z-3*z**4))==0
assert s.diff(G,z,3)==24*z
poly=s.expand((t**3+1)**2-4*g**3*t**3)
assert s.factor(s.discriminant(poly,t))==2985984*g**9*(g-1)**3*(g*g+g+1)**3
H=t**3+1-2*z**3
assert s.expand(t**3*H.subs({t:1/t,z:z/t})-H)==0
assert s.expand(H.subs({t:w*t,z:w**2*z})-H).subs(w**3,1)==0
# Local smoothness condition in Z=1; the two partials imply a=u^3=v^3.
u,v,A=s.symbols('u v A')
Fuv=s.expand(F.subs({X:u,Y:v,Z:1}))
vw=u*v
assert s.expand(u*s.diff(Fuv,u)/6-(2*u**3-g*vw*(1+g*vw)))==0
assert s.expand(v*s.diff(Fuv,v)/6-(2*v**3-g*vw*(1+g*vw)))==0
Fw=8*A+1-6*g*vw-3*g*g*vw*vw
assert s.expand(Fw.subs(A,g*vw*(1+g*vw)/2)-(g*vw-1)**2)==0
# The ramification criterion away from zero uses t^3=z^3 and H=0, hence t^3=z^3=1.
a,b=s.symbols('a b')
assert s.solve_poly_system([a+1-2*b,a-b],a,b)==[(1,1)]
print('FLEX_INCIDENCE_FERMAT_S3_EXACT_OK')
