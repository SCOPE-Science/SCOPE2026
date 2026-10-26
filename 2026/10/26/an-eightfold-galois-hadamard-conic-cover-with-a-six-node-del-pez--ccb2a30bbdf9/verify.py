#!/usr/bin/env python3
"""Exact identities for the Hadamard square of a smooth diagonal conic."""
import sympy as s
z0,z1,z2,t,u=s.symbols('z0 z1 z2 t u')
B=s.expand((z0*z0+z1*z1-z2*z2)**2-4*z0*z0*z1*z1)
F=s.prod([z0+i*z1+j*z2 for i in (1,-1) for j in (1,-1)])
assert s.expand(B-F)==0
x=lambda v:s.Matrix([1-v*v,s.I*(1+v*v),2*v])
X,Y=x(t),x(u)
assert s.expand(sum(c*c for c in X))==0
assert s.expand(sum(c*c for c in Y))==0
Z=[s.expand(X[i]*Y[i]) for i in range(3)]
W=s.expand(X[0]**2*Y[1]**2-X[1]**2*Y[0]**2)
assert s.factor(W*W-B.subs(dict(zip((z0,z1,z2),Z))))==0
# Degree-two invariant-field relation: a=X0^2/X1^2.
a=s.factor(X[0]**2/X[1]**2)
P=s.factor(Z[1]**2*a*a+(Z[0]**2+Z[1]**2-Z[2]**2)*a+Z[0]**2)
assert P==0
assert s.factor((Z[0]**2+Z[1]**2-Z[2]**2)+2*Z[1]**2*a-W)==0
# Four branch lines are in general position.
from itertools import combinations
vec=[s.Matrix([1,i,j]) for i in (1,-1) for j in (1,-1)]
assert len(vec)==4
assert all(abs(s.det(s.Matrix.hstack(*triple)))==4 for triple in combinations(vec,3))
print('VERIFY_OK: quartic factorization, conic parametrization, invariant field, six crossings')
