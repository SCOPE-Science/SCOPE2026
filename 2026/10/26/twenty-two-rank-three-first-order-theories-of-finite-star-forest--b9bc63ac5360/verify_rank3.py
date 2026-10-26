#!/usr/bin/env python3
"""Exact rank-three FO theory census for finite undirected star forests.

Usage: python3 verify_rank3.py [--crosscheck]
Output: deterministic manifest CSV, followed by summary and optional direct EF tests.
Only the Python standard library is required.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import csv
import sys


def graph(profile):
    """Disjoint union of c_0 copies of K1, c_1 of K2, c_2 of K1,2, c_3 of K1,3."""
    rows = []
    for leaves, mult in enumerate(profile):
        for _ in range(mult):
            base = len(rows)
            rows.extend([0] * (leaves + 1))
            for v in range(base + 1,base + leaves + 1):
                rows[base] |= 1 << v
                rows[v] |= 1 << base
    return tuple(rows)


def atom(rows, x, y, z):
    """All three equality and adjacency atoms, encoded in a six-bit integer."""
    return ((x == y) << 5) | ((x == z) << 4) | ((y == z) << 3) | \
           (((rows[x] >> y)&1) << 2) | (((rows[x] >> z)&1) << 1) | ((rows[y] >> z)&1)


def rank3_type(rows):
    """The exact three-fold Hintikka powerset invariant, no graph comparisons approximated."""
    n = len(rows)
    pair_rank1 = [[frozenset(atom(rows,x,y,z) for z in range(n))
                   for y in range(n)] for x in range(n)]
    vertex_rank2 = [frozenset(pair_rank1[x]) for x in range(n)]
    return frozenset(vertex_rank2)


def profiles():
    for c in product(range(4),repeat=4):
        if any(c):
            yield c


def order(c):
    return sum((i+1)*v for i,v in enumerate(c))


def census():
    groups = defaultdict(list)
    for c in profiles():
        groups[rank3_type(graph(c))].append(c)
    ordered = sorted(groups.values(),key=lambda g:(min((order(c),c) for c in g),tuple(g)))
    assignments = {}
    reps = {}
    for k,cs in enumerate(ordered,1):
        rep = min(cs,key=lambda c:(order(c),c))
        reps[k]=rep
        for c in cs: assignments[c]=k
    return assignments,reps


def emit_csv(assignments,reps,output):
    with open(output,'w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['K1','K2','K1_2','K1_3','rank3_class','representative','order'])
        for c in profiles():
            w.writerow([*c,assignments[c],'-'.join(map(str,reps[assignments[c]])),order(c)])


def is_partial_iso(G,H,a,b):
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i]==a[j]) != (b[i]==b[j]):
                return False
            if bool((G[a[i]]>>a[j])&1) != bool((H[b[i]]>>b[j])&1):
                return False
    return True


def ef_equivalent(G,H):
    @lru_cache(maxsize=None)
    def rec(a,b,r):
        if not is_partial_iso(G,H,a,b):return False
        if r==0:return True
        for x in range(len(G)):
            if not any(rec(a+(x,),b+(y,),r-1) for y in range(len(H))):return False
        for y in range(len(H)):
            if not any(rec(a+(x,),b+(y,),r-1) for x in range(len(G))):return False
        return True
    return rec((),(),3)


def main():
    assignments,reps=census()
    assert len(assignments)==255
    assert len(reps)==22
    assert max(order(c) for c in reps.values()) == 9
    assert reps[22] == (0,0,3,0)
    assert len(set(reps.values()))==22
    emit_csv(assignments,reps,Path(__file__).with_name('rank3_manifest.csv'))
    print('canonical_profiles=255 rank3_theories=22 sharp_kernel_order=9')
    print('representatives:', [(i,reps[i]) for i in sorted(reps)])
    if '--crosscheck' in sys.argv:
        # A genuinely separate recursion over Spoiler/Duplicator game positions.
        for i in range(1,23):
            for j in range(i+1,23):
                assert not ef_equivalent(graph(reps[i]), graph(reps[j])),(i,j)
        print('direct_EF_pairwise_inequivalence=231/231')
        # sample redundant canonical profiles having different star sizes.
        pairs=[((0,0,0,3),(0,0,3,0)),((0,3,0,0),(0,3,0,0)),
               ((1,1,3,3),(1,1,1,0)),((3,3,3,3),(2,1,1,0))]
        for a,b in pairs:
            assert ef_equivalent(graph(a),graph(b)) == (assignments[a]==assignments[b]),(a,b)
        print('direct_EF_selected_equivalence_tests=4/4')

if __name__=='__main__':main()
