#!/usr/bin/env python3
"""Exact pair-extension spectra for Cartesian products of undirected cycles.
For each pair type, the four bits of the mask record witnesses with
adjacencies (to first vertex, to second vertex) 00, 01, 10, 11.
"""
from itertools import product

def spectrum(lengths):
    vertices = list(product(*(range(k) for k in lengths)))
    u=vertices[0]
    d=len(lengths)
    def adjacent(x,y):
        diff=[i for i in range(d) if x[i]!=y[i]]
        return len(diff)==1 and ((x[diff[0]]-y[diff[0]])%lengths[diff[0]] in (1,lengths[diff[0]]-1))
    result=set()
    for v in vertices[1:]:
        pat=0
        for w in vertices[1:]:
            if w==v: continue
            t=(int(adjacent(u,w))<<1) | int(adjacent(v,w))
            pat |= 1<<t
        result.add((int(adjacent(u,v)),pat))
    return tuple(sorted(result))

def label(L):
    if len(L)==1 and L[0]<=6: return 'cycle'+str(L[0])
    if len(L)==1: return 'stable-triangle-free'
    if all(n>=4 for n in L): return 'stable-triangle-free'
    if all(n==3 for n in L): return 'all-triangle-2' if len(L)==2 else 'all-triangle-3plus'
    return 'mixed-triangle-other'

EXPECTED={
'cycle3':((1,8),),
'cycle4':((0,8),(1,6)),
'cycle5':((0,14),(1,7)),
'cycle6':((0,6),(0,15),(1,7)),
'stable-triangle-free':((0,7),(0,15),(1,7)),
'all-triangle-2':((0,15),(1,15)),
'all-triangle-3plus':((0,7),(0,15),(1,15)),
'mixed-triangle-other':((0,7),(0,15),(1,7),(1,15)),
}

if __name__=='__main__':
    tested=0
    counts={k:0 for k in EXPECTED}
    for d,maxlength in [(1,16),(2,10),(3,6),(4,4),(5,3)]:
        for L in product(range(3,maxlength+1),repeat=d):
            if tuple(sorted(L))!=L: continue
            got=spectrum(L)
            label_=label(L)
            assert got==EXPECTED[label_],(L,label_,got,EXPECTED[label_])
            counts[label_]+=1
            tested+=1
    assert all(v>0 for v in counts.values())
    assert len(set(EXPECTED.values()))==8
    print('PASS: all',tested,'sampled dimension/order tuples match eight claimed pair spectra')
    print('Number of samples per class:',counts)
    for name,types in EXPECTED.items():print(name,types)
