#!/usr/bin/env python3
"""Exact Hintikka-type calculation for carousel tournaments at depth four.

This finite algorithm is a self-contained proof of each finite comparison:
from any prefix p, a rank-r formula sees the atomic diagram at p and
exactly the set (not multiplicities) of rank-(r-1) types obtained by
appending one vertex. The recursion therefore enumerates all rank-r
first-order types, including quantifier alternations and negations.
"""
from functools import lru_cache
from collections import defaultdict

interned = {}
def intern(key):
    if key not in interned: interned[key] = len(interned) + 1
    return interned[key]

def atomic(n, p):
    h=(n-1)//2
    return tuple(0 if a==b else (1 if 0 < (b-a)%n <= h else 2)
                 for i,a in enumerate(p) for b in p[i+1:])

@lru_cache(None)
def hintikka(n, p, r):
    a=atomic(n, p)
    if r==0: return intern((r,len(p),a))
    children=tuple(sorted({hintikka(n,p+(v,),r-1) for v in range(n)}))
    return intern((r,len(p),a,children))

def classify(max_n=19):
    groups=defaultdict(list)
    for n in range(1,max_n+1,2):
        t=hintikka(n,tuple(),4)
        groups[t].append(n)
        print(f'n={n:2} rank4_id={t} distinct_atomic_type_keys={len(interned)}')
    assert all(len(v)==1 for v in groups.values() if v[0]<15)
    assert groups[hintikka(15,tuple(),4)] == [15,17,19]
    assert len(groups)==8
    print('EXACT_SMALL_CASE_CHECK_PASS: eight types through n=19; the first seven sizes are isolated.')
    print('Remaining n>=15 proved by the antipodally paired gap-game lemma in RESULT.md.')

if __name__ == '__main__': classify()
