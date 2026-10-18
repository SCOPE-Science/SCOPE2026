#!/usr/bin/env python3
"""Independent finite checks for cycle-power strong-majority colorings.

Run: python3 verify_cycle_majority.py
Only Python's standard library is used. The general proof is separate.
"""
from collections import Counter
from itertools import product
from math import gcd


def valuation_two(a):
    t = 0
    while a % 2 == 0:
        t += 1
        a //= 2
    return t


def predicted_two(n, k):
    return n % 2 == 0 if k % 2 == 0 else n % (2 ** (valuation_two(k + 1) + 1)) == 0


def neighbors(n, k, v):
    return [((v + d) % n) for d in range(-k, k + 1) if d != 0]


def valid(w, k):
    n = len(w)
    for v in range(n):
        counts = Counter(w[u] for u in neighbors(n, k, v))
        if max(counts.values()) > k:
            return False
    return True


def cyclic_three(n):
    q, r = divmod(n, 3)
    return tuple(map(int, '012' * q + ('', '1', '01')[r]))


def binary_witness(n, k):
    if not predicted_two(n, k):
        return None
    if k % 2 == 0:
        return tuple(i % 2 for i in range(n))
    p = 2 ** valuation_two(k + 1)
    return tuple((i // p) % 2 for i in range(n))


def brute_binary_count(n, k):
    adjacency = [neighbors(n, k, v) for v in range(n)]
    count = 0
    for mask in range(1 << n):
        if all(sum(1 if (mask >> j) & 1 else -1 for j in adjacency[v]) == 0
               for v in range(n)):
            count += 1
    return count


def check_local_junction():
    expected = {
        1: {'01210', '10120', '12101', '20121', '21012'},
        2: {'01012', '01201', '10120', '12010', '20101', '20120'},
    }
    for r in (1, 2):
        w = '012' * 4 + ('', '1', '01')[r]
        n = len(w)
        inserted = set(range(n - r, n))
        windows = {
            ''.join(w[(i + j) % n] for j in range(-2, 3))
            for i in range(n)
            if inserted.intersection((i + j) % n for j in range(-2, 3))
        }
        assert windows == expected[r], (r, windows)
        assert all(max(sum(s[j] == c for j in (0, 1, 3, 4))
                       for c in '012') <= 2 for s in windows)
    return 11


def main():
    windows_checked = check_local_junction()
    constructive = 0
    two_constructive = 0
    for k in range(2, 61):
        for n in range(2 * k + 2, min(4 * k + 80, 301)):
            assert valid(cyclic_three(n), k), ('three', n, k)
            constructive += 1
            w = binary_witness(n, k)
            if w is not None:
                assert valid(w, k), ('two', n, k)
                two_constructive += 1
    brute_cases = 0
    count_cases = 0
    for k in range(2, 8):
        for n in range(2 * k + 2, 17):
            actual = brute_binary_count(n, k)
            assert (actual > 0) == predicted_two(n, k), (n, k, actual)
            brute_cases += 1
            if gcd(n, k) == 1:
                g = gcd(n, k + 1)
                expected = (1 << g) if n // g % 2 == 0 else 0
                assert actual == expected, (n, k, actual, expected)
                count_cases += 1
    print('PASS: %d local 5-letter junction windows' % windows_checked)
    print('PASS: %d explicit 3-color constructions; %d explicit 2-color constructions' % (constructive, two_constructive))
    print('PASS: %d exhaustive two-color existence tests with up to 16 vertices' % brute_cases)
    print('PASS: %d exact coprime-case labelled coloring counts' % count_cases)


if __name__ == '__main__':
    main()
