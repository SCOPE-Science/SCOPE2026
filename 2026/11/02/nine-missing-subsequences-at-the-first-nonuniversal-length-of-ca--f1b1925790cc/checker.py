#!/usr/bin/env python3
"""Standalone finite verification of the alternating-gap subsequence theorem.
The infinite statement is proved mathematically in RESULT.md; this code checks samples.
"""
from itertools import product

def canonical(M):
    assert M >= 4 and M % 2 == 0
    return '101000' * (M // 2 - 1) + '101'

def cantor(k):
    w = '1'
    for _ in range(k):
        w = ''.join('101' if x == '1' else '000' for x in w)
    return w

def positions(w, u):
    i, out = 0, []
    for letter in u:
        found = w.find(letter, i)
        if found == -1:
            return None
        out.append(found + 1)
        i = found + 1
    return out

def expected(M):
    return {a + '1' * (M - 3) + b
            for a in ('00', '01', '11')
            for b in ('00', '10', '11')}

def verify(w, M):
    assert all(positions(w, ''.join(t)) is not None
               for t in product('01', repeat=M))
    missing = {''.join(t) for t in product('01', repeat=M+1)
               if positions(w, ''.join(t)) is None}
    assert missing == expected(M), (M, sorted(missing))
    return (M, len(w), len(missing))

def main():
    for M in (4, 6, 8, 10, 12, 14):
        print('canonical', *verify(canonical(M), M))
    for k in (2, 3, 4):
        print('Cantor', k, *verify(cantor(k), 2**k))
    M = 6
    for heavy in product((3, 4, 6), repeat=M//2-1):
        gaps = [1 if j%2 == 1 else heavy[j//2-1] for j in range(1,M)]
        w = '1' + ''.join('0'*g + '1' for g in gaps)
        verify(w, M)
    print('PASS')

if __name__ == '__main__':
    main()
