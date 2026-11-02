#!/usr/bin/env python3
"""Independent set-based three-round EF game test for finite grid posets.

Implements the alternating-quantifier back-and-forth recursion using
four-valued pair relations; different code and primitive from bit signatures.
"""
from itertools import product
from collections import defaultdict

def relation(p, q):
    if p == q:
        return '='
    if p[0] <= q[0] and p[1] <= q[1]:
        return '<'
    if p[0] >= q[0] and p[1] >= q[1]:
        return '>'
    return '#'

def game_signature(a,b):
    V=list(product(range(a),range(b)))
    # The final move is an atomic comparison of three pebbled elements.
    # This keeps the order of the three selections; no quotient by automorphisms.
    def atom(x,y,z):
        return (relation(x,y),relation(x,z),relation(y,z))
    # For each pair, all atomic replies in the last move.
    two=[]
    for x in V:
        t=[]
        for y in V:
            t.append(frozenset(atom(x,y,z) for z in V))
        two.append(t)
    # The second move can be made in either structure, hence equality
    # (rather than inclusion) of the sets of possible pair states.
    one=frozenset(frozenset(two[i][j] for j in range(len(V)))
                  for i in range(len(V)))
    # First move: equality of the sets of one-pebble states.
    return one

def run():
    sig={}
    for a in range(1,8):
        for b in range(a,8):
            sig[a,b]=game_signature(a,b)
    groups=defaultdict(list)
    for k,v in sig.items(): groups[v].append(k)
    assert len(groups)==21
    for rep in ((1,7),(2,6),(3,6),(4,6),(5,6)):
        assert rep in sig
    assert sig[5,6]==sig[7,7]==sig[6,6]
    assert sig[5,5]!=sig[5,6]
    assert sig[4,5]!=sig[4,6]
    assert sig[1,6]!=sig[1,7]
    print('CHECK PASS: 28 exact three-round game states, 21 equivalence classes')
    for key in sorted(groups.values(), key=lambda x:x[0]):
        print('class',key)

if __name__=='__main__':run()
