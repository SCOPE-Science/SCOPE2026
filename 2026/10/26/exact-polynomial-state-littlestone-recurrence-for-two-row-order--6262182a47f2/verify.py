#!/usr/bin/env python3
"""Exact Littlestone ranks for ideals in a two-row finite grid.

All arithmetic is integer/exact. No external dependencies.
Usage: python3 verify.py
"""
from functools import lru_cache
from math import log2
import json
from pathlib import Path

THRESHOLDS = (1, 2, 3, 5, 8, 12, 17, 25, 36, 52)

@lru_cache(None)
def core(A, B, C, D):
    """Rank on {(a,b): A<=a<=B, C<=b<=D, b<=a}, normalized."""
    assert A <= B and C <= D and A >= C and D <= B
    if A == B and C == D:
        return 0
    v = 0
    for t in range(A + 1, B + 1):
        v = max(v, 1 + min(rank(A, t - 1, C, D), rank(t, B, C, D)))
    for t in range(C + 1, D + 1):
        v = max(v, 1 + min(rank(A, B, C, t - 1), rank(A, B, t, D)))
    return v

def rank(A, B, C, D):
    A = max(A, C)
    D = min(D, B)
    assert A <= B and C <= D, (A, B, C, D)
    return core(A, B, C, D)

# Independently enumerate the actual hypothesis vectors, not rectangular states.
def brute(n):
    H = [(a, b) for a in range(n + 1) for b in range(a + 1)]
    masks = []
    for row in (0, 1):
        for t in range(1, n + 1):
            masks.append(sum((1 << j) for j, p in enumerate(H) if p[row] >= t))

    @lru_cache(None)
    def ld(S):
        best = 0
        for mask in masks:
            yes = S & mask
            no = S ^ yes
            if yes and no:
                best = max(best, 1 + min(ld(yes), ld(no)))
        return best
    return ld((1 << len(H)) - 1)

def make_tree(A, B, C, D, depth):
    # Emit a genuinely complete mistake-tree witness using exact choices.
    assert rank(A, B, C, D) >= depth
    if depth == 0:
        return None
    A = max(A, C)
    D = min(D, B)
    for row in (0, 1):
        lo, hi = (A, B) if row == 0 else (C, D)
        for t in range(lo + 1, hi + 1):
            left = (A, t - 1, C, D) if row == 0 else (A, B, C, t - 1)
            right = (t, B, C, D) if row == 0 else (A, B, t, D)
            if rank(*left) >= depth - 1 and rank(*right) >= depth - 1:
                return {'row': row + 1, 'column': t,
                        'zero': make_tree(*left, depth - 1),
                        'one': make_tree(*right, depth - 1)}
    raise AssertionError('no witness at requested depth')

def check_tree(tree, n, depth):
    H = [(a, b) for a in range(n + 1) for b in range(a + 1)]
    leaves = [0]
    def rec(node, possible, remaining):
        if remaining == 0:
            assert node is None and possible
            leaves[0] += 1
            return
        assert isinstance(node, dict) and set(node)== {'row','column','zero','one'}
        row, col = node['row'] - 1, node['column']
        assert row in (0, 1) and 1 <= col <= n
        no = [p for p in possible if p[row] < col]
        yes = [p for p in possible if p[row] >= col]
        assert no and yes, (row, col, remaining)
        rec(node['zero'], no, remaining - 1)
        rec(node['one'], yes, remaining - 1)
    rec(tree, H, depth)
    assert leaves[0] == (1 << depth)
    return leaves[0]

def main():
    assert rank(0, 0, 0, 0) == 0
    for n in range(17):
        a=rank(0,n,0,n); b=brute(n)
        assert a == b, (n,a,b)
    print('INDEPENDENT_HYPOTHESIS_ENUMERATION_OK n=0..16')
    checks=[]
    for depth, n in enumerate(THRESHOLDS, 1):
        prev=rank(0,n-1,0,n-1)
        got=rank(0,n,0,n)
        assert prev == depth-1 and got == depth, (depth,n,prev,got)
        checks.append([depth,n,prev,got])
    print('EXACT_THRESHOLD_BOUNDARIES_OK', json.dumps(checks, separators=(',',':')))
    print('POLYNOMIAL_STATE_RANK_RECURRENCE_OK cache_states', core.cache_info().currsize)
    witness=make_tree(0,52,0,52,10)
    leaves=check_tree(witness,52,10)
    witness_path=Path(__file__).with_name('depth10_n52_witness.json')
    witness_path.write_text(json.dumps(witness, separators=(',',':'))+'\n',encoding='utf-8')
    print('FULL_SHATTERED_TREE_OK n=52 depth=10 paths', leaves)
    print('WITNESS_FILE', witness_path.name, 'bytes',witness_path.stat().st_size)
    print('ALL_CHECKS_OK')

if __name__=='__main__':
    main()
