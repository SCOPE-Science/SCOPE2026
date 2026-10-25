"""Exact finite simplicial verification for the exceptional circulant manifold core.
Requires Python 3 and SymPy. No external data or services.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
import json

N = 16
STEPS = {1, 4, 8, 12, 15}
EDGES = {tuple(sorted((i, (i+s)%N))) for i in range(N) for s in STEPS}
assert len(EDGES) == 40

def independent(t):
    return all((u,v) not in EDGES for u,v in combinations(t,2))

faces = {k: [c for c in combinations(range(N),k) if independent(c)] for k in (1,2,3,4)}
assert {k:len(v) for k,v in faces.items()} == {1:16,2:80,3:144,4:80}
assert not any(independent(c) for c in combinations(range(N),5))
all_facets = set(faces[4])
removed = {tuple(sorted((i%N,(i+2)%N,(i+7)%N,(i+9)%N))) for i in range(N)}
assert len(removed) == 16 and removed <= all_facets
core_tetra = sorted(all_facets - removed)
core_tri = sorted({f for t in core_tetra for f in combinations(t,3)})
core_edges = sorted({e for t in core_tetra for e in combinations(t,2)})
assert (len(core_edges),len(core_tri),len(core_tetra)) == (80,128,64)
assert set(core_edges) == set(faces[2])

# The core is a closed combinatorial 3-manifold: every triangle is in two
# tetrahedra, and each vertex link is a combinatorial 2-sphere.
incidence = defaultdict(list)
for idx,t in enumerate(core_tetra):
    for omitted in range(4):
        f = t[:omitted]+t[omitted+1:]
        incidence[f].append((idx, (-1)**omitted))
assert len(incidence)==128 and all(len(x)==2 for x in incidence.values())

def connected_graph(vertices,edges):
    vset=set(vertices)
    assert vset
    seen={next(iter(vset))}
    while True:
        nxt=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
        if nxt==seen: return nxt==vset
        seen=nxt

link_vectors=[]
for v in range(N):
    tris={tuple(u for u in t if u!=v) for t in core_tetra if v in t}
    eds={e for f in tris for e in combinations(f,2)}
    verts={u for e in eds for u in e}
    edge_deg=Counter(e for tri in tris for e in combinations(tri,2))
    assert len(verts)==10 and len(eds)==24 and len(tris)==16
    assert all(c==2 for c in edge_deg.values())
    assert connected_graph(verts, eds)
    assert len(verts)-len(eds)+len(tris)==2
    link_vectors.append((len(verts),len(eds),len(tris)))

# Orientability: propagate the signed sum of the two induced orientations on
# each common triangle and check compatibility around all dual cycles.
neighbor = defaultdict(list)
for f,pair in incidence.items():
    (a,sa),(b,sb)=pair
    neighbor[a].append((b,-sa*sb))
    neighbor[b].append((a,-sa*sb))
orientation={0:1}; queue=deque([0])
while queue:
    i=queue.popleft()
    for j,rel in neighbor[i]:
        guess=orientation[i]*rel
        if j in orientation: continue
        else: orientation[j]=guess;queue.append(j)
assert len(orientation)==64
orientation_conflicts=sum(orientation[a]*sa+orientation[b]*sb!=0 for (a,sa),(b,sb) in incidence.values())
assert orientation_conflicts>0 # obstruction to a global orientation

# Exact signed integer boundary matrices; Smith diagonal gives torsion too.
def boundary(lower,upper):
    lid={f:i for i,f in enumerate(lower)}
    entries={}
    for j,face in enumerate(upper):
        for omit in range(len(face)):
            sub=face[:omit]+face[omit+1:]
            entries[lid[sub],j]=(-1)**omit
    return SparseMatrix(len(lower),len(upper),entries)

def smith_data(mat):
    D=smith_normal_form(mat,domain=ZZ)
    ds=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    return len(ds), Counter(ds)

M2=boundary(core_edges,core_tri)
M3=boundary(core_tri,core_tetra)
K2=boundary(faces[2],faces[3])
K3=boundary(faces[3],faces[4])
assert smith_data(M2)==(64,Counter({1:64}))
assert smith_data(M3)==(64,Counter({1:63,2:1}))
assert smith_data(K2)==(65,Counter({1:65}))
assert smith_data(K3)==(79,Counter({1:79}))

new_tri=sorted(set(faces[3])-set(core_tri))
assert len(new_tri)==16
R3=boundary(new_tri, sorted(removed)) if False else None
# Boundary in relative chain complex: throw away triangles already in core.
tri_i={f:i for i,f in enumerate(new_tri)}
rel_entries={}
for j,t in enumerate(sorted(removed)):
    for omit in range(4):
        f=t[:omit]+t[omit+1:]
        if f in tri_i:rel_entries[tri_i[f],j]=(-1)**omit
relative=SparseMatrix(16,16,rel_entries)
assert all(sum(1 for i in range(16) if relative[i,j])==2 for j in range(16))
assert all(sum(1 for j in range(16) if relative[i,j])==2 for i in range(16))
assert smith_data(relative)==(15,Counter({1:15}))
assert connected_graph(range(16),{(a,b) for row in range(16) for a,b in combinations([col for col in range(16) if relative[row,col]],2)})

# The primitive full 3-cycle has absolute coefficients one on core tetrahedra
# and two on the 16 removed tetrahedra. There are no 4-simplices.
import math
ker = K3.nullspace()
assert len(ker) == 1
den = math.lcm(*(entry.q for entry in ker[0]))
coeff = [int(entry*den) for entry in ker[0]]
gcd = math.gcd(*coeff)
coeff = [a//gcd for a in coeff]
assert K3*SparseMatrix(80,1,{(i,0):a for i,a in enumerate(coeff)}) == SparseMatrix(144,1,{})
assert Counter(abs(a) for i,a in enumerate(coeff) if faces[4][i] not in removed) == Counter({1:64})
assert Counter(abs(a) for i,a in enumerate(coeff) if faces[4][i] in removed) == Counter({2:16})
# The support of the unique nonzero mod-two 3-cycle is exactly the core.
assert sum(a%2 for a in coeff) == 64

result={
 'graph_vertices':16,'graph_edges':40,'all_faces':{str(k-1):len(v) for k,v in faces.items()},
 'core_faces':{'0':16,'1':80,'2':128,'3':64},
 'core_link_f_vector':list(link_vectors[0]),'all_vertex_links_spheres':True,
 'core_orientable':False,'orientation_obstruction_faces':orientation_conflicts,
 'core_smith_boundary2':{'rank':64,'nonzero_factors':{'1':64}},
 'core_smith_boundary3':{'rank':64,'nonzero_factors':{'1':63,'2':1}},
 'full_smith_boundary2':{'rank':65,'nonzero_factors':{'1':65}},
 'full_smith_boundary3':{'rank':79,'nonzero_factors':{'1':79}},
 'relative_new_triangles':16,'relative_removed_tetrahedra':16,
 'relative_smith_boundary3':{'rank':15,'nonzero_factors':{'1':15}},
 'relative_dual_cycle_connected':True,
 'core_homology':{'H0':'Z','H1':'Z','H2':'Z/2','H3':'0'},
 'full_integral_betti':[1,0,0,1],
 'full_top_cycle_abs_coefficients':{'core_tetrahedra':1,'belt_tetrahedra':2},
 'relative_H3_to_H2_core':'mod2', 'full_H3_to_relative_H3':'multiplication_by_2'
}
print(json.dumps(result,sort_keys=True,indent=2))
print('VERIFY_OK_EXCEPTIONAL_CIRCULANT_MANIFOLD_CORE')
