#!/usr/bin/env python3
"""Finite checks for the Alexander dual of ordinary three-cut hypercube complexes.
The uniform proof uses elementary collapses and cellular duality; this is a corroborating checker.
"""
from itertools import combinations
from math import comb

def gf2_rank(columns):
    piv={}
    for v in columns:
        while v:
            k=v.bit_length()-1
            if k in piv: v^=piv[k]
            else:
                piv[k]=v
                break
    return len(piv)

def hamming(x,y):return (x^y).bit_count()

def test(d):
    n=1<<d
    verts=list(range(n))
    edges=list(combinations(verts,2))
    e_index={e:i for i,e in enumerate(edges)}
    # Independent construction: a 3-face is included iff its induced Q_d graph is connected.
    triangles=[t for t in combinations(verts,3) if sum(hamming(a,b)==1 for a,b in combinations(t,2))==2]
    t_index={t:i for i,t in enumerate(triangles)}
    # Independent construction: a 4-face is included iff all four 3-subsets are connected.
    tetras=[tuple(s) for s in combinations(verts,4) if all(tuple(t) in t_index for t in combinations(s,3))]
    squares=[]
    for v in verts:
        for a,b in combinations(range(d),2):
            sq=tuple(sorted((v,v^(1<<a),v^(1<<b),v^(1<<a)^(1<<b))))
            squares.append(sq)
    squares=set(squares)
    assert set(tetras)==squares
    assert len(triangles)==4*len(squares)
    assert len(squares)==comb(d,2)*(1<<(d-2))
    # Every 3-face has a unique tetrahedral parent; every distance-two edge has one.
    cover={t:0 for t in triangles}
    for s in tetras:
        for t in combinations(s,3):cover[t]+=1
    assert set(cover.values())=={1}
    diag_owners={e:0 for e in edges if hamming(*e)==2}
    for s in tetras:
        for e in combinations(s,2):
            if e in diag_owners:diag_owners[e]+=1
    assert set(diag_owners.values())=={1}
    # Explicit two elementary collapses per tetra, reducing to triangulated squares.
    final_faces=[]
    for s in tetras:
        a,b,c,z=s
        # Pick a Hamiltonian square cyclic order a,b,c,z using only Hamming-1 steps.
        for P in __import__('itertools').permutations(s):
            if all(hamming(P[i],P[(i+1)%4])==1 for i in range(4)):
                a,b,c,z=P;break
        else:raise AssertionError('not a square')
        # remove tetra with triangle (a,b,z), then triangle (b,c,z) with diagonal (b,z).
        assert hamming(b,z)==2 and hamming(a,c)==2
        final_faces.extend([tuple(sorted((a,b,c))),tuple(sorted((a,c,z)))])
    assert len(final_faces)==2*len(squares)
    # Ranks of the exact simplicial chain complex modulo two for each d.
    b1=[(1<<u)|(1<<v) for u,v in edges]  # chain group C0
    b2=[sum(1<<e_index[e] for e in combinations(t,2)) for t in triangles]
    b3=[sum(1<<t_index[tuple(t)] for t in combinations(s,3)) for s in tetras]
    r1,r2,r3=map(gf2_rank,(b1,b2,b3))
    H1=len(edges)-r1-r2
    H2=len(triangles)-r2-r3
    H3=len(tetras)-r3
    mu=(1<<(d-3))*(d*d-5*d+8)-1
    h=(1<<(d-1))*sum(comb(d,j) for j in range(3,d+1))
    assert r1==n-1 and r3==len(tetras)
    assert (H1,H2,H3)==(h,mu,0)
    assert H1==sum(1 for e in edges if hamming(*e)>=3)
    print(f'd={d} N={n} edges={len(edges)} triangles={len(triangles)} tetrahedra={len(tetras)} ranks=({r1},{r2},{r3}) dual_Betti=(H1={H1},H2={H2}) cut_Betti=(degree{n-5}:{mu},degree{n-4}:{h})')

if __name__=='__main__':
    for d in (3,4,5):test(d)
    print('HYPERCUBE_ORDINARY_THREE_CUT_DUAL_FINITE_CHECKS_OK')
