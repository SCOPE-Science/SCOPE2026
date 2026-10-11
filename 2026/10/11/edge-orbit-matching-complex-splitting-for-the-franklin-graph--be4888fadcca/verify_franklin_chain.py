#!/usr/bin/env python3
"""Separately implemented simplicial-chain checks for Franklin edge-deletion/link profiles."""
from collections import defaultdict


def franklin_edges():
    jumps = [5 if j % 2 == 0 else -5 for j in range(12)]
    E = {tuple(sorted((i, (i + 1) % 12))) for i in range(12)}
    for i, j in enumerate(jumps):
        E.add(tuple(sorted((i, (i + j) % 12))))
    return tuple(sorted(E))


def matchings_by_size(edges):
    # An independent recursion over occupied graph-vertex sets.
    tiers = defaultdict(list)
    def recurse(start, used, face):
        tiers[len(face)].append(face)
        for j in range(start, len(edges)):
            x, y = edges[j]
            if ((used >> x) & 1) or ((used >> y) & 1):
                continue
            recurse(j + 1, used | (1 << x) | (1 << y), face + (j,))
    recurse(0, 0, ())
    return [tiers[k] for k in range(max(tiers) + 1)]


def rank2(tiers, k):
    index = {f: i for i, f in enumerate(tiers[k - 1])}
    pivots = {}
    rank = 0
    for f in tiers[k]:
        x = 0
        for pos in range(k):
            x ^= 1 << index[f[:pos] + f[pos + 1:]]
        while x:
            pivot = x.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = x
                rank += 1
                break
            x ^= pivots[pivot]
    return rank


def rank3(tiers, k):
    index = {f: i for i, f in enumerate(tiers[k - 1])}
    pivots = {}
    rank = 0
    for f in tiers[k]:
        vector = {}
        for pos in range(k):
            vector[index[f[:pos] + f[pos + 1:]]] = 1 if pos % 2 == 0 else 2
        while vector:
            row = max(vector)
            if row not in pivots:
                inv = 1 if vector[row] == 1 else 2
                pivots[row] = {u: (v * inv) % 3 for u, v in vector.items()}
                rank += 1
                break
            factor = vector[row]
            for u, v in pivots[row].items():
                b = (vector.get(u, 0) - factor * v) % 3
                if b:
                    vector[u] = b
                else:
                    vector.pop(u, None)
    return rank


def reduced_betti(edges, characteristic=2):
    tiers = matchings_by_size(edges)
    ranks = {k: (rank2(tiers,k) if characteristic == 2 else rank3(tiers,k))
             for k in range(1,len(tiers))}
    # Tier zero is the augmented empty face, whose boundary from vertices has rank one.
    betti = {}
    for k in range(1,len(tiers)):
        b = len(tiers[k])-ranks.get(k,0)-ranks.get(k+1,0)
        if b:
            betti[k-1]=b
    return betti, tuple(len(t) for t in tiers[1:])


def main():
    E=franklin_edges()
    assert len(E)==18
    target={(2*j,2*j+1) for j in range(6)}
    assert len(target)==6 and target.issubset(E)
    full, fv = reduced_betti(E)
    assert full == {3:12} and fv == (18,117,336,417,186,17)
    full3,_ = reduced_betti(E,3)
    assert full3 == full
    print('full_field2_and_field3=',full,'fvector=',fv)
    distribution={}
    for edge in E:
        deleted = tuple(x for x in E if x != edge)
        link = tuple(x for x in E if not set(x).intersection(edge))
        b1, f1 = reduced_betti(deleted,2)
        b2, f2 = reduced_betti(link,2)
        cls = 'A' if edge in target else 'B'
        if cls == 'A':
            assert b1 == {3:8} and b2 == {2:4}
            assert f1 == (17,104,280,325,137,12)
            assert f2 == (13,56,92,49,5)
        else:
            assert b1 == {3:10} and b2 == {2:2}
            assert f1 == (17,104,280,324,133,11)
            assert f2 == (13,56,93,53,6)
        distribution[cls] = distribution.get(cls,0)+1
    assert distribution == {'A':6, 'B':12}
    print('all_18_edges_characteristic2=',distribution,'A=(deletion8,link4)','B=(deletion10,link2)')
    for e in ((0,1),(0,5)):
        de = tuple(f for f in E if f != e)
        li = tuple(f for f in E if not set(f).intersection(e))
        assert reduced_betti(de,3)[0] == ({3:8} if e==(0,1) else {3:10})
        assert reduced_betti(li,3)[0] == ({2:4} if e==(0,1) else {2:2})
    print('representative_characteristic3_checks=passed')
    print('SECOND_CHAIN_VERIFIED')

if __name__=='__main__':
    main()
