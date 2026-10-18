#!/usr/bin/env python3
"""Exhaustive check: finite width-at-most-two strict posets through six points.
Uses all upper-triangular binary relations, independent of permutation encoding.
"""
from collections import defaultdict
from itertools import permutations, product


def edges(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return frozenset(pairs[k] for k in range(len(pairs)) if mask & (1 << k))


def admissible(n, E):
    # A naturally labelled transitive irreflexive relation is exactly a poset.
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in E:
                continue
            for k in range(j + 1, n):
                if (j, k) in E and (i, k) not in E:
                    return False
    # No three-element antichain (width at most two).
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (i, j) not in E and (i, k) not in E and (j, k) not in E:
                    return False
    return True


def signature(n, E):
    return tuple(sorted((sum((j, i) in E for j in range(n)),
                         sum((i, j) in E for j in range(n))) for i in range(n)))


def isomorphic(n, E, F):
    da = [(sum((j, i) in E for j in range(n)),sum((i, j) in E for j in range(n))) for i in range(n)]
    db = [(sum((j, i) in F for j in range(n)),sum((i, j) in F for j in range(n))) for i in range(n)]
    s = sorted(set(da))
    cls_a = [[i for i in range(n) if da[i] == d] for d in s]
    cls_b = [[i for i in range(n) if db[i] == d] for d in s]
    if any(len(a) != len(b) for a, b in zip(cls_a, cls_b)):
        return False
    for parts in product(*(permutations(b) for b in cls_b)):
        f = [None] * n
        for a, b in zip(cls_a, parts):
            for x, y in zip(a, b): f[x] = y
        if all(((i,j) in E)==((f[i],f[j]) in F) for i in range(n) for j in range(n)):
            return True
    return False


def run():
    target_classes=[1,2,4,10,26,75]
    for n in range(1,7):
        bins=defaultdict(list)
        considered=0
        for mask in range(1<<(n*(n-1)//2)):
            E=edges(n,mask)
            if not admissible(n,E):continue
            considered+=1
            sig=signature(n,E)
            if not any(isomorphic(n,E,F) for F in bins[sig]):
                bins[sig].append(E)
        types=sum(map(len,bins.values()))
        collision=[(sig,vs) for sig,vs in bins.items() if len(vs)>1]
        print(f'n={n} naturally_labelled_posets={considered} types={types} signatures={len(bins)} collision_groups={len(collision)}')
        assert types == target_classes[n-1]
        assert len(collision)==(1 if n==6 else 0)
        if n==6:
            assert len(collision[0][1])==2
            sig,reps=collision[0]
            print('unique_collision_signature=',sig)
            for ind,E in enumerate(reps):
                print('  P'+str(ind+1)+'_relations=', sorted((i+1,j+1) for i,j in E))
                assert admissible(n,E)
                assert signature(n,E)==sig
            assert not isomorphic(n,*reps)
    print('PASS: complete finite classification, unique six-point collision')

if __name__=='__main__':run()
