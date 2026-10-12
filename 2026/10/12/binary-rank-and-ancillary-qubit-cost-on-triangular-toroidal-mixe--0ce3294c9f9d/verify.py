#!/usr/bin/env python3
"""Exact binary-rank checks for finite triangular toroidal graphs.

Uses only the Python standard library. The finite checks corroborate, but do not
replace, the unrestricted algebraic rank proof.
"""
from math import gcd


def rank2(rows):
    pivots = {}
    for word in rows:
        while word:
            high = word.bit_length() - 1
            if high not in pivots:
                pivots[high] = word
                break
            word ^= pivots[high]
    return len(pivots)


def adjacency_rows(m, n):
    offsets = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))
    out = []
    for a in range(m):
        for b in range(n):
            vertex = a * n + b
            word = 0
            for da, db in offsets:
                target = ((a + da) % m) * n + (b + db) % n
                assert target != vertex
                assert not ((word >> target) & 1), (m, n, vertex, target)
                word |= 1 << target
            assert word.bit_count() == 6
            out.append(word)
    return out


def polynomial_product(*terms):
    monomials = {(0, 0)}
    for term in terms:
        nxt = set()
        for a, b in monomials:
            for da, db in term:
                z = (a + da, b + db)
                if z in nxt:
                    nxt.remove(z)
                else:
                    nxt.add(z)
        monomials = nxt
    return monomials


def orbit_intersection_dimension(m, n):
    """Independent orbit-space calculation with parity constraints on orbit values."""
    g = gcd(m, n)
    # Choosing values on diagonal orbits, a row sum is (n/g)*C,
    # and a column sum is (m/g)*C, C=sum of the orbit values.
    parity_constraints = []
    if (n // g) % 2:
        parity_constraints.append((1 << g) - 1)
    if (m // g) % 2:
        parity_constraints.append((1 << g) - 1)
    assert parity_constraints
    return g - rank2(parity_constraints)


def main():
    assert polynomial_product(
        {(1, 0), (0, 0)}, {(0, 1), (0, 0)},
        {(1, 1), (0, 0)}, {(-1, -1)}
    ) == {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)}

    rank_cases = 0
    winding_cases = 0
    for m in range(3, 26):
        for n in range(3, 26):
            g = gcd(m, n)
            expected_nullity = m + n + g - 2
            expected_rank = m * n - expected_nullity
            assert expected_rank % 2 == 0
            assert orbit_intersection_dimension(m, n) == g - 1
            winding_cases += 1
            rows = adjacency_rows(m, n)
            assert rank2(rows) == expected_rank, (m, n, rank2(rows), expected_rank)
            rank_cases += 1

    oriented_cases = 0
    for m, n in ((3, 3), (3, 5), (4, 4), (5, 6), (6, 8), (8, 11)):
        rows = adjacency_rows(m, n)
        N = m * n
        directed = [0] * N
        for i in range(N):
            for j in range(i + 1, N):
                if (rows[i] >> j) & 1:
                    if (7 * i + 11 * j) % 13 < 6:
                        directed[i] |= 1 << j
                    else:
                        directed[j] |= 1 << i
        sym = [0] * N
        for i in range(N):
            for j in range(N):
                if (directed[i] >> j) & 1:
                    sym[i] ^= 1 << j
                    sym[j] ^= 1 << i
        assert sym == rows
        assert rank2(sym) == m * n - m - n - gcd(m, n) + 2
        oriented_cases += 1

    print('VERIFY_OK symbolic_factorization=1 '
          f'all_parity_rank_tests={rank_cases} '
          f'diagonal_orbit_parity_tests={winding_cases} '
          f'orientation_tests={oriented_cases} '
          'm_n_each_3_to_25=true')


if __name__ == '__main__':
    main()
