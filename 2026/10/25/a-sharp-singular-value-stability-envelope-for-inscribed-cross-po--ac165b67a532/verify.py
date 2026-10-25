"""Exact-rational supporting-hyperplane and volume-factor tests.

Run: python verify.py
This is finite verification of the explicit equality configurations, not a
replacement for the dimension-uniform proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def solve(A, b):
    n = len(b)
    rows = [[F(z) for z in row] + [F(b[i])] for i, row in enumerate(A)]
    for j in range(n):
        k = next((i for i in range(j, n) if rows[i][j]), None)
        assert k is not None
        rows[j], rows[k] = rows[k], rows[j]
        pivot = rows[j][j]
        rows[j] = [v / pivot for v in rows[j]]
        for i in range(n):
            if i != j:
                coeff = rows[i][j]
                rows[i] = [u - coeff * v for u, v in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def determinant(A):
    n = len(A)
    rows = [[F(x) for x in row] for row in A]
    result = F(1)
    for j in range(n):
        k = next((i for i in range(j, n) if rows[i][j]), None)
        if k is None:
            return F(0)
        if k != j:
            rows[j], rows[k] = rows[k], rows[j]
            result = -result
        pivot = rows[j][j]
        result *= pivot
        for i in range(j + 1, n):
            v = rows[i][j] / pivot
            rows[i] = [a - v*b for a, b in zip(rows[i], rows[j])]
    return result


def check(d, a, b, c):
    r, t = F(a, c), F(b, c)
    assert a*a + b*b == c*c and 0 < 2*t < r
    points = {}
    for i in range(d):
        for sign in (-1, 1):
            vec = [F(0)] * d
            vec[i] += sign*r
            vec[(i+1) % d] += t
            points[i, sign] = tuple(vec)
            assert sum(x*x for x in vec) == 1

    for signs in product((-1, 1), repeat=d):
        rows = [points[i, signs[i]] for i in range(d)]
        n = solve(rows, [F(1)]*d)
        assert determinant(rows) != 0
        for i in range(d):
            assert sum(x*y for x,y in zip(n, points[i, signs[i]])) == 1
            assert sum(x*y for x,y in zip(n, points[i, -signs[i]])) < 1

    # Strictly positive barycentric coefficients realize the origin.
    q = t / r
    total = [F(0)] * d
    for i in range(d):
        for sign in (-1, 1):
            weight = (1 - sign*q) / (2*d)
            assert weight > 0
            total = [z + weight*x for z,x in zip(total,points[i,sign])]
    assert total == [0]*d

    C = [[points[j,1][i]-points[j,-1][i] for j in range(d)] for i in range(d)]
    assert C == [[(2*r if i == j else F(0)) for j in range(d)] for i in range(d)]
    assert determinant(C)/factorial(d) == (2*r)**d/factorial(d)
    D = 4*d*(1-r)
    assert (2*r)**d/factorial(d) == F(2**d,factorial(d)) * (1-D/F(4*d))**d

for d in range(2, 7):
    for a,b,c in ((12,5,13),(24,7,25),(40,9,41)):
        check(d,a,b,c)
print('PASS: 15 exact-rational equality examples; 372 signed-facet certificates')
