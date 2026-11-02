#!/usr/bin/env python3
"""Exhaustive tests for extremal Rule-184 ring clearance and its Catalan encoding.
Python 3 standard library only. The proof for arbitrary length is in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def catalan(m):
    return comb(2 * m, m) // (m + 1)


def evolve(x, n):
    mask = (1 << n) - 1
    next_occupied = (x >> 1) | ((x & 1) << (n - 1))
    moving = x & (~next_occupied & mask)
    return (x ^ moving) | ((moving << 1) & mask) | (moving >> (n - 1))


def no_adjacent(x, n):
    return not (x & ((x >> 1) | ((x & 1) << (n - 1))))


def clearance_time(x, n):
    k = x.bit_count()
    if not 0 < k < n:
        raise ValueError('Only nontrivial fixed-density classes are considered')
    minority = min(k, n-k)
    mask = (1 << n) - 1
    for t in range(minority):
        v = x if k <= n-k else (~x & mask)
        if no_adjacent(v, n):
            return t
        x = evolve(x, n)
    raise AssertionError(('bound failed', n, k, x))


def cyclic_gaps(x, n):
    positions = [i for i in range(n) if x >> i & 1]
    return tuple(((positions[(j + 1) % len(positions)]
                   - positions[j]) % n) - 1 for j in range(len(positions)))


def minplus_time(gaps):
    k = len(gaps)
    deltas = tuple(v - 1 for v in gaps)
    times = []
    for i in range(k):
        best, first, running = 0, 0, 0
        for j in range(1, k):
            running += deltas[(i + j - 1) % k]
            if running < best:
                best, first = running, j
        times.append(first)
    return max(times)


def complement_reverse(x, n):
    # Reverse circular positions, then interchange occupied and empty.
    mask = (1 << n) - 1
    reversed_x = sum(((x >> i) & 1) << ((-i) % n) for i in range(n))
    return mask ^ reversed_x


def extremal_cut_count(gaps):
    k = len(gaps)
    d = tuple(v - 1 for v in gaps)
    result = 0
    for i in range(k):
        s = 0
        ok = True
        # Scan backwards across the k-1 included gaps.
        for j in range(1, k):
            s += d[(i + k - 1 - j) % k]
            if s >= 0:
                ok = False
                break
        result += ok
    return result


def verify():
    # Independent state-space simulation against the min-plus formula and
    # the proposed exact count for every nontrivial density.
    checks = 0
    for n in range(2, 17):
        counts = defaultdict(int)
        for x in range(1, (1 << n) - 1):
            k = x.bit_count()
            t = clearance_time(x, n)
            reduced = x if k <= n-k else complement_reverse(x, n)
            gaps = cyclic_gaps(reduced, n)
            assert t == minplus_time(gaps), (n, x, t, gaps)
            if t == min(k, n-k) - 1:
                assert extremal_cut_count(gaps) == 1
                counts[k] += 1
            else:
                assert extremal_cut_count(gaps) == 0
            checks += 1
        for k in range(1, n):
            m = min(k, n-k)
            assert counts[k] == n * catalan(m-1), (n, k, counts[k])
            assert counts[k] <= comb(n, k)

    # The strict-negative-prefix sequences are exactly Catalan-counted,
    # independent of the number of extra holes.
    def prefix_sequences(length, state=0):
        if length == 0:
            yield ()
            return
        for d in range(-1, -state):
            for continuation in prefix_sequences(length-1, state+d):
                yield (d,) + continuation

    for m in range(0, 9):
        assert sum(1 for _ in prefix_sequences(m)) == catalan(m)

    # Additional larger rings using direct simulation and min-plus paths.
    from random import Random
    rng = Random(271828)
    for n in (17, 18, 19, 24, 39, 64, 101):
        for _ in range(800):
            k = rng.randint(1, n-1)
            x = sum(1 << i for i in rng.sample(range(n), k))
            t = clearance_time(x, n)
            red = x if k <= n-k else complement_reverse(x, n)
            gaps = cyclic_gaps(red, n)
            assert t == minplus_time(gaps)
            assert extremal_cut_count(gaps) == int(t == min(k, n-k) - 1)
    print('VERIFY_OK', 'exhaustive_states', checks,
          'ring_lengths', '2..16', 'random_comparisons', 5600)

if __name__ == '__main__':
    verify()
