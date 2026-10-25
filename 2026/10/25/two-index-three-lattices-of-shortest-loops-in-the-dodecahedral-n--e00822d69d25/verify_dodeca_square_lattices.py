#!/usr/bin/env python3
"""Exact finite computation for two systolic orbit lattices in the dodecahedral neighborhood complex.

Requires networkx and sympy; see requirements.txt. No network access.
"""
from itertools import combinations, permutations
from collections import Counter, deque
import networkx as nx
import sympy as sp


def edges_and_graph():
    edge_set = set()
    for i in range(10):
        edge_set.add(tuple(sorted((i, (i + 1) % 10))))
        edge_set.add((i, i + 10))
        edge_set.add(tuple(sorted((10 + i, 10 + (i + 2) % 10))))
    assert len(edge_set) == 30
    g = nx.Graph()
    g.add_nodes_from(range(20))
    g.add_edges_from(sorted(edge_set))
    assert all(g.degree(v) == 3 for v in g)
    return g


def canonical_square_edges(v):
    # Of the three possible unoriented four-cycles on four given vertices,
    # include those with all four edges in the neighborhood one-skeleton.
    a, b, c, d = v
    return ((a,b,c,d), (a,b,d,c), (a,c,b,d))


def shortest_cycles(k):
    candidates = []
    for vv in combinations(range(20),4):
        for tup in canonical_square_edges(vv):
            if all(k.has_edge(tup[i],tup[(i+1)%4]) for i in range(4)):
                # Choose canonical orientation/starting point, among cyclic shifts and reversals.
                opts=[]
                for seq in (tup,tup[::-1]):
                    for s in range(4):opts.append(seq[s:]+seq[:s])
                candidates.append(min(opts))
    assert len(candidates)==len(set(candidates))
    return sorted(candidates)


def coordinate(cycle, cotree_index):
    out=[0]*len(cotree_index)
    for a,b in zip(cycle, cycle[1:]+cycle[:1]):
        edge=tuple(sorted((a,b)))
        if edge in cotree_index:
            out[cotree_index[edge]] += 1 if a<b else -1
    return sp.Matrix(out)


def p_rank(A,p):
    # Completely independent modular row elimination.
    arr=[[int(A[i,j])%p for j in range(A.cols)] for i in range(A.rows)]
    m,n=A.rows,A.cols
    rank=0
    for j in range(n):
        i=next((i for i in range(rank,m) if arr[i][j]),None)
        if i is None:continue
        arr[rank],arr[i]=arr[i],arr[rank]
        v=pow(arr[rank][j],-1,p)
        arr[rank]=[v*x%p for x in arr[rank]]
        for i in range(rank+1,m):
            v=arr[i][j]
            if v:arr[i]=[(a-v*b)%p for a,b in zip(arr[i],arr[rank])]
        rank+=1
        if rank==m:break
    return rank


def run():
    g=edges_and_graph()
    faces=sorted({tuple(sorted(g.neighbors(v))) for v in g})
    assert len(faces)==20
    edges=sorted({tuple(sorted(e)) for f in faces for e in combinations(f,2)})
    assert len(edges)==60
    multiplicity=Counter(tuple(sorted(e)) for f in faces for e in combinations(f,2))
    assert all(x==1 for x in multiplicity.values())
    k=nx.Graph();k.add_nodes_from(range(20));k.add_edges_from(edges)
    assert nx.is_connected(k)
    assert len([v for v in combinations(range(20),3) if all(k.has_edge(*e) for e in combinations(v,2))])==20
    # Every three-edge loop is therefore filled; four-edge squares are the shortest essential loops.
    squares=shortest_cycles(k)
    assert len(squares)==60
    assert len({frozenset(c) for c in squares})==60
    assert all(not k.has_edge(c[0],c[2]) and not k.has_edge(c[1],c[3]) for c in squares)
    orb1=[j for j,c in enumerate(squares) if g.subgraph(c).number_of_edges()==1]
    orb0=[j for j,c in enumerate(squares) if g.subgraph(c).number_of_edges()==0]
    assert len(orb0)==len(orb1)==30
    assert set(orb0+orb1)==set(range(60))
    autos=list(nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter())
    assert len(autos)==120
    def edge_signature(c):return frozenset(tuple(sorted((c[i],c[(i+1)%4]))) for i in range(4))
    sigs={edge_signature(c):i for i,c in enumerate(squares)}
    for ids in (orb1,orb0):
        orbit={sigs[frozenset(tuple(sorted((perm[a],perm[b]))) for a,b in edge_signature(squares[ids[0]]))] for perm in autos}
        assert orbit==set(ids)
    # Deterministic BFS spanning tree of the neighborhood one-skeleton.
    vis={0};dq=deque([0]);tree=set()
    while dq:
        v=dq.popleft()
        for w in sorted(k.neighbors(v)):
            if w not in vis:
                vis.add(w);dq.append(w);tree.add(tuple(sorted((v,w))))
    assert len(tree)==19
    cotree=[e for e in edges if e not in tree]
    assert len(cotree)==41
    cx={e:i for i,e in enumerate(cotree)}
    tris=sp.Matrix.hstack(*[coordinate(list(f),cx) for f in faces])
    square_matrix=sp.Matrix.hstack(*[coordinate(list(s),cx) for s in squares])
    piv=list(tris.T.rref()[1]);free=[i for i in range(41) if i not in piv]
    assert len(piv)==20 and len(free)==21
    pivot_det=int(tris[piv,:].det(method='domain-ge'))
    assert abs(pivot_det)==1
    projection=square_matrix[free,:]-tris[free,:]*tris[piv,:].inv()*square_matrix[piv,:]
    assert all(v.q==1 for v in projection)
    # The integer projection realizes integral H_1=Z^21 exactly.
    chosen=[]
    for ids in (orb1,orb0):
        mat=projection[:,ids]
        cols=list(mat.rref()[1]);assert len(cols)==21
        d=int(mat[:,cols].det(method='domain-ge'))
        assert abs(d)==3
        assert p_rank(mat,3)==20
        assert p_rank(mat,101)==21
        chosen.append([ids[j] for j in cols])
    # A concrete twenty-from-one-orbit plus one-from-the-other integral basis.
    base=chosen[0]
    replacement=None
    for j in range(21):
        for new in orb0:
            test=base[:];test[j]=new
            dd=int(projection[:,test].det(method='domain-ge'))
            if abs(dd)==1:
                replacement=(j,new,dd,test)
                break
        if replacement:break
    assert replacement is not None
    # Symmetrically, the second orbit admits a 20+1 integral basis.
    base2=chosen[1];replacement2=None
    for j in range(21):
        for new in orb1:
            test=base2[:];test[j]=new
            dd=int(projection[:,test].det(method='domain-ge'))
            if abs(dd)==1:
                replacement2=(j,new,dd,test);break
        if replacement2:break
    assert replacement2 is not None
    # Both 30-element orbits have index three; any single square from other orbit
    # completes generation by transitivity and the full symmetry invariance of the lattice.
    print('VERIFY_OK_DODECAHEDRAL_TWO_SQUARE_ORBITS_INDEX_THREE')
    print('F_VECTOR',20,60,20,'AUTOMORPHISMS',len(autos))
    print('FOUR_CYCLE_TOTAL',60,'ORBIT_ONE_EDGE',len(orb1),'ORBIT_ZERO_EDGE',len(orb0))
    print('REP_ONE_EDGE',squares[orb1[0]],'REP_ZERO_EDGE',squares[orb0[0]])
    print('H1_RANK',len(free),'PIVOT_DET',pivot_det,'PIVOT_ROWS',piv)
    for n,base in enumerate(chosen):
        mat=projection[:,base]
        print('ORBIT',n,'SELECTED_GLOBAL_SQUARES',base,'MINOR',int(mat.det(method='domain-ge')),
              'MOD3_RANK',p_rank(projection[:,orb1 if n==0 else orb0],3))
    print('MIXED_BASIS_0',replacement[3],'DET',replacement[2])
    print('MIXED_BASIS_1',replacement2[3],'DET',replacement2[2])
    print('COTREE_EDGE_LIST',cotree)
    print('H1_QUOTIENT_EACH_ORBIT_Z3; FULL_SQUARE_LATTICE_Z21')

if __name__=='__main__':run()
