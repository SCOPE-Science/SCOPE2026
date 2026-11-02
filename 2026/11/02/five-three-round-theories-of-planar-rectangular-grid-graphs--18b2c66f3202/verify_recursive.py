#!/usr/bin/env python3
"""Unreduced first-order rank-three types by recursive atomic-diagram sets.
No grid geometry or preclassified extension categories are used.
"""
from functools import lru_cache


def graph(m, n):
    coords = [(r,c) for r in range(m) for c in range(n)]
    return [[abs(r-s)+abs(c-t)==1 for s,t in coords] for r,c in coords]


def theory(m, n):
    A = graph(m, n)
    N = len(A)
    @lru_cache(None)
    def atomic(seq):
        return tuple((int(seq[i] == seq[j]), int(A[seq[i]][seq[j]]))
                     for i in range(len(seq)) for j in range(i+1,len(seq)))
    @lru_cache(None)
    def subformula(rank, seq):
        if rank == 0:
            return atomic(seq)
        return frozenset(subformula(rank-1,seq+(v,)) for v in range(N))
    return subformula(3,tuple())


def main():
    reps=[(2,2),(2,3),(2,4),(3,3),(2,5)]
    signatures=[theory(*pair) for pair in reps]
    assert len(set(signatures))==5
    cls={t:k for k,t in enumerate(signatures)}
    checked=0
    for m in range(2,8):
        for n in range(m,8):
            predicted = ((2,2) if (m,n)==(2,2) else
                         (2,3) if (m,n)==(2,3) else
                         (2,4) if (m,n)==(2,4) else
                         (3,3) if (m,n)==(3,3) else (2,5))
            got=theory(m,n)
            assert cls[got] == reps.index(predicted), (m,n)
            checked+=1
    for m,n in [(2,8),(2,9),(3,8),(4,8),(6,8),(8,8)]:
        got=theory(m,n)
        assert got == signatures[4],(m,n)
        checked+=1
    print('RECURSIVE_LOGIC_CHECK_PASS')
    print('structures_checked=',checked)
    print('all_five_representative_theories_distinct=True')
    print('all_other_tested_rectangles_equivalent_to_2x5=True')
    print('last_check=',(8,8))

if __name__ == '__main__':
    main()
