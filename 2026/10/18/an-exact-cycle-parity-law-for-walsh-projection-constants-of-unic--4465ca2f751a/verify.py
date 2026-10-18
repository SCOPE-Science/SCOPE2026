"""Exact arithmetic checks for edge-character projection constants.

The infinite-family proof is analytic; these tests independently enumerate
spin configurations and parity-constrained edge-sign configurations.
"""
from fractions import Fraction
from itertools import product
from math import comb


def predicted(m, k):
    assert m >= k >= 3
    a = Fraction(m * comb(m - 1, (m - 1) // 2), 2 ** (m - 1))
    if k % 2:
        return a
    s = k // 2
    h = (m - 2) // 2
    b = Fraction(comb(m - 2, h), 2 ** (m - 2))
    correction = (-1) ** (s - 1) * b * Fraction(comb(h, s - 1), comb(m - 2, 2 * s - 2))
    return a + correction


def graph_edges(m, k, mode):
    edges = [(i, (i + 1) % k) for i in range(k)]
    if mode == 'star':
        edges += [(0, k + j) for j in range(m - k)]
        n = m
    elif mode == 'path':
        edges += [(0 if j == 0 else k + j - 1, k + j) for j in range(m - k)]
        n = m
    elif mode == 'disjoint':
        edges += [(k + 2 * j, k + 2 * j + 1) for j in range(m - k)]
        n = k + 2 * (m - k)
    else:
        raise ValueError(mode)
    assert len(edges) == m
    return n, edges


def vertex_average(m, k, mode):
    n, edges = graph_edges(m, k, mode)
    total = 0
    for bits in range(1 << n):
        energy = sum((1 if (bits >> u & 1) == (bits >> v & 1) else -1) for u, v in edges)
        total += abs(energy)
    return Fraction(total, 1 << n)


def parity_average(m, k):
    total = 0
    for bits in range(1 << m):
        if (bits & ((1 << k) - 1)).bit_count() & 1:
            continue
        energy = m - 2 * bits.bit_count()
        total += abs(energy)
    return Fraction(total, 1 << (m - 1))


def main():
    checks = 0
    for m in range(3, 14):
        for k in range(3, m + 1):
            expected = predicted(m, k)
            assert parity_average(m, k) == expected, (m, k, 'parity')
            checks += 1
            for mode in ('star', 'path'):
                assert vertex_average(m, k, mode) == expected, (m, k, mode)
                checks += 1
            if m <= 9:
                assert vertex_average(m, k, 'disjoint') == expected, (m, k, 'disjoint')
                checks += 1
            if k % 2 == 0:
                a = Fraction(m * comb(m - 1, (m - 1) // 2), 2 ** (m - 1))
                assert (expected - a) * (-1) ** (k // 2 - 1) > 0
                checks += 1
            else:
                a = Fraction(m * comb(m - 1, (m - 1) // 2), 2 ** (m - 1))
                assert expected == a
                checks += 1
    assert (predicted(6, 4), predicted(6, 5), predicted(6, 6)) == (
        Fraction(7, 4), Fraction(15, 8), Fraction(9, 4))
    print('UNICYCLE_WALSH_PROJECTION_EXACT_OK', checks)
    print('SIX_EDGE_CYCLE_LENGTHS', [str(predicted(6, k)) for k in (4, 5, 6)])


if __name__ == '__main__':
    main()
