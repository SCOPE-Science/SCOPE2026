#!/usr/bin/env python3
"""Exact finite-chain verification for Franklin graph scale-two Rips octahedron lattices.

Run: python verify_franklin.py
Dependencies: networkx >= 3.0; sympy >= 1.12.
All cellular coefficients and determinants are integers; modular ranks provide exact lower bounds.
"""
from itertools import combinations, product
from collections import Counter
from math import gcd
import networkx as nx
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V = tuple(range(12))
G = nx.cycle_graph(12)
for v in V:
    G.add_edge(v, (v+(5 if v%2==0 else -5))%12)
assert G.number_of_edges() == 18 and nx.is_bipartite(G)
# Independent conventional labeling of the Franklin graph.
assert nx.is_isomorphic(G, nx.LCF_graph(12,[-5,-3,3,5],3))
auto = list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(auto) == 48
D = dict(nx.all_pairs_shortest_path_length(G))
assert max(D[u][v] for u in V for v in V) == 3
R = nx.Graph()
R.add_nodes_from(V)
R.add_edges_from((u,v) for u,v in combinations(V,2) if D[u][v] <= 2)
# At threshold two, the missing edges are precisely distance-three pairs.
H = nx.Graph()
H.add_nodes_from(V)
H.add_edges_from((u,v) for u,v in combinations(V,2) if D[u][v] == 3)
assert nx.is_isomorphic(H,G)
F = {tuple(sorted(face)) for clique in nx.find_cliques(R)
     for k in range(1,len(clique)+1) for face in combinations(clique,k)}
faces = {k: sorted(f for f in F if len(f)==k+1) for k in range(6)}
assert tuple(len(faces[k]) for k in range(6)) == (12,48,76,45,12,2)
c2 = faces[2]
index2 = {f:i for i,f in enumerate(c2)}
index1 = {f:i for i,f in enumerate(faces[1])}

def boundary(simplex, index):
    out = [0]*len(index)
    for j in range(len(simplex)):
        out[index[simplex[:j]+simplex[j+1:]]] = (-1)**j
    return out

def modrank(cols, p):
    basis = {}
    for col in cols:
        x = {i: v%p for i,v in enumerate(col) if v%p}
        while x:
            k = min(x)
            if k not in basis:
                basis[k] = x
                break
            b = basis[k]
            t = x[k]*pow(b[k],-1,p)%p
            for i,v in b.items():
                z = (x.get(i,0)-t*v)%p
                if z:x[i] = z
                else:x.pop(i,None)
    return len(basis)

D2 = [boundary(s,index1) for s in c2]
D3 = [boundary(s,index2) for s in faces[3]]
assert modrank(D2,101) == 37
assert modrank(D3,101) == 35
for s in faces[3]:
    bd = boundary(s,index2)
    # signed boundary of boundary = zero
    assert all(sum(bd[j]*D2[j][i] for j in range(len(c2))) == 0
               for i in range(len(index1)))

def sign_order(triple):
    return -1 if sum(triple[i]>triple[j] for i in range(3) for j in range(i+1,3))%2 else 1

def octahedron(verts):
    missing = sorted((u,v) for u,v in combinations(verts,2) if not R.has_edge(u,v))
    if len(missing)!=3 or len({x for e in missing for x in e})!=6:
        return None
    x = [0]*len(c2)
    for choice in product((0,1),repeat=3):
        triple = tuple(missing[i][choice[i]] for i in range(3))
        sgn = sign_order(triple)
        for j in range(3): sgn *= (1 if choice[j] else -1)
        x[index2[tuple(sorted(triple))]] = sgn
    assert any(x)
    assert all(sum(x[j]*D2[j][i] for j in range(len(c2)))==0
               for i in range(len(index1)))
    return x

Oct = [(verts, z) for verts in combinations(V,6)
       if (z:=octahedron(verts)) is not None]
assert len(Oct)==20

# Choose exactly 35 independent third boundaries and four independent octahedral cycles
# by a deterministic mod-two pivot calculation; the integral certificate follows.
def add_bit_column(col, pivots):
    bits = sum(1<<i for i,c in enumerate(col) if c&1)
    while bits:
        key = bits.bit_length()-1
        if key not in pivots:
            pivots[key]=bits
            return True
        bits ^= pivots[key]
    return False
pivots={}
chosen_bd=[j for j,col in enumerate(D3) if add_bit_column(col,pivots)]
chosen_oct=[j for j,(_,col) in enumerate(Oct) if add_bit_column(col,pivots)]
assert len(chosen_bd)==35 and chosen_oct==[0,1,2,4]
columns=[D3[j] for j in chosen_bd]+[Oct[j][1] for j in chosen_oct]
assert len(columns)==39

# A direct unimodular minor certificate in the original C_2 basis.
residual=[[col[i] for col in columns] for i in range(len(c2))]
rows=[]
for k in range(39):
    candidates=[i for i in range(len(c2)) if i not in rows and abs(residual[i][k])==1]
    assert candidates, ('no integral unit pivot',k)
    i=candidates[0]; a=residual[i][k]; rows.append(i)
    for h in range(len(c2)):
        if h==i or h in rows: continue
        factor=residual[h][k]*a
        if factor:
            residual[h][k:]=[z-factor*w for z,w in zip(residual[h][k:],residual[i][k:])]
M=Matrix([[columns[j][i] for j in range(39)] for i in rows])
assert M.det()==-1
Minv=M.inv()
# Every third boundary is in the 35-column integral boundary lattice;
# this also proves rank(d_3) <= 35, not merely a modular lower bound.
for col in D3:
    x=Minv*Matrix([col[i] for i in rows])
    assert all(z.q==1 for z in x)
    assert all(x[j]==0 for j in range(35,39))
    assert all(sum(int(x[j])*columns[j][i] for j in range(35))==col[i]
               for i in range(len(c2)))
coords={}
for verts,col in Oct:
    x=Minv*Matrix([col[i] for i in rows])
    assert all(z.q==1 for z in x)
    assert all(sum(int(x[j])*columns[j][i] for j in range(39))==col[i]
               for i in range(len(c2)))
    v=tuple(map(int,x[-4:]))
    assert gcd(*v)==1
    coords[verts]=v
assert len(coords)==20

remaining=set(coords);orbits=[]
while remaining:
    rep=min(remaining)
    orbit={tuple(sorted(p[x] for x in rep)) for p in auto}
    assert orbit <= set(coords)
    orbits.append((rep,orbit))
    remaining-=orbit
orbits.sort(key=lambda x:len(x[1]))
assert [len(o) for _,o in orbits]==[8,12]
orb8=orbits[0][1];orb12=orbits[1][1]
A8=Matrix([coords[s] for s in sorted(orb8)]).T
A12=Matrix([coords[s] for s in sorted(orb12)]).T
snf8=[abs(int(d)) for d in smith_normal_form(A8,domain=ZZ).diagonal() if d]
snf12=[abs(int(d)) for d in smith_normal_form(A12,domain=ZZ).diagonal() if d]
assert snf8==[1,1,1,1] and snf12==[1,1,1]
for v in orb12:assert -coords[v][0]-coords[v][1]+coords[v][3]==0
for v in orb8:assert abs(-coords[v][0]-coords[v][1]+coords[v][3])==1
assert len([v for v in orb8 if abs(-coords[v][0]-coords[v][1]+coords[v][3])==1])==8

# All nontrivial 2-homology on six vertices in a flag complex must be an
# induced octahedron: flag lower-bound/equality lemma (proved in RESULT.md).
# Independently check the mod-two census of every induced subset of size <=6.
for k in range(0,7):
    nnonzero=0
    for W in combinations(V,k):
        Wset=set(W)
        e1=[f for f in faces[1] if set(f)<=Wset]
        e2=[f for f in faces[2] if set(f)<=Wset]
        e3=[f for f in faces[3] if set(f)<=Wset]
        if not e2:continue
        j1={f:i for i,f in enumerate(e1)}
        j2={f:i for i,f in enumerate(e2)}
        d2=[boundary(f,j1) for f in e2]
        d3=[boundary(f,j2) for f in e3]
        b2=len(e2)-modrank(d2,2)-modrank(d3,2)
        if b2:
            assert k==6 and W in coords and b2==1
            nnonzero+=1
    assert nnonzero == (20 if k==6 else 0), (k,nnonzero)

print('VERIFY_OK_FRANKLIN_OCTAHEDRAL_ORBIT_LATTICE')
print('GRAPH_V_E 12 18; AUT_ORDER 48; DIAMETER 3')
print('RIPS2_FACE_VECTOR 12 48 76 45 12 2')
print('BOUNDARY_RANKS_MOD101 D2=37 D3=35')
print('OCTAHEDRAL_MINIMAL_SUPPORTS 20; SIX_SUBSETS_TESTED 924')
print('BOUNDARY_COLUMNS',chosen_bd)
print('UNIT_MINOR_ROWS',rows)
print('UNIT_MINOR_DETERMINANT -1')
print('H2_INTEGRAL Z^4')
print('ORBIT8_REP',min(orb8),'LATTICE_SNF',snf8)
print('ORBIT12_REP',min(orb12),'LATTICE_SNF',snf12)
print('ORBIT12_ANNIHILATOR [-1,-1,0,1]')
print('EXPLICIT_OCTAHEDRAL_BASIS', [Oct[j][0] for j in chosen_oct])
