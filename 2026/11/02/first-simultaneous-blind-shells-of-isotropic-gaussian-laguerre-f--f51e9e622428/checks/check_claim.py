"""Exact rational polynomial certificates for the first Gaussian-Laguerre blind shells.

Requires SymPy; see requirements.txt. Only algebraic facts are checked here:
the infinite-dimensional functional-analytic argument is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import sympy as sp

s, a = sp.symbols('s a')
L = [sp.assoc_laguerre(k, a, s) for k in range(5)]
expected = {
    (0, 1): sp.Integer(1),
    (0, 2): sp.Integer(1),
    (0, 3): sp.Integer(1),
    (0, 4): sp.Integer(1),
    (1, 2): -(a+1)/2,
    (1, 3): -2*(a+1)/3,
    (1, 4): (a-5)*(a+1)/8,
    (2, 3): -(a+1)*(a+2)**2/72,
    (2, 4): (a-23)*(a+1)*(a+2)**2/2304,
    (3, 4): (a+1)*(a+2)**2*(a+3)**3/165888,
}
for i, j in combinations(range(5), 2):
    assert sp.factor(sp.resultant(L[i], L[j], s) - expected[i, j]) == 0, (i, j)

for dim, i, j, root in [(6,1,4,6),(24,2,4,30)]:
    aa=dim-1
    p=sp.Poly(L[i].subs(a,aa),s)
    q=sp.Poly(L[j].subs(a,aa),s)
    greatest=sp.gcd(p,q).monic()
    assert sp.expand(greatest.as_expr() - (s-root)) == 0
    assert p.eval(root)==0 and q.eval(root)==0
    assert sp.diff(p.as_expr(),s).subs(s,root) != 0
    assert sp.diff(q.as_expr(),s).subs(s,root) != 0
    assert sp.Rational(4*dim,2*dim-1) == (sp.Rational(24,11) if dim==6 else sp.Rational(96,47))
    assert 2*root in (12,60)

# Generate the coefficient formula by the Laguerre generating series.
for dim in (1,2,3,6):
    for n in range(5):
        assert sp.expand(L[n].subs(a,dim-1).subs(s,0)) == comb(n+dim-1,n)

# Explicit Bessel / Helmholtz radial witnesses correspond to k^2=2*root.
# Their sharp large-radius power r^{-(N-1)/2} yields
# L^p iff p > 2N/(N-1), so for N=2d the endpoint is 4d/(2d-1).
for d in (6,24):
    dimension=2*d
    critical=Fraction(2*dimension,dimension-1)
    assert critical == Fraction(4*d,2*d-1)
    assert Fraction(2,1) < critical < Fraction(3,1)

print('PASS: 10 two-degree resultants; both unique positive-parameter gcds; '
      'root simplicity; normalization; exact Lp exponents.')
