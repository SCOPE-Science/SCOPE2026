#!/usr/bin/env python3
"""Finite independent checks for local binary cubic representation counts.
Run: python3 verify.py. No outside libraries required.
"""
from collections import Counter
from functools import lru_cache

@lru_cache(None)
def predicted(n, r):
    q = 3 ** n
    r %= q
    if n == 0:
        return 1
    if n == 1:
        return 3
    s = r % 9
    if s in (1, 8):
        return 2 * q
    if s in (2, 7):
        return q
    if s:
        return 0
    if n == 2:
        return 27
    return 2 * q + (81 * predicted(n - 3, r // 27) if r % 27 == 0 else 0)

def independently_count(n):
    q=3**n
    residues=Counter(pow(x,3,q) for x in range(q))
    # A different route: exact integral cyclic convolution of the cube frequency table.
    actual=[0]*q
    for a,ca in residues.items():
        for b,cb in residues.items():
            actual[(a+b)%q]+=ca*cb
    return actual

if __name__=='__main__':
    total=0
    for n in range(1,9):
        q=3**n
        actual=independently_count(n)
        for r,obs in enumerate(actual):
            expected=predicted(n,r)
            assert obs==expected,(n,r,obs,expected)
            total+=1
        assert sum(actual)==q*q
        if n>=2: assert actual[1]==2*q
        print(f'n={n}; modulus={q}; targets_checked={q}; r0={actual[0]}; r1={actual[1]}; all_equal=YES')
    print(f'PASS total_target_checks={total}')
