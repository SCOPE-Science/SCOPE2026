#!/usr/bin/env python3
"""Finite checks for triangle-avoidance complexes of joins of cycle graphs.
No third-party packages.  The all-size proof is mathematical, not exhaustive search.
"""
from itertools import combinations
from math import comb

CASES = [(4, 4), (4, 5), (5, 5), (4, 4, 4), (4, 5, 5),
         (5, 5, 5), (4, 6, 4), (6, 6, 4), (4, 4, 4, 4),
         (4, 4, 4, 5)]

def cycle_type(n):
    k, a = divmod(n, 3)
    return ((k-1, 2) if a == 0 else (k-1, 1) if a == 1 else (k, 1))

def predicted(lengths):
    count = {}
    r = len(lengths)
    def add(d, v): count[d] = count.get(d, 0) + v
    add(1, comb(r-1,2))
    types=[cycle_type(n) for n in lengths]
    for d,c in types: add(d+1, (r-1)*c)
    for (d,c),(e,f) in combinations(types,2): add(d+e+1, c*f)
    return {d:v for d,v in count.items() if v}

def faces_by_direct_triangle_test(lengths):
    n=sum(lengths)
    starts=[];v=0
    for ln in lengths: starts.append(tuple(range(v,v+ln)));v+=ln
    edges=set()
    for block in starts:
        for x,y in zip(block, block[1:]+block[:1]):
            edges.add(tuple(sorted((x,y))))
    for a,b in combinations(starts,2):
        for x in a:
            for y in b:
                edges.add((min(x,y),max(x,y)))
    tris=[]
    for a,b,c in combinations(range(n),3):
        if (a,b) in edges and (a,c) in edges and (b,c) in edges:
            tris.append((1<<a)|(1<<b)|(1<<c))
    levels={}
    for mask in range(1,1<<n):
        if not any(mask&t==t for t in tris):
            levels.setdefault(mask.bit_count()-1,[]).append(mask)
    return levels, len(tris)

def rank_gf2(columns):
    pivots={}
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k not in pivots:
                pivots[k]=x
                break
            x ^= pivots[k]
    return len(pivots)

def homology(levels):
    dmax=max(levels)
    ranks={0:1}  # augmentation C_0 -> C_{-1} for reduced homology
    for degree in range(1,dmax+1):
        lookup={face:k for k,face in enumerate(levels[degree-1])}
        cols=[]
        for face in levels[degree]:
            c=0; x=face
            while x:
                bit=x&-x;x-=bit
                c ^= 1<<lookup[face^bit]
            cols.append(c)
        ranks[degree]=rank_gf2(cols)
    ranks[dmax+1]=0
    return {d:len(v)-ranks[d]-ranks[d+1] for d,v in levels.items()
            if len(v)-ranks[d]-ranks[d+1]}

def main():
    total=0
    for case in CASES:
        levels,tris=faces_by_direct_triangle_test(case)
        actual=homology(levels)
        expected=predicted(case)
        assert actual==expected, (case, actual, expected)
        face_count=sum(map(len,levels.values()))
        total+=face_count
        print('CASE',','.join(map(str,case)),'triangles',tris,
              'faces',face_count,'betti',sorted(actual.items()))
    print('ALL_PASS','cases',len(CASES),'faces',total)

if __name__=='__main__': main()
