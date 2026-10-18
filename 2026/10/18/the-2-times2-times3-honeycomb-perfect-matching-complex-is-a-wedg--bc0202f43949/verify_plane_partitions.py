#!/usr/bin/env python3
"""Independent plane-partition and exhaustive discrete-Morse verification.
All computations use exact integer bit masks; no external packages needed.
"""
from itertools import product
from collections import Counter


def make_complex(a,b,c):
    tilings=[]
    for heights in product(range(c+1), repeat=a*b):
        h=[heights[i*b:(i+1)*b] for i in range(a)]
        if any(h[i][j] < h[i+1][j] for i in range(a-1) for j in range(b)):
            continue
        if any(h[i][j] < h[i][j+1] for i in range(a) for j in range(b-1)):
            continue
        tiles=set()
        for i in range(a):
            for j in range(b):
                z=h[i][j]
                tiles.add(('z',i-z,j-z))
        for j in range(b):
            for z in range(c):
                x=sum(h[i][j]>z for i in range(a))
                tiles.add(('x',x-z,j-z))
        for i in range(a):
            for z in range(c):
                y=sum(h[i][j]>z for j in range(b))
                tiles.add(('y',i-z,y-z))
        assert len(tiles)==a*b+a*c+b*c
        tilings.append(tiles)
    edges=sorted(set().union(*tilings))
    ids={tile:i for i,tile in enumerate(edges)}
    facets={sum(1<<ids[t] for t in tiling) for tiling in tilings}
    assert len(facets)==len(tilings)
    faces={0}
    for f in facets:
        sub=f
        while sub:
            faces.add(sub)
            sub=(sub-1)&f
    return edges,facets,faces


def morse_reduction(faces,pivots):
    unmatched=set(faces)
    unmatched.discard(0)  # ordinary face poset; exactly one 0-cell survives
    log=[]
    for p in pivots:
        b=1<<p
        lower=[s for s in unmatched if not(s&b) and (s|b) in unmatched]
        for s in lower:
            unmatched.remove(s)
            unmatched.remove(s|b)
        log.append((p,len(lower),len(unmatched)))
    return log,unmatched

cases=[
    ((2,2,1),(12,1),6,19,{0:1,1:1}),
    ((2,2,2),(1,16,8,13,20,26),20,30,{0:1,3:2}),
    ((2,2,3),(24,1,17,12,40,6,7,28,34),50,41,{0:1,4:2}),
]
for (a,b,c),pivots,facets_expected,vertices_expected,critical_expected in cases:
    edges,facets,faces=make_complex(a,b,c)
    assert (len(facets),len(edges))==(facets_expected,vertices_expected)
    face_count=len(faces)
    fvec=[sum(1 for s in faces if s and s.bit_count()==k+1) for k in range(a*b+a*c+b*c)]
    log,critical=morse_reduction(faces,pivots)
    assert Counter(s.bit_count()-1 for s in critical)==critical_expected
    print('case',a,b,c,'perfect matchings',len(facets),'edge vertices',len(edges),'faces including empty',face_count)
    print('f-vector',fvec)
    print('Morse stages',log)
    print('critical bit masks',sorted(critical))
    if c==3:
        assert face_count==2517788
        assert log==[(24,1011305,495177),(1,247522,133),(17,30,73),(12,26,21),(40,3,15),(6,3,9),(7,1,7),(28,1,5),(34,1,3)]
        assert sorted(critical)==[16777216,2155873346,137439215754]
        assert fvec==[41,706,6186,31566,104477,241386,407750,517618,501141,371866,210600,89700,27900,6000,800,50]
print('VERIFIED: one critical vertex plus two critical dimension-four simplices for H(2,2,3).')
