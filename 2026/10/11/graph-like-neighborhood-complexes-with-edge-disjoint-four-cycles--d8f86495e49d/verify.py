#!/usr/bin/env python3
"""Finite corroboration for edge-disjoint-square neighborhood complexes.

Enumerate all labeled connected graphs on four through six vertices with
exactly one unoriented four-cycle, plus larger examples with edge-disjoint squares. Independently compute the open-neighborhood
complex over F_2, its nerve, and the two-disc comparison complex. This code is
not a substitute for the all-parameter nerve-lemma proof.
"""
from itertools import combinations
from collections import Counter


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def is_bipartite(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = {0: 0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v in color:
                if color[v] == color[u]:
                    return False
            else:
                color[v] = 1 - color[u]
                stack.append(v)
    return True


def squares(n, edges):
    eset = {frozenset(e) for e in edges}
    result = []
    for quad in combinations(range(n), 4):
        a, b, c, d = quad
        # There are three partitions of four vertices into opposite pairs.
        for x, y, z, w in [(a, b, c, d), (a, c, b, d), (a, d, b, c)]:
            if all(frozenset(pair) in eset for pair in ((x, z), (x, w), (y, z), (y, w))):
                result.append(((x, y), (z, w)))
    return result


def simplicial_faces(facets):
    faces = {()}
    for facet in facets:
        vert = sorted(facet)
        for j in range(1, len(vert)+1):
            faces.update(combinations(vert, j))
    return faces


def gf2rank(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            k = x.bit_length() - 1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    return len(pivots)


def reduced_betti(faces):
    maxd = max(len(face) for face in faces)-1
    counts = [0]*(maxd+1)
    ranks = [0]*(maxd+2)
    face_levels = [[f for f in faces if len(f) == k+1] for k in range(maxd+1)]
    for k in range(maxd+1):
        counts[k] = len(face_levels[k])
    for d in range(1, maxd+1):
        oldindex = {f:i for i,f in enumerate(face_levels[d-1])}
        columns = []
        for f in face_levels[d]:
            col = 0
            for j in range(len(f)):
                sub = f[:j]+f[j+1:]
                col ^= 1 << oldindex[sub]
            columns.append(col)
        ranks[d] = gf2rank(columns)
    return [counts[d] - ranks[d] - ranks[d+1] - (1 if d == 0 else 0) for d in range(maxd+1)]


def neighborhood_facets(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def nerve_faces(n, neighborhoods):
    facets=[]
    for w in range(n):
        facets.append({v for v in range(n) if w in neighborhoods[v]})
    # This is mathematically the nerve of the cover by neighborhood simplices.
    return simplicial_faces(facets)


def canonical_W_facets(n, edges, square):
    # Right-label n+i and left-label i; each square has two lifted disks.
    uv = [(u, n+v) for u,v in edges] + [(v,n+u) for u,v in edges]
    triangles = []
    for ((a,c),(b,d)) in square:
        triangles += [(a,n+b,n+d),(c,n+b,n+d),
                      (b,n+a,n+c),(d,n+a,n+c)]
    return uv + triangles


def W_cover_nerve(n, edges, square):
    neighbors = neighborhood_facets(n,edges)
    special_edges = {u: [] for u in range(n)}
    for ((a,c),(b,d)) in square:
        for u in (a,c): special_edges[u].append((n+b,n+d))
        for u in (b,d): special_edges[u].append((n+a,n+c))
    cover = []
    for u in range(n):
        facets = [[u,n+v] for v in neighbors[u]]
        for x,y in special_edges[u]:
            facets.append((u,x,y))
        cover.append(simplicial_faces(facets))
    nerve = {()}
    for k in range(1,n+1):
        for centers in combinations(range(n),k):
            meet = set.intersection(*(cover[u] for u in centers))
            if any(meetface for meetface in meet):
                nerve.add(centers)
    return nerve


def assert_w_collapses(n, edges, square):
    F = simplicial_faces(canonical_W_facets(n,edges,square))
    for ((a,c),(b,d)) in square:
      for outer, diag, triangle in [
          ((a,n+b),(n+b,n+d),(a,n+b,n+d)),
          ((b,n+a),(n+a,n+c),(b,n+a,n+c))]:
        assert tuple(sorted(outer)) in F
        tri = tuple(sorted(triangle))
        edge = tuple(sorted(outer))
        assert tri in F
        assert [z for z in F if set(edge).issubset(z)] == [tri,edge] or set(z for z in F if set(edge).issubset(z)) == {tri,edge}
        F.remove(tri);F.remove(edge)
        # remaining triangle shares diagonal, which is now free
        rem = (c,n+b,n+d) if outer[0]==a else (d,n+a,n+c)
        tri = tuple(sorted(rem)); edge=tuple(sorted(diag))
        assert set(z for z in F if set(edge).issubset(z)) == {tri,edge}
        F.remove(tri); F.remove(edge)
    assert all(len(f)<=2 for f in F)
    return F


def verify(n,edges):
    sq = squares(n,edges)
    assert len(sq) >= 1
    edges_of_squares=[]
    for ((a,c),(b,d)) in sq:
        edges_of_squares.append({frozenset(x) for x in ((a,b),(a,d),(c,b),(c,d))})
    assert all(not edges_of_squares[i].intersection(edges_of_squares[j])
               for i in range(len(sq)) for j in range(i+1,len(sq)))
    N=simplicial_faces(neighborhood_facets(n,edges))
    W=simplicial_faces(canonical_W_facets(n,edges,sq))
    Nnerve=nerve_faces(n,neighborhood_facets(n,edges))
    assert Nnerve==W_cover_nerve(n,edges,sq), 'two good-cover nerves differ'
    collapsed=assert_w_collapses(n,edges,sq)
    bN=reduced_betti(N)
    bW=reduced_betti(W)
    bB=reduced_betti(collapsed)
    while bN and bN[-1]==0: bN.pop()
    while bW and bW[-1]==0: bW.pop()
    while bB and bB[-1]==0: bB.pop()
    assert bN == bW == bB, (n,edges,bN,bW,bB)
    v=n;e=len(edges)
    bp=is_bipartite(n,edges)
    k=len(sq)
    pred=(2*e-2*v+2-2*k if bp else 2*e-2*v+1-2*k)
    assert (bN[0] if bN else 0) == (1 if bp else 0), (edges,bN,bp)
    assert (bN[1] if len(bN)>1 else 0) == pred, (edges,bN,pred)
    assert all(x==0 for x in bN[2:]), (edges,bN)
    return bp,pred


def main():
    count=Counter(); examples={}
    for n in range(4,7):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            edges=[e for i,e in enumerate(pairs) if mask>>i&1]
            if len(edges)<4 or not connected(n,edges):
                continue
            if len(squares(n,edges)) != 1:
                continue
            bp,beta=verify(n,edges)
            count[(n, bp)]+=1
            examples.setdefault((n,bp), (edges,beta))
    assert count[(4,True)] == 3, count
    assert count[(4,False)] == 6, count
    # Two mutually vertex-disjoint four-cycles, with optional extra cycles.
    base = [(0,1),(1,2),(2,3),(3,0),
            (4,5),(5,6),(6,7),(7,4), (3,4)]
    bowtie = [(0,1),(1,2),(2,3),(3,0),
              (0,4),(4,5),(5,6),(6,0)]
    triple = bowtie + [(0,7),(7,8),(8,9),(9,0)]
    cases = [
        (10,triple),
        (12,triple+[(0,10),(10,11),(11,0)]),
        (7,bowtie),
        (9,bowtie+[(0,7),(7,8),(8,0)]),
        (8,base),
        (8,base+[(0,2)]),  # one diagonal, adding an odd cycle
        (10,base+[(0,8),(8,9),(9,0)]),  # added triangle, no new square
        (13,base+[(0,8),(8,9),(9,10),(10,11),(11,12),(12,0)]),  # added six-cycle
        (12,base+[(1,i) for i in range(8,12)]),  # one high-degree vertex
    ]
    for n,edges in cases:
        assert connected(n,edges)
        bp,beta=verify(n,edges)
        print(f'k={len(squares(n,edges))} example n={n} bipartite={bp} beta1={beta} maximal_degree={max(len(x) for x in neighborhood_facets(n,edges))}')
    for (n,bp),c in sorted(count.items()):
        print(f'n={n} bipartite={bp} labeled_graphs={c} sample_beta1={examples[(n,bp)][1]}')
    print('VERIFY_OK: all connected labeled unique-four-cycle graphs on 4..6 vertices and nine edge-disjoint multi-square cases; exact cover nerves, free-pair collapses, F2 homology.')

if __name__ == '__main__':
    main()
