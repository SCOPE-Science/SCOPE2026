"""Reproduce the polynomial and ellipse-integral identities for a quadratic flow.

Requires SymPy.  This script checks exact algebraic statements, not infinite-time
behavior, existence of attractors, or historical originality.
"""
import sympy as sp
x, y, z = sp.symbols('x y z', real=True)
F = sp.Matrix([y + 2*x*y + x*z, 1-2*x*x + y*z, x-x*x-y*y])
V = (x-1)**2 + y*y + (z+1)**2
Q = x*x+x*y+y*y-x
assert sp.expand(sp.Matrix([sp.diff(V,v) for v in (x,y,z)]).dot(F)+2*Q)==0
X,Y=sp.symbols('X Y',real=True)
assert sp.expand(Q.subs({x:X+sp.Rational(2,3),y:Y-sp.Rational(1,3)})) == X*X+X*Y+Y*Y-sp.Rational(1,3)
A=sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]])
c=sp.Rational(1,3)
area=sp.simplify(sp.pi*c/sp.sqrt(A.det()))
assert sp.simplify(area-2*sp.pi/(3*sp.sqrt(3)))==0
# Ellipse E is the affine image of the disk of radius sqrt(c) under A^{-1/2}.
# Its uniform second moment about its centroid is (c/4) A^{-1}.
m=sp.Matrix([sp.Rational(2,3),-sp.Rational(1,3)])
center=sp.Matrix([1,0])
mean_rho2=sp.simplify(((m-center).dot(m-center)) + (c* A.inv()/4).trace())
assert mean_rho2 == sp.Rational(4,9)
# The outgoing normal flux integrates -Q/R on the large sphere.
# The average of -Q over E is c/2 by a disk change of variables.
positive_integral=sp.simplify(area*c/2)
assert sp.simplify(positive_integral-sp.pi/(9*sp.sqrt(3)))==0
lead_area=sp.simplify(area/(2*sp.pi))
lead_flux=sp.simplify(2*positive_integral)
assert sp.simplify(lead_area-1/(3*sp.sqrt(3)))==0
assert sp.simplify(lead_flux-2*sp.pi/(9*sp.sqrt(3)))==0
# Reversibility: S*F = -F(S*x)
S=sp.diag(1,-1,-1)
assert all(sp.expand(v)==0 for v in S*F+F.subs({x:x,y:-y,z:-z}, simultaneous=True))
assert sp.expand(sum(sp.diff(F[i], (x,y,z)[i]) for i in range(3))-2*(y+z))==0
print('PASS: exact radial identity, ellipse location/area/moment, leading outward-area and flux constants, reversibility, divergence')
print('elliptic area', area, 'rho2 mean',mean_rho2,'area fraction coefficient',lead_area,'flux coefficient',lead_flux)
