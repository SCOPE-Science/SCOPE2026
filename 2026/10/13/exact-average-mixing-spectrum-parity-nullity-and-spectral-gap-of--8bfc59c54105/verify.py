#!/usr/bin/env python3
"""Exact integer verification of folded-hypercube quantum average mixing spectra.

Usage: python3 verify.py
Only the Python standard library is needed. Finite tests corroborate, but do
not replace, the proof for arbitrary dimension.
"""
from fractions import Fraction
from math import comb


def eigenvalue_formula(d, w):
    if w == 0:
        return Fraction(1)
    if w % 2:
        raise ValueError("Characters of the folded cube have even weight")
    if w < d:
        return Fraction(comb(w, w // 2), 2 ** w)
    return Fraction(comb(d, d // 2), 2 ** (d - 1)) if d % 4 == 0 else Fraction(0)


def run_case(d):
    assert d >= 3
    n = 1 << (d - 1)
    even_characters = [a for a in range(1 << d) if a.bit_count() % 2 == 0]
    assert len(even_characters) == n
    generators = [1 << i for i in range(d - 1)] + [n - 1]
    assert len(generators) == len(set(generators)) == d

    # Independently check every adjacency eigenvector and eigenvalue.
    adj_tests = 0
    for a in even_characters:
        lam = d - 2 * a.bit_count()
        for x in range(n):
            lhs = sum((-1) ** ((a & (x ^ g)).bit_count() % 2)
                      for g in generators)
            rhs = lam * ((-1) ** ((a & x).bit_count() % 2))
            assert lhs == rhs
            adj_tests += 1

    # Compute the spectral projectors from orthogonal Walsh characters,
    # squaring entries before taking the long-time mean.
    even_r = list(range(0, d + 1, 2))
    groups = [[a for a in even_characters if a.bit_count() == r]
              for r in even_r]
    first_row_scaled = []
    for z in range(n):
        sums = [sum(1 if ((a & z).bit_count() % 2 == 0) else -1
                    for a in group) for group in groups]
        first_row_scaled.append(sum(s * s for s in sums))
    assert sum(first_row_scaled) == n * n
    assert first_row_scaled[0] == sum(len(group) ** 2 for group in groups)

    # Transform the independently constructed average matrix; no floating point.
    eigen_tests = 0
    nulls = []
    smallest_pos = Fraction(1)
    for a in even_characters:
        e_scaled = sum(v if ((a & z).bit_count() % 2 == 0) else -v
                       for z, v in enumerate(first_row_scaled))
        eig = Fraction(e_scaled, n * n)
        expected = eigenvalue_formula(d, a.bit_count())
        assert eig == expected, (d, a, eig, expected)
        if eig == 0:
            nulls.append(a)
        else:
            assert eig > 0
            smallest_pos = min(smallest_pos, eig)
        eigen_tests += 1
    expected_nulls = [((1 << d) - 1)] if d % 4 == 2 else []
    assert nulls == expected_nulls
    expected_gap = Fraction(comb(2 * ((d - 1) // 2), (d - 1) // 2),
                            4 ** ((d - 1) // 2))
    assert smallest_pos == expected_gap
    return n, adj_tests, eigen_tests, len(nulls)


def main():
    total_adj = total_modes = 0
    for d in range(3, 10):
        n, adj, modes, nullity = run_case(d)
        total_adj += adj
        total_modes += modes
        print("d=%d vertices=%d nullity=%d exact_modes=%d" %
              (d, n, nullity, modes))
    print("VERIFY_OK dimensions=3..9 adjacency_tests=%d eigenmodes=%d"
          % (total_adj, total_modes))


if __name__ == "__main__":
    main()
