"""Exact characteristic-zero verification for a nine-line realization family.

Requires Python 3 and SymPy. Every assertion is over Q[a], not a
floating-point test; the specialised rank check is over Q.
"""
import itertools
import sympy as s

a = s.symbols('a')
X, Y, Z = s.symbols('x y z')
T, W = s.symbols('T W')
points = [
    (1, 0, 0), (0, 1, 0), (1, a, 0),
    (0, 0, 1), (a - 1, 0, a), (0, 1, 1),
    (1, 1, 1), (a - 1, a**2, a), (a - 1, a - 1, a),
]
flats = [
    (1, 2, 3), (1, 4, 5), (1, 6, 7), (2, 4, 6),
    (3, 5, 7), (3, 6, 8), (4, 7, 9), (2, 5, 8, 9),
]
expected_zero = {
    tuple(sorted(triple))
    for flat in flats for triple in itertools.combinations(flat, 3)
}
assert len(expected_zero) == 11
allowed_factors = {a, a - 1, a*a - a + 1}
zero_triples = set()
nonzero_count = 0
for inds in itertools.combinations(range(1, 10), 3):
    D = s.factor(s.det(s.Matrix([points[i-1] for i in inds])))
    if D == 0:
        zero_triples.add(inds)
    else:
        nonzero_count += 1
        poly = s.Poly(D, a)
        for factor, multiplicity in s.factor_list(poly)[1]:
            assert s.Poly(factor, a).as_expr() in allowed_factors, (inds, factor)
assert zero_triples == expected_zero
assert nonzero_count == 73

# Degree-four logarithmic derivations with zero z coefficient have the
# form A=x*ell5*U, B=y*(y+z)*V with U,V quadratic.
monomials = [X**2, Y**2, Z**2, X*Y, X*Z, Y*Z]
base = [X*((a - 1)*X+a*Z)*m for m in monomials]
base += [Y*(Y+Z)*m for m in monomials]
remaining = [points[i-1] for i in (3, 7, 8, 9)]
rows = []
for u, v, w in remaining:
    replacement = {X:-v*T-w*W, Y:u*T, Z:u*W}
    polys = [s.Poly(s.expand((u if j < 6 else v) * term.subs(
        replacement, simultaneous=True)), T, W) for j,term in enumerate(base)]
    for j in range(5):
        rows.append([s.factor(p.coeff_monomial(T**j * W**(4-j)))
                     for p in polys])
M = s.Matrix(rows)
assert M.shape == (20, 12)
rows_12 = [3, 5, 2, 6, 4, 11, 7, 8, 12, 17, 13, 18]
assert s.factor(M[rows_12,:].det(method='domain-ge')) == (
    a**14 * (a - 2) * (a - 1)**20 * (a*a - a + 1)**3)

M2 = M.subs(a, 2)
ker = s.Matrix([-1,6,4,2,3,8,9,8,8,20,16,20])
assert M2 * ker == s.zeros(20, 1)
rows_11 = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 18]
assert M2[rows_11, list(range(11))].det(method='domain-ge') == -5898240

# This proves exactly one degree-four syzygy at a=2 and none elsewhere
# in the open realization space. A fourfold point provides degree five.
print('PASS: 11 prescribed and 73 nonzero triple minors;')
print('PASS: 20x12 determinant and unique rank-eleven jump at a=2.')
