#!/usr/bin/env python3
"""Finite independent checks for the dyadic lag-one correlation phase identity."""
from collections import Counter
from itertools import accumulate


def digit_bit(n):
    # Occurrences of adjacent ones in the ordinary binary expansion.
    return ((n & (n >> 1)).bit_count()) & 1


def recursive_bits(n):
    b = [0] * (n + 1)
    for j in range(1, n + 1):
        m = j >> 1
        b[j] = b[m] ^ ((m & 1) if (j & 1) else 0)
    return b


def predicted(k, j, edge):
    q = j // (1 << (k - 1))
    return (1 if (k - 2 + q) % 2 == 0 else -1) * (edge(q) - edge(q + 1))


def check():
    N = 1 << 17
    r = recursive_bits(N + 1)
    assert all(r[j] == digit_bit(j) for j in range(N + 2))
    edges = [1 if r[j] == r[j + 1] else -1 for j in range(N + 1)]
    prefix = list(accumulate(edges, initial=0))
    def edge(j):
        return 1 if digit_bit(j) == digit_bit(j + 1) else -1

    cases = 0
    for k in range(3, 12):
        length = 1 << k
        for j in range(N - length + 1):
            direct = prefix[j + length] - prefix[j]
            rhs = predicted(k, j, edge)
            assert direct == rhs, (k, j, direct, rhs)
            assert direct in (-2, 0, 2)
            cases += 1
    for m in range(2, 14):
        histogram = Counter(predicted(3, q * 4, edge) for q in range(1 << m))
        assert histogram == {-2: 1 << (m - 2), 0: 1 << (m - 1), 2: 1 << (m - 2)}, (m, histogram)

    # Check independent digit generation at large offsets without storing a prefix.
    high_cases = 0
    for k in (3, 5, 7, 9, 11):
        length = 1 << k
        for base in (10**6 + 123, 10**9 + 127, 2**35 + 311, 2**41 + 91):
            for delta in (-1, 0, 1, 2):
                j = base + delta
                direct = sum(edge(i) for i in range(j, j + length))
                assert direct == predicted(k, j, edge)
                high_cases += 1
    print(f"VERIFY_OK independent_generators={N + 2} sliding_windows={cases} dyadic_histograms_m2_to13=12 large_offset_checks={high_cases}")


if __name__ == '__main__':
    check()
