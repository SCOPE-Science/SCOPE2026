#!/usr/bin/env python3
"""Finite-field checks for the subfield-rank law for reused one-bit trace leakage.

The script implements GF(2^m) for m=2,3,4, computes the F_2-rank of
computation columns, and verifies that this rank equals the rank of the
corresponding trace-leakage functionals. It also checks the no-amplification
identity for base-field computation matrices and full share recovery in a
rank-saturated one-input example.
"""

from itertools import product
import random

IRR = {2: 0b111, 3: 0b1011, 4: 0b10011}


def gf_mul(a, b, m):
    mod = IRR[m]
    mask = (1 << m) - 1
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= mod
    return out & mask


def gf_square(a, m):
    return gf_mul(a, a, m)


def gf_trace(a, m):
    s = 0
    x = a
    for _ in range(m):
        s ^= x
        x = gf_square(x, m)
    assert s in (0, 1)
    return s


def gf_dot(g, x, m):
    z = 0
    for a, b in zip(g, x):
        z ^= gf_mul(a, b, m)
    return z


def binary_rank(rows, width):
    rows = list(rows)
    rank = 0
    for col in range(width - 1, -1, -1):
        pivot = next((r for r in range(rank, len(rows)) if (rows[r] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for r in range(len(rows)):
            if r != rank and ((rows[r] >> col) & 1):
                rows[r] ^= rows[rank]
        rank += 1
    return rank


def expand_column(g, m):
    """Pack g in GF(2^m)^K as a Km-bit vector over GF(2)."""
    word = 0
    for a, val in enumerate(g):
        for t in range(m):
            if (val >> t) & 1:
                word |= 1 << (a * m + t)
    return word


def functional_row(g, beta, m):
    """Truth-functional coefficient row of x -> Tr(beta <g,x>) on a polynomial basis."""
    K = len(g)
    word = 0
    for a in range(K):
        for t in range(m):
            x = [0] * K
            x[a] = 1 << t
            y = gf_mul(beta, gf_dot(g, x, m), m)
            if gf_trace(y, m):
                word |= 1 << (a * m + t)
    return word


def subfield_rank(columns, m):
    if not columns:
        return 0
    K = len(columns[0])
    return binary_rank([expand_column(g, m) for g in columns], K * m)


def leakage_rank(columns, beta, m):
    if not columns:
        return 0
    K = len(columns[0])
    return binary_rank([functional_row(g, beta, m) for g in columns], K * m)


def random_columns(K, N, m, rng):
    return [[rng.randrange(1 << m) for _ in range(K)] for _ in range(N)]


def check_rank_identity():
    rng = random.Random(260919)
    checked = 0
    for m in (2, 3, 4):
        for K in range(1, 4):
            for N in range(K, min(K * m + 2, 8)):
                for _ in range(200):
                    cols = random_columns(K, N, m, rng)
                    d = subfield_rank(cols, m)
                    for beta in range(1, 1 << m):
                        assert leakage_rank(cols, beta, m) == d
                        checked += 1
    return checked


def check_base_field_no_amplification():
    columns = [
        [1, 0, 0], [0, 1, 0], [0, 0, 1],
        [1, 1, 0], [0, 1, 1], [1, 1, 1],
    ]
    checked = 0
    for m in (2, 3, 4):
        assert subfield_rank(columns, m) == 3
        for beta in range(1, 1 << m):
            for x in product(range(1 << m), repeat=3):
                direct = [gf_trace(gf_mul(beta, a, m), m) for a in x]
                out = []
                for g in columns:
                    out.append(gf_trace(gf_mul(beta, gf_dot(g, x, m), m), m))
                predicted = [sum((g[a] & direct[a]) for a in range(3)) & 1 for g in columns]
                assert out == predicted
                checked += 1
    return checked


def check_rank_saturation_recovers_share():
    checked = 0
    for m in (2, 3, 4):
        alpha = 2
        coeffs = []
        cur = 1
        for _ in range(m):
            coeffs.append([cur])
            cur = gf_mul(cur, alpha, m)
        assert subfield_rank(coeffs, m) == m
        for beta in range(1, 1 << m):
            seen = {}
            for x in range(1 << m):
                transcript = tuple(
                    gf_trace(gf_mul(beta, gf_mul(g[0], x, m), m), m)
                    for g in coeffs
                )
                assert transcript not in seen
                seen[transcript] = x
                checked += 1
            assert len(seen) == (1 << m)
    return checked


def check_systematic_random_threshold_formula():
    checked = 0
    for D in range(1, 5):
        for L in range(D, min(D + 3, 6)):
            total = 1 << (D * L)
            full = 0
            for packed in range(total):
                rows = []
                z = packed
                for _ in range(L):
                    rows.append(z & ((1 << D) - 1))
                    z >>= D
                if binary_rank(rows, D) == D:
                    full += 1
            expected_num = 1
            for i in range(D):
                expected_num *= (1 << L) - (1 << i)
            assert full == expected_num
            assert total == 1 << (D * L)
            checked += 1
    return checked


def main():
    a = check_rank_identity()
    b = check_base_field_no_amplification()
    c = check_rank_saturation_recovers_share()
    d = check_systematic_random_threshold_formula()
    print("PASS")
    print(f"rank_identity_checks={a}")
    print(f"base_field_transcript_checks={b}")
    print(f"rank_saturation_share_checks={c}")
    print(f"random_threshold_exact_cases={d}")


if __name__ == "__main__":
    main()
