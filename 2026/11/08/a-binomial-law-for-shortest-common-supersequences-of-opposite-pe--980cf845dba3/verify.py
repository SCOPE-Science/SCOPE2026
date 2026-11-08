#!/usr/bin/env python3
"""Independent exact checks for reverse-permutation-power SCS theorem.

Run: python3 verify.py
Requires Python standard library only. These finite checks corroborate a written
proof and do not prove the infinite-parameter theorem by exhaustion.
"""
from functools import lru_cache
from itertools import combinations, permutations
from math import comb


def claimed(q, k, ell):
    A = (q - 1) * k - ell + 1
    B = (q - 1) * ell - k + 1
    minimum = max(q * k, q * ell, (q - 1) * (k + ell) + 1)
    return minimum, (comb(A + B, A) if A >= 0 and B >= 0 else 1)


def direct_dynamic(x, y):
    @lru_cache(None)
    def solve(i, j):
        if i == len(x):
            return len(y) - j, 1
        if j == len(y):
            return len(x) - i, 1
        if x[i] == y[j]:
            n, count = solve(i + 1, j + 1)
            return n + 1, count
        p, u = solve(i + 1, j)
        t, v = solve(i, j + 1)
        d = min(p, t)
        return d + 1, (u if p == d else 0) + (v if t == d else 0)
    return solve(0, 0)


def embeds(sub, word):
    at = 0
    for c in word:
        if at < len(sub) and c == sub[at]:
            at += 1
    return at == len(sub)


def greedy_merge(q, k, ell, solo):
    """Build a word from the independent X/Y solo decisions and forced matches."""
    x = tuple(range(q)) * k
    y = tuple(range(q - 1, -1, -1)) * ell
    a = (q - 1) * k - ell + 1
    b = (q - 1) * ell - k + 1
    assert a >= 0 and b >= 0 and len(solo) == a + b
    assert solo.count(0) == a and solo.count(1) == b
    i = j = p = 0
    out = []

    def single():
        nonlocal i, j, p
        choice = solo[p]
        p += 1
        if choice == 0:
            assert i < len(x)
            if j < len(y):
                assert x[i] != y[j]
            out.append(x[i]); i += 1
        else:
            assert j < len(y)
            if i < len(x):
                assert x[i] != y[j]
            out.append(y[j]); j += 1

    def common():
        nonlocal i, j
        assert i < len(x) and j < len(y) and x[i] == y[j]
        out.append(x[i]); i += 1; j += 1

    for _ in range(q - 1):
        single()
    for h in range(k + ell - 1):
        common()
        if h < k + ell - 2:
            for _ in range(q - 2):
                single()
    for _ in range(q - 1):
        single()
    assert p == len(solo) and i == len(x) and j == len(y)
    return tuple(out)


def direct_language(x, y):
    @lru_cache(None)
    def solve(i, j):
        if i == len(x): return {y[j:]}
        if j == len(y): return {x[i:]}
        if x[i] == y[j]: return {(x[i],) + u for u in solve(i + 1, j + 1)}
        first = {(x[i],) + u for u in solve(i + 1, j)}
        second = {(y[j],) + u for u in solve(i, j + 1)}
        m = min(min(map(len, first)), min(map(len, second)))
        return {s for s in first | second if len(s) == m}
    return solve(0, 0)


def run():
    checked = 0
    for q in range(2, 9):
        for k in range(1, 9):
            for ell in range(1, 9):
                x = tuple(range(q)) * k
                y = tuple(range(q - 1, -1, -1)) * ell
                got = direct_dynamic(x, y)
                expected = claimed(q, k, ell)
                assert got == expected, (q, k, ell, got, expected)
                checked += 1
    language_configs = 0
    merge_cases = 0
    for q in range(2, 7):
        for k in range(1, 5):
            for ell in range(1, 5):
                x = tuple(range(q)) * k
                y = tuple(range(q - 1, -1, -1)) * ell
                A = (q - 1) * k - ell + 1
                B = (q - 1) * ell - k + 1
                if min(A, B) < 0 or A + B > 13:
                    continue
                distinct = set()
                for positions in combinations(range(A + B), A):
                    membership = set(positions)
                    solo = tuple(0 if j in membership else 1 for j in range(A + B))
                    word = greedy_merge(q, k, ell, solo)
                    assert embeds(x, word) and embeds(y, word)
                    distinct.add(word)
                    merge_cases += 1
                assert len(distinct) == comb(A + B, A), (q,k,ell)
                if len(distinct) <= 4000 and q * max(k, ell) <= 20:
                    direct = direct_language(x, y)
                    assert direct == distinct, (q,k,ell, len(direct),len(distinct))
                    language_configs += 1
    print(f'VERIFY_OK dynamic_configurations={checked} constructed_words={merge_cases} full_language_configurations={language_configs}')

if __name__ == '__main__':
    run()
