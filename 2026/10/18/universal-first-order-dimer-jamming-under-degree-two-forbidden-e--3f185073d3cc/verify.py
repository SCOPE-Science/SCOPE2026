#!/usr/bin/env python3
"""Exact finite checks for sparse-forbidden-edge dimer jamming.

No finite check substitutes for the uniform asymptotic proof.
Run: python3 verify_universal_jamming.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations


def probability(N, missing):
    missing = {tuple(sorted(x)) for x in missing}
    assert N % 2 == 0 and N >= 4
    assert all(0 <= a < b < N for a, b in missing)
    assert all(sum(i in e for e in missing) <= 2 for i in range(N))
    @lru_cache(maxsize=None)
    def rec(mask):
        vertices = [i for i in range(N) if mask & (1 << i)]
        if not vertices:
            return Fraction(0)
        edges = [(i,j) for a,i in enumerate(vertices) for j in vertices[a+1:]
                 if (i,j) not in missing]
        if not edges:
            assert len(vertices) == 2 and tuple(vertices) in missing
            return Fraction(1)
        return sum((rec(mask ^ (1 << i) ^ (1 << j))
                   for i,j in edges), Fraction())/len(edges)
    return rec((1 << N)-1)


def examples():
    checked=0
    for N in (6,8,10,12):
        types={
           'matching': [(i,i+1) for i in range(0,N,2)],
           'cycle': [(i,(i+1)%N) for i in range(N)],
           'path': [(i,i+1) for i in range(N-1)],
        }
        for label, missing in types.items():
            m=len(missing)
            p=probability(N,missing)
            assert 0 <= p <= 1
            if label == 'matching' and N==6: assert p == Fraction(1,5)
            if label == 'matching' and N==8: assert p == Fraction(8,65)
            if label == 'cycle' and N==6: assert p == Fraction(1,3)
            if label == 'path' and N==6: assert p == Fraction(22,75)
            print(f'N={N:2d}, {label:9}, forbidden={m:2d}, exact_failure={p}, ratio_to_first_order={float(p*Fraction(N*N-1,3*m)):.9f}')
            checked+=1
    # Two disjoint triangles of forbidden edges on six vertices produce the complete bipartite K_{3,3},
    # whose greedy dimer adsorption *always* reaches perfect coverage.
    triangles=[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5)]
    assert probability(6,triangles) == 0
    checked+=1
    # An independent exhaustive edge-order calculation for N=6 with H=C_6.
    N=6
    forbidden={tuple(sorted((i,(i+1)%N))) for i in range(N)}
    edges=[(i,j) for i in range(N) for j in range(i+1,N) if (i,j) not in forbidden]
    assert len(edges)==9
    failures=0; total=0
    for order in permutations(range(len(edges))):
        matched=0
        for ei in order:
            i,j=edges[ei]
            if not ((matched>>i)&1 or (matched>>j)&1):
                matched |= (1<<i)|(1<<j)
        if matched != (1<<N)-1:
            failures+=1
        total+=1
    assert total == 362880 and Fraction(failures,total) == Fraction(1,3)
    assert probability(6,forbidden)==Fraction(failures,total)
    print(f'exact_DPs={checked}; independent_edge_orders={total}; failing_orders={failures}; all_passed')

if __name__ == '__main__': examples()
