#!/usr/bin/env python3
"""Exact reproducible algebra for the doubled ten-node Segre configuration.

Requires Python 3 and SymPy 1.14 (or a compatible version).  All polynomial
operations are over QQ.  No network access or additional data files required.
"""
from itertools import combinations, combinations_with_replacement
from sympy import QQ, Matrix, Poly, diff, expand, groebner, symbols

x0, x1, x2, x3, x4 = symbols('x0 x1 x2 x3 x4')
xs = (x0, x1, x2, x3, x4)
s = sum(xs)
quadrics = [xs[i]**2 - x0**2 for i in range(1, 5)] + [s**2 - x0**2]
f = sum(z**3 for z in xs) - s**3
pair_products = [a*b for i, a in enumerate(quadrics) for b in quadrics[i:]]
order = (x1, x2, x3, x4, x0)

# Reduced Groebner bases computed in exact rational arithmetic.
g_i = groebner(quadrics, *order, order='grevlex', domain=QQ)
g_j = groebner(pair_products + [f], *order, order='grevlex', domain=QQ)
g_sq = groebner(pair_products, *order, order='grevlex', domain=QQ)

def lead_tuple(g):
    return tuple(int(a) for a in g.LM(order='grevlex').exponents)

l_i = sorted(lead_tuple(g) for g in g_i.polys)
l_j = sorted(lead_tuple(g) for g in g_j.polys)

expected_i = [
    (1,0,1,1,0), (0,1,1,1,0), (2,0,0,0,0),
    (1,1,0,0,0), (0,2,0,0,0), (0,0,2,0,0), (0,0,0,2,0),
]
expected_j = [
    (1,0,3,1,0), (0,1,3,1,0), (1,0,1,3,0), (0,1,1,3,0),
    (4,0,0,0,0), (1,3,0,0,0), (0,4,0,0,0),
    (2,0,2,0,0), (1,1,2,0,0), (0,2,2,0,0), (0,0,4,0,0),
    (2,0,1,1,0), (1,1,1,1,0), (0,2,1,1,0),
    (2,0,0,2,0), (1,1,0,2,0), (0,2,0,2,0),
    (0,0,2,2,0), (0,0,0,4,0), (2,1,0,0,0),
]
assert l_i == sorted(expected_i), (l_i, expected_i)
assert l_j == sorted(expected_j), (l_j, expected_j)
assert all(m[4] == 0 for m in l_i + l_j)

def degree_exponents(degree, n=4):
    if n == 1:
        yield (degree,)
        return
    for a in range(degree+1):
        for rest in degree_exponents(degree-a, n-1):
            yield (a,) + rest

def standard_counts(leads):
    out = []
    for degree in range(7):
        cnt = 0
        for e in degree_exponents(degree):
            if not any(all(e[j] >= lm[j] for j in range(4)) for lm in leads):
                cnt += 1
        out.append(cnt)
    return out

assert standard_counts(l_i) == [1, 4, 5, 0, 0, 0, 0]
assert standard_counts(l_j) == [1, 4, 10, 19, 16, 0, 0]

# Ten distinct projective points of the Segre ten-node configuration.
points = []
for size in (1, 2):
    for chosen in combinations(range(1, 5), size):
        points.append((1,) + tuple(1 if i in chosen else -1 for i in range(1, 5)))
assert len(points) == len(set(points)) == 10
for point in points:
    evaluation = dict(zip(xs, point))
    assert all(q.subs(evaluation) == 0 for q in quadrics)
    assert f.subs(evaluation) == 0
    assert all(diff(f, v).subs(evaluation) == 0 for v in xs)

# Independent exact first-jet interpolation in degree 3 and 4.
def all_exponents(degree, n=5):
    if n == 1:
        yield (degree,)
        return
    for a in range(degree+1):
        for rest in all_exponents(degree-a, n-1):
            yield (a,) + rest

def jet_rank(degree):
    mons = list(all_exponents(degree))
    rows = []
    for point in points:
        rows.append([__import__('math').prod(point[i]**e[i] for i in range(5)) for e in mons])
        for j in range(1, 5):
            rows.append([e[j] * __import__('math').prod(point[i]**(e[i] - int(i == j))
                             for i in range(5)) if e[j] else 0 for e in mons])
    return Matrix(rows).rank()

assert jet_rank(3) == 34
assert jet_rank(4) == 50

# The cyclic symbolic defect is the apolar algebra of a nondegenerate quadric.
rem = lambda poly: expand(g_sq.reduce(poly)[1])
unit = rem(f*x0**2)
assert unit != 0
for i, a in enumerate(xs):
    for j, b in enumerate(xs):
        expected = unit if i == j else -unit/5
        assert expand(rem(f*a*b) - expected) == 0
for a, b, c in combinations_with_replacement(xs, 3):
    assert rem(f*a*b*c) == 0
linear_remainders = [Poly(rem(f*a), *xs) for a in xs]
monoms = sorted(set().union(*(set(t.monoms()) for t in linear_remainders)))
assert Matrix([[t.coeff_monomial(m) for m in monoms] for t in linear_remainders]).rank() == 5
pairing = Matrix([[1 if i == j else QQ(-1, 5) for j in range(5)] for i in range(5)])
assert pairing.det() == QQ(1296, 3125)

print('10 Segre nodes; defining ideal: five quadrics')
print('GB initial ideal of I: 7 generators, no x0 factor')
print('GB initial ideal of I^2+(F): 20 generators, no x0 factor')
print('Standard monomial h-vector for I:', standard_counts(l_i)[:3])
print('Standard monomial h-vector for I^(2):', standard_counts(l_j)[:5])
print('First-jet interpolation ranks in degrees 3,4:', jet_rank(3), jet_rank(4))
print('Symbolic defect Hilbert vector: (1,5,1), shifted by degree 3')
print('Quadratic pairing diagonal=1, off-diagonal=-1/5, determinant=1296/3125')
print('VERIFY_OK')
