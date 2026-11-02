"""Exhaustive checks for bounded-run binary-word exchange geometry.

Run: python verify_descent.py
"""
from itertools import combinations
from collections import defaultdict


def feasible(p, n, k, r, s):
    if len(p) != k or any(not (1 <= v <= n) for v in p):
        return False
    word = ['0'] * n
    if len(set(p)) != len(p):
        return False
    for v in p:
        word[v-1] = '1'
    w = ''.join(word)
    return '0'*r not in w and '1'*s not in w


def descend(p, z, n, r, s):
    k = len(p)
    original = sum(a-b for a,b in zip(p,z))
    steps = 0
    while p != z:
        for j in range(k):
            if p[j] > z[j]:
                t = list(p)
                t[j] -= 1
                t = tuple(t)
                if feasible(t,n,k,r,s):
                    p = t
                    steps += 1
                    break
        else:
            raise AssertionError(('blocked monotone descent',n,k,r,s,p,z))
    assert steps == original
    return steps


def run():
    counts = defaultdict(int)
    total_comparisons = 0
    for n in range(1,11):
        for r in range(2,6):
            for s in range(2,6):
                if r == s == 2: continue
                for k in range(n+1):
                    arr = [p for p in combinations(range(1,n+1),k) if feasible(p,n,k,r,s)]
                    if not arr: continue
                    aset = set(arr)
                    # Lattice meet/join, and all-pairs constructive paths via meet.
                    for i,p in enumerate(arr):
                        for q in arr[i:]:
                            z = tuple(min(x,y) for x,y in zip(p,q))
                            w = tuple(max(x,y) for x,y in zip(p,q))
                            assert z in aset and w in aset,(n,k,r,s,p,q,z,w)
                            d = descend(p,z,n,r,s)+descend(q,z,n,r,s)
                            assert d == sum(abs(x-y) for x,y in zip(p,q))
                            total_comparisons += 1
                    counts[(r,s)] += len(arr)
    # Boundary counterexample: forbidden 00 and 11.
    assert feasible((1,3),4,2,2,2)
    assert feasible((2,4),4,2,2,2)
    assert all(not feasible((1,2),4,2,2,2) for _ in range(1))
    print('DESCENT_ALL_PASS',len(counts),'run-bound pairs;',total_comparisons,'state-pair comparisons')

if __name__ == '__main__': run()
