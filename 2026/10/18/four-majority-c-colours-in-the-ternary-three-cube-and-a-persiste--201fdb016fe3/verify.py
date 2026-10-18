#!/usr/bin/env python3
"""Independent finite checks for the ternary Hamming majority-colouring theorem.

Requires only Python 3.10+ standard library. Run: python3 verify.py.
These finite checks do not replace the unrestricted proofs in RESULT.md.
"""
from itertools import product, combinations
from collections import Counter
from math import comb

SYMBOLS=("A","B","C","D")
TABLE=(("A","C","B"),("D","D","B"),("A","C","A"))

def vertices(dim):
    return list(product(range(3),repeat=dim))

def neighbors(vertex):
    for i in range(len(vertex)):
        for value in range(3):
            if value != vertex[i]:
                yield vertex[:i]+(value,)+vertex[i+1:]

def colors(vertex):
    x,y=vertex[0],vertex[1]
    answer=[TABLE[x][y]]
    for i in range(3,len(vertex),2):
        answer.append(vertex[i])
    return tuple(answer)

def valid_coloring(dim):
    assert dim>=3 and dim%2==1
    vv=vertices(dim)
    cc={v:colors(v) for v in vv}
    for v in vv:
        same=sum(cc[v]==cc[w] for w in neighbors(v))
        assert same >= dim, (dim,v,same)
    assert len(set(cc.values())) == 4*(3**((dim-3)//2))
    return len(cc),len(set(cc.values()))

def rectangles():
    found=set()
    for whole in range(3):
        for partial in range(3):
            if partial==whole:
                continue
            fixed=3-whole-partial
            for f in range(3):
                for two in combinations(range(3),2):
                    cells=tuple(sorted(v for v in vertices(3)
                                      if v[fixed]==f and v[partial] in two))
                    assert len(cells)==6
                    found.add(cells)
    assert len(found)==54
    return found

def minimum_class_census():
    vv=vertices(3)
    index={v:i for i,v in enumerate(vv)}
    adj=[sum(1<<index[w] for w in neighbors(v)) for v in vv]
    valid=set()
    for choice in combinations(range(27),6):
        mask=sum(1<<v for v in choice)
        if all((mask & adj[v]).bit_count()>=3 for v in choice):
            valid.add(tuple(vv[i] for i in choice))
    expected=rectangles()
    assert valid==expected, (len(valid),len(expected),len(valid^expected))
    return len(valid),comb(27,6)

if __name__=='__main__':
    six_checked,examined=minimum_class_census()
    assert six_checked==54
    examples=[(dim,*valid_coloring(dim)) for dim in (3,5,7,9)]
    print('PASS: all',examined,'six-vertex subsets checked;',six_checked,'valid, exactly 54 rectangles.')
    print('PASS: constructions by dimension, vertices, colours:',examples)
