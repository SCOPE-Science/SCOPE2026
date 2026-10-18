#!/usr/bin/env python3
"""Finite consistency checks for three-axis nonattacking-rook complexes.

All claims about arbitrary board lengths are established by the accompanying proof;
this program verifies the combinatorial gluing mechanism and small boundary ranks.
"""
from itertools import permutations, combinations, product
from collections import Counter, defaultdict
from math import factorial

PERMS=tuple(permutations(range(3)))

def signs4(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(4) for j in range(i+1,4))%2 else 1

def rank_mod(columns, prime):
    """Deterministic column elimination on sparse vectors over F_prime."""
    pivot={}
    for v0 in columns:
        v={k: x%prime for k,x in v0.items() if x%prime}
        while v:
            i=min(v)
            if i not in pivot:
                inv=pow(v[i],-1,prime)
                pivot[i]={j: a*inv%prime for j,a in v.items() if a*inv%prime}
                break
            scale=v[i]
            for j,a in pivot[i].items():
                x=(v.get(j,0)-scale*a)%prime
                if x: v[j]=x
                else: v.pop(j,None)
    return len(pivot)

def bdy_faces(tri):
    return [(tri[:j]+tri[j+1:],(-1)**j) for j in range(3)]

def chess_faces(n):
    vertices={(i,k) for i in range(3) for k in range(n)}
    edges={frozenset(((i,k),(j,l))) for i in range(3) for j in range(i+1,3) for k in range(n) for l in range(n) if k!=l}
    tri=[tuple((i,ks[i]) for i in range(3)) for ks in permutations(range(n),3)]
    return vertices,edges,tri

def full_faces(n):
    vertices={(i,j,k) for i in range(3) for j in range(3) for k in range(n)}
    edges={frozenset((a,b)) for a,b in combinations(vertices,2) if all(a[t]!=b[t] for t in range(3))}
    tris=[tuple((i,perm[i],ks[i]) for i in range(3)) for perm in PERMS for ks in permutations(range(n),3)]
    return vertices,edges,tris

def check(n):
    v,e,t=full_faces(n)
    assert (len(v),len(e),len(t))==(9*n,18*n*(n-1),6*n*(n-1)*(n-2))
    blocks={pi:{(i,pi[i],k) for i in range(3) for k in range(n)} for pi in PERMS}
    # Every graph edge lives in exactly one full chessboard block.
    assignments={}
    for edge in e:
        pts=tuple(edge)
        permissible=[pi for pi,vs in blocks.items() if set(pts)<=vs]
        assert len(permissible)==1
        assignments[edge]=permissible[0]
    for tri in t:
        ps={assignments[frozenset(face)] for face,_ in bdy_faces(tri)}
        assert len(ps)==1
    assert set().union(*blocks.values())==v
    graph=[]
    for a,b in combinations(PERMS,2):
        size=len(blocks[a]&blocks[b]);assert size in (0,n)
        if size: graph.extend([(a,b)]*size)
    assert len(graph)==9*n
    for aa,bb,cc in combinations(PERMS,3):
        assert not blocks[aa]&blocks[bb]&blocks[cc]
    # For every shared vertex there are exactly two block memberships.
    assert all(sum(point in block for block in blocks.values())==2 for point in v)
    assert len({(a,b) for a,b in graph})==9
    # Check all boundaries under the block-coordinate map, with signs.
    # Orient facets by the first coordinate i = 0,1,2.
    for tri in t:
        pi=next(pi for pi,vs in blocks.items() if set(tri)<=vs)
        for face,s in bdy_faces(tri):
            edge=frozenset(face)
            assert assignments[edge]==pi
            assert frozenset((i,k) for i,j,k in face) in chess_faces_cache[n][1]
    cv,ce,ct=chess_faces_cache[n]
    assert len(cv)==3*n and len(ce)==3*n*(n-1) and len(ct)==n*(n-1)*(n-2)
    ce_index={f:i for i,f in enumerate(sorted(ce,key=lambda f:tuple(sorted(f))))}
    columns=[]
    edge_degrees=Counter()
    for tri in ct:
        col={}
        for face,s in bdy_faces(tri):
            edge=frozenset(face);edge_degrees[edge]+=1
            ix=ce_index[edge];col[ix]=s
        columns.append(col)
    assert set(edge_degrees.values())=={n-2}
    ranks=(rank_mod(columns,2),rank_mod(columns,101))
    assert ranks[0]==ranks[1]
    # Connected ordinary chessboard graph, via BFS.
    adj=defaultdict(set)
    for edge in ce:
        a,b=tuple(edge);adj[a].add(b);adj[b].add(a)
    reached={next(iter(cv))}
    while True:
        new=reached|set().union(*(adj[x] for x in reached))
        if new==reached:break
        reached=new
    assert len(reached)==len(cv)
    if n==3:
        assert ranks==(6,6)
        assert all(x==1 for x in edge_degrees.values())
        base='wedge4_S1'; b1=4; b2=0
    elif n==4:
        assert ranks==(23,23)
        # Orientability of the triangulated 2-manifold:
        oriented={}
        for tri in ct:
            vals=tuple(z for i,z in tri)
            missing=next(k for k in range(4) if k not in vals)
            parity=signs4(vals+(missing,))
            for edge,s in bdy_faces(tri):
                ix=ce_index[frozenset(edge)]
                oriented[ix]=oriented.get(ix,0)+parity*s
        assert set(oriented.values())=={0}
        assert all(x==2 for x in edge_degrees.values())
        for vertex in cv:
            link_edges={frozenset((a,b)) for tri in ct if vertex in tri for (a,b) in [tuple(set(tri)-{vertex})]}
            link_v={v for edge in link_edges for v in edge}
            assert len(link_v)==6 and len(link_edges)==6
            deg=Counter(v for edge in link_edges for v in edge)
            assert set(deg.values())=={2}
        assert len(cv)-len(ce)+len(ct)==0
        base='torus';b1=2;b2=1
    else:
        # For n>=5, simply connected by Björner--Lovasz--Vrecica--Zivaljevic.
        assert n>=5
        b2=len(ct)-ranks[0]
        assert b2==n**3-6*n*n+8*n-1
        base='wedge_S2';b1=0
    top=6*b2
    circles=9*n-5+6*b1
    reduced_euler=len(v)-len(e)+len(t)-1
    assert top-circles==reduced_euler
    print(f'n={n} f={(len(v),len(e),len(t))} chess_rank={ranks[0]} base={base} H1={circles} H2={top} graph_cycle={9*n-5}')

chess_faces_cache={n:chess_faces(n) for n in range(3,8)}
for n in range(3,8):check(n)
print('VERIFY_OK BLOCK_COVER SIX_ORDINARY_CHESSBOARDS NINE_N_POINT_GLUINGS NO_TRIPLE_INTERSECTIONS')
