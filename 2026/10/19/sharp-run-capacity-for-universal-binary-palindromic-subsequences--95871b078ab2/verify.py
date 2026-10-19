#!/usr/bin/env python3
"""Finite independent tests for the sharp palindromic-subsequence run bound."""
from itertools import product


def palindromes(k):
    for half in product('01', repeat=(k + 1) // 2):
        p = ''.join(half)
        yield p + p[:k // 2][::-1]


def embeds(pattern, host):
    i = 0
    for character in host:
        if i < len(pattern) and pattern[i] == character:
            i += 1
    return i == len(pattern)


def universal_pal(host, k):
    return all(embeds(p, host) for p in palindromes(k))


def number_runs(host):
    return 0 if not host else 1 + sum(a != b for a, b in zip(host, host[1:]))


def witness(k):
    m = k // 2
    return '0011' * m + ('01' if k % 2 else '')


def arches(host):
    count, symbols = 0, set()
    for a in host:
        symbols.add(a)
        if len(symbols) == 2:
            count += 1
            symbols.clear()
    return count


def run_all_checks():
    for k in range(1, 29):
        w = witness(k)
        needed = 2 * ((k + 1) // 2)
        assert len(w) == 2 * k
        assert number_runs(w) == needed
        assert arches(w[1:]) >= k - 1
        assert arches(w[:-1]) >= k - 1
        assert universal_pal(w, k)
    print('WITNESS CHECKS PASSED for every k=1..28')

    for n in range(1, 13):
        for letters in product('01', repeat=n):
            w = ''.join(letters)
            r = number_runs(w)
            for k in range(1, n // 2 + 1):
                if universal_pal(w, k):
                    assert 2 * ((k + 1) // 2) <= r, (w, k, r)
                    assert w.count('0') >= k and w.count('1') >= k
    print('EXHAUSTIVE RUN AND LENGTH LOWER BOUNDS PASSED for all binary hosts n=1..12')

    for r in range(1, 37):
        w = witness(r) if r % 2 == 0 else (witness(r-1) + '0' if r > 1 else '0')
        k = 2 * (r // 2)
        assert number_runs(w) == r
        if k:
            assert universal_pal(w, k)
    print('EXACT RUN-CAPACITY CONSTRUCTIONS PASSED for r=1..36')
    print('ALL FINITE CHECKS PASSED; infinite statement follows from RESULT.md')


if __name__ == '__main__':
    run_all_checks()
