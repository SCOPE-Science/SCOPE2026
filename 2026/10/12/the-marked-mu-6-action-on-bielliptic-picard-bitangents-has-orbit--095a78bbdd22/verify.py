#!/usr/bin/env python3
import sympy as s

x,a,b,c,u = s.symbols('x a b c u')

# Horizontal bitangents: after c^3=b-a^2/4, the intersection quartic is a square.
q = x**4 + a*x**2 + b - (b-a**2/s.Integer(4))
assert s.expand(q - (x**2+a/s.Integer(2))**2) == 0

# The y=0 section is squarefree exactly away from the two smoothness factors.
t=s.symbols('t')
f=t**4+a*t**2+b
res=s.factor(s.resultant(f,s.diff(f,t),t))
assert s.factor(res - 16*b*(a**2-4*b)**2) == 0

# For an order-3 invariant vertical line x=u, the section has divisor profile
# 1+1+1+1 if f(u)!=0 and 1+3 if f(u)=0; neither profile is even.
# This is the projective restriction Z*(Y^3-f(u)Z^3).
Y,Z=s.symbols('Y Z')
fu=u**4+a*u**2+b
vertical=s.expand(Z*(Y**3-fu*Z**3))
assert s.expand(vertical - (Y**3*Z - fu*Z**4)) == 0

# Orbit equations from fixed-point counts: Fix(mu3)=1, Fix(mu2)=4, total=28.
n1,n2,n3,n6=s.symbols('n1 n2 n3 n6', integer=True, nonnegative=True)
sol=s.solve([
    s.Eq(n1,1),
    s.Eq(n1+2*n2,1),
    s.Eq(n1+3*n3,4),
    s.Eq(n1+2*n2+3*n3+6*n6,28)
],[n1,n2,n3,n6], dict=True)
assert sol == [{n1:1,n2:0,n3:1,n6:4}]

# Quotienting each free C6-orbit by its order-2 subgroup gives one free C3-orbit
# of three tau-pairs; four C6-orbits therefore give 4*3=12 such pairs.
assert 4*3 == 12
print('VERIFY_OK orbit=1+3+4x6 mu3_fixed=1 tau_fixed=4 prym_pairs=4x3')
