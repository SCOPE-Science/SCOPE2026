"""Exact finite verification of Pappus point/edge graph-metric Rips homology characters.
Requires networkx==3.6.1. Run: python verify.py
"""
import collections
import itertools
import math
import networkx as nx

P = nx.pappus_graph()
assert P.number_of_nodes() == 18 and P.number_of_edges() == 27
assert nx.is_bipartite(P) and nx.is_connected(P)
assert all(d==3 for _,d in P.degree())
vertices = sorted(P.nodes())
edges = sorted(tuple(sorted(e)) for e in P.edges())
L = nx.line_graph(P)
assert set(L.nodes()) == set(edges)

def rips_faces(G, vertex_list, radius):
    distances = dict(nx.all_pairs_shortest_path_length(G))
    Q = nx.Graph()
    Q.add_nodes_from(vertex_list)
    Q.add_edges_from((a,b) for a,b in itertools.combinations(vertex_list,2)
                     if distances[a][b] <= radius)
    faces = [tuple(sorted(s)) for s in nx.enumerate_all_cliques(Q)]
    return faces

Pfaces = rips_faces(P,vertices,2)
Lfaces = rips_faces(L,edges,2)
assert tuple(sum(len(s)==k for s in Pfaces) for k in range(1,5)) == (18,81,108,18)
assert tuple(sum(len(s)==k for s in Lfaces) for k in range(1,6)) == (27,162,270,135,27)

def binary_ranks(faces):
    faces_by_size={k:sorted([s for s in faces if len(s)==k])
                   for k in range(1,max(map(len,faces))+1)}
    ranks={0:0,max(faces_by_size):0}
    for k in range(2,max(faces_by_size)+1):
        rowidx={f:i for i,f in enumerate(faces_by_size[k-1])}
        pivots={}
        for simplex in faces_by_size[k]:
            vector=0
            for j in range(k):
                vector ^= 1<<rowidx[simplex[:j]+simplex[j+1:]]
            while vector:
                pivot=vector.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot]=vector
                    break
                vector ^= pivots[pivot]
        ranks[k-1]=len(pivots)
    betti=[len(faces_by_size[k])-ranks[k-1]-ranks[k]
           for k in range(1,max(faces_by_size)+1)]
    return tuple(ranks[k] for k in range(1,max(faces_by_size))),tuple(betti)

rankP,bettiP=binary_ranks(Pfaces)
rankL,bettiL=binary_ranks(Lfaces)
assert rankP == (17,64,18), rankP
assert rankL == (26,136,108,27), rankL
assert bettiP == (1,0,26,0),bettiP
assert bettiL == (1,0,26,0,0),bettiL

color=nx.bipartite.color(P)
autos=list(nx.algorithms.isomorphism.GraphMatcher(P,P).isomorphisms_iter())
assert len(autos)==216

def permutation_order(mapping):
    seen=set(); n=1
    for v in vertices:
        if v in seen:continue
        x=v;length=0
        while x not in seen:
            seen.add(x);length+=1;x=mapping[x]
        n=math.lcm(n,length)
    return n

def reduced_Lefschetz(faces, action):
    total=-1
    for face in faces:
        transformed=tuple(action[v] for v in face)
        if set(transformed)!=set(face):continue
        inversions=sum(transformed[i]>transformed[j]
                       for i in range(len(face)) for j in range(i+1,len(face)))
        total += (-1)**(len(face)-1+inversions)
    return total

classes=collections.Counter()
for g in autos:
    ge={e:tuple(sorted((g[e[0]],g[e[1]]))) for e in edges}
    trP=reduced_Lefschetz(Pfaces,g)
    trL=reduced_Lefschetz(Lfaces,ge)
    key=(permutation_order(g),int(color[0]!=color[g[0]]),trP,trL)
    classes[key]+=1
expected={
 (1,0,26,26):1,
 (2,0,0,0):18,
 (2,0,-10,2):9,
 (2,1,2,-4):18,
 (3,0,2,2):12,
 (3,0,5,5):12,
 (3,0,-1,-1):2,
 (4,1,2,2):18,
 (6,0,0,0):36,
 (6,0,-1,-1):18,
 (6,1,-1,-1):36,
 (12,1,-1,-1):36,
}
assert dict(classes)==expected,(classes,expected)
assert sum(v for (o,d,a,b),v in classes.items() if a!=b)==27
print('PAPPUS: vertices=18, edges=27, automorphisms=216')
print('POINT_RIPS_FVECTOR (18,81,108,18), F2_BOUNDARY_RANKS',rankP,'F2_BETTIS',bettiP)
print('FLAG_RIPS_FVECTOR (27,162,270,135,27), F2_BOUNDARY_RANKS',rankL,'F2_BETTIS',bettiL)
print('CHARACTER_CLASSES: (order, swaps_bipartition, point_trace, flag_trace, count)')
for k,v in sorted(classes.items()):print((*k,v))
print('INEQUIVALENT_IN_27_AUTOMORPHISMS')
print('VERIFY_OK_PAPPUS_POINT_FLAG_RIPS_CHARACTERS')
