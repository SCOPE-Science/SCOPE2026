#!/usr/bin/env python3
"""Exact independent small-parameter check of alternating complement formulas.

This public checker contains no external dependencies.
"""
from functools import lru_cache
from math import comb

@lru_cache(maxsize=None)
def complements(w, u):
    if not u:
        return frozenset((w,))
    if not w:
        return frozenset()
    results = {w[0] + v for v in complements(w[1:], u)}
    if w[0] == u[0]:
        results.update(complements(w[1:], u[1:]))
    return frozenset(results)

def prescribed(m, k):
    result = set()
    for bits in range(1 << m):
        run_count = sum((bits >> i) & 1 and (i == 0 or not ((bits >> (i-1)) & 1))
                        for i in range(m))
        if run_count <= k:
            result.add(''.join('ba' if (bits >> i) & 1 else 'ab' for i in range(m)))
    return result

def verify():
    tests = 0
    for n in range(0, 12):
        for k in range(n+1):
            m = n-k
            actual = set(complements('ab'*n, 'ab'*k))
            target = prescribed(m, k)
            assert actual == target, (n, k, actual ^ target)
            count = sum(comb(m+1, 2*j) for j in range(min(k, (m+1)//2)+1))
            count_alt = sum(comb(m, j) for j in range(min(2*k, m)+1))
            assert len(actual) == count == count_alt, (n,k,len(actual),count,count_alt)
            tests += 1
    print(f'ALTERNATING_COMPLEMENTS_VERIFY_OK {tests} parameter pairs, n<=11')
if __name__ == '__main__':
    verify()
