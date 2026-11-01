#!/usr/bin/env python3
"""Exact finite checks for the graph-metric Rips filtration of the McGee graph.

Requires Python 3 and networkx. The general topological arguments are in RESULT.md.
"""
from collections import Counter
from itertools import combinations, product
from math import prod
import networkx as nx

N = 24
G = nx.cycle_graph(N)
for i in range(N):
    shift = (12, 7, -7)[i % 3]
    G.add_edge(i, (i + shift) % N)
assert G.number_of_edges() == 36
assert sorted(dict(G.degree()).values()) == [3] * N
assert nx.is_connected(G)
D = dict(nx.all_pairs_shortest_path_length(G))
assert max(max(row.values()) for row in D.values()) == 4
hist = Counter(D[i][j] for i in range(N) for j in range(i + 1, N))
assert hist == {1: 36, 2: 72, 3: 144, 4: 24}, hist
# Verify shortest cycle length independently using shortest routes after removing an edge.
minimum_cycle_length = min(nx.shortest_path_length(nx.Graph([(a,b) for a,b in G.edges() if {a,b}!={u,v}]),u,v)+1 for u,v in G.edges())
assert minimum_cycle_length == 7

# Radius two: enumerate every simplex from the power graph and construct
# an explicitly valid sequence of elementary simplicial collapses.
power2 = nx.Graph()
power2.add_nodes_from(G)
power2.add_edges_from((i,j) for i in range(N) for j in range(i+1,N) if D[i][j] <= 2)
max_cliques = [frozenset(s) for s in nx.find_cliques(power2)]
assert len(max_cliques) == 24 and all(len(s)==4 for s in max_cliques)
assert set(max_cliques) == {frozenset([v]+list(G.neighbors(v))) for v in G.nodes()}
faces=set()
for simplex in max_cliques:
    for k in range(1,len(simplex)+1):
        faces.update(frozenset(x) for x in combinations(simplex,k))
assert Counter(len(x) for x in faces) == {1:24,2:108,3:96,4:24}
initial_faces = len(faces)

def elementary_collapse(facet, free_face):
    assert facet in faces and free_face in faces
    assert len(free_face)+1 == len(facet), (facet,free_face)
    assert sum(free_face.issubset(s) for s in faces if len(s)==len(facet)) == 1, (facet,free_face)
    # A free face also must lie in no higher-dimensional coface.
    assert sum(free_face.issubset(s) for s in faces if len(s)>len(facet)) == 0
    faces.remove(facet)
    faces.remove(free_face)

for v in range(N):
    hood=sorted(G.neighbors(v))
    elementary_collapse(frozenset([v]+hood),frozenset(hood))
    for a,b in combinations(hood,2):
        elementary_collapse(frozenset([v,a,b]),frozenset([a,b]))
remaining={frozenset([i]) for i in G.nodes()} | {frozenset(e) for e in G.edges()}
assert faces==remaining and initial_faces -len(faces) == 192

# Radius three: graph of omitted edges is six pairwise disjoint four-cycles.
H=nx.Graph()
H.add_nodes_from(range(N))
H.add_edges_from((i,j) for i in range(N) for j in range(i+1,N) if D[i][j]==4)
components=sorted((tuple(sorted(c)) for c in nx.connected_components(H)))
assert len(components)==6 and all(len(c)==4 for c in components)
assert all(nx.is_isomorphic(H.subgraph(c),nx.cycle_graph(4)) for c in components)
assert all(H.degree(i)==2 for i in range(N))
assert components == [(0,6,12,18),(1,5,13,17),(2,10,14,22),
                      (3,9,15,21),(4,8,16,20),(7,11,19,23)]

# Each cycle has two bipartition classes of size 2.  They give the two
# vertices in the equivariant S^0 deformation retract of Ind(C4).
classes=[]
for comp in components:
    color=nx.bipartite.color(H.subgraph(comp))
    blocks=sorted(tuple(sorted(x for x in comp if color[x]==bit)) for bit in [0,1])
    assert len(blocks)==2 and all(len(b)==2 for b in blocks)
    classes.append(tuple(blocks))
assert prod([3]*6)==729 # face count (including empty) after S^0 retraction
polynomial=[1]
for _ in range(6):
    p=[0]*(len(polynomial)+2)
    for i,c in enumerate(polynomial):
        for j,a in enumerate((1,4,2)):
            p[i+j]+=c*a
    polynomial=p
assert polynomial[1:]==[24,252,1520,5820,14784,25376,29568,23280,12160,4032,768,64],polynomial
assert sum(polynomial)-1==117648

# Compute the action on the 12 bipartition classes and check the
# resulting orientation determinant against the complete reduced
# simplicial Lefschetz alternating trace of the cross-polytope sphere.
representatives=[block for pair in classes for block in pair]
index={frozenset(b):i for i,b in enumerate(representatives)}
assert len(index)==12

def permutation_sign(seq):
    inversions=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return (-1)**(inversions%2)

# Faces of join of six copies S^0: at most one point per pair.
small_faces=[]
for choices in product((-1,0,1), repeat=6):
    f=tuple(2*j+choice for j,choice in enumerate(choices) if choice>=0)
    if f: small_faces.append(f)
assert len(small_faces)==728

au=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(au)==32
character_counts=Counter()
for phi in au:
    rho=[index[frozenset(phi[x] for x in block)] for block in representatives]
    assert sorted(rho)==list(range(12))
    perm_pairs=[rho[2*j]//2 for j in range(6)]
    assert perm_pairs == [rho[2*j+1]//2 for j in range(6)]
    assert sorted(perm_pairs)==list(range(6))
    swaps=sum((rho[2*j]%2)==1 for j in range(6))
    determinant=permutation_sign(perm_pairs)*(-1)**swaps
    # independent signed simplicial Lefschetz trace, on actual face action
    alternating_trace=-1 # reduced augmentation correction
    for face in small_faces:
        mapped=[rho[i] for i in face]
        if set(mapped)!=set(face):continue
        reordered=[sorted(mapped).index(v) for v in mapped]
        signed_trace=permutation_sign(reordered)
        alternating_trace += ((-1)**(len(face)-1))*signed_trace
    assert alternating_trace==-determinant, (phi,alternating_trace,determinant)
    character_counts[determinant]+=1
assert character_counts=={1:16,-1:16}
r={i:(i+3)%N for i in range(N)}
assert any(r==phi for phi in au)

def character_of(phi):
    rho=[index[frozenset(phi[x] for x in block)] for block in representatives]
    return permutation_sign([rho[2*j]//2 for j in range(6)])*(-1)**sum(rho[2*j]%2 for j in range(6))
assert character_of(r)==-1
half={i:(i+12)%N for i in range(N)}
assert character_of(half)==1

print('MCGEE_RIPS_CERTIFICATE_OK')
print('vertices=24 edges=36 girth=7 diameter=4 distance_pairs='+repr(dict(sorted(hist.items()))))
print('radius2_f=(24,108,96,24) elementary_collapse_pairs=96 remainder_edges=36')
print('radius3_distance4_components='+repr(components))
print('radius3_faces=117648 homotopy=S5; rips_barcodes=(H0:23[0,1),H1:13[1,3),H5:1[3,4))')
print('automorphisms=32 orientation_preserving=16 orientation_reversing=16')
print('signed_simplicial_Lefschetz_checks=32 generator_shift3=-1 halfturn=+1')
