#!/usr/bin/env python3
"""Symbolically check the eight-state invariant transfer matrix and first moments.

Requires SymPy; the independent full-graph rational checker `verify.py` is stdlib-only.
"""
import sympy as s

q=s.symbols('q',positive=True,real=True)
z=s.symbols('z')
m=q*q
c=(m-1)/(m+1)
b=-2*q/(m+1)
U=s.Matrix([
 [0,c,0,0,b,0,0,0],
 [c,0,b,0,0,0,0,0],
 [0,0,0,0,0,0,1,0],
 [b,0,-c,0,0,0,0,0],
 [0,0,0,0,0,0,0,1],
 [0,b,0,0,-c,0,0,0],
 [0,0,0,0,0,1,0,0],
 [0,0,0,1,0,0,0,0],
])
assert s.simplify(U.T*U-s.eye(8)) == s.zeros(8)
charpoly=s.factor(U.charpoly(z).as_expr())
expected=s.factor((z*z-1)**2 * (z*z-c*z+1)*(z*z+c*z+1))
assert s.simplify(charpoly-expected)==0

p=s.Matrix([1,0,q,0,0,0,0,0])
target=s.Matrix([0,1,0,0,q,0,0,0])
initial=[]
for t in (1,3,5):
  initial.append(s.factor((target.T*U**t*p)[0]/(m+1)))
  theta_cos=c/2
  formula=-(m+1)/(3*m+1)+2*m*s.chebyshevt(t,theta_cos)/(3*m+1)
  assert s.simplify(initial[-1]-formula)==0
print('symbolic factorization: OK')
print('symbolic first three odd amplitudes: OK')
print('SYMBOLIC_VERIFY_OK')
