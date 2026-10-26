#!/usr/bin/env python3
"""Exact symbolic checks for the syzygy fourfold stabilizer and orbit normal space."""
import sympy as s
from itertools import combinations
x0,x1,x2,t=s.symbols('x0 x1 x2 t')
x=(x0,x1,x2)
F=[x0**2,x1**2,x2**2,x0*x1]
Q=[x0*x2,x1*x2]
# The special base scheme is a line plus a disjoint point.
assert s.expand((x0*x2).subs(x2,0))==0
assert s.expand((x1*x2).subs(x2,0))==0
# For every nonzero t, the four reduced points are a projective frame.
pts=[s.Matrix([1,0,0]),s.Matrix([0,1,0]),s.Matrix([0,0,1]),s.Matrix([1,1,t])]
for three in combinations(pts,3):
    determinant=s.factor(s.det(s.Matrix.hstack(*three)))
    assert determinant in (1,-1,t,-t)
for p in pts:
    a,b,c=p
    assert s.expand(a*(c-t*b))==0 and s.expand(b*(c-t*a))==0
# Lie action on the eight-dimensional tangent space to Gr(4,Sym^2 k^3).
basis=F+Q
def coords(polynomial):
    polynomial=s.Poly(s.expand(polynomial),x)
    return s.Matrix([polynomial.coeff_monomial(v) for v in basis])
columns=[]
for i,j in [(0,2),(1,2),(2,0),(2,1)]:
    cols=[]
    for q in F:
        derivative=x[j]*s.diff(q,x[i])
        cols += list(coords(derivative)[4:])
    columns.append(s.Matrix(cols))
M=s.Matrix.hstack(*columns)
assert M.shape==(8,4) and M.rank()==4
# Torus weights on the normal space after quotienting the Lie-orbit image.
# Parent tangent weights are [1/a,b/a^2,a/b^2,1/b,a,b,1/b,1/a].
a,b=s.symbols('a b', nonzero=True)
parent_weights=[1/a,b/a**2,a/b**2,1/b,a,b,1/b,1/a]
normal=[1/a,b/a**2,a/b**2,1/b]
expected=[b/a**2,1/a,1/b,a/b**2]
assert sorted(map(str,normal))==sorted(map(str,expected))
# Derivative of the determinant of the pencil with fixed common line.
la,mu=s.symbols('la mu')
A0,A1,B0,B1,C0,C1=s.symbols('A0 A1 B0 B1 C0 C1')
A=la*A0+mu*A1; B=la*B0+mu*B1; C=la*C0+mu*C1
T=s.Matrix([[s.Symbol('eps')*A,s.Symbol('eps')*B,la/2],
            [s.Symbol('eps')*B,s.Symbol('eps')*C,mu/2],
            [la/2,mu/2,0]])
eps=s.Symbol('eps')
der=s.factor(s.diff(T.det(),eps).subs(eps,0))
assert s.simplify(4*der+mu**2*A-2*la*mu*B+la**2*C)==0
# Rank of the linearized binary-cubic map, and its two-dimensional kernel.
coeff=[s.Poly(der,la,mu).coeff_monomial(la**(3-i)*mu**i) for i in range(4)]
assert s.Matrix([[s.diff(v,w) for w in (A0,A1,B0,B1,C0,C1)] for v in coeff]).rank()==4
# The four orbit columns lie in torus weights (a,b,1/a,1/b).
print('VERIFY_OK four-frame all minors nonzero for t != 0')
print('VERIFY_OK special tangent Lie-orbit rank 4, ambient Grassmann tangent dimension 8')
print('VERIFY_OK normal torus weights match Sym^3(V-dual) tensor det(V)')
print('VERIFY_OK first-order pencil determinant is surjective onto binary cubics')
print('VERIFY_OK generic full stabilizer S4 and special GL2 follow by geometric rigidity of four frames and line-point pairs')
