"""Exact vertex-statistic checks for Loday's three canonical polytopes.

Run with: python3 artifacts/verify.py
Python standard library only. The all-dimension theorem is proved in RESULT.md;
finite checks do not replace the proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb


@lru_cache(maxsize=None)
def tree_vertices(n):
    if n == 0:
        return ((),)
    result = []
    for a in range(n):
        b = n - a - 1
        for left in tree_vertices(a):
            for right in tree_vertices(b):
                result.append(left + ((a + 1) * (b + 1),) + right)
    return tuple(result)


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def j_permutation(n):
    return Fraction(n * (n - 1) * (n + 1), 12)


def j_associahedron(n):
    return Fraction(n * (n - 1) * (n + 1) * (2 * n + 1), 60)


def j_parallelepiped(n):
    return Fraction((n - 1) ** 3, 2)


vertex_checks = 0
for n in range(1, 11):
    verts = tree_vertices(n)
    assert len(verts) == catalan(n)
    barycenter = Fraction(n + 1, 2)
    assert all(sum(v) == n * (n + 1) // 2 for v in verts)
    for i in range(n):
        assert Fraction(sum(v[i] for v in verts), len(verts)) == barycenter
    radial_mean = sum(
        (sum((Fraction(x) - barycenter) ** 2 for x in v) for v in verts),
        Fraction(0)
    ) / len(verts)
    assert radial_mean == j_associahedron(n)
    vertex_checks += len(verts)

cube_checks = 0
for n in range(2, 10):
    # The signed edge roots have Euclidean length squared 2.
    amplitude = Fraction(n - 1, 2)
    vals = []
    for signs in product((-1, 1), repeat=n - 1):
        displacement = [Fraction(0) for _ in range(n)]
        for i, sign in enumerate(signs):
            displacement[i] += amplitude * sign
            displacement[i + 1] -= amplitude * sign
        vals.append(sum(x ** 2 for x in displacement))
    assert sum(vals, Fraction(0)) / len(vals) == j_parallelepiped(n)
    cube_checks += len(vals)

# Independent coefficient computation for the tree squared-coordinate toll:
# S(z) = z(1 - 2z)^2 (1 - 4z)^(-7/2).
coef = [Fraction(1)]
for k in range(1, 72):
    coef.append(coef[-1] * Fraction(4 * k + 10, k))
for n in range(1, 71):
    sn = coef[n - 1]
    if n >= 2:
        sn -= 4 * coef[n - 2]
    if n >= 3:
        sn += 4 * coef[n - 3]
    expected = Fraction(catalan(n) * n * (n + 1) * (n * n + 7 * n + 7), 30)
    assert sn == expected, (n, sn, expected)

for n in range(2, 101):
    p, a, r = j_permutation(n), j_associahedron(n), j_parallelepiped(n)
    assert (p == a == r) if n == 2 else (p < a < r if n <= 10 else p < r < a)
    assert a - p == Fraction(n * (n - 2) * (n - 1) * (n + 1), 30)
    assert r - a == Fraction(-(n - 2) * (n - 1) * (2 * n * n - 23 * n + 15), 60)

print(f'VERIFY_OK tree_vertices={vertex_checks} signed_vertices={cube_checks} gf_coefficients=70 comparison_dimensions=99')
