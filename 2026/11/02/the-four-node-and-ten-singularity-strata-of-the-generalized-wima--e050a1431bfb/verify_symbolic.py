#!/usr/bin/env python3
"""Standalone symbolic identities supporting the genus-six/rational-sextic boundary."""
import sympy as s
x,y,z,X,Y,Z,a,b,u,v,t=s.symbols('x y z X Y Z a b u v t')
Q=X**3+Y**3+Z**3+a*(X**2*Y+Y**2*Z+Z**2*X)+b*(X*Y**2+Y*Z**2+Z*X**2)-3*(a+b+1)*X*Y*Z
S=x**6+y**6+z**6+a*(x**4*y**2+y**4*z**2+z**4*x**2)+b*(x**2*y**4+y**2*z**4+z**2*x**4)-3*(a+b+1)*x**2*y**2*z**2
assert s.expand(Q.subs({X:x*x,Y:y*y,Z:z*z})-S)==0
assert s.expand(Q.subs({X:1+u,Y:1+v,Z:1})-(a+b+3)*(u*u-u*v+v*v)-(u**3+a*u*u*v+b*u*v*v+v**3))==0
assert s.rem(1+a*t+b*t**2+t**3,t**2-t+1,t)==(a+b)*t-b
r=s.symbols('r')
P=t**3+a*t*t+b*t+1
D=a*a*b*b-4*(a**3+b**3)+18*a*b-27
assert s.expand(s.discriminant(P,t)-D)==0
P2=t**3+b*t*t+a*t+1
R=(a+b+2)*t**3-(a+2*b+3)*t**2+(b+3)*t-1
assert s.simplify(s.resultant(P2,R,t)+(a+b+3)**3*(a*a+a*b+b*b))==0
# For a triple root of the axis cubic, the boundary exclusions force the root to be -1.
L=s.rem((-3*r)+(3*r*r)+3,r**3+1,r)
W=s.rem((-3*r)**2+(-3*r)*(3*r*r)+(3*r*r)**2,r**3+1,r)
assert s.expand(L-3*(r*r-r+1))==0
assert s.expand(W-9*(r*r-r+1))==0
print('SYMBOLIC_VERIFY_OK')
