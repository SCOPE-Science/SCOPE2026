#!/usr/bin/env python3
"""Exact polynomial proof checks in characteristic five (requires SymPy)."""
from itertools import combinations
import sympy as s
A, B, X, Z = s.symbols('A B X Z')
P = [
    A**2+2, B**2+2,
    A**2-A*B+B**2-1+2*(A+B),
    A**2-A*B+B**2-1-2*(A+B),
    A**2*B**2+2*(A**2+B**2)-2*A*B+1,
]
F = (X**4+A*X**2+1)*(X**4+B*X**2+1)
G = s.Poly(s.expand(F**2), X)
h2, h4, h8 = [G.nth(n) for n in (2,4,8)]
assert all(s.Poly(u-v, A,B,modulus=5).is_zero for u,v in (
    (h2,2*(A+B)), (h4,A*A-A*B+B*B-1),
    (h8,A*A*B*B+2*(A*A+B*B)-2*A*B+1)))
# The following are exact saturated ideal generators, using z*Delta-1.
expected = [
    [A+B,A*A+2], [-A+B-1,A*A+2], [-A+B+1,A*A+2],
    [-2*A+B,A*A+2], [-A+B+1,A*A-2*A-2],
    [-A+B-1,A*A+2*A-2], [2*A+B,A*A-2],
    [A+B,A*A-2], [A+B+2,A*A+2*A-2],
    [A+B-2,A*A-2*A-2],
]
Delta = (A-B)*(A*A-4)*(B*B-4)
for ((i,j), expected_generators) in zip(combinations(range(5),2), expected):
    g = s.groebner([P[i],P[j],Z*Delta-1], Z,B,A,modulus=5)
    eliminated = [p.as_expr() for p in g.polys if Z not in p.as_expr().free_symbols]
    assert len(eliminated)==2
    assert all(s.Poly(u-v,A,B,modulus=5).is_zero for u,v in zip(eliminated,expected_generators)),(i,j,eliminated)
    # A^2+cA+d has nonsquare nonzero discriminant in F_5.
    quad = s.Poly(expected_generators[1],A,modulus=5)
    assert quad.degree()==2 and quad.is_irreducible
for i,j,k in combinations(range(5),3):
    g=s.groebner([P[i],P[j],P[k],Z*Delta-1],Z,B,A,modulus=5)
    assert len(g.polys)==1 and g.polys[0].as_expr()==1,(i,j,k)
print('SYMBOLIC_VERIFY_OK: coefficients, ten saturated loci and ten empty triple intersections')
