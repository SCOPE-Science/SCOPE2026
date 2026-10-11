#!/usr/bin/env python3
"""Exact algebraic checks of a nilpotent shift Euclidean-radius threshold theorem.

Requires sympy; numpy is used only for optional finite-dimensional regression checks.
The analytic theorem is in RESULT.md; finite tests cannot establish it.
"""
import sympy as S
r, z = S.symbols('r z', real=True)
h = S.sqrt(2)
k = 5 + S.Rational(7,2)*h
B = (6 + 7*h)*(r-h)*(r-(25*h+14)/31)
N = 2 + 2*z + r*r
Q = S.expand(k*(N*N/2-(2*r+z)**2)-4*z*(1+r)**2)
assert S.simplify(S.expand(Q-(k*(r*r-2)**2/2+B*z+k*z*z))) == 0
Delta = S.expand(B*B-2*k*k*(r*r-2)**2)
Delta_factor = (35+14*h)*(r-h)**2*(r-12-9*h)*(r-(5*h-4)/17)
assert S.simplify(S.expand(Delta-Delta_factor)) == 0
A = (2+h)/4
beta = h/2
gamma = (h-1)/2
assert S.simplify(2*A*A/(beta*gamma)-k) == 0
s,t = S.symbols('s t', real=True)
assert S.simplify(S.expand(4*s+(t*t-8)*s*s-((2*S.sqrt(s*(1-2*s)))**2+t*t*s*s))) == 0
# The following numerical regression is independent of the exact symbolic identities.
try:
 import numpy as np
 for n in (3,4,5,6,7,8,9):
  J=np.diag(np.ones(n-1),1)
  C=(J+J.T)/2
  D=(J@J+(J@J).T)/2
  beta_n=np.cos(np.pi/(int(np.ceil(n/2))+1))
  assert abs(np.linalg.eigvalsh(D)[-1]-beta_n)<1e-11
  if n%2 == 0:
   vals, vecs=np.linalg.eigh(D)
   top=vecs[:,-2:]
   # Degenerate eigenspace contains vectors with nonzero C expectation.
   restricted=top.T@C@top
   assert np.linalg.norm(restricted)>1e-9
  if n==3:
   for tval in (0.0,1.0,2.0,3.0,5.0):
    target=2/np.sqrt(8-tval*tval) if tval<=2 else tval/2
    # Supporting-angle maximization; identity checked by dense angular sampling.
    vals=[]
    for angle in np.linspace(0,np.pi/2,4001):
     vals.append(np.linalg.eigvalsh(np.cos(angle)*C+tval*np.sin(angle)*D)[-1])
    assert abs(max(vals)-target)<1e-5
except ImportError:
 pass
print('JORDAN_PAIR_SATURATION_CERTIFICATE_OK')
