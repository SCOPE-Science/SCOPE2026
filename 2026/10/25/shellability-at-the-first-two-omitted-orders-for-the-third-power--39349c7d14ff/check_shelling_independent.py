#!/usr/bin/env python3
"""Independently test every old/new facet intersection against codimension-one intersections."""
import json
from itertools import combinations
from pathlib import Path


def triple_disconnected(n,t):
    adjacency={v:set() for v in t}
    for u,v in combinations(t,2):
        delta=abs(u-v)
        if min(delta,n-delta)<=3:
            adjacency[u].add(v);adjacency[v].add(u)
    start=t[0]; seen={start};todo=[start]
    while todo:
        v=todo.pop()
        for w in adjacency[v]-seen:
            seen.add(w);todo.append(w)
    return len(seen)!=3


def verify(n,sequence):
    allv=(1<<n)-1
    expected=[allv ^sum(1<<v for v in t) for t in combinations(range(n),3) if triple_disconnected(n,t)]
    assert sorted(expected)==sorted(sequence)
    assert len(set(sequence))==len(expected)
    previous=[];top_cells=0;face_masks=set()
    for i,f in enumerate(sequence):
        ridge_family=set()
        for v in range(n):
            if f & (1<<v):
                ridge=f ^(1<<v)
                if any((ridge & g)==ridge for g in previous):
                    ridge_family.add(ridge)
        if previous:
            assert ridge_family,('empty prior intersection',n,i)
            for g in previous:
                intersection=f&g
                assert any((intersection& ridge)==intersection for ridge in ridge_family),(n,i,'nonpure')
        if previous and len(ridge_family)==n-3:
            top_cells+=1
        sub=f
        while sub:
            face_masks.add(sub)
            sub=(sub-1)&f
        previous.append(f)
    assert top_cells=={13:1,14:8}[n]
    assert len(face_masks)=={13:7904,14:16067}[n]
    return len(expected),len(face_masks),top_cells

if __name__=='__main__':
    cert=json.loads((Path(__file__).parent/'shellings.json').read_text())
    for n in (13,14):
        t=verify(n,cert['shellings'][str(n)])
        print(f'n={n} independent_facets={t[0]} independent_nonempty_faces={t[1]} top_cells={t[2]} SHELLING=PASS')
    print('INDEPENDENT_COMBINATORIAL_CHECK_OK')
