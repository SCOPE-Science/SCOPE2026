#!/usr/bin/env python3
"""Exact algebraic checks for the sextic triple-well separatrix identities."""
import sympy as s
x,u,a,k=s.symbols('x u a k', positive=True)
V=k*x**2*(x**2-a**2)**2
h=4*k*a**6/s.Integer(27)
assert s.simplify(h-V-k*(x*x-a*a/3)**2*(4*a*a/3-x*x))==0
assert s.simplify(s.diff(V,x)-2*k*x*(x*x-a*a)*(3*x*x-a*a))==0
print('HAMILTONIAN_FACTORIZATION_PASS')
r=s.sqrt(s.Rational(1,3))
Icenter=s.integrate((r*r-u*u)*s.sqrt(4*r*r-u*u),(u,0,r))
Iouter=s.integrate((u*u-r*r)*s.sqrt(4*r*r-u*u),(u,r,2*r))
assert s.simplify(Icenter-s.sqrt(3)/12)==0
assert s.simplify(Iouter-s.sqrt(3)/12)==0
print('ACTION_PARTITION_2_TO_1_TO_1_PASS')
I1=s.integrate(u*(u*u-r*r)*s.sqrt(4*r*r-u*u),(u,r,2*r))
I3=s.integrate(u**3*(u*u-r*r)*s.sqrt(4*r*r-u*u),(u,r,2*r))
assert s.simplify(I1-s.Rational(2,15))==0
assert s.simplify(I3-s.Rational(38,315))==0
assert s.simplify(I3/I1-s.Rational(19,21))==0
print('MELNIKOV_WEIGHTED_INTEGRALS_AND_SLOPE_PASS')
assert 1-s.Rational(19,21)==s.Rational(2,21)
assert s.diff(V,x,2).subs(x,a/s.sqrt(3)).simplify()==-8*k*a**4/3
print('HOPF_TO_HOMOCLINIC_GAP_AND_SADDLE_PASS')
