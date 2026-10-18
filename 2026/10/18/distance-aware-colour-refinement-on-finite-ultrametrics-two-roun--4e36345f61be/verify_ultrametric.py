#!/usr/bin/env python3
"""Exhaustive small ultrametric isometry-census and synchronous distance-aware 1-WL."""
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import combinations

@lru_cache(None)
def integer_partitions(n,minimum=1):
    if n==0: return ((),)
    return tuple((k,)+rest for k in range(minimum,n+1) for rest in integer_partitions(n-k,k))

@lru_cache(None)
def macro_types(n):
    # One distance-2 ball has subballs at distance 1 of these sizes.
    return integer_partitions(n)

def structures(n):
    atoms=tuple(sorted((p,) for j in range(1,n+1) for p in macro_types(j)))
    sizes=[sum(x[0]) for x in atoms]
    def rec(start,left, acc):
        if left==0:
            yield tuple(acc)
            return
        for i in range(start,len(atoms)):
            if sizes[i]>left: continue
            acc.append(atoms[i][0])
            yield from rec(i,left-sizes[i],acc)
            acc.pop()
    return list(rec(0,n,[]))

def dist_matrix(obj):
    clusters=[]
    for m,blocks in enumerate(obj):
        for b,s in enumerate(blocks):
            clusters.extend([(m,b)]*s)
    n=len(clusters)
    return tuple(tuple(0 if i==j else (1 if clusters[i]==clusters[j] else (2 if clusters[i][0]==clusters[j][0] else 3)) for j in range(n)) for i in range(n))

def colors(dist, rounds=2):
    n=len(dist)
    col=[0]*n
    output=[tuple(sorted(Counter(col).items()))]
    for k in range(rounds):
        raw=[]
        for i in range(n):
            neighbor_by_distance=tuple(tuple(sorted(Counter(col[j] for j in range(n) if dist[i][j]==d).items())) for d in range(4))
            raw.append((col[i], neighbor_by_distance))
        # Canonical raw-tuples, synchronized between independently run structures.
        uniq=sorted(set(raw))
        idx={x:i for i,x in enumerate(uniq)}
        col=[idx[x] for x in raw]
        output.append(tuple(sorted(Counter(col).items())))
    return output

def invariant(dist,rounds):
    # Raw recursively nested colors rather than a per-structure integer ID, to ensure cross-structure comparison.
    n=len(dist)
    c=[0]*n
    for k in range(rounds):
        c=[(c[i],tuple(tuple(sorted(Counter(c[j] for j in range(n) if dist[i][j]==d).items(),key=repr)) for d in range(4))) for i in range(n)]
    return tuple(sorted(Counter(c).items(),key=repr))

def main():
    for n in range(1,9):
        objects=structures(n)
        group1=defaultdict(list); group2=defaultdict(list)
        for obj in objects:
            d=dist_matrix(obj)
            group1[repr(invariant(d,1))].append(obj)
            group2[repr(invariant(d,2))].append(obj)
        amb1=[x for x in group1.values() if len(x)>1]
        amb2=[x for x in group2.values() if len(x)>1]
        print(f'n={n} isometry_types={len(objects)} one_round_ambiguous_classes={len(amb1)} pair_sizes={[len(x) for x in amb1]} two_round_ambiguous_classes={len(amb2)}')
        if n<8: assert not amb1
        if n==8:
            assert len(amb1)==1 and len(amb1[0])==2
            for g in amb1:
                print('  first ambiguity',g)
                assert set(g)=={((1,1,2),(1,1,2)),((1,1,1,1),(2,2))}
        assert not amb2
    print('ALL TESTS PASSED')

if __name__=='__main__': main()
