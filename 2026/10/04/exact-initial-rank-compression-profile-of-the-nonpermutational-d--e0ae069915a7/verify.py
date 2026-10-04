#!/usr/bin/env python3
from collections import deque, defaultdict
from math import ceil


def transitions(n):
    a = {}
    b = {}
    for q in range(1, n + 1):
        if q <= n - 2:
            a[q] = q + 1
            b[q] = q + 1
        elif q == n - 1:
            a[q] = 1
            b[q] = n
        else:
            a[q] = 1
            b[q] = 2
    return a, b


def image(S, t):
    return frozenset(t[q] for q in S)


def apply_word(n, word):
    a, b = transitions(n)
    ts = {'a': a, 'b': b}
    S = frozenset(range(1, n + 1))
    for ch in word:
        S = image(S, ts[ch])
    return S


def bfs_profile(n):
    a, b = transitions(n)
    ts = [('a', a), ('b', b)]
    Q = frozenset(range(1, n + 1))
    dist = {Q: 0}
    ways = {Q: 1}
    rep = {Q: ''}
    dq = deque([Q])
    while dq:
        S = dq.popleft()
        d = dist[S]
        for ch, t in ts:
            T = image(S, t)
            nd = d + 1
            if T not in dist:
                dist[T] = nd
                ways[T] = ways[S]
                rep[T] = rep[S] + ch
                dq.append(T)
            elif dist[T] == nd:
                ways[T] += ways[S]
    profile = {}
    for s in range(1, n):
        target = n - s
        dmin = min(d for S, d in dist.items() if len(S) <= target)
        count = sum(ways[S] for S, d in dist.items() if len(S) <= target and d == dmin)
        reps = sorted(rep[S] for S, d in dist.items() if len(S) <= target and d == dmin)
        profile[s] = (dmin, count, reps[0])
    return profile


def expected_holes(n, k):
    return set(range(2, 2 * k + 1, 2)) | {n}


def check_symbolic_samples():
    for n in range(4, 201):
        kmax = ceil(n / 2) - 1
        for k in range(1, kmax + 1):
            word = 'ba' * k
            S = apply_word(n, word)
            H = set(range(1, n + 1)) - set(S)
            assert H == expected_holes(n, k), (n, k, H, expected_holes(n, k))
        saturated = apply_word(n, 'ba' * kmax)
        after_one_more = apply_word(n, 'ba' * (kmax + 1))
        assert len(after_one_more) == len(saturated), (n, len(saturated), len(after_one_more))


def check_exhaustive():
    rows = []
    for n in range(4, 19):
        p = bfs_profile(n)
        m = ceil(n / 2)
        assert p[1][0] == 1
        for s in range(2, m + 1):
            d, count, word = p[s]
            expected = 'ba' * (s - 1)
            assert d == 2 * s - 2, (n, s, d)
            assert count == 1, (n, s, count)
            assert word == expected, (n, s, word, expected)
        s0 = m + 1
        if s0 <= n - 1:
            assert p[s0][0] > 2 * s0 - 2, (n, s0, p[s0][0])
        rows.append((n, [p[s][0] for s in range(1, min(n - 1, m + 1) + 1)]))
    return rows


def main():
    check_symbolic_samples()
    rows = check_exhaustive()
    print('symbolic_witness_check n=4..200: PASS')
    print('power_automaton_bfs n=4..18: PASS')
    print('shortest_word_uniqueness through ceil(n/2): PASS')
    print('strict_next_deficiency_boundary n=4..18: PASS')
    for n, vals in rows:
        print(f'n={n} threshold_prefix={vals}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
