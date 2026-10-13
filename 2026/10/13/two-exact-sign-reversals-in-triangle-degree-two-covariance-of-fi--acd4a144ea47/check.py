"""Exact checks for the degree-two vertex / triangle covariance in uniform fixed-edge random graphs.
Only Python standard library is required; run: python degree2_triangle_check.py.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def falling(x, k):
    z = 1
    for j in range(k):
        z *= x - j
    return z


def predicted(n, m):
    N = comb(n, 2)
    B = comb(n - 1, 2)
    if m < 3 or m > B + 2:
        return Fraction(0)
    e_deg2 = Fraction(n * comb(n - 1, 2) * comb(B, m - 2), comb(N, m))
    conditional = Fraction(comb(n - 1, 3) * falling(m - 2, 3), falling(B, 3)) + Fraction(m - 2, B)
    mean_tri = Fraction(comb(n, 3) * falling(m, 3), falling(N, 3))
    return e_deg2 * (conditional - mean_tri)


def brute(n):
    edges = list(combinations(range(n), 2))
    N = len(edges)
    triples = [frozenset(combinations(t, 2)) for t in combinations(range(n), 3)]
    checked = 0
    for m in range(N + 1):
        degree_sum = tri_sum = prod_sum = 0
        for selection in combinations(edges, m):
            ss = set(selection)
            degrees = [0] * n
            for a, b in selection:
                degrees[a] += 1
                degrees[b] += 1
            v2 = sum(d == 2 for d in degrees)
            tri = sum(t.issubset(ss) for t in triples)
            degree_sum += v2
            tri_sum += tri
            prod_sum += v2 * tri
        denom = comb(N, m)
        actual = Fraction(prod_sum, denom) - Fraction(degree_sum * tri_sum, denom * denom)
        assert actual == predicted(n, m), (n, m, actual, predicted(n, m))
        checked += 1
    return checked


def q(n, m):
    B = comb(n - 1, 2)
    N = comb(n, 2)
    return (Fraction(1, B) +
            Fraction(comb(n - 1, 3) * (m - 3) * (m - 4), B * (B - 1) * (B - 2)) -
            Fraction(comb(n, 3) * m * (m - 1), N * (N - 1) * (N - 2)))


def main():
    # Every labeled simple graph for n<=6 is processed, including all edge counts.
    count = sum(brute(n) for n in range(4, 7))
    # Independent test of sign change and strict convexity on a broad finite grid.
    signs = 0
    for n in range(6, 201):
        B = comb(n - 1, 2)
        assert q(n, 3) > 0 and q(n, n) < 0 and q(n, B + 2) > 0
        a = q(n, 5) - 2 * q(n, 4) + q(n, 3)
        assert a > 0
        ms = sorted(set([3, 4, 5, max(3, n-1), n, n+1, B//4, B//2, B, B+1, B+2]))
        for m in ms:
            if not 3 <= m <= B+2:
                continue
            x = q(n, m)
            if m == 3 or m == B+2:
                assert x > 0
            # This check tests the signed closed expression directly.
            if n<=40:
                assert predicted(n, m) == (Fraction(n*comb(n-1,2)*comb(B,m-2),comb(comb(n,2),m)) * (m-2) * x)
            signs += 1
    print(f"VERIFIED exact graph-enumeration cells={count}, exact q evaluations={signs}, positive quadratic coefficient for n=6..200")

if __name__ == '__main__':
    main()
