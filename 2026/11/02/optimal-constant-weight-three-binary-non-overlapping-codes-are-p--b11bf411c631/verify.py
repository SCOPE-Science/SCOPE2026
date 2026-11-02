#!/usr/bin/env python3
"""Reproduce exact fixed-weight-three non-overlapping code calculations."""
from itertools import combinations
from math import comb


def code(n):
    h = n // 3
    b = n - h - 1
    result = []
    for i in range(1, h + 1):
        for j in range(i + 1, b + 1):
            letters = ['0'] * n
            for t in (0, i, j):
                letters[t] = '1'
            result.append(''.join(letters))
    return result


def overlaps(u, v):
    assert len(u) == len(v)
    return any(u[:k] == v[-k:] for k in range(1, len(u)))


def primitive(s):
    n = len(s)
    return all(s != s[:d] * (n // d) for d in range(1, n) if n % d == 0)


def canonical(s):
    return min(s[i:] + s[:i] for i in range(len(s)))


def cardinality(n):
    return ((n - 1) * (n - 2)) // 6


def check():
    overlap_pairs = 0
    primitive_necklaces = 0
    tested_words = 0
    for n in range(3, 27):
        C = code(n)
        expected = cardinality(n)
        h = n // 3
        assert len(C) == h * (n - h - 1) - h * (h + 1) // 2 == expected
        orbit_set = set()
        for u in C:
            assert u.count('1') == 3 and u[0] == '1' and u[-1] == '0'
            assert primitive(u)
            rot = canonical(u)
            assert rot not in orbit_set
            orbit_set.add(rot)
            for v in C:
                assert not overlaps(u, v)
                overlap_pairs += 1
        full_orbits = set()
        for positions in combinations(range(n), 3):
            w = ['0'] * n
            for pos in positions:
                w[pos] = '1'
            w = ''.join(w)
            if primitive(w):
                full_orbits.add(canonical(w))
            tested_words += 1
        assert full_orbits == orbit_set
        primitive_necklaces += len(orbit_set)
    for n in range(3, 1001):
        h = n // 3
        a = h * (n - h - 1) - h * (h + 1) // 2
        b = (comb(n, 3) - (n // 3 if n % 3 == 0 else 0)) // n
        assert a == b == cardinality(n)
    print('VERIFY_OK lengths=3..26 total_weight_three_words=%d primitive_necklaces=%d codeword_pair_tests=%d formula_lengths=3..1000' % (tested_words, primitive_necklaces, overlap_pairs))


if __name__ == '__main__':
    check()
