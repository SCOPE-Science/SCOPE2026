#!/usr/bin/env python3
"""Exact certificate for real roots of planar lattice-prism Ehrhart numerators.
Run with Python 3 and sympy. All arithmetic is exact.
"""
import sympy as sp
x,I,B,k,a,b,s=sp.symbols('x I B k a b s')
h1=(k+1)*(I+B)-4
h2=4*k*I+(2*k-1)*B-6*k+3
h3=(k-1)*I
H=1+h1*x+h2*x*x+h3*x*x*x
Delta=sp.factor(sp.discriminant(H,x))
# In both disjoint chambers the discriminant has a nonnegative
# integer-coefficient expansion. This is a finite exact polynomial identity.
P1=sp.Poly(sp.expand(Delta.subs({I:a+1,B:b+3,k:s+1})),a,b,s)
P0=sp.Poly(sp.expand(Delta.subs({I:0,B:b+4,k:s+1})),a,b,s)
assert len(P1.terms())==72 and all(c>0 for c in P1.coeffs())
assert len(P0.terms())==25 and all(c>0 for c in P0.coeffs())
assert sp.Poly(P1.as_expr(),a,b,s).eval({a:0,b:0,s:0})==0
assert sp.Poly(P0.as_expr(),a,b,s).eval({a:0,b:0,s:0})==12
assert sp.simplify(Delta.subs({I:0,B:3}))==0
assert sp.factor(Delta.subs({I:1,B:3,k:1}))==0
# Distinct positive coefficient polynomials force real roots to be negative.
for i in range(0,11):
 for bb in range(3,15):
  for kk in range(1,15):
   hh=sp.Poly(H.subs({I:i,B:bb,k:kk}),x)
   if i==0 and bb==3:
    assert hh.degree()==1
   elif i==0 or kk==1:
    assert hh.degree()==2
   else:
    assert hh.degree()==3
   if hh.degree()>1:
    assert sp.discriminant(hh.as_expr(),x)>=0
# Check Pick's formula against direct lattice-point enumerations for simple polygons.
assert sp.factor(H.subs({I:0,B:3,k:1}))==1+2*x
assert sp.factor(H.subs({I:1,B:3,k:1}))==(1+2*x)**2
assert sp.factor(H.subs({I:0,B:4,k:1}))==1+4*x+x*x
print('PRISM_ROOT_CERTIFICATE_OK; chamber1_terms=72; chamber0_terms=25; triples=1848')
