#!/usr/bin/env python3
"""Exhaustive finite checks of circular palindromic languages."""
from itertools import product

def cantor(k):
    w = '1'
    for j in range(k):
        w = w + '0' * (3 ** j) + w
    return w

def palindromes(w, circular=False):
    n = len(w)
    hay = w + w if circular else w
    out = set()
    for i in range(n):
        for length in range(1, n + 1):
            if not circular and i + length > n:
                break
            s = hay[i:i + length]
            if s == s[::-1]:
                out.add(s)
    return out

def transfer(w):
    n = len(w)
    return palindromes(w) | {
        w[-d:] + w[:d] for d in range(1, n // 2 + 1)
    }

def verify():
    for n in range(3, 15):
        count = 0
        for tail in product('01', repeat=(n // 2) - 1):
            left = '1' + ''.join(tail)
            for middle in ('01' if n % 2 else ('',)):
                w = left + middle + left[::-1]
                if '11' in w:
                    continue
                assert len(w) == n
                assert palindromes(w, circular=True) == transfer(w)
                count += 1
        assert count > 0
        print('Boundary transfer PASS', n, count)
    for k in range(6):
        w = cantor(k)
        n = len(w)
        ordinary = palindromes(w)
        circular = palindromes(w, circular=True)
        assert circular == transfer(w)
        if k >= 1:
            assert len(ordinary) == n
            assert len(circular) == (3 * n - 1) // 2
            m = 3 ** (k - 1)
            for length in range(1, n + 1):
                expected = (2 if length == 1 else
                    3 if length % 2 == 1 and length <= m else
                    2 if length % 2 == 0 and length < m else 1)
                assert sum(len(s) == length for s in circular) == expected
        if k >= 2:
            a, b = cantor(k - 1), cantor(k - 2)
            r, m = len(b), len(a)
            predicted = (
                palindromes(a)
                | {'0' * t for t in range(r + 1, m + 1)}
                | {'0' * t + b + '0' * t for t in range(1, r + 1)}
                | {a[-t:] + '0' * m + a[:t] for t in range(1, m + 1)}
            )
            assert ordinary == predicted
        print('Cantor rank PASS', k, n, len(ordinary), len(circular))
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    verify()
