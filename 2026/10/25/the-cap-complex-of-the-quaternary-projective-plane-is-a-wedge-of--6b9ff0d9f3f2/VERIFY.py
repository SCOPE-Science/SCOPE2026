#!/usr/bin/env python3
"""Exact, dependency-free verification of the PG(2,4) cap-complex Morse reduction."""
from itertools import product, combinations
from collections import Counter, deque
from math import comb

def gf4mul(a,b):
    p=0
    for i in range(2):
        if (a>>i)&1: p ^= b<<i
    # Polynomial reduction modulo z^2+z+1.
    if p&8: p ^= 0b1110
    if p&4: p ^= 0b111
    return p

def coords():
    inv={a:next(b for b in (1,2,3) if gf4mul(a,b)==1) for a in (1,2,3)}
    pts=set()
    for x in product(range(4),repeat=3):
        if x==(0,0,0): continue
        leading=next(a for a in x if a!=0)
        pts.add(tuple(gf4mul(z,inv[leading]) for z in x))
    return tuple(sorted(pts))

def main():
    points=coords()
    assert len(points)==21
    assert gf4mul(2,2)==3 and gf4mul(3,3)==2 and gf4mul(2,3)==1
    # Enumerate all projective lines by nonzero covectors, normalized as points.
    lines=[]
    for a in points:
        line=frozenset(i for i,x in enumerate(points)
            if gf4mul(a[0],x[0]) ^ gf4mul(a[1],x[1]) ^ gf4mul(a[2],x[2]) == 0)
        assert len(line)==5
        lines.append(line)
    assert len(set(lines))==21
    line_through={}
    for i,j in combinations(range(21),2):
        through=[L for L in lines if i in L and j in L]
        assert len(through)==1
        line_through[i,j]=through[0]
    # Independently enumerate ALL candidate subsets up to size seven, not merely
    # recursively reachable faces. A triple is forbidden iff collinear.
    forbidden=set()
    for L in lines:
        forbidden.update(combinations(sorted(L),3))
    assert len(forbidden)==210
    faces=[()]
    counts=[]
    for size in range(1,8):
        group=[]
        for face in combinations(range(21),size):
            if any(trip in forbidden for trip in combinations(face,3)):
                continue
            group.append(face)
        counts.append(len(group))
        faces.extend(group)
    assert counts == [21,210,1120,2520,1008,168,0],counts
    assert len(faces)==5048
    faceset=set(faces)
    # Greedy vertex-toggle matching, with vertices 0,...,20 considered in order.
    remaining=faceset.copy()
    matching={}
    for v in range(21):
        for F in tuple(remaining):
            if v in F: continue
            G=tuple(sorted(F+(v,)))
            if G in remaining:
                matching[F]=G
                remaining.remove(F)
                remaining.remove(G)
    assert len(matching)==2149
    assert () in matching and len(matching[()])==1
    crit=Counter(len(F)-1 for F in remaining)
    assert crit==Counter({3:750}),crit
    # Remove the empty-face match to obtain an ordinary Forman matching:
    # one critical zero-cell and 750 critical three-cells.
    nonempty_matching={F:G for F,G in matching.items() if F}
    assert len(nonempty_matching)==2148
    # Exhaustively verify acyclicity of the associated directed Hasse graph.
    # Unmatched inclusions are oriented downward; matched pairs upward.
    cells=[F for F in faces if F]
    number={F:i for i,F in enumerate(cells)}
    arcs=[[] for _ in cells]
    indeg=[0]*len(cells)
    transitions=0
    for G in cells:
        if len(G)<2:continue
        for i in range(len(G)):
            F=G[:i]+G[i+1:]
            if nonempty_matching.get(F)==G:
                u,v=number[F],number[G]
            else:
                u,v=number[G],number[F]
            arcs[u].append(v)
            indeg[v]+=1
            transitions+=1
    queue=deque(i for i,d in enumerate(indeg) if d==0)
    visited=0
    while queue:
        v=queue.popleft();visited+=1
        for w in arcs[v]:
            indeg[w]-=1
            if indeg[w]==0:queue.append(w)
    assert visited==len(cells),('directed cycle',visited,len(cells))
    assert all(d==0 for d in indeg)
    # Euler characteristic from exhaustive face counts: 1-750.
    euler=sum((-1)**(i) *counts[i] for i in range(6))
    assert euler==-749
    print('VERIFY_OK')
    print('points=21 lines=21 collinear_triples=210')
    print('face_vector=21,210,1120,2520,1008,168')
    print('nonempty_cells=5047 matching_pairs=2148')
    print('critical_vector=(1,0,0,750,0,0)')
    print('directed_arcs=%d vertices_toposorted=%d'%(transitions,visited))
    print('euler_characteristic=-749 homotopy_type=wedge_750_S3')
if __name__ == '__main__':main()
