"""Exact and numerical verification of sextic harmonic sampling on D-type root shells.
Requires sympy and numpy; run with python research27_sextic_checker.py.
"""
import itertools
import math
import sympy as sp
import numpy as np

n, t = sp.symbols('n t', integer=True, positive=True)
P = sp.factor(sp.gegenbauer(6, (n-2)/2, t) / sp.gegenbauer(6, (n-2)/2, 1))
u, v = sp.factor(P.subs(t, sp.Rational(1, 2))), sp.factor(P.subs(t, 0))
expected = [
 (n-16)**2*(n-2)*(n+6)/(16*(n-1)*(n+1)*(n+3)),
 (n+4)*(n**3-18*n**2+560*n-1536)/(32*(n-1)*(n+1)*(n+3)),
 15*(n-4)*(n+4)*(n+6)/(16*(n-1)*(n+1)*(n+3)),
 (n+4)*(n**2-n+3)/((n-1)*(n+1)*(n+3)),
]
computed = [
 1+v+4*(n-2)*u+(n-2)*(n-3)*v,
 1+2*(n-4)*u+(1-2*(n-3))*v,
 1-4*u+3*v,
 1-v,
]
assert all(sp.factor(x-y)==0 for x,y in zip(expected, computed))
print('Exact four-branch Gegenbauer/Johnson factorization: PASS')
assert sp.factor(expected[0])==sp.factor((n-16)**2*(n-2)*(n+6)/(16*(n-1)*(n+1)*(n+3)))
assert sp.factor(sp.diff(n**3-18*n**2+560*n-1536,n))==3*n**2-36*n+560
for N in range(5,60):
 ev = [sp.Rational(x.subs(n,N)) for x in [sp.factor(z) for z in expected]]
 assert (ev[0]==0)==(N==16)
 assert all(x>0 for x in ev[1:])
 print_line = N in (5,8,15,16,17)
 if print_line: print('Dimension',N,'eigenvalues',*[str(x) for x in ev])
print('Exact rational nonnegativity/rank checks for n=5..59: PASS')

for N in (5,6,7,8,9,12,16,17):
 X=[]
 for a in range(N):
  for b in range(a+1,N):
   for sign in (-1,1):
    row=np.zeros(N);row[a]=1;row[b]=sign;X.append(row/np.sqrt(2))
 X=np.array(X)
 normalized_poly=sp.Poly(P.subs(n,N),t)
 inner=X@X.T
 G=np.zeros_like(inner)
 for (power,), coefficient in normalized_poly.terms():
  G += float(coefficient)*inner**power
 vals=np.linalg.eigvalsh(G)
 multiplicities=[1,N-1,N*(N-3)//2,N*(N-1)//2]
 prediction=np.sort(np.concatenate([np.repeat(float(expected[j].subs(n,N)),multiplicities[j]) for j in range(4)]))
 assert len(prediction)==N*(N-1)
 err=float(np.max(np.abs(vals-prediction)))
 assert err < 3e-12,(N,err)
 print(f'Direct Gram eigenvalues n={N}: max absolute discrepancy {err:.3e}; rank={sum(z>1e-9 for z in vals)}')
print('Independent direct-matrix spectral comparisons: PASS')
