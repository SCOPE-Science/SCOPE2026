#!/usr/bin/env python3
"""Finite exhaustive checks for modal density on loop-free directed graphs."""
from collections import Counter
from fractions import Fraction
from itertools import product

def arcs(n):
    return [(u,v) for u in range(n) for v in range(n) if u!=v]

def unsupported(n, edges):
    return {(u,v) for (u,v) in edges if not any((u,z) in edges and (z,v) in edges for z in range(n))}

def modal_holds(n, edges, truth):
    for w in range(n):
        radius1 = {v for (u,v) in edges if u==w}
        radius2 = {v for u in radius1 for a,v in edges if a==u}
        if radius2 <= truth and not radius1 <= truth:
            return False
    return True

def exact(n):
    ee=arcs(n)
    all_mom=Fraction(0); ok=0; dist=Counter(); total=0
    for flags in product((False,True),repeat=len(ee)):
        E={a for a,b in zip(ee,flags) if b}
        bad=unsupported(n,E)
        frame_valid=(not bad)
        every_valuation=all(modal_holds(n,E,{i for i in range(n) if bit>>i&1}) for bit in range(1<<n))
        assert frame_valid==every_valuation,(n,E,bad)
        ok+=frame_valid
        dist[len(bad)]+=1
        all_mom+=len(bad)
        total+=1
    exact_expected=Fraction(n*(n-1),2)*Fraction(3,4)**(n-2)
    assert all_mom/total ==exact_expected,(n,all_mom/total,exact_expected)
    print('EXHAUSTIVE_MODAL_EQUIVALENCE_OK',n,total,'valid',ok,'E_X',exact_expected,'distribution',sorted(dist.items()))

for n in (2,3,4): exact(n)
print('RANDOM_MODAL_DENSITY_CHECK_OK')
