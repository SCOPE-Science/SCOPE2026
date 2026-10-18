#!/usr/bin/env python3
"""Finite checks for near-perfect subsequence universality in Dyck words.
Uses an independent next-occurrence automaton and exhaustive balanced generation.
"""
from collections import defaultdict
from itertools import product


def dyck_words(n):
    def build(prefix, ups, downs):
        if downs == n:
            yield prefix
            return
        if ups < n:
            yield from build(prefix + '0', ups + 1, downs)
        if downs < ups:
            yield from build(prefix + '1', ups, downs + 1)
    yield from build('', 0, 0)


def universality_sas(w):
    # The shortest-absent word length and its count are computed by a
    # next-occurrence automaton, without using the arch or transfer theorem.
    N = len(w)
    next_pos = [-1, -1]
    length = [0] * (N + 1)
    count = [0] * (N + 1)
    for i in range(N, -1, -1):
        candidates = [(1, 1) if x < 0 else (1 + length[x + 1], count[x + 1])
                      for x in next_pos]
        smallest = min(x for x, _ in candidates)
        length[i] = smallest
        count[i] = sum(c for x, c in candidates if x == smallest)
        if i:
            next_pos[int(w[i - 1])] = i - 1
    return length[0] - 1, count[0]


def arch_count(w):
    seen = set()
    count = 0
    for c in w:
        seen.add(c)
        if len(seen) == 2:
            seen.clear()
            count += 1
    return count


def family(n):
    for j in range(1, n):
        for bits in product(('01', '10'), repeat=n - 1 - j):
            yield '01' * (j - 1) + '001' + ''.join(bits) + '1'


def matrix_sas_family(w):
    # Two-letter forbidden-pair transfer, calculated independently from all
    # pair-subsequence relations of the factor, not hard-coded matrices.
    blocks = []
    pending = ''
    seen = set()
    for ch in w:
        pending += ch
        seen.add(ch)
        if len(seen) == 2:
            blocks.append(pending)
            pending = ''
            seen.clear()
    assert blocks
    blocks[-1] += pending
    row = [1, 1]
    for block in blocks:
        h = [[int(not any(block[i] == str(a) and block[t] == str(b)
                          for i in range(len(block)) for t in range(i + 1, len(block))))
              for b in range(2)] for a in range(2)]
        row = [sum(row[a] * h[a][b] for a in range(2)) for b in range(2)]
    return sum(row)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def brute_sas(w, k):
    missing = 0
    for candidate in product('01', repeat=k + 1):
        it = iter(w)
        if not all(any(x == c for x in it) for c in candidate):
            missing += 1
    return missing


if __name__ == '__main__':
    all_class = 0
    all_dyck = 0
    for n in range(2, 13):
        wanted = set(family(n))
        assert len(wanted) == 2 ** (n - 1) - 1
        actual = set()
        maxima = (0, 0)
        for w in dyck_words(n):
            all_dyck += 1
            k, s = universality_sas(w)
            assert k == arch_count(w)
            if k == n - 1:
                actual.add(w)
                assert matrix_sas_family(w) == s
                if n <= 8:
                    assert brute_sas(w, k) == s
                if s > maxima[0]:
                    maxima = (s, 1)
                elif s == maxima[0]:
                    maxima = (s, maxima[1] + 1)
        assert actual == wanted, (n, len(actual), len(wanted))
        assert maxima[0] == fib(n), (n, maxima)
        assert maxima[1] == (1 if n <= 3 else 2), (n, maxima)
        all_class += len(actual)
    # Separate direct checks of the proposed two extremizer constructions.
    for n in range(4, 80):
        for first in ('01', '10'):
            mids = [first if t % 2 == 0 else ('10' if first == '01' else '01')
                    for t in range(n - 3)]
            w = '001' + ''.join(mids) + '011'
            assert universality_sas(w) == (n - 1, fib(n)), n
    print(f'VERIFY_OK dyck_semilength_2_to_12={all_dyck} near_perfect={all_class} '
          f'exact_family_and_extremizers=11 direct_SAS_levels_2_to_8=7 '
          f'symbolic_witness_levels_4_to_79=76')
