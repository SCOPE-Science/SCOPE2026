"""Exact finite-range checks for the cyclic-quotient basket formulas.
The universal assertions are proved symbolically in RESULT.md.
"""
from itertools import permutations
from math import gcd


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def classify(A, B):
    assert B >= 1 and B <= A <= 2 * B and gcd(A, B) == 1
    C = A - B
    vertices = {tuple(t[:2]) for t in permutations((-A, B, C))}
    assert len(vertices) == (3 if A == 2 * B else 6)
    if A == 2 * B:
        assert (A, B) == (2, 1)
        assert vertices == {(-2, 1), (1, -2), (1, 1)}
        assert all(abs(det(a, b)) == 3 for a, b in
                   [((-2, 1), (1, 1)), ((1, 1), (1, -2)), ((1, -2), (-2, 1))])
        return
    minus_u, minus_v = (-A, B), (-A, C)
    plus_u, plus_v = (B, -A), (B, C)
    m1, m2 = A * (2 * B - A), B * (2 * A - B)
    assert det(minus_u, minus_v) == m1
    assert det(plus_u, plus_v) == m2
    g, z, w = egcd(B, A)
    assert g == 1
    r1 = -z
    s1 = (-1 - B * r1) // A
    assert det(minus_u, (r1, s1)) == 1
    p1 = det(minus_v, (r1, s1))
    assert (p1 - (1 + (2 * B - A) * r1)) == 0
    assert ((p1 * minus_u[0] + m1 * r1,
             p1 * minus_u[1] + m1 * s1) == minus_v)
    g, z, w = egcd(A, B)
    assert g == 1
    r2 = z
    s2 = (1 - A * r2) // B
    assert det(plus_u, (r2, s2)) == 1
    p2 = det(plus_v, (r2, s2))
    assert p2 == 1 - (2 * A - B) * r2
    assert (p2 * plus_u[0] + m2 * r2,
            p2 * plus_u[1] + m2 * s2) == plus_v
    if m1 > 1:
        assert gcd(-p1, m1) == 1
    if m2 > 1:
        assert gcd(-p2, m2) == 1
    facet_pairs = []
    for i in range(3):
        for bnd in (-A, B):
            here = {tuple(v) for v in permutations((-A, B, C)) if v[i] == bnd}
            if len(here) == 2:
                v, w = tuple(here)
                assert abs(det(v[:2], w[:2])) == (m1 if bnd == -A else m2)
                facet_pairs.append((i, bnd))
    assert len(facet_pairs) == 6


def main():
    cases = 0
    for B in range(1, 81):
        for A in range(B, 2 * B + 1):
            if gcd(A, B) == 1:
                classify(A, B)
                cases += 1
    print(f"TORIC_SURFACE_BASKET_CHECK_OK; exact instances={cases}")


if __name__ == "__main__":
    main()
