"""Independently enumerate maximum induced matchings of Q_d, d=2..5.
The mathematical theorem for all dimensions does not depend on this finite test.
"""
from collections import Counter


def run(d):
    vertices=range(1<<d)
    edges=[(v,v^(1<<j),j) for v in vertices for j in range(d) if (v&(1<<j))==0]
    # An induced matching is equivalent to an independent set in L(Q_d)^2.
    conflict=[]
    for a,(x,y,i) in enumerate(edges):
        m=0
        for b,(u,v,j) in enumerate(edges):
            if any(p==q or (p^q).bit_count()==1 for p in (x,y) for q in (u,v)):
                m|=1<<b
        conflict.append(m)
    # independently specified construction (all direction-parity classes)
    expected=[]
    for i in range(d):
        for parity in range(2):
            indices=[j for j,(x,y,k) in enumerate(edges) if k==i and
                    ((x&~(1<<i)).bit_count()&1)==parity]
            expected.append(frozenset(indices))
    k=1<<(d-2)
    for b in expected: assert len(b)==k
    out=[]
    calls=0
    def search(chosen, candidates):
        nonlocal calls
        calls+=1
        if len(chosen)==k:
            out.append(frozenset(chosen)); return
        if len(chosen)+candidates.bit_count()<k:return
        while candidates:
            lsb=candidates&-candidates
            candidates^=lsb
            i=lsb.bit_length()-1
            search(chosen+[i],candidates&~conflict[i])
    search([], (1<<len(edges))-1)
    got=set(out)
    assert len(out)==len(got)
    assert got==set(expected), (d, len(out),len(set(expected)))
    print(f'd={d} vertices={1<<d} edges={len(edges)} size={k} maxima={len(got)} expected={2*d} nodes={calls}')

for d in (2,3,4,5): run(d)
