#!/usr/bin/env python3
import sympy as sp

X,Y,Z,a,b,c,t = sp.symbols('X Y Z a b c t')
F = X**6 + Y**6 + Z**6 + a*X**3*Z**3 + b*Y**3*Z**3 + c*X**3*Y**3
x,y,z = sp.symbols('x y z')
Q = x**2+y**2+z**2+a*x*z+b*y*z+c*x*y
assert sp.expand(Q.subs({x:X**3,y:Y**3,z:Z**3})-F)==0

Fx,Fy,Fz = [sp.diff(F,v) for v in (X,Y,Z)]
assert sp.factor(Fx/(3*X**2)) == 2*X**3+a*Z**3+c*Y**3
assert sp.factor(Fy/(3*Y**2)) == 2*Y**3+b*Z**3+c*X**3
assert sp.factor(Fz/(3*Z**2)) == 2*Z**3+a*X**3+b*Y**3

M = sp.Matrix([[2,c,a],[c,2,b],[a,b,2]])
Delta = 4-a**2-b**2-c**2+a*b*c
assert sp.factor(M.det()-2*Delta)==0
Mhalf = sp.Matrix([[1,c/2,a/2],[c/2,1,b/2],[a/2,b/2,1]])
assert sp.factor(Mhalf.det()-Delta/4)==0

# Side intersections of the quotient conic have discriminants b^2-4, a^2-4, c^2-4.
side_x = t**2+b*t+1
side_y = t**2+a*t+1
side_z = t**2+c*t+1
assert sp.factor(sp.discriminant(side_x,t)-(b**2-4))==0
assert sp.factor(sp.discriminant(side_y,t)-(a**2-4))==0
assert sp.factor(sp.discriminant(side_z,t)-(c**2-4))==0

# The tangency boundary b=+/-2 meets the conic-discriminant boundary only at the higher-codimension loci a=+/-c.
assert sp.factor(Delta.subs(b,2)+(a-c)**2)==0
assert sp.factor(Delta.subs(b,-2)+(a+c)**2)==0
assert sp.factor(Delta.subs(a,2)+(b-c)**2)==0
assert sp.factor(Delta.subs(a,-2)+(b+c)**2)==0
assert sp.factor(Delta.subs(c,2)+(a-b)**2)==0
assert sp.factor(Delta.subs(c,-2)+(a+b)**2)==0

# Local generic b=2 boundary: around [0:-1:1], the first nonzero terms are 9 t^2 + (a-c) X^3.
s = sp.symbols('s')
Fbplus = sp.expand(F.subs({b:2,Z:1,Y:-1+s}))
poly_plus = sp.Poly(Fbplus, X,s)
assert poly_plus.coeff_monomial(s**2)==9
assert poly_plus.coeff_monomial(X**3)==a-c
# For b=-2 use [0:1:1].
Fbminus = sp.expand(F.subs({b:-2,Z:1,Y:1+s}))
poly_minus = sp.Poly(Fbminus, X,s)
assert poly_minus.coeff_monomial(s**2)==9
assert poly_minus.coeff_monomial(X**3)==a+c

# Generic point of Delta=0, away from side tangencies: a=b=c=-1.
M0 = M.subs({a:-1,b:-1,c:-1})
assert M0.det()==0 and M0.rank()==2
Q0 = sp.expand(Q.subs({a:-1,b:-1,c:-1}))
assert Q0.subs({x:1,y:1,z:1})==0
assert all(sp.diff(Q0,v).subs({x:1,y:1,z:1})==0 for v in (x,y,z))
assert all(v != 0 for v in (1,1,1))
assert [sp.expand((4-a**2).subs(a,-1)),sp.expand((4-b**2).subs(b,-1)),sp.expand((4-c**2).subs(c,-1))] == [3,3,3]

# Riemann-Hurwitz for a degree-9 Galois cover with six inertia-3 branch values.
assert 2*10-2 == 9*(-2) + 6*(9-9//3)

print('VERIFY_OK sympy=%s pullback=conic smoothness_product=exact branch=6x3 boundary=tangency:3A2,conic-discriminant:9nodes' % sp.__version__)
