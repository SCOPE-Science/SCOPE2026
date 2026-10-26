#!/usr/bin/env python3
"""Exact five-cell distance-equalizer basis census for rectangular rook graphs.

The finite normal-form computation is exhaustive for every board p,q >= 5:
each 5-cell set is a pair of set partitions of five labels; two fresh
coordinate labels per axis suffice to represent every exterior pair.
Only the Python standard library is required.
"""
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import csv

K = 5

def set_partitions(n):
    # Each tuple is a restricted-growth labeling of a set partition.
    def rec(word, nblocks):
        if len(word) == n:
            yield tuple(word)
        else:
            for b in range(nblocks + 1):
                yield from rec(word + [b], max(nblocks, b + 1))
    yield from rec([0], 1)

def canon(edges):
    rows = sorted({x for x, y in edges})
    cols = sorted({y for x, y in edges})
    ri = {x: i for i,x in enumerate(rows)}
    ci = {x: i for i,x in enumerate(cols)}
    masks = [0] * len(rows)
    for x,y in edges:
        masks[ri[x]] |= 1 << ci[y]
    b = len(cols)
    return min(tuple(sorted(sum((bool(mask & (1<<j))) << t[j] for j in range(b))
                           for mask in masks))
               for t in permutations(range(b)))

def edges_of(shape):
    return {(i,j) for i,mask in enumerate(shape)
            for j in range(max(shape).bit_length()) if mask & (1<<j)}

def valid(shape, p, q, witness=False):
    E = edges_of(shape)
    a = len(shape)
    b = max(shape).bit_length()
    if p < a or q < b:
        raise ValueError('The shape does not fit the board')
    # Each exterior pair uses at most two unused row/column coordinates.
    nr = a + min(2, p-a)
    nc = b + min(2, q-b)
    pts = [(i,j) for i in range(nr) for j in range(nc) if (i,j) not in E]
    for x,y in combinations(pts,2):
        # 1-bit = at graph distance 1 from the landmark. Exterior cells
        # cannot be at distance zero, so bitwise complement detects failure.
        ix = sum(1<<k for k,(r,c) in enumerate(sorted(E)) if x[0]==r or x[1]==c)
        iy = sum(1<<k for k,(r,c) in enumerate(sorted(E)) if y[0]==r or y[1]==c)
        if (ix ^ iy) == (1<<K)-1:
            return (False,(x,y)) if witness else False
    return (True,None) if witness else True

def aut(shape):
    E = edges_of(shape)
    a,b = len(shape), max(shape).bit_length()
    return sum({(rr[i],cc[j]) for i,j in E}==E
               for rr in permutations(range(a))
               for cc in permutations(range(b)))

def fall(n,k):
    return factorial(n)//factorial(n-k)

def known_count(p,q):
    return (9*fall(p,3)*fall(q,3)//4 +
            fall(p,5)*fall(q,5)//120 +
            (q+5*q*(q-1) if p==5 else 0) +
            (p+5*p*(p-1) if q==5 else 0))

def independent_brute(p,q):
    # Entirely separate pairwise-hit calculation on the original board.
    n=p*q
    V=[divmod(i,q) for i in range(n)]
    E=[]
    for u,v in combinations(range(n),2):
        x,y=V[u],V[v]
        mask=(1<<u)|(1<<v)
        for i,z in enumerate(V):
            if (x[0]!=z[0])+(x[1]!=z[1]) == (y[0]!=z[0])+(y[1]!=z[1]):
                mask |= 1<<i
        E.append(mask)
    total=0
    for cells in combinations(range(n),K):
        chosen=sum(1<<i for i in cells)
        if all(chosen&mask for mask in E):
            total+=1
    return total

def main():
    partitions=list(set_partitions(K))
    assert len(partitions)==52
    patterns=set()
    admissible=0
    for r in partitions:
        for c in partitions:
            coords=list(zip(r,c))
            if len(set(coords))==K:
                admissible+=1
                patterns.add(canon(coords))
    assert len(patterns)==34, len(patterns)
    with Path(__file__).with_name('PATTERNS.tsv').open(encoding='utf-8', newline='') as handle:
        certificate=list(csv.DictReader(handle,delimiter='\t'))
    assert len(certificate)==34
    for row in certificate:
        s=tuple(map(int,row['row_masks'].split(',')))
        assert s in patterns
        assert int(row['occupied_rows'])==len(s)
        assert int(row['occupied_cols'])==max(s).bit_length()
        assert int(row['axis_preserving_automorphisms'])==aut(s)
        for p,q in [(5,5),(5,6),(6,5),(6,6),(7,7)]:
            assert int(row[f'valid_{p}x{q}'])==int(valid(s,p,q))
        for p,q in [(5,5),(5,6),(6,5),(6,6),(7,7)]:
            passed,witness=valid(s,p,q,True)
            assert row[f'obstruction_{p}x{q}']==('' if passed else str(witness))
    core={(1,1,7),(1,2,7),(1,3,5),(1,3,6),(1,2,4,8,16)}
    extra_cols={(31,),(1,30)}
    extra_rows={(1,1,1,1,1),(1,1,1,1,2)}
    assert len(core|extra_cols|extra_rows)==9
    assert all(s in patterns for s in core|extra_cols|extra_rows)
    cases=list(product((5,6,7),repeat=2))
    for p,q in cases:
        observed={s for s in patterns if valid(s,p,q)}
        expected=core|(extra_rows if p==5 else set())|(extra_cols if q==5 else set())
        assert observed==expected,(p,q,observed^expected)
        by_orbit=sum(fall(p,len(s))*fall(q,max(s).bit_length())//aut(s)
                     for s in observed)
        assert by_orbit==known_count(p,q),(p,q,by_orbit,known_count(p,q))
    assert {s:aut(s) for s in core}=={(1,1,7):4,(1,2,7):2,(1,3,5):2,(1,3,6):1,(1,2,4,8,16):120}
    assert [(p,q,independent_brute(p,q)) for p,q in [(5,5),(5,6),(6,6)]]==[
        (5,5,8430),(5,6,17076),(6,6,36720)]
    print('VERIFIED: 52 partitions,',admissible,'admissible pairs, 34 patterns, nine boundary cases')
    print('VERIFIED: nine winning patterns on 5x5, seven on a thin >=6 board, five in the >=6 core')
    print('VERIFIED: exact automorphisms, orbit counts and independent direct enumeration')
    print('VALUES: 5x5=8430 5x6=17076 5x7=31087 6x6=36720 7x7=152145')

if __name__=='__main__':
    main()
