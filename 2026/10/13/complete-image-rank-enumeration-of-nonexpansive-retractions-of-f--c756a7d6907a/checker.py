#!/usr/bin/env python3
"""Independent exhaustive checks for image-rank counts of chain contractions."""
from itertools import product


def predicted(n):
    results = {}
    for r in range(1, n + 1):
        lengths = n - r
        positions = [0] * r
        positions[0] = 1
        walks = [1]
        for _ in range(lengths):
            positions = [sum(positions[max(0, j - 1):min(r, j + 2)])
                         for j in range(r)]
            walks.append(sum(positions))
        results[r] = sum(walks[j] * walks[lengths - j]
                         for j in range(lengths + 1))
    return results


def enumerate_maps(n):
    counts = {r: 0 for r in range(1, n + 1)}
    interval_counts = {}
    for f in product(range(n), repeat=n):
        if any(abs(f[j + 1] - f[j]) > 1 for j in range(n - 1)):
            continue
        if any(f[f[j]] != f[j] for j in range(n)):
            continue
        rank = len(set(f))
        counts[rank] += 1
        if n == 7 and rank == 3:
            lo = min(f)
            interval_counts[lo] = interval_counts.get(lo, 0) + 1
    return counts, interval_counts


def verify():
    for n in range(1, 8):
        expected = predicted(n)
        observed, intervals = enumerate_maps(n)
        assert observed == expected, (n, expected, observed)
        if n >= 2:
            assert expected[2] == (n - 1) * 2 ** (n - 2)
        if n >= 3:
            assert expected[n - 1] == 4
        if n >= 5:
            assert expected[n - 2] == 14
        if n == 7:
            assert [intervals.get(i, 0) for i in range(5)] == [29, 24, 25, 24, 29]
            assert [expected[i] for i in range(1, 8)] == [7, 192, 131, 46, 14, 4, 1]
            assert expected[3] == 131
    a_6, a_7 = 12, 29
    proposed = 2 * (a_7 + 3 * a_6)
    assert proposed == 130 != predicted(7)[3]
    print("VERIFY_OK")


if __name__ == "__main__":
    verify()
