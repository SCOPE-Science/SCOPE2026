#!/usr/bin/env python3
"""Independent enumeration and binary homology check for edge-matching complexes.
The graph is built from its explicit 18-edge list; no discrete Morse data are used.
"""
from collections import Counter
EDGES=((0,1),(0,7),(0,11),(1,2),(1,11),(2,3),(2,10),(3,4),(3,5),
       (4,5),(4,9),(5,6),(6,7),(6,8),(7,8),(8,9),(9,10),(10,11))
BETAS=(12,18,13,16,15,15,12,15,15,14,16,18,14,13,15,17,12,17)

def enumerate_by_bruteforce():
    faces = []
    for mask in range(1,1<<18):
        used = 0
        t = mask
        valid = True
        while t:
            bit = t & -t
            t -= bit
            u,v = EDGES[bit.bit_length()-1]
            support = (1<<u)|(1<<v)
            if used & support:
                valid = False
                break
            used |= support
        if valid:
            faces.append(mask)
    return faces

def rank_gf2(columns):
    pivots = {}
    for c in columns:
        while c:
            pivot = c.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = c
                break
            c ^= pivots[pivot]
    return len(pivots)

def check_one(faces, expected):
    bydim = [[] for _ in range(6)]
    for f in faces:
        bydim[f.bit_count()-1].append(f)
    assert sum(len(x) for x in bydim) == len(faces)
    ranks = [0]
    for k in range(1,6):
        low_idx = {f:i for i,f in enumerate(bydim[k-1])}
        cols=[]
        for high in bydim[k]:
            coeffs = 0
            t = high
            while t:
                bit=t&-t;t-=bit
                coeffs ^= 1<<low_idx[high^bit]
            cols.append(coeffs)
        ranks.append(rank_gf2(cols))
    betti = [len(bydim[k]) - ranks[k] - (ranks[k+1] if k<5 else 0)
             for k in range(6)]
    assert betti == [1,0,0,expected,0,0], (expected, betti)
    assert sum((-1)**k*len(bydim[k]) for k in range(6)) == 1-expected
    return [len(x) for x in bydim], ranks

def main():
    F=enumerate_by_bruteforce()
    assert len(F)==1025
    f,r=check_one(F,20)
    assert f==[18,117,333,397,152,8]
    assert r==[0,17,100,233,144,8]
    for i,beta in enumerate(BETAS):
        deletions=[s for s in F if not (s & (1<<i))]
        check_one(deletions,beta)
    print('FRUCHT_EDGE_MATCHING_CHAINS_OK full_f=(18,117,333,397,152,8) boundary_ranks=(0,17,100,233,144,8) checks=19')

if __name__=='__main__':
    main()
