#!/usr/bin/env python3
"""Independent finite checks for antisquare-free Dyck-word rigidity.

Standard-library only. The infinite statement is proved in RESULT.md;
these exhaustive small cases do not substitute for that proof.
"""
from math import comb

def dyck(n):
    def rec(prefix, opened, closed):
        if closed == n:
            yield prefix
            return
        if opened < n:
            yield from rec(prefix + '0', opened + 1, closed)
        if closed < opened:
            yield from rec(prefix + '1', opened, closed + 1)
    yield from rec('', 0, 0)

def complement(word):
    return ''.join('1' if c == '0' else '0' for c in word)

def first_nontrivial_antisquare(word):
    for half in range(2, len(word)//2 + 1):
        for start in range(len(word)-2*half+1):
            left = word[start:start+half]
            if word[start+half:start+2*half] == complement(left):
                return (start, half, word[start:start+2*half])
    return None

def candidate(n):
    if n == 0:
        return ''
    if n == 1:
        return '01'
    return '0'*(n-1) + '10' + '1'*(n-1)

def check():
    totals = 0
    for n in range(1, 13):
        words = list(dyck(n))
        assert len(words) == comb(2*n,n)//(n+1), n
        survivors = [w for w in words if first_nontrivial_antisquare(w) is None]
        assert survivors == [candidate(n)], (n, survivors)
        totals += len(words)
    for n in range(1, 81):
        assert first_nontrivial_antisquare(candidate(n)) is None, n
    # Independently stress-test every excluded first-return case with a,b up to 18.
    for a in range(19):
        for b in range(19):
            word = '0' + candidate(a) + '1' + candidate(b)
            if b == 0 and a != 1:
                assert first_nontrivial_antisquare(word) is None, (a,b)
            elif (a,b) == (0,1):
                assert first_nontrivial_antisquare(word) is None
            else:
                assert first_nontrivial_antisquare(word) is not None, (a,b)
    print('ANTISQUARE_DYCK_RIGIDITY_PASS total_Dyck_tested=', totals,
          'survivors_one_each_n=1..12', 'explicit_candidates_checked_to_n=80',
          'branch_pairs_checked=',19*19)

if __name__ == '__main__':
    check()
