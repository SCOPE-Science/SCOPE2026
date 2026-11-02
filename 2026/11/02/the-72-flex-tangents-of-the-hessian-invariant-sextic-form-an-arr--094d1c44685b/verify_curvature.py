#!/usr/bin/env python3
"""Exact symmetric-differentiation and contact checks for the invariant sextic.
The accompanying incidence program provides a separate exact line-arrangement proof.
"""
import sympy as s
x,y,z,r=s.symbols('x y z r')
F=x**6+y**6+z**6-10*(x**3*y**3+x**3*z**3+y**3*z**3)
Q=[x*x-x*y-x*z+y*y-y*z+z*z,
   x*x-x*y-x*z+y*y+2*y*z+z*z,
   x*x-x*y+2*x*z+y*y-y*z+z*z,
   x*x+2*x*y-x*z+y*y-y*z+z*z]
H=s.hessian(F,(x,y,z)).det(method='berkowitz')
assert s.expand(H-108000*x*y*z*(x+y+z)*s.prod(Q))==0
assert s.expand(F.subs({x:0,y:1,z:r})-(r**6-10*r**3+1))==0
assert s.expand(F.subs(z,r*y)-x**3*(x**3-10*(1+r**3)*y**3)-y**6*(r**6-10*r**3+1))==0
# A sixfold ordinary-flex slice: substitution in F leaves exactly x^3 times a unit
# at each [0:1:r] when r^6-10r^3+1=0.
assert s.gcd(s.Poly(r**6-10*r**3+1,r),s.Poly(1+r**3,r)).degree()==0
assert s.gcd(s.Poly(r**6-10*r**3+1,r),s.Poly(6*r**5-30*r**2,r)).degree()==0
# The modular specialization of K=Q(omega,r) used for excluding coincidences
# extends to the subring of algebraic integers because the sextic is irreducible
# over Q(omega), as checked exactly using algebraic field arithmetic.
omega=(-1+s.sqrt(-3))/2
assert s.Poly(r**6-10*r**3+1,r,extension=[omega]).is_irreducible
# Verify the four primal projective generators underlying the dual incidence orbit.
def F3(a,b,c):return a**6+b**6+c**6-10*(a**3*b**3+a**3*c**3+b**3*c**3)
for xyz,scale in [((y,z,x),1),((x,omega*y,omega**2*z),1),
                  ((x+y+z,x+omega*y+omega**2*z,x+omega**2*y+omega*z),-27),
                  ((x,omega*y,omega*z),1)]:
    assert s.Poly(s.expand(F3(*xyz)-scale*F),x,y,z,extension=[omega]).is_zero
print('MASCHKE_HESSIAN_FACTOR_SMOOTH_SLICE_TANGENCY_IRREDUCIBILITY_PASS')
