#!/usr/bin/env python3
"""Exact finite verification of the Euclidean Vietoris--Rips filtration on the 18 roots of type B3.

Uses only Python's standard library. Vertex coordinates, inclusive metric,
triangulated cuboctahedral boundary, and collapse pairs are regenerated or checked.
"""
from __future__ import annotations
import collections
import itertools
import json
from pathlib import Path

V=sorted(set(
    tuple(s if j==i else 0 for j in range(3))
    for i in range(3) for s in (-1,1)
) | {
    tuple(x) for x in itertools.product((-1,0,1), repeat=3)
    if sum(a!=0 for a in x)==2
})
assert len(V)==18
N=len(V)
SHORT={i for i,v in enumerate(V) if sum(c*c for c in v)==1}
LONG=set(range(N))-SHORT
assert len(SHORT)==6 and len(LONG)==12

def sqdist(i,j):
    return sum((a-b)*(a-b) for a,b in zip(V[i],V[j]))

def indices(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask^=bit

def subfaces(mask):
    s=mask
    while s:
        yield s
        s=(s-1)&mask

def rips_faces(threshold):
    adjacency=[sum(1<<j for j in range(N) if j!=i and sqdist(i,j)<=threshold)
               for i in range(N)]
    result=set()
    stack=[(0,(1<<N)-1)]
    while stack:
        mask,choices=stack.pop()
        if mask:
            assert mask not in result
            result.add(mask)
        while choices:
            bit=choices&-choices
            choices^=bit
            j=bit.bit_length()-1
            stack.append((mask|bit, choices&adjacency[j]))
    return result

def fvector(faces):
    return tuple(collections.Counter(s.bit_count()-1 for s in faces).get(k,0)
                 for k in range(max(s.bit_count() for s in faces)))

def boundary_facets():
    triangular=[]
    for abc in itertools.combinations(sorted(LONG),3):
        if all(sqdist(a,b)==2 for a,b in itertools.combinations(abc,2)):
            triangular.append(sum(1<<i for i in abc))
    assert len(triangular)==8
    square_fans=[]
    for i in sorted(SHORT):
        adjacent=[j for j in sorted(LONG) if sqdist(i,j)==1]
        assert len(adjacent)==4
        for j,k in itertools.combinations(adjacent,2):
            if sqdist(j,k)==2:
                square_fans.append((1<<i)|(1<<j)|(1<<k))
    assert len(square_fans)==24
    facets=set(triangular+square_fans)
    B={s for f in facets for s in subfaces(f)}
    assert len(facets)==32 and fvector(B)==(18,48,32)
    return facets,B

def verify_sphere(facets,B):
    edge_to_facets=collections.defaultdict(list)
    for tri in facets:
        for v in indices(tri):
            edge=tri^(1<<v)
            edge_to_facets[edge].append(tri)
    assert len(edge_to_facets)==48 and all(len(v)==2 for v in edge_to_facets.values())
    # Every vertex link is a single combinatorial cycle.
    for v in range(N):
        node_edges=[]
        for tri in facets:
            if tri>>v&1:
                other=list(indices(tri^(1<<v)))
                node_edges.append(tuple(other))
        graph=collections.defaultdict(set)
        for a,b in node_edges:
            graph[a].add(b);graph[b].add(a)
        assert graph and all(len(nei)==2 for nei in graph.values())
        reached={next(iter(graph))}
        while True:
            extended=reached|set().union(*(graph[z] for z in reached))
            if extended==reached:break
            reached=extended
        assert len(reached)==len(graph)
    # Check entire triangular-facet adjacency connected.
    seen={next(iter(facets))}
    while True:
        nxt=seen|{q for p in seen for edge in (p^(1<<v) for v in indices(p))
                  for q in edge_to_facets[edge]}
        if seen==nxt:break
        seen=nxt
    assert seen==facets
    assert sum((-1)**i*k for i,k in enumerate(fvector(B)))==2
    # Connected, closed triangulated surface with Euler characteristic 2 is S^2.

def verify_bridge_decomposition(K2,B):
    short_edges=set()
    bridges=set()
    for j in LONG:
        endpoints=[i for i in sorted(SHORT) if sqdist(i,j)==1]
        assert len(endpoints)==2 and sqdist(*endpoints)==2
        a,b=endpoints
        edge=(1<<a)|(1<<b)
        short_edges.add(edge)
        bridges.add(edge|(1<<j))
    assert len(short_edges)==12 and len(bridges)==12
    Y=B|short_edges|bridges
    short_triangles={sum(1<<i for i in abc)
                     for abc in itertools.combinations(sorted(SHORT),3)
                     if all(sqdist(i,j)==2 for i,j in itertools.combinations(abc,2))}
    assert len(short_triangles)==8
    assert K2==(Y|short_triangles)
    # In Y every new short-to-short edge is free in its unique bridge triangle.
    for edge in short_edges:
        upper=[tri for tri in bridges if edge&tri==edge]
        assert len(upper)==1 and edge not in B
    return Y,short_triangles

def replay_relative_collapses(K3,B,certificate):
    working=set(K3)
    for a,b in certificate:
        assert isinstance(a,int) and isinstance(b,int)
        assert a in working and b in working and a not in B and b not in B
        assert (b^a).bit_count()==1 and a&b==a
        assert len([a|(1<<v) for v in range(N)
                    if not(a>>v&1) and (a|(1<<v)) in working])==1
        working.remove(a); working.remove(b)
    assert working==B
    return len(certificate)

def greedy_morse(F):
    remaining=set(F)
    pairs=[]
    for v in range(N):
        bit=1<<v
        # Sequential toggles; no face is used in more than one pair.
        for a in sorted(remaining):
            b=a|bit
            if not a&bit and a in remaining and b in remaining:
                remaining.remove(a);remaining.remove(b)
                pairs.append((a,b))
    assert 2*len(pairs)+len(remaining)==len(F)
    assert all(b.bit_count()==a.bit_count()+1 and ((b^a) & ((b^a)-1))==0
               for a,b in pairs)
    return pairs,remaining

def verify_acyclic(F,pairs):
    # Directed Hasse graph: matched edges lower->upper; other edges upper->lower.
    nodes=sorted(F)
    index={mask:i for i,mask in enumerate(nodes)}
    indegree=[0]*len(nodes)
    adjacency=[[] for _ in nodes]
    matching={(a,b) for a,b in pairs}
    hasse=0
    for b in nodes:
        if b.bit_count()==1: continue
        for v in indices(b):
            a=b^(1<<v)
            if (a,b) in matching:
                src,dst=index[a],index[b]
            else:
                src,dst=index[b],index[a]
            adjacency[src].append(dst)
            indegree[dst]+=1
            hasse+=1
    pending=collections.deque(i for i,d in enumerate(indegree) if d==0)
    visited=0
    while pending:
        src=pending.popleft();visited+=1
        for dst in adjacency[src]:
            indegree[dst]-=1
            if indegree[dst]==0:pending.append(dst)
    assert visited==len(F),f'directed cycle: {visited}/{len(F)}'
    return hasse

def rank_mod2(boundary_columns):
    pivots={}
    for c in boundary_columns:
        while c:
            i=c.bit_length()-1
            if i in pivots:c^=pivots[i]
            else:
                pivots[i]=c
                break
    return len(pivots)

def mod2_betti(F):
    bydim=collections.defaultdict(list)
    for s in F:
        bydim[s.bit_count()-1].append(s)
    for l in bydim.values():l.sort()
    maxdim=max(bydim)
    ranks={0:0}
    for k in range(1,maxdim+1):
        row={s:i for i,s in enumerate(bydim[k-1])}
        cols=[]
        for b in bydim[k]:
            col=sum(1<<row[b^(1<<i)] for i in indices(b))
            cols.append(col)
        ranks[k]=rank_mod2(cols)
    ranks[maxdim+1]=0
    betti=[len(bydim[k])-ranks[k]-ranks[k+1] for k in range(maxdim+1)]
    return tuple(betti)

def main():
    distance_counts=collections.Counter(sqdist(i,j) for i in range(N) for j in range(i+1,N))
    assert dict(sorted(distance_counts.items()))=={1:24,2:36,3:24,4:15,5:24,6:24,8:6}
    print('roots=18; distance_sq_pairs='+json.dumps(dict(sorted(distance_counts.items()))))
    stages={t:rips_faces(t) for t in (0,1,2,3,4,5,6)}
    expected={0:(18,),1:(18,24),2:(18,60,52),3:(18,84,148,120,48,8),
              4:(18,99,232,249,108,9),
              5:(18,123,448,993,1422,1343,828,318,68,6),
              6:(18,147,720,2355,5418,8989,10836,9420,5760,2352,576,64)}
    for t,F in stages.items():
        assert fvector(F)==expected[t],(t,fvector(F))
        print('stage_sq='+str(t)+'; fvector='+str(fvector(F)))
    facets,B=boundary_facets()
    verify_sphere(facets,B)
    assert B<=stages[2]
    Y,short_triangles=verify_bridge_decomposition(stages[2],B)
    print('B_boundary_sphere=18,48,32; bridge_pairs=12; octahedron_triangles=8')
    assert stages[3]>=B
    certificate=json.loads((Path(__file__).parent/'collapse_to_boundary.json').read_text('utf8'))
    assert certificate['squared_threshold']==3
    assert [tuple(v) for v in certificate['vertex_order']]==V
    collapsed=replay_relative_collapses(stages[3],B,certificate['free_face_pairs'])
    assert collapsed==164
    print('relative_collapses_sq3='+str(collapsed)+'; residual=B')
    assert mod2_betti(stages[1])==(1,7)
    assert mod2_betti(stages[2])==(1,0,9)
    assert mod2_betti(stages[3])==(1,0,1,0,0,0)
    print('mod2_betti_sq1=(1,7); sq2=(1,0,9); sq3=(1,0,1,0,0,0)')
    for t in (4,5,6):
        F=stages[t]
        pairs,crit=greedy_morse(F)
        assert len(crit)==1 and next(iter(crit)).bit_count()==1
        incidences=verify_acyclic(F,pairs)
        print(f'sq{t}: {len(F)} faces, {len(pairs)} Morse pairs, one critical vertex, {incidences} verified Hasse incidences')
    assert rips_faces(8)==set(range(1,(1<<N)))
    print('sq8=full 18-simplex')
    print('VERIFY_OK')
if __name__=='__main__':main()
