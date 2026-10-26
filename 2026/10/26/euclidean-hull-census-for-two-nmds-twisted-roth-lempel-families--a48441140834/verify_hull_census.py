#!/usr/bin/env python3
"""Exact Euclidean-hull census for two twisted Roth--Lempel families over F_37.

No external packages are required. All subset conditions and matrix ranks are
computed with exact arithmetic modulo 37.
"""
from collections import Counter
from itertools import combinations

P = 37
ALPHA = tuple(range(1, 12))
K = 5


def rank_mod(matrix, p=P):
    a = [[entry % p for entry in row] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for r in range(m):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [(a[r][c] - factor * a[rank][c]) % p
                        for c in range(n)]
        rank += 1
        if rank == m:
            break
    return rank


def subset_sums(size):
    out = []
    for subset in combinations(ALPHA, size):
        s1 = sum(subset) % P
        s2 = sum(subset[i] * subset[j]
                 for i in range(size) for j in range(i + 1, size)) % P
        out.append((s1, s2))
    return tuple(out)


S4 = subset_sums(4)
S5 = subset_sums(5)


def is_nmds(ell, eta, delta):
    inv_eta = pow(eta, -1, P)
    inv_eta_delta = pow((eta * delta) % P, -1, P)
    if ell == 4:
        # Theorem 4.2 for ell = k-1 in arXiv:2609.17304v1.
        condition_a = not any(
            s1 == (-inv_eta) % P and s2 == (-delta * inv_eta) % P
            for s1, s2 in S5
        )
        condition_b = (
            any((eta * s1) % P == P - 1 for s1, _ in S5)
            or any((delta - s1 - eta * (s1 * s1 - s2)) % P == 0
                   for s1, s2 in S4)
        )
        return condition_a and condition_b

    if ell == 3:
        # Theorem 4.3 for ell = k-2 in arXiv:2609.17304v1.
        condition_a = not any(s1 == 0 and s2 == inv_eta for s1, s2 in S4)
        condition_b = not any(
            (s1 == 0 and s2 == inv_eta)
            or (s1 == inv_eta_delta and s2 == inv_eta)
            for s1, s2 in S5
        )
        condition_c = (
            any((eta * s2) % P == 1 for _, s2 in S5)
            or any((1 + eta * (s1 * s1 - s2)) % P == 0
                   or (delta * (1 + eta * (s1 * s1 - s2)) - s1) % P == 0
                   for s1, s2 in S4)
        )
        return condition_a and condition_b and condition_c

    raise ValueError("Only the two boundary cases ell=3,4 are covered")


def generator_matrix(ell, eta, delta):
    rows = []
    for i in range(K):
        row = []
        for a in ALPHA:
            value = pow(a, i, P)
            if i == ell:
                value = (value + eta * pow(a, K, P)) % P
            row.append(value)
        if i == 3:
            tail = [0, 1]
        elif i == 4:
            tail = [1, delta]
        else:
            tail = [0, 0]
        rows.append(row + tail)
    return rows


def hull_dimension(ell, eta, delta):
    g = generator_matrix(ell, eta, delta)
    assert rank_mod(g) == K
    gram = [[sum(g[i][t] * g[j][t] for t in range(len(g[0]))) % P
             for j in range(K)] for i in range(K)]
    return K - rank_mod(gram)


def main():
    expected = {
        3: {
            "all": {0: 1266, 1: 30},
            "nmds": {0: 584, 1: 9},
            "exceptional": [(9, 9), (9, 17), (10, 5), (11, 19),
                            (17, 9), (19, 34), (23, 8), (23, 18), (34, 26)],
            "nmds_count": 593,
        },
        4: {
            "all": {0: 1258, 1: 38},
            "nmds": {0: 943, 1: 27},
            "exceptional": [(2, 5), (2, 31), (6, 18), (6, 31), (8, 9),
                            (10, 28), (10, 34), (13, 19), (13, 25),
                            (17, 22), (17, 35), (18, 6), (18, 8),
                            (21, 11), (21, 22), (24, 6), (25, 12),
                            (25, 34), (26, 4), (27, 35), (27, 36),
                            (29, 11), (34, 12), (35, 4), (35, 19),
                            (36, 7), (36, 10)],
            "nmds_count": 970,
        },
    }
    for ell in (3, 4):
        all_counts = Counter()
        nmds_counts = Counter()
        nmds_pairs = []
        for eta in range(1, P):
            for delta in range(1, P):
                hdim = hull_dimension(ell, eta, delta)
                all_counts[hdim] += 1
                if is_nmds(ell, eta, delta):
                    nmds_counts[hdim] += 1
                    nmds_pairs.append((eta, delta))
        exceptional = sorted((eta, delta) for eta, delta in nmds_pairs
                             if hull_dimension(ell, eta, delta) == 1)
        got = {
            "all": dict(sorted(all_counts.items())),
            "nmds": dict(sorted(nmds_counts.items())),
            "exceptional": exceptional,
            "nmds_count": len(nmds_pairs),
        }
        assert got == expected[ell], (ell, got, expected[ell])
        print(f"ell={ell}: all_pairs={36*36}, all_hulls={got['all']}, "
              f"nmds_pairs={got['nmds_count']}, nmds_hulls={got['nmds']}")
        print("  nonzero-hull NMDS pairs:", exceptional)
    assert is_nmds(4, 1, 1) and hull_dimension(4, 1, 1) == 0
    assert is_nmds(3, 3, 1) and hull_dimension(3, 3, 1) == 0
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
