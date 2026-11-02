#!/usr/bin/env python3
"""Self-contained exact checks for membership queries to two-row grid ideals.

Usage: python3 verify_grid_ideal_learning.py
Only Python standard library is required. This program checks finite instances;
proofs of all-size statements are supplied separately.
"""
from functools import lru_cache
from math import comb

THRESHOLDS = {1:1,2:2,3:3,4:5,5:8,6:12,7:17,8:25,9:36,10:52}


def ldim_by_vectors(n):
    """Independent hypothesis-bitset recurrence, for the full grid."""
    H = [(a,b) for b in range(n+1) for a in range(b+1)]
    M = [(sum(1 << i for i, p in enumerate(H) if p[row] >= j))
         for row in range(2) for j in range(1,n+1)]
    @lru_cache(None)
    def go(S):
        if S.bit_count() <= 1:
            return 0
        best = 0
        upper = S.bit_count().bit_length()-1
        for Q in M:
            p = S & Q
            z = S ^ p
            if not p or not z:
                continue
            if min(p.bit_count(),z.bit_count()) < (1 << best):
                continue
            d = 1+min(go(p),go(z))
            if d > best:
                best = d
            if best == upper:
                return best
        return best
    ans = go((1 << len(H))-1)
    return ans, len(H)


def ldim_by_bounds(A,B,C,D):
    """Normalize interval state before the geometric-state cache lookup."""
    return _bound_core(A,min(B,D),max(C,A),D)

@lru_cache(None)
def _bound_core(A,B,C,D):
    if A > B or C > D:
        return -1   # empty family, never accepted as a decision-tree child
    if A == B and C == D:
        return 0
    ans = 0
    for j in range(A+1, B+1):
        left = ldim_by_bounds(A,j-1,C,D)
        right = ldim_by_bounds(j,B,C,D)
        if left >= 0 and right >= 0:
            ans = max(ans,1 + min(left,right))
    for j in range(C+1,D+1):
        left = ldim_by_bounds(A,B,C,j-1)
        right = ldim_by_bounds(A,B,j,D)
        if left >= 0 and right >= 0:
            ans = max(ans,1 + min(left,right))
    return ans


def main():
    # O(n^5)-time interval-state recurrence, evaluated through the last jump.
    dims = {n: ldim_by_bounds(0,n,0,n) for n in range(1,53)}
    assert dims[52] == 10
    # For 53..60 the old class embeds and the class count is below 2048.
    for n in range(53,61):
        assert comb(n+2,2) < 2048
        dims[n] = 10
    # Independent bit-vector recurrence checks representative exact values,
    # including both sides of the nontrivial jump thresholds.
    sampled = set(range(1,16)) | {16,17,24,25,35,36,51,52,60}
    for n in sorted(sampled):
        dim,N = ldim_by_vectors(n)
        assert N == comb(n+2,2)
        assert dim == dims[n], (n,dim,dims[n])
    print('TWO_INDEPENDENT_RECURSIONS_AGREE_PASS',len(sampled),flush=True)
    changed = {}
    before = 0
    for n,d in dims.items():
        if d > before:
            assert d == before+1
            changed[d] = n
            before=d
    assert changed == THRESHOLDS, (changed,THRESHOLDS)
    print('EXACT_THRESHOLDS_1_TO_60_PASS',sorted(changed.items()),flush=True)
    print('BOUND_STATE_RECURRENCE_PASS n=1..52; monotonicity-and-count n=53..60',flush=True)
    n=7
    all_h=[(a,b) for b in range(n+1) for a in range(b+1)]
    counts=sorted({sum(p[row]>=j for p in all_h) for row in range(2) for j in range(1,n+1)})
    assert counts == [1,3,6,8,10,15,21,26,28,30,33,35]
    assert all(min(c,36-c)<16 for c in counts)
    assert dims[7] == 4 and dims[6] == 4
    print('FIRST_ENTROPY_OBSTRUCTION_PASS n=7 count=36 Ldim=4 info_bound=5',flush=True)
    for n in range(1,10001):
        k=n//2
        product=(k+1)*(n-k+1)
        lower=(k+1).bit_length()-1 + (n-k+1).bit_length()-1
        cap=comb(n+2,2).bit_length()-1
        assert cap-lower<=2
        assert product <= comb(n+2,2)
    print('ASYMPTOTIC_BOUND_ARITHMETIC_SAMPLE_PASS n=1..10000',flush=True)
    print('TWO_ROW_GRID_IDEALS_ALL_NEW_CHECKS_PASS')

if __name__ == '__main__':
    main()
