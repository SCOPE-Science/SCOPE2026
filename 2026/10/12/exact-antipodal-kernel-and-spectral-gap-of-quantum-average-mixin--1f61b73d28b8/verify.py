#!/usr/bin/env python3
"""Exact, standalone checks for average quantum mixing on halved hypercubes.

Python 3 standard library only. Graph and spectral normalizations are independent
of any floating-point matrix diagonalization.
"""
from fractions import Fraction
from math import comb


def weight(v):
    return v.bit_count()


def central_even(w):
    return Fraction(comb(w, w // 2), 2**w) if w % 2 == 0 else Fraction(0)


def claimed(d, w):
    a, b = central_even(w), central_even(d - w)
    return a + b - a * b if d % 2 == 0 else a + b


def eigenvalue(d, w):
    return ((d - 2 * w)**2 - d) // 2


def verify_graph(d):
    vertices = [x for x in range(2**d) if weight(x) % 2 == 0]
    n = len(vertices)
    # Quotient-dual representatives: the last bit of a is zero.
    chars = list(range(2**(d - 1)))
    table = [[1 if weight(a & x) % 2 == 0 else -1 for x in vertices]
             for a in chars]
    groups = {}
    for i, a in enumerate(chars):
        groups.setdefault(eigenvalue(d, weight(a)), []).append(i)
    # Reconstruct eigenfunctions directly from every graph edge.
    adjacency_tests = 0
    for i, a in enumerate(chars):
        theta = eigenvalue(d, weight(a))
        for j, x in enumerate(vertices):
            lhs = sum(table[i][j2] for j2, y in enumerate(vertices)
                      if weight(x ^ y) == 2)
            assert lhs == theta * table[i][j]
            adjacency_tests += 1
    # Fourier kernel of the actual spectral-projector Schur-square sum.
    numerator = []
    for j in range(n):
        numerator.append(sum(sum(table[i][j] for i in indices)**2
                             for indices in groups.values()))
    # Character eigenvalues computed by exact orthogonal Fourier transform.
    for i, a in enumerate(chars):
        num = sum(numerator[j] * table[i][j] for j in range(n))
        got = Fraction(num, n * n)
        assert got == claimed(d, weight(a)), (d, a, got, claimed(d, weight(a)))
    assert sum(numerator) == n * n  # stochastic row sum
    if d % 2 == 0:
        antipode = (1 << d) - 1
        place = {x: j for j, x in enumerate(vertices)}
        for j, x in enumerate(vertices):
            assert numerator[j] == numerator[place[x ^ antipode]]
        actual_positive = sum(claimed(d, weight(a)) > 0 for a in chars)
        assert actual_positive == n // 2
        assert all((claimed(d, weight(a)) == 0) == (weight(a) % 2 == 1)
                   for a in chars)
        m = d // 2
        u, v = 2 * (m // 2), 2 * ((m + 1) // 2)
        gap = claimed(d, u)  # equivalent to choice w=2 floor(m/2)
        assert gap == 1 - (1 - central_even(u)) * (1 - central_even(v))
        assert gap == min(claimed(d, weight(a)) for a in chars
                          if claimed(d, weight(a)) > 0)
    return adjacency_tests, n


def main():
    total_checks = 0
    total_modes = 0
    for d in range(3, 11):
        checks, n = verify_graph(d)
        total_checks += checks
        total_modes += n
    # Exhaustive combinatorial cross-count for small through medium dimensions;
    # this is a check of the counting formula, not a proof for all d.
    cross_checks = 0
    for d in range(4, 26, 2):
        for w in range(d + 1):
            count = 0
            for t in range(w + 1):
                for u in range(d - w + 1):
                    if (2*t == w or 2*u == d - w):
                        count += comb(w, t) * comb(d - w, u)
            assert Fraction(count, 2**d) == claimed(d, w)
            cross_checks += 1
    print("VERIFY_OK exact_graph_dimensions=3..10 adjacency_identities=%d "
          "character_modes=%d binomial_cross_checks=%d "
          "d6_rank=16/32 d8_rank=64/128" %
          (total_checks, total_modes, cross_checks))


if __name__ == '__main__':
    main()
