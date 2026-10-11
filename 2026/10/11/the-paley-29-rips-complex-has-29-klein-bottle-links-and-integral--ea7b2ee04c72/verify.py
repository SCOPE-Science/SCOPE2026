#!/usr/bin/env python3
"""Exact integral-topology checks for the clique complex of the order-29 Paley graph.
Requires only the Python standard library; see RESULT.md for the mathematical deductions.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

P = 29
RESIDUES = {x*x % P for x in range(1,P)}
VERTICES = tuple(range(P))
EDGES = tuple((a,b) for a in VERTICES for b in range(a+1,P)
              if (a-b) % P in RESIDUES)
EDGESET = set(EDGES)
NEIGHBORS = {v:tuple(w for w in VERTICES if w != v and
                     tuple(sorted((v,w))) in EDGESET) for v in VERTICES}


def cliques():
    # Enumerate ALL cliques, prove absence of a five-clique by testing every five-set.
    out = {}
    for k in range(1,6):
        out[k] = [c for c in combinations(VERTICES,k)
                  if all((a,b) in EDGESET for a,b in combinations(c,2))]
    assert not out[5]
    assert tuple(map(lambda k:len(out[k]),(1,2,3,4)))==(29,203,406,203)
    return out


def orientability(facets):
    # A closed pure d-complex is orientable precisely when top facets can
    # be signed so that their orientations cancel at each codimension-one face.
    incidence = defaultdict(list)
    for t in facets:
        for j in range(len(t)):
            incidence[t[:j]+t[j+1:]].append((t,(-1)**j))
    assert incidence and all(len(v)==2 for v in incidence.values())
    adjacency=defaultdict(list)
    for face,tw in incidence.items():
        (u,au),(v,av)=tw
        adjacency[u].append((v,-au*av,face))
        adjacency[v].append((u,-au*av,face))
    root=facets[0];sign={root:1};parent={root:None};depth={root:0}
    queue=deque([root]);bad=None
    while queue:
        u=queue.popleft()
        for v,rel,face in adjacency[u]:
            if v not in sign:
                sign[v]=sign[u]*rel
                parent[v]=u;depth[v]=depth[u]+1
                queue.append(v)
            elif sign[v]!=sign[u]*rel and bad is None:
                bad=(u,v,face)
    assert len(sign)==len(facets)
    return (bad is None),bad,(len(facets),len(incidence))


def check_links(F):
    # Verify a triangulated connected closed surface at every vertex.
    summaries=[]
    for v in VERTICES:
        triples=sorted(tuple(w for w in tet if w!=v)
                       for tet in F[4] if v in tet)
        verts={w for tri in triples for w in tri}
        edges={e for tri in triples for e in combinations(tri,2)}
        incidence=Counter(e for tri in triples for e in combinations(tri,2))
        assert (len(verts),len(edges),len(triples))==(14,42,28)
        assert set(incidence.values())=={2}
        # Every link vertex itself has a six-cycle as its link in the surface.
        for w in verts:
            # Simpler direct construction of six triangles incident to w.
            es=[tuple(x for x in tri if x!=w) for tri in triples if w in tri]
            adjacency=defaultdict(set)
            for a,b in es:adjacency[a].add(b);adjacency[b].add(a)
            assert len(adjacency)==6 and len(es)==6
            assert all(len(adj)==2 for adj in adjacency.values())
            start=min(adjacency);reached={start};stack=[start]
            while stack:
                for nxt in adjacency[stack.pop()]:
                    if nxt not in reached:reached.add(nxt);stack.append(nxt)
            assert len(reached)==6
        # Connectivity of the surface itself.
        link_graph=defaultdict(set)
        for a,b in edges:link_graph[a].add(b);link_graph[b].add(a)
        stack=[min(verts)];seen={stack[0]}
        while stack:
            for w in link_graph[stack.pop()]:
                if w not in seen:seen.add(w);stack.append(w)
        assert seen==verts
        orientable,bad,_=orientability(triples)
        assert not orientable and bad is not None
        # Closed connected surface: Euler 0 and nonorientable -> Klein bottle.
        summaries.append((v,14,42,28,'nonorientable'))
    return summaries


def check_edge_links(F):
    # In a normal 3-pseudomanifold every 1-simplex has a connected circle link.
    for edge in F[2]:
        a,b=edge
        vertices=set(w for tri in F[3] if a in tri and b in tri
                     for w in tri if w not in edge)
        link_edges=set(tuple(w for w in tet if w not in edge)
                       for tet in F[4] if a in tet and b in tet)
        assert len(vertices)==6 and len(link_edges)==6
        adjacency=defaultdict(set)
        for x,y in link_edges:adjacency[x].add(y);adjacency[y].add(x)
        assert all(len(adj)==2 for adj in adjacency.values())
        seen={min(vertices)};todo=list(seen)
        while todo:
            for w in adjacency[todo.pop()]:
                if w not in seen:seen.add(w);todo.append(w)
        assert seen==vertices


def integral_h1_unit_elimination(F):
    # The integral 1-cycle lattice has the non-tree edges as coordinates.
    # Quotient by boundaries of all triangles; integral unit pivots give
    # a complete unimodular presentation reduction, proving H_1=0.
    # Deterministic spanning tree rooted at zero.
    parent={0:None};todo=deque([0])
    while todo:
        u=todo.popleft()
        for v in NEIGHBORS[u]:
            if v not in parent:parent[v]=u;todo.append(v)
    assert len(parent)==P
    tree={tuple(sorted((u,v))) for v,u in parent.items() if u is not None}
    residual_rows=set(F[2])-tree
    assert len(tree)==28 and len(residual_rows)==175
    columns=[]
    for a,b,c in F[3]:
        columns.append({e:coeff for e,coeff in
                        [((a,b),1),((a,c),-1),((b,c),1)]
                        if e not in tree})
    row={r:{} for r in residual_rows}
    col=[dict(c) for c in columns]
    for j,c in enumerate(col):
        for r,v in c.items():row[r][j]=v
    pivot_count=0
    while residual_rows:
        options=((len(row[r])*len(col[j]),r,j,v)
                 for r in residual_rows for j,v in row[r].items()
                 if abs(v)==1)
        try:_,r,j,a=min(options)
        except ValueError:break
        assert a in (-1,1)
        for s,v in list(col[j].items()):
            if s==r:continue
            multiplier=v*a
            for k,x in list(row[r].items()):
                nv=row[s].get(k,0)-multiplier*x
                if nv==0:
                    row[s].pop(k,None);col[k].pop(s,None)
                else:
                    row[s][k]=nv;col[k][s]=nv
        assert set(col[j])=={r}
        for k in list(row[r]):col[k].pop(r)
        del row[r];residual_rows.remove(r);col[j].clear()
        pivot_count+=1
    assert pivot_count==175 and not residual_rows
    return pivot_count


def mod2_boundary_ranks(F):
    # Independent rank reduction over F_2 using bit-packed oriented faces.
    ranks={}
    for k in (2,3,4):
        lower={face:i for i,face in enumerate(F[k-1])}
        pivots={}
        for simplex in F[k]:
            column=0
            for face in combinations(simplex,k-1):
                column ^= 1 << lower[face]
            while column:
                highest=column.bit_length()-1
                if highest in pivots:column ^=pivots[highest]
                else:pivots[highest]=column;break
        ranks[k-1]=len(pivots)
    assert (ranks[1],ranks[2],ranks[3])==(28,175,202)
    return ranks


def main():
    assert len(RESIDUES)==14 and len(EDGES)==203
    # Strong regularity implies diameter exactly two.
    assert all(v in NEIGHBORS[u] or any(w in NEIGHBORS[v] for w in NEIGHBORS[u])
               for u in VERTICES for v in VERTICES if u!=v)
    F=cliques()
    assert all(sum(w in NEIGHBORS[v] for w in NEIGHBORS[u]
                   if w!=u and w!=v)==(6 if v in NEIGHBORS[u] else 7)
               for u in VERTICES for v in VERTICES if u!=v)
    triangle_tetra=Counter(face for tet in F[4]
                           for face in combinations(tet,3))
    assert len(triangle_tetra)==406 and set(triangle_tetra.values())=={2}
    orientable,conflict,_=orientability(F[4])
    assert not orientable and conflict is not None
    links=check_links(F)
    check_edge_links(F)
    pivots=integral_h1_unit_elimination(F)
    ranks=mod2_boundary_ranks(F)
    # Thus f=(29,203,406,203), a connected nonorientable normal
    # 3-pseudomanifold. Connected unbalanced signed dual incidence has
    # Smith factors 1^202, 2. Its boundary transpose is a signed-graph
    # incidence matrix; a dual spanning tree gives 202 unit factors, while
    # a frustrated cycle gives the final 2. Hence H3=0 and tors H2=Z/2.
    # H1=0 from 175 unimodular ∂2 pivots. Euler=29 gives rank H2=28.
    euler=29-203+406-203
    assert euler==29
    print('VERIFY_OK vertices=29 edges=203 triangles=406 tetrahedra=203 '
          'triangle_degrees=2 dual_connected=yes dual_nonorientable=yes '
          'vertex_links=29_Klein_bottles edge_links=203_C6 '
          'unit_d2_pivots=%d mod2_ranks=(%d,%d,%d) H0=Z H1=0 H2=Z^28+Z/2 H3=0' % (pivots,ranks[1],ranks[2],ranks[3]))
    print('NONORIENTABLE_DUAL_CONFLICT',conflict)


if __name__=='__main__':
    main()
