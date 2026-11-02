"""Independent finite reconstruction of the Sylvester-graph distance algebra.

Requires NetworkX >=3 and NumPy >=1.24. Uses NetworkX's classical
Hoffman--Singleton graph only as a combinatorial input, not as a stored
negative-type or distance-spectrum table.
"""
import math
import networkx as nx
import numpy as np

H = nx.hoffman_singleton_graph()
assert H.number_of_nodes() == 50 and H.number_of_edges() == 175
edge = next(iter(H.edges()))
removed = set(edge)
for v in edge:
    removed.update(H.neighbors(v))
G = H.subgraph([v for v in H if v not in removed]).copy()
assert G.number_of_nodes() == 36 and G.number_of_edges() == 90
assert set(dict(G.degree()).values()) == {5}
vertices = sorted(G)
N = len(vertices)
shortest = dict(nx.all_pairs_shortest_path_length(G))
D = np.array([[shortest[v][u] for u in vertices] for v in vertices], dtype=int)
assert D.max() == 3 and np.array_equal(D,D.T)
assert all(tuple(int(np.sum(D[i]==j)) for j in range(4))==(1,5,20,10) for i in range(36))
A = (D==1).astype(np.int64)
I = np.eye(N,dtype=np.int64)
A2 = (D==2).astype(np.int64)
A3 = (D==3).astype(np.int64)
assert np.array_equal(A@A -5*I,A2)
assert np.array_equal(A@A@A-2*A@A-9*A+10*I,4*A3)
# Independently confirm the complete equitable distance intersection array.
for i in range(N):
    for j in range(N):
        h = int(D[i,j]); counts = [int(sum(D[i,k]==ell and A[j,k] for k in range(N))) for ell in range(4)]
        desired = [[0,5,0,0],[1,0,4,0],[0,1,2,2],[0,0,4,1]][h]
        assert counts == desired, (i,j,h,counts,desired)
vals=np.linalg.eigvalsh(A.astype(float))
assert np.allclose(vals,np.repeat([-3.,-1.,2.,5.],[9,10,16,1]),atol=2e-12)
root_low,root_high=0.0,1.0
for _ in range(90):
    mid=(root_low+root_high)/2
    if 3**mid-2**mid<0.25:root_low=mid
    else:root_high=mid
crit=(root_low+root_high)/2
assert abs(crit-0.421967970792407646)<1e-14
# Full 36-by-36 distance spectra, with multiplicities, at three test exponents.
for p in [0.0,0.3,crit,0.5,1.0]:
    T=(A.astype(float)+2**p*A2+3**p*A3)
    exact=[-3+4*2**p-2*3**p,-1-4*2**p+4*3**p,2-2**p-2*3**p,5+20*2**p+10*3**p]
    expected=np.repeat(exact,[9,10,16,1])
    assert np.allclose(np.sort(np.linalg.eigvalsh(T)),np.sort(expected),atol=2e-10)
    eigs=np.linalg.eigvalsh(T)
    if p<crit-1e-8: assert sum(eigs[:-1]>1e-9)==0
    if p>crit+1e-8: assert sum(eigs>1e-9)==11
# Identify the maximal cliques of the distance-three rook graph and recover
# six row/column coordinate classes. This independently certifies the geometric
# description of the ten-dimensional critical nullspace.
R = nx.from_numpy_array(A3)
cliques = [frozenset(C) for C in nx.find_cliques(R)]
assert len(cliques)==12 and all(len(C)==6 for C in cliques)
T = nx.Graph()
T.add_nodes_from(range(12))
for i in range(12):
    for j in range(i+1,12):
        if len(cliques[i]&cliques[j])==1: T.add_edge(i,j)
assert nx.is_bipartite(T)
rows,cols=nx.bipartite.sets(T)
rows,cols=sorted(rows),sorted(cols)
assert len(rows)==len(cols)==6 and T.number_of_edges()==36
coord=[]
for v in range(N):
    rr=[i for i,j in enumerate(rows) if v in cliques[j]]
    cc=[i for i,j in enumerate(cols) if v in cliques[j]]
    assert len(rr)==len(cc)==1
    coord.append((rr[0],cc[0]))
assert len(set(coord))==36
contrast=[]
for dim in (0,1):
    for i in range(5):
        f=np.array([int(x[dim]==i)-int(x[dim]==5) for x in coord], dtype=np.int64)
        assert np.array_equal(A@f,-f)
        assert np.array_equal(A2@f,-4*f)
        assert np.array_equal(A3@f,4*f)
        contrast.append(f)
assert np.linalg.matrix_rank(np.column_stack(contrast).astype(float))==10
# At the critical exponent, ten zero eigenvalues and 25 negative eigenvalues.
Z=A.astype(float)+2**crit*A2+3**crit*A3
z=np.linalg.eigvalsh(Z)
assert sum(abs(z)<1e-9)==10 and sum(z< -1e-8)==25 and sum(z>1e-8)==1
print('SYLVESTER_POWERED_DISTANCE_OK 36 vertices; 90 edges; 1296 intersection comparisons; 5 full powered-distance spectra; explicit rook-grid nullity 10')
