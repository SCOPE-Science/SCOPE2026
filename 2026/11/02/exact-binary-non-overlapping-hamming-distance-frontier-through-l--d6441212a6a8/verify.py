#!/usr/bin/env python3
"""Recompute finite cross-bifix-free/Hamming optima, with exact clique bounds.

Usage: python3 verify.py
Requires only Python >=3.9 and certificates.json in the same directory.
"""
from pathlib import Path
from itertools import combinations
import json


def no_self_overlap(word):
    n = len(word)
    return all(word[:k] != word[n-k:] for k in range(1, n))


def compatible(a, b, d):
    n = len(a)
    if sum(x != y for x, y in zip(a, b)) < d:
        return False
    return all(a[:k] != b[-k:] and b[:k] != a[-k:] for k in range(1, n))


def vertices(n):
    return [format(x, '0%db' % n)
            for x in range(1 << n)
            if not (x & (1 << (n-1))) and (x & 1)
            and no_self_overlap(format(x, '0%db' % n))]


def clique_number(words, d):
    # The graph's vertex order is fixed, and all candidate words are enumerated.
    m = len(words)
    adj = [0] * m
    for i in range(m):
        for j in range(i + 1, m):
            if compatible(words[i], words[j], d):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    best = 0

    def ordered_greedy_colors(P):
        # Every color class is an independent set; colors are nondecreasing.
        order, bound = [], []
        color = 0
        remaining = P
        while remaining:
            color += 1
            Q = remaining
            while Q:
                t = Q & -Q
                v = t.bit_length() - 1
                Q ^= t
                remaining ^= t
                Q &= ~adj[v]
                order.append(v)
                bound.append(color)
        return order, bound

    def rec(P, depth):
        nonlocal best
        if not P:
            best = max(best, depth)
            return
        order, colors = ordered_greedy_colors(P)
        for index in range(len(order) - 1, -1, -1):
            if depth + colors[index] <= best:
                return
            v = order[index]
            rec(P & adj[v], depth + 1)
            P ^= 1 << v

    rec((1 << m) - 1, 0)
    return best


def main():
    path = Path(__file__).with_name('certificates.json')
    records = json.loads(path.read_text(encoding='utf-8'))['rows']
    expected = {(n, d) for n in range(2, 12) for d in range(2, n + 1)}
    assert {(e['n'], e['d']) for e in records} == expected
    assert len(records) == len(expected)
    all_words = {}
    for n, d in sorted(expected):
        e = next(e for e in records if e['n'] == n and e['d'] == d)
        if n not in all_words:
            all_words[n] = vertices(n)
        code = e['code']
        assert len(code) == e['size'] and len(set(code)) == len(code)
        assert all(w in all_words[n] for w in code)
        assert all(compatible(a, b, d) for a, b in combinations(code, 2))
        exact = clique_number(all_words[n], d)
        assert exact == e['size'], (n, d, exact, e['size'])
    # Compare the first Hamming-distance-two penalties with the published
    # unqualified cross-bifix-free maxima at these two lengths.
    assert next(x['size'] for x in records if (x['n'],x['d'])==(10,2)) == 23
    assert next(x['size'] for x in records if (x['n'],x['d'])==(11,2)) == 42
    print('VERIFY_OK', len(records), 'exact finite parameter pairs')


if __name__ == '__main__':
    main()
