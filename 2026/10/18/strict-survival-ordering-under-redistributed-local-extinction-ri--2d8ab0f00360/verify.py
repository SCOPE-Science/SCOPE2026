#!/usr/bin/env python3
"""Exact identities and finite numerical diagnostics for two-patch survival ordering.

Requires sympy, numpy, scipy. The analytic positivity proof is in RESULT.md;
finite calculations here check formulas and examples, not the all-time theorem.
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm

z, a, b, c, S, P = sp.symbols('z a b c S P', positive=True)
Q = sp.Matrix([[-(a+b), b, a], [c, -(a+c), 0], [c, 0, -(b+c)]])
R = (z*sp.eye(3) - Q).inv()
D = z*(z+S+c)**2+P*(z+S+2*c)
U = ((z+S+c)**2-P)/D
specific = lambda expr: sp.factor(expr.subs({S:a+b,P:a*b}))
checks = {
    'determinant':sp.det(z*sp.eye(3)-Q)-specific(D),
    'survival Laplace': (R*sp.ones(3,1))[0]-specific(U),
    'R(B,U)': R[0,1]*specific(D)-b*(z+b+c),
    'R(B,V)': R[0,2]*specific(D)-a*(z+a+c),
    'R(U,V)': R[1,2]*specific(D)-a*c,
    'product derivative':-sp.diff(U,P)-(z+S+c)**2*(2*z+S+2*c)/D**2,
    'Laplace-positive factors':U+P/D-(z+S+c)**2/D,
}
for label, expression in checks.items():
    assert sp.simplify(sp.factor(expression)) == 0, label

mean = sp.factor(U.subs(z,0))
assert sp.simplify(mean - ((S+c)**2-P)/(P*(S+2*c)))==0
assert sp.simplify(sp.diff(mean,P)+(S+c)**2/(P**2*(S+2*c)))==0
assert mean.subs({S:4,P:4,c:1})==sp.Rational(7,8)
assert mean.subs({S:4,P:3,c:1})==sp.Rational(11,9)

count=0
min_gap=10.0
for total in [1.0, 4.0, 9.0]:
  for colonization in [0.0, 0.1, 1.0, 5.0]:
    for balanced_fraction in [0.10,0.20,0.35]:
      a1,b1=total*balanced_fraction,total*(1-balanced_fraction)
      a0,b0=total*0.5,total*0.5
      Q1=np.array([[-total,b1,a1],[colonization,-a1-colonization,0],[colonization,0,-b1-colonization]],float)
      Q0=np.array([[-total,b0,a0],[colonization,-a0-colonization,0],[colonization,0,-b0-colonization]],float)
      for t in [0.001,0.05,0.25,1.0,3.0,7.0]:
        s1=float(expm(t*Q1)[0].sum())
        s0=float(expm(t*Q0)[0].sum())
        gap=s1-s0
        assert gap>0 or (abs(gap)<1e-12 and t*total<=0.05), (total,colonization,balanced_fraction,t,gap)
        if gap>0:
            min_gap=min(min_gap,gap)
        count+=1
print('PASS: all',len(checks),'symbolic resolvent and derivative identities.')
print('PASS: exact example mean 7/8 and 11/9.')
print('PASS:',count,'finite matrix-exponential inequality diagnostics.')
print('Min positive checked gap:',min_gap)
print('The infinite-time, infinite-parameter claim is supported by the analytic Laplace-positive convolution proof, not these diagnostics.')
