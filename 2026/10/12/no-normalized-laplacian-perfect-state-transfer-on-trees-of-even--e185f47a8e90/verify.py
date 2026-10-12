"""Exact finite corroboration for normalized-Laplacian spectral parity on trees.

Run: python3 verify.py. Python standard library only. The theorem for arbitrary
order follows from the accompanying proof, not these finite tests.
"""
from fractions import Fraction
from math import comb


def edge_list_path(n):
    return [(i, i + 1) for i in range(n - 1)]


def edge_list_star(n):
    return [(0, i) for i in range(1, n)]


def edge_list_double_star(p, q):
    return [(0, 1)] + [(0, j) for j in range(2, 2 + p)] + [
        (1, j) for j in range(2 + p, 2 + p + q)
    ]


def edge_list_broom(leaves, handle):
    return [(0, i) for i in range(1, leaves + 1)] + [
        (leaves + j, leaves + j + 1) if j else (0, leaves + 1)
        for j in range(handle)
    ]


def tree_coefficients(n, edges):
    assert n >= 2 and len(edges) == n - 1
    deg = [0] * n
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        deg[u] += 1
        deg[v] += 1
    assert all(deg)
    # For a tree, only fixed points and pair transpositions contribute
    # to the determinant of z*D-(D-A).
    terms = []

    def rec(i, busy, pairs):
        if i == len(edges):
            weight = (-1) ** pairs
            unmatched = n - 2 * pairs
            for v in range(n):
                if not ((busy >> v) & 1):
                    weight *= deg[v]
            terms.append((unmatched, weight))
            return
        u, v = edges[i]
        rec(i + 1, busy, pairs)
        if not (busy >> u) & 1 and not (busy >> v) & 1:
            rec(i + 1, busy | (1 << u) | (1 << v), pairs + 1)

    rec(0, 0, 0)
    return deg, terms


def value(terms, x):
    return sum((w * (x - 1) ** k for k, w in terms), Fraction(0))


def derivative_zero(terms):
    return sum(w * k * (-1) ** (k - 1) for k, w in terms if k)


def run():
    cases = []
    for n in range(2, 17, 2):
        cases.extend([("path", n, edge_list_path(n)),
                      ("star", n, edge_list_star(n))])
    for p, q in [(1, 1), (1, 3), (2, 2), (1, 5), (2, 4),
                 (3, 3), (1, 7), (2, 6), (3, 5), (4, 4), (5, 5)]:
        cases.append(("double_star", p + q + 2,
                      edge_list_double_star(p, q)))
    for leaves, handle in [(3, 2), (3, 4), (4, 3), (5, 2),
                           (5, 4), (6, 3), (7, 4)]:
        n = leaves + handle + 1
        if n % 2 == 0:
            cases.append(("broom", n, edge_list_broom(leaves, handle)))

    probes = 0
    for family, n, edges in cases:
        deg, terms = tree_coefficients(n, edges)
        assert value(terms, Fraction(0)) == 0, (family, n)
        assert derivative_zero(terms) == -2 * (n - 1), (family, n)
        assert value(terms, Fraction(2)) == 0, (family, n)
        # Every below probe must be nonroot; this independently corroborates
        # the parity obstruction for a finite set of rational candidates.
        for q in range(3, 20, 2):
            for p in range(2, 2 * q, 2):
                if __import__('math').gcd(p, q) > 1:
                    continue
                probes += 1
                assert value(terms, Fraction(p, q)) != 0, (family, n, p, q)
    print("VERIFY_OK tree_cases=%d parity_probes=%d derivative_and_endpoint_identities=%d" %
          (len(cases), probes, len(cases) * 3))

if __name__ == "__main__":
    run()
