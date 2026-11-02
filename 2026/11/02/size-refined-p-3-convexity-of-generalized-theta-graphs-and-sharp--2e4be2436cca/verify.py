"""Independent P3-convex-set checks for parallel-path graphs.

Run: python3 verify.py. Uses only the Python standard library.
"""
from collections import Counter
from itertools import product
from math import comb


def graph(lengths):
    n = 2 + sum(length - 1 for length in lengths)
    adj = [set() for _ in range(n)]
    fresh = 2
    for length in lengths:
        vertices = [0] + list(range(fresh, fresh + length - 1)) + [1]
        fresh += length - 1
        for u, v in zip(vertices, vertices[1:]):
            adj[u].add(v)
            adj[v].add(u)
    assert fresh == n
    return adj


def brute_polynomial(lengths):
    adj = graph(lengths)
    n = len(adj)
    counts = Counter()
    for subset in range(1 << n):
        if all(
            ((subset >> u) & 1)
            or sum((subset >> v) & 1 for v in adj[u]) <= 1
            for u in range(n)
        ):
            counts[subset.bit_count()] += 1
    return +counts


def arm_transfer(length, a, b):
    """Independent four-state dynamic programming for one arm.

    Result indexed by (first internal bit, last internal bit, weight).
    """
    internal = length - 1
    dp = Counter()
    for first in (0, 1):
        dp[(a, first, first, first)] += 1
    for _ in range(1, internal):
        updated = Counter()
        for (prior, current, first, weight), multiplicity in dp.items():
            for nxt in (0, 1):
                if (prior, current, nxt) == (1, 0, 1):
                    continue
                updated[(current, nxt, first, weight + nxt)] += multiplicity
        dp = updated
    result = Counter()
    for (prior, current, first, weight), multiplicity in dp.items():
        if (prior, current, b) == (1, 0, 1):
            continue
        result[(first, current, weight)] += multiplicity
    return result


def transfer_polynomial(lengths):
    total = Counter()
    for a, b in product((0, 1), repeat=2):
        states = Counter({(0, 0, 0): 1})
        for length in lengths:
            arm = arm_transfer(length, a, b)
            nxt = Counter()
            for (first_sum, last_sum, weight), count in states.items():
                for (first, last, extra), frequency in arm.items():
                    ff = first_sum + first
                    ll = last_sum + last
                    if not a and ff > 1:
                        continue
                    if not b and ll > 1:
                        continue
                    nxt[(min(ff, 1), min(ll, 1), weight + extra)] += count * frequency
            states = nxt
        for (_, _, weight), count in states.items():
            total[weight + a + b] += count
    return +total


def equal_three_polynomial(r):
    counts = Counter({0: 1, 1: 2*r, 2: r*r})
    # The two cases with exactly one terminal selected.
    for j in range(r + 1):
        counts[j + 1] += 2*comb(r, j)
    for j in range(r):
        counts[j + 3] += 2*r*comb(r - 1, j)
    # Both terminals selected.
    for j in range(r + 1):
        counts[2 + 2*j] += comb(r, j)
    return +counts


def run():
    for r in range(3, 9):
        lengths = [3]*r
        direct = brute_polynomial(lengths)
        transferred = transfer_polynomial(lengths)
        closed = equal_three_polynomial(r)
        assert direct == transferred == closed, (r, direct, transferred, closed)
        assert sum(direct.values()) == (r+1)**2 + (r+3)*2**r
        assert direct[2*r + 2] == 1
        assert direct[2*r + 1] == 0
        assert direct[2*r] == r
        expected_support = set(range(r + 3)) | set(range(2*((r+3)//2), 2*r + 3, 2))
        assert {j for j,v in direct.items() if v} == expected_support
        print('EQUAL_THREE_LENGTHS_OK', r, sum(direct.values()))

    mixed = [
        [2, 2, 2], [2, 2, 3], [2, 3, 3], [3, 3, 4],
        [2, 3, 4], [2, 2, 2, 3, 3], [2, 4, 4],
        [4, 4, 4], [2, 2, 5], [3, 4, 5], [2, 5, 5],
        [2, 2, 2, 2, 2, 2],
    ]
    for lengths in mixed:
        direct = brute_polynomial(lengths)
        transferred = transfer_polynomial(lengths)
        assert direct == transferred, (lengths, direct, transferred)
        print('MIXED_ARMS_OK', lengths, sum(direct.values()))
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
