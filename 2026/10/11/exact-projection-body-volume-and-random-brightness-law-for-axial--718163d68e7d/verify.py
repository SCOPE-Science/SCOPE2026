#!/usr/bin/env python3
"""Symbolic checks for the exact axial-cubic brightness theorem.

Requires SymPy. This is an algebraic reproducibility check, not an
independent proof of the continuous support-function criterion.
"""
from sympy import (symbols, Rational, S, pi, diff, integrate, simplify,
                   expand, factor, cos, sin, acos, sqrt, trigsimp)

z, t, tau, theta, y = symbols('z t tau theta y', real=True)
x1, x2, x3 = symbols('x1 x2 x3', real=True)
F = x3**3 - Rational(3, 5)*x3*(x1*x1+x2*x2+x3*x3)
assert simplify(diff(F, x1, 2)+diff(F, x2, 2)+diff(F, x3, 2)) == 0
p = z**3-Rational(3, 5)*z
h = 1 + t*p
az = expand(h-z*diff(h, z))
mer = expand(az+(1-z*z)*diff(h, z, 2))
assert az == 1-2*t*z**3
assert simplify(mer-(1+t*(6*z-8*z**3))) == 0
assert simplify(az.subs(t, Rational(1, 2))-(1-z)*(z*z+z+1)) == 0
assert simplify(mer.subs(t, Rational(1, 2))-(1-z)*(2*z+1)**2) == 0
# The only stationary points of the cubic meridional perturbation
# on [-1,1] are z=+/-1/2; evaluate the four endpoints/stationary points.
g = 6*z-8*z**3
assert simplify(diff(g,z)-6*(1-4*z*z)) == 0
assert [g.subs(z,v) for v in [-1,-Rational(1,2),Rational(1,2),1]] == [2,-2,2,-2]
# Restriction of the zonal cubic to a great circle, retaining translation.
plane = tau**3*cos(theta)**3-Rational(3,5)*tau*cos(theta)
three = tau**3*cos(3*theta)/4
one = (Rational(3,4)*tau**3-Rational(3,5)*tau)*cos(theta)
assert trigsimp(plane-three-one) == 0
A = t*tau**3/4
angle_support = 1+A*cos(3*theta)
plane_area = simplify(integrate(expand(angle_support**2-diff(angle_support,theta)**2),
                                (theta,0,2*pi))/2)
assert simplify(plane_area-pi*(1-t*t*tau**6/4)) == 0
# Area measure is the determinant of the two spherical curvature radii.
detQ = expand(az*mer)
vol = simplify(2*pi*integrate(expand(h*detQ),(z,-1,1))/3)
surface = simplify(2*pi*integrate(detQ,(z,-1,1)))
assert simplify(vol-(4*pi/3-16*pi*t*t/35)) == 0
assert simplify(surface-(4*pi-16*pi*t*t/35)) == 0
# The projection body has support b(v)=pi*(1-k*(1-z*z)^3), k=t*t/4.
k = symbols('k', real=True)
q = 1-k*(1-z*z)**3
qaz = expand(q-z*diff(q,z))
qmer = expand(qaz+(1-z*z)*diff(q,z,2))
proj_integral = simplify(integrate(expand(q*qaz*qmer),(z,-1,1)))
proj_volume = simplify(2*pi**4*proj_integral/3)
proj_expected = (4*pi**4/3)*(1-Rational(12,35)*t*t-Rational(32,1001)*t**4+Rational(640,46189)*t**6)
assert simplify(proj_volume.subs(k,t*t/4)-proj_expected) == 0
normalized = 1-Rational(12,35)*t*t-Rational(32,1001)*t**4+Rational(640,46189)*t**6
assert simplify(normalized.subs(t,Rational(1,2))-Rational(1475168,1616615)) == 0
assert simplify(diff(normalized,t)-8*t*(16800*t**4-25840*t*t-138567)/1616615)==0
# A uniform direction has z=cos(theta) uniform on [-1,1].
EY = simplify(integrate((1-z*z)**3,(z,-1,1))/2)
assert EY == Rational(16,35)
assert simplify(4*pi*(1-t*t*EY/4)-surface) == 0
cdf = 1-sqrt(1-y**Rational(1,3))
pdf = 1/(6*y**Rational(2,3)*sqrt(1-y**Rational(1,3)))
assert simplify(diff(cdf,y)-pdf) == 0
assert simplify(cdf.subs(y,0)) == 0
assert simplify(cdf.subs(y,1)) == 1
assert simplify(4*pi/3-16*pi*(Rational(1,2))**2/35-Rational(128,105)*pi)==0
print('VERIFY_OK')
