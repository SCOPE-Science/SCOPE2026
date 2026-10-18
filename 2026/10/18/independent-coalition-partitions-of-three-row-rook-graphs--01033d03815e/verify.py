#!/usr/bin/env python3
"""Exhaustive independent-coalition checks on small labeled rook graphs.

Only uses the graph definition (row/column adjacency) and an explicit
set-partition enumerator; no optimization or theorem formula is assumed.
"""
from collections import Counter
from itertools import combinations


def independent(B):
    return len({r for r,c in B}) == len(B) == len({c for r,c in B})


def dominates(n,B):
    return all(any((r==a or c==b) for a,b in B)
               for r in range(3) for c in range(n))


def valid(n,blocks):
    universe={(r,c) for r in range(3) for c in range(n)}
    if sum(map(len,blocks))!=3*n or set().union(*blocks)!=universe or any(not B or not independent(B) for B in blocks):
        return False
    for i,B in enumerate(blocks):
        if dominates(n,B):
            if len(B)!=1:return False
            continue
        if not any(i!=j and independent(B|C) and dominates(n,B|C)
                   and not dominates(n,C) for j,C in enumerate(blocks)):
            return False
    return True


def partitions(items):
    if not items:
        yield []
        return
    x,*rest=items
    for P in partitions(rest):
        yield [frozenset((x,))]+P
        for j in range(len(P)):
            yield P[:j]+[P[j]|frozenset((x,))]+P[j+1:]


def triple_is_valid_fast(n,pairs):
    # Directly test every block's existence of a suitable partner using
    # pairwise row and column comparisons (independent dominating triples).
    chosen=set().union(*pairs)
    if len(chosen)!=6:return False
    singles={(r,c) for r in range(3) for c in range(n)}-chosen
    def good(p,c):
        T=tuple(p)+(c,)
        return independent(T) and dominates(n,T)
    for c in singles:
        if not any(good(p,c) for p in pairs):return False
    for p in pairs:
        if not any(good(p,c) for c in singles):return False
    return True


def predicted(n):
    out=set()
    for a in range(n):
        for b in range(n):
            if a==b:continue
            out.add(frozenset((frozenset(((1,a),(2,b))),
                               frozenset(((0,b),(2,a))),
                               frozenset(((0,a),(1,b))))))
            for d in range(n):
                if d in (a,b):continue
                out.add(frozenset((frozenset(((1,a),(2,b))),
                                   frozenset(((0,a),(2,d))),
                                   frozenset(((0,b),(1,d))))))
    return out


def main():
    P=Counter()
    profiles=Counter()
    scanned=0
    for pi in partitions([(r,c) for r in range(3) for c in range(3)]):
        scanned+=1
        if valid(3,pi):
            P[len(pi)]+=1
            if len(pi)==6:
                pairs=[B for B in pi if len(B)==2]
                profile=tuple(sorted(sum(1 for B in pairs if all(r!=q for r,c in B)) for q in range(3)))
                profiles[profile]+=1
    assert scanned==21147 and max(P)==6 and P[6]==54,P
    assert profiles=={(1,1,1):12,(0,1,2):36,(0,0,3):6},profiles
    print('FULL_3x3 partitions',scanned,'valid_by_size',dict(sorted(P.items())),'max',max(P),'maximizers',P[6],'missing_row_profiles',dict(sorted(profiles.items())))

    for n in range(4,9):
        cells=[(r,c) for r in range(3) for c in range(n)]
        blocks=[frozenset(x) for x in combinations(cells,2) if independent(x)]
        # Every partition with 3n, 3n-1 or 3n-2 parts has at most two pairs.
        for t in (0,1,2):
            for ps in combinations(blocks,t):
                if len(set().union(*ps))!=2*t:continue
                singles=[frozenset((c,)) for c in set(cells)-set().union(*ps)]
                assert not valid(n,list(ps)+singles)
        # Every partition with exactly 3n-3 parts must have three 2-blocks.
        found=set()
        for ps in combinations(blocks,3):
            if triple_is_valid_fast(n,ps):
                found.add(frozenset(ps))
        want=predicted(n)
        assert found==want,(n,len(found),len(want))
        assert len(found)==n*(n-1)**2
        print('EXHAUSTIVE_NEAR_MAX',n,'pair_types',len(blocks),'maximum',3*n-3,'maximizers',len(found))
    print('VERIFY_OK')

if __name__=='__main__':main()
