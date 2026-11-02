#!/usr/bin/env python3
"""Symbolic infinite-ladder check of neighbor degrees in five prism template orbits.
Vertices represented as (integer column, layer 0/1), without a modulus.
"""
from collections import Counter

TEMPLATES = (
    frozenset([(0,0),(1,0),(0,1),(1,1)]),
    frozenset([(0,0),(1,0),(0,1),(-1,1)]),
    frozenset([(0,0),(1,0),(2,0),(3,0)]),
    frozenset([(0,0),(1,0),(2,0),(0,1)]),
    frozenset([(0,0),(1,0),(3,0),(1,1)]),
)

def equiv(T):
    """Test if finite 4-set T is a translated, reflected, or layer-swapped template."""
    first_col=min(i for i,z in T)
    for shape in TEMPLATES:
        for sign in (-1,1):
            for swap in (0,1):
                rel=frozenset((sign*i,z^swap) for i,z in shape)
                for j in range(-6,7):
                    if frozenset((i+j,z) for i,z in rel)==T:
                        return True
    return False

def count_neighbors(S):
    neighbors=set()
    for lost in S:
        kept=S-{lost}
        # If a new 4-set is a template it has span <=3 in Z.
        # It contains a kept site, so the new site is within <=3 columns of it.
        for col in range(-5,8):
            for layer in (0,1):
                v=(col,layer)
                if v not in kept and v!=lost:
                    T=frozenset(kept|{v})
                    if equiv(T):neighbors.add(T)
    return len(neighbors)

assert tuple(map(count_neighbors,TEMPLATES))==(12,8,8,8,5)
print('SYMBOLIC_INFINITE_LADDER_LOCAL_DEGREES_PASS')
for i,T in enumerate(TEMPLATES):print('orbit',i,'degree',count_neighbors(T))
