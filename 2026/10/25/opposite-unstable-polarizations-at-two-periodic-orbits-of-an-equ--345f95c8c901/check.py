"""Standalone exact geometry and 2x2 collision cocycle diagnostics.
Uses only public geometry and standard specular reflection.
"""
import sympy as s
from math import acosh, sqrt, isclose
D=s.Integer(1)
r=s.Rational(1,20)
c=s.sqrt(3)/2
B=s.symbols('B',positive=True)
# Ellipsoid x^2+y^2+B^2 z^2=r^2, local x graph at (r,0,0)
y,z=s.symbols('y z')
x=s.sqrt(r*r-y*y-B*B*z*z)
assert s.simplify(-s.diff(x,y,2).subs({y:0,z:0})-1/r)==0
assert s.simplify(-s.diff(x,z,2).subs({y:0,z:0})-B**2/r)==0
C=[s.Matrix([D/s.sqrt(3)*s.cos(2*s.pi*j/3),D/s.sqrt(3)*s.sin(2*s.pi*j/3)]) for j in range(3)]
Q=[(1-r*s.sqrt(3)/D)*v for v in C]
flights=[s.simplify(s.sqrt((Q[(j+1)%3]-Q[j]).dot(Q[(j+1)%3]-Q[j]))) for j in range(3)]
assert all(s.simplify(v-(D-s.sqrt(3)*r))==0 for v in flights)
for j in range(3):
    vin=s.simplify((Q[j]-Q[(j-1)%3])/flights[j])
    vout=s.simplify((Q[(j+1)%3]-Q[j])/flights[j])
    n=-C[j]/s.sqrt(C[j].dot(C[j]))
    assert s.simplify(vin-2*(vin.dot(n))*n-vout)==s.zeros(2,1)
    assert s.simplify(n.dot(vout)-c)==0
psi_par=2/(r*c)
psi_perp=2*B**2*c/r
assert s.solve(s.Eq(psi_par,psi_perp),B)==[2/s.sqrt(3)]
# P = [[1,l],[psi,1+l psi]], det=1, spectral radius=e^acosh(1+l psi/2)
def radius(ell,psi):
    P=s.Matrix([[1,ell],[psi,1+ell*psi]])
    assert s.simplify(P.det()-1)==0
    return s.simplify(P.trace()/2)
l2=D-2*r;l3=flights[0]
assert s.simplify(radius(l2,2/r)-(1+l2/r))==0
assert s.simplify(radius(l2,2*B**2/r)-(1+l2*B**2/r))==0
assert s.simplify(radius(l3,psi_par)-(1+l3/(r*c)))==0
assert s.simplify(radius(l3,psi_perp)-(1+l3*B**2*c/r))==0
for beta in [1.01,1.06,1.12,1.15]:
    a2p=acosh(float(1+l2/r));a2v=acosh(float(1+beta**2*l2/r))
    a3p=acosh(float(1+l3/(r*c)));a3v=acosh(float(1+beta**2*c*l3/r))
    assert a2v>a2p and a3p>a3v
crit=2/sqrt(3)
assert isclose(acosh(float(1+l3/(r*c))),acosh(float(1+crit**2*c*l3/r)),abs_tol=1e-12)
for beta in [1.17,1.4,2.0]:
    assert acosh(float(1+beta**2*c*l3/r))>acosh(float(1+l3/(r*c)))
print('SYMBOLIC_REFLECTION_CURVATURE_MONODROMY_PASS')
print('INVERTED_PERIODIC_POLARIZATIONS_PASS 4')
print('EXACT_CRITICAL_BETA',str(s.simplify(2/s.sqrt(3))))
print('CRITICAL_DEGENERACY_AND_REVERSAL_PASS')
print('ALL_CHECKS_PASS')
