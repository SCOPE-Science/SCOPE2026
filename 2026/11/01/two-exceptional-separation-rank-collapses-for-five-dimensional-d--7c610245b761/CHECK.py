#!/usr/bin/env python3
"""Exact rank checks for a five-dimensional axial ellipsoid section kernel."""
import sympy as S
w,t=S.symbols('w t')
def coefficient_matrix(b2,a2,s):
    h=S.Integer(b2)+(S.Integer(a2)-S.Integer(b2)-S.Integer(s)**2)*w**2
    v=S.Integer(s)*w
    f=S.Poly(S.expand((h+2*v*t-t*t)**2),t)
    coeff=[S.Poly(f.coeff_monomial(t**j),w) for j in range(5)]
    return S.Matrix([[p.coeff_monomial(w**i) for p in coeff] for i in range(5)])
for b2,a2,s,expected in [(4,4,0,1),(4,9,0,3),(4,5,1,3),(4,7,1,4),(4,8,1,5),(4,2,1,5),(4,4,1,5),(9,34,5,3),(9,84,5,4)]:
    matrix=coefficient_matrix(b2,a2,s)
    r=matrix.rank()
    assert r==expected,(b2,a2,s,r,expected)
    print(f'b2={b2}, a2={a2}, center={s} -> exact rank {r}')
# Symbolic pivot factorization for nonzero center and b>0, allowing v as independent variable.
b, beta, v=S.symbols('b beta v', nonzero=True, real=True)
h=b+beta*v*v
f=S.Poly(S.expand((h+2*v*t-t*t)**2),t)
mat=S.Matrix([[S.Poly(f.coeff_monomial(t**j),v).coeff_monomial(v**i) for j in range(5)] for i in range(5)])
D=S.factor(mat.det())
print('symbolic determinant of five polynomial coefficients:',D)
assert S.simplify(D-32*beta**3*(beta-2))==0
# Test each polynomial identity at infinitely many formal w by expansion; no finite sampling needed.
q=S.symbols('q',positive=True)
for b2,a2,s in [(4,5,1),(4,7,1),(4,8,1)]:
   h=S.Integer(b2)+(S.Integer(a2)-S.Integer(b2)-s*s)*w*w;v=s*w
   assert S.expand((h+2*v*t-t*t)**2 - (S.Integer(b2)+(a2-b2)*w*w-(t-s*w)**2)**2)==0
print('ALL exact symbolic checks passed')
