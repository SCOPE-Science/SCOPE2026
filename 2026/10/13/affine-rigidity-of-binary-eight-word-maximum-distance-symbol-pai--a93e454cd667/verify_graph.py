#!/usr/bin/env python3
"""Exact exhaustive clique census of short binary pair-metric MDS codes."""
from collections import Counter

EXPECTED = {3:(7,1,1), 4:(11,1,2), 5:(21,5,20), 6:(36,4,32), 7:(64,2,32)}

def pair_distance(x,y,n):
    z=x^y
    mask=(1<<n)-1
    return (z|((z<<1)&mask)|(z>>(n-1))).bit_count()

for n,(expected_nodes,expected_zero,expected_total) in EXPECTED.items():
    candidates=[x for x in range(1,1<<n) if pair_distance(0,x,n)>=n-1]
    assert len(candidates)==expected_nodes
    neighbors={x:{y for y in candidates if y>x and pair_distance(x,y,n)>=n-1}
               for x in candidates}
    codes=[]
    def extend(selected,options):
        if len(selected)==7:
            codes.append(frozenset((0,*selected)))
            return
        if len(selected)+len(options)<7:
            return
        for j,x in enumerate(options):
            extend(selected+[x],[y for y in options[j+1:] if y in neighbors[x]])
    extend([],candidates)
    assert len(codes)==expected_zero
    for code in codes:
        assert len(code)==8
        assert all((x^y) in code for x in code for y in code)
        assert min(pair_distance(x,y,n) for x in code for y in code if x!=y)==n-1
    labeled=set()
    for code in codes:
        for z in range(1<<n):
            labeled.add(frozenset(x^z for x in code))
    assert len(labeled)==expected_total
    print(f'n={n}: candidates={len(candidates)} through_zero={len(codes)} labeled={len(labeled)}')
print('VERIFY_OK: complete nonlinear search for all possible lengths 3..7.')
