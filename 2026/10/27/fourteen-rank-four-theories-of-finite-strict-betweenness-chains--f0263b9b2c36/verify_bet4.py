#!/usr/bin/env python3
"""Exact finite EF-type enumerator for strict ternary betweenness chains.
Usage: python3 verify_bet4.py
No external dependencies; integer type IDs are only canonical internal names.
"""
from functools import lru_cache
from collections import defaultdict

_intern = {}

def encode(symbolic):
    if symbolic not in _intern:
        _intern[symbolic] = len(_intern) + 1
    return _intern[symbolic]

def between(a,b,c):
    return (a < b < c) or (c < b < a)

@lru_cache(maxsize=None)
def type_of(n, assignment, rank):
    k = len(assignment)
    equalities = tuple(assignment[i] == assignment[j]
                       for i in range(k) for j in range(i))
    triples = tuple(between(assignment[i],assignment[j],assignment[h])
                    for i in range(k) for j in range(k) for h in range(k)
                    if i != j and j != h and i != h)
    atomic = encode(('atomic', k, equalities, triples))
    if rank == 0:
        return atomic
    extensions = frozenset(type_of(n,assignment+(p,),rank-1) for p in range(n))
    return encode(('quantified', atomic, extensions))

def main():
    for rank, cutoff in ((1,1),(2,2),(3,6),(4,14)):
        signatures = [type_of(n, (), rank) for n in range(1,16)]
        assert len(set(signatures)) == cutoff, (rank,signatures)
        assert len(set(signatures[:cutoff])) == cutoff
        assert len(set(signatures[cutoff-1:])) == 1
        groups = defaultdict(list)
        for n, sig in enumerate(signatures,1):
            groups[sig].append(n)
        classes = sorted(groups.values(),key=lambda block:block[0])
        print(f'RANK={rank} CLASSES={classes}')
    # The two-level character sets after Spoiler's first move must coincide.
    root14 = {type_of(14,(a,),3) for a in range(14)}
    root15 = {type_of(15,(a,),3) for a in range(15)}
    assert root14 == root15
    root13 = {type_of(13,(a,),3) for a in range(13)}
    assert root13 != root14
    print('POINTED_RANK3_14_15_EQUAL=YES; 13_14_EQUAL=NO')
    print(f'STATES={type_of.cache_info().currsize}; CANONICAL_TYPES={len(_intern)}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
