#!/usr/bin/env python3
"""Exhaustive first-order rank-three type census for finite disjoint chain posets.
All statements in this source concern mathematics and reproducibility only.
"""
from functools import lru_cache
from itertools import combinations_with_replacement
import hashlib, json


def poset(lengths):
    assert 1 <= len(lengths) <= 3 and all(n > 0 for n in lengths)
    points = [(i,j) for i,n in enumerate(lengths) for j in range(n)]
    # For an ordered pair, 0=equality, 1=less, 2=greater, 3=incomparable.
    rel = tuple(tuple(0 if a == b else
                      (1 if a[0] == b[0] and a[1] < b[1] else
                       2 if a[0] == b[0] else 3)
                      for b in points) for a in points)
    return rel


def atomic(rel, indices):
    return tuple(rel[i][j] for i in indices for j in indices)


def invariant_recursive(rel, rank=3):
    size = len(rel)
    @lru_cache(None)
    def hintikka(xs, left):
        atom = atomic(rel, xs)
        if left == 0:
            return (atom,)
        extensions = frozenset(hintikka(xs + (t,), left-1) for t in range(size))
        return atom, extensions
    return hintikka((), rank)


def invariant_triple_profiles(rel):
    """An independent, nonrecursive realization of three quantifier layers."""
    n = len(rel)
    def triple(x,y,z):
        return (rel[x][x],rel[x][y],rel[x][z],
                rel[y][x],rel[y][y],rel[y][z],
                rel[z][x],rel[z][y],rel[z][z])
    pointed = set()
    for x in range(n):
        profile = set()
        for y in range(n):
            diagram=(rel[x][x],rel[x][y],rel[y][x],rel[y][y])
            witness_types = frozenset(triple(x,y,z) for z in range(n))
            profile.add((diagram,witness_types))
        pointed.add(((rel[x][x],),frozenset(profile)))
    return frozenset(pointed)


def census(k):
    classes_a, classes_b = {}, {}
    for lengths in combinations_with_replacement(range(1,8),k):
        rel = poset(lengths)
        ka = invariant_recursive(rel)
        kb = invariant_triple_profiles(rel)
        classes_a.setdefault(ka, []).append(lengths)
        classes_b.setdefault(kb, []).append(lengths)
    partition_a = sorted(tuple(v) for v in classes_a.values())
    partition_b = sorted(tuple(v) for v in classes_b.values())
    assert partition_a == partition_b, 'independent type constructions differ'
    mergers = [list(group) for group in partition_a if len(group)>1]
    minima = [min(group, key=lambda v:(sum(v),v)) for group in partition_a]
    bound = max(map(sum,minima))
    max_rep = [v for v in minima if sum(v)==bound]
    return len(partition_a),len(list(combinations_with_replacement(range(1,8),k))),bound,max_rep,mergers


def main():
    expected = {1:(7,7,7),2:(27,28,13),3:(68,84,19)}
    tables = []
    for k in (1,2,3):
        count,total,bound,rep,mergers = census(k)
        assert (count,total,bound)==expected[k]
        print('STRATUM_OK', 'components='+str(k),'capped='+str(total),
              'rank3_types='+str(count),'sharp_vertices='+str(bound),'extremal='+str(rep))
        print('MERGER_LIST',k,json.dumps(mergers,separators=(',',':')))
        tables.append({'k':k,'capped':total,'types':count,'bound':bound,'extremal':rep,'mergers':mergers})
    assert sum(t['types'] for t in tables)==102
    # Between different component counts in {1,2,3}, q<=3 sentences
    # express an antichain of size 2 or 3; the three strata are disjoint.
    print('TOTAL_THREE_ROUND_THEORIES_OK',102)
    # Finite checks across truncation boundary supplement the general EF proof.
    for lengths in ((8,),(9,),(1,8),(8,8),(4,8),(2,5,9),(8,8,8),(2,8,9),(5,7,9),(9,9,9)):
        trunc=tuple(min(x,7) for x in lengths)
        assert invariant_triple_profiles(poset(lengths)) == invariant_triple_profiles(poset(trunc))
    print('TRUNCATION_BOUNDARY_SAMPLES_OK',10)
    certificate_json=json.dumps(tables,sort_keys=True,separators=(',',':')).encode()
    print('MERGER_TABLE_SHA256',hashlib.sha256(certificate_json).hexdigest())
    print('VERIFY_OK')

if __name__=='__main__':main()
