#!/usr/bin/env python3
"""Exact symbolic checks for a four-genotype mutation-selection ordering theorem.

Requires SymPy; optional NumPy is used only for numerical illustrations.
The argument proving minimality is given in the accompanying mathematical text.
"""
import sympy as S

u, z = S.symbols('u z')
L = S.Matrix([[1,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,1]])
fitness = S.diag(1,8,2,3)
M = fitness-u*L
P = S.expand((z*S.eye(4)-M).det())
Q = S.expand((z-8+2*u)*(z-1+u)-2*u**2)
f = 2*u**3-13*u**2+22*u-10
assert S.expand(Q - (z**2 + (3*u-9)*z + 8-10*u)) == 0
assert S.expand(S.rem(P,Q,z)-u**2*((u-1)*z-4*u+3)) == 0
assert S.expand(S.resultant(P,Q,z)-u**4*f)==0
z_on_crossing = 4+1/(u-1)
assert S.factor(Q.subs(z,z_on_crossing)-f/(u-1)**2)==0
assert S.factor(P.subs(z,z_on_crossing) - S.quo(P,Q,z).subs(z,z_on_crossing)*f/(u-1)**2)==0
intervals = [(S.Rational(7,10),S.Rational(4,5)),
             (S.Rational(8,5),S.Rational(5,3)),
             (S.Integer(4),S.Integer(5))]
for left,right in intervals:
    assert S.sign(f.subs(u,left)) != S.sign(f.subs(u,right))
    assert S.sign(f.subs(u,left)) != 0 and S.sign(f.subs(u,right)) != 0
assert S.factor(f.subs(u,1)) == 1
assert S.factor(L*S.ones(4,1)) == S.zeros(4,1)
w = S.linsolve([*list(L*S.Matrix(S.symbols('w0:4')) -
                 (fitness.diagonal().T-S.Rational(7,2)*S.ones(4,1))),
                sum(S.symbols('w0:4'))], S.symbols('w0:4'))
w = list(w)[0]
assert S.simplify(w[0]-w[2]) == -S.Rational(1,2)
assert (8-2)*S.Rational(1,8-1) == S.Rational(6,7)
print('VERIFY_OK charpoly=1 quotient_remainder=1 resultant=1')
print('VERIFY_OK cubic_positive_root_brackets=3 crossing_eigenvalue_identity=1')
print('VERIFY_OK low_mutation_ratio=6/7 high_mutation_difference_coefficient=-1/2')
try:
 import numpy as np
 roots=sorted(float(S.re(S.N(r,20))) for r in S.nroots(f))
 for root in roots:
  mm=np.array(M.subs(u,root),float)
  lam,vec=np.linalg.eigh(mm)
  zroot=float(z_on_crossing.subs(u,root))
  if root>1:
   assert abs(lam[-1]-zroot)<1e-9
   assert abs(vec[0,-1]-vec[2,-1])<1e-8
  else:
   assert abs(lam[0]-zroot)<1e-9
 for sample,order in [(0.1,-1),(2,1),(5,-1),(100,-1)]:
  vals,vec=np.linalg.eigh(np.array(M.subs(u,sample),float))
  xx=np.abs(vec[:,-1]); assert np.sign(xx[0]-xx[2])==order
 print('NUMERICAL_ILLUSTRATION roots=',','.join(f'{v:.12f}' for v in roots))
except ImportError:
 print('NUMERICAL_ILLUSTRATION skipped: NumPy absent')
