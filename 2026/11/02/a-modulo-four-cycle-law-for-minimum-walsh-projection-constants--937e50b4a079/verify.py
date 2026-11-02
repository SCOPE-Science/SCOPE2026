"""Exact-rational tests for projection constants of graph-supported Walsh subspaces.
No external packages are needed. Tests are finite checks, not an infinite proof.
"""
from fractions import Fraction
from itertools import product
from math import comb


def rademacher_baseline(m):
    return Fraction(m * comb(m - 1, (m - 1) // 2), 2 ** (m - 1))


def predicted(m, ell):
    baseline = rademacher_baseline(m)
    if ell % 2:
        return baseline
    k = ell // 2
    if m % 2:
        q = Fraction((m + 1) * comb(m, (m - 1) // 2), 2 ** m)
    else:
        q = Fraction(m * comb(m, m // 2), 2 ** m)
    delta = (-1) ** (k - 1) * q * Fraction(comb(m // 2, k), (2 * k - 1) * comb(m, 2 * k))
    return baseline + delta


def unicyclic_edges(m, ell):
    """ell-cycle and a pendant path with m-ell additional edges."""
    edges = [(i, (i + 1) % ell) for i in range(ell)]
    edges += [(ell - 1 if j == ell else j - 1, j) for j in range(ell, m)]
    return edges


def direct(m, ell):
    edges = unicyclic_edges(m, ell)
    assert len(edges) == m and len(set(tuple(sorted(e)) for e in edges)) == m
    total = sum(abs(sum(x[u] * x[v] for u, v in edges))
                for x in product((-1, 1), repeat=m))
    return Fraction(total, 2 ** m)


def moment_direct(m, ell):
    total = sum(abs(sum(vals)) * __import__('math').prod(vals[:ell])
                for vals in product((-1, 1), repeat=m))
    return Fraction(total, 2 ** m)


if __name__ == '__main__':
    cases = 0
    for m in range(3, 12):
        for ell in range(3, m + 1):
            actual = direct(m, ell)
            assert actual == predicted(m, ell), (m, ell, actual, predicted(m, ell))
            if ell % 2 == 0:
                assert moment_direct(m, ell) == actual - rademacher_baseline(m)
            cases += 1
    assert predicted(4, 4) == 1
    assert predicted(6, 6) == Fraction(9, 4)
    assert predicted(5, 5) == rademacher_baseline(5)
    print('UNICYCLIC_WALSH_EXACT_OK', cases)
