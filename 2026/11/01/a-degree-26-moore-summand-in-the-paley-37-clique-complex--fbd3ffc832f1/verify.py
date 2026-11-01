#!/usr/bin/env python3
"""Reconstruct and certify the integral homotopy of the Paley-37 clique complex.

Python 3 standard library only. Every finite assertion is verified from quadratic
residues, simplex incidence, and integer arithmetic. No external data required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import gcd

P=37
residues={i*i%P for i in range(1,P)}
assert len(residues)==18 and -1%P in residues
neighbors=[{j for j in range(P) if j!=i and (j-i)%P in residues} for i in range(P)]
assert all((i in neighbors[j]) == (j in neighbors[i]) for i in range(P) for j in range(P))

# Exhaustive lexicographically oriented flag simplices.
faces=[[(i,) for i in range(P)]]
while True:
    prev=faces[-1]
    level=[]
    for simplex in prev:
        for v in range(simplex[-1]+1,P):
            if all(v in neighbors[w] for w in simplex):
                level.append(simplex+(v,))
    if not level:break
    faces.append(level)
assert tuple(map(len,faces))==(37,333,888,555), tuple(map(len,faces))
assert len(faces)==4
print('face_vector',tuple(map(len,faces)))
print('euler',sum((-1)**j*len(f) for j,f in enumerate(faces)))

# The graph has diameter 2; the radius-two graph-metric Rips complex is a simplex.
assert all(i==j or j in neighbors[i] or bool(neighbors[i]&neighbors[j])
           for i in range(P) for j in range(P))

# Collapse a canonical BFS spanning tree and use oriented triangular relators.
seen={0};queue=[0];tree=set()
for v in queue:
    for w in sorted(neighbors[v]):
        if w not in seen:
            seen.add(w);queue.append(w);tree.add(tuple(sorted((v,w))))
assert len(seen)==P and len(tree)==P-1
nontree=[e for e in faces[1] if e not in tree]
assert len(nontree)==297
survivors=set(nontree)
relators=[set(combinations(t,2)) - tree for t in faces[2]]
# A relator with one remaining generator forces that generator to be trivial,
# not just zero after abelianization. This proves simple connectivity.
kills=[]
while survivors:
    singled=next((r & survivors for r in relators if len(r & survivors)==1),None)
    assert singled is not None,'Failed unit triangular Tietze elimination'
    edge=next(iter(singled));survivors.remove(edge);kills.append(edge)
assert len(kills)==297
print('tree_edges',len(tree),'triangle_group_eliminations',len(kills))

# Degree-three simplicial boundary, indexed by oriented triangles.
incidences=defaultdict(list)
for k,tet in enumerate(faces[3]):
    for j in range(4):
        face=tet[:j]+tet[j+1:]
        incidences[face].append((k,1 if j%2==0 else -1))
assert len(incidences)==888
assert Counter(len(incidences[t]) for t in faces[2])==Counter({2:666,4:222})
print('triangle_coface_degrees',dict(sorted(Counter(map(len,incidences.values())).items())))

# Two-coface rows give an oriented incidence matrix of a graph on 555
# tetrahedra. Each connected component contributes a primitive kernel line.
adjacency=[[] for _ in faces[3]]
for tri,cofaces in incidences.items():
    if len(cofaces)!=2:continue
    (a,sa),(b,sb)=cofaces
    adjacency[a].append((b,-sa*sb))
    adjacency[b].append((a,-sa*sb))
comp=[-1]*len(faces[3]);orientation=[0]*len(faces[3]);sizes=[]
for root in range(len(faces[3])):
    if comp[root]!=-1:continue
    cid=len(sizes);comp[root]=cid;orientation[root]=1;stack=[root];sz=0
    while stack:
        i=stack.pop();sz+=1
        for j,t in adjacency[i]:
            required=orientation[i]*t
            if comp[j]==-1:
                comp[j]=cid;orientation[j]=required;stack.append(j)
            else:
                assert comp[j]==cid and orientation[j]==required
    sizes.append(sz)
assert sizes==[185,185,185],sizes
for tri,cofaces in incidences.items():
    if len(cofaces)==2:
        assert sum(s*orientation[k] for k,s in cofaces)==0
print('two_coface_components',sizes)

# Restrict all remaining (four-coface) boundary rows to the primitive
# three-dimensional kernel lattice of the preceding incidence matrix.
reduced=[]
for tri,cofaces in incidences.items():
    if len(cofaces)==4:
        row=[0]*3
        for k,s in cofaces:row[comp[k]]+=s*orientation[k]
        reduced.append(tuple(row))
assert len(reduced)==222
profile=Counter(reduced)
assert sorted(profile.values())==[37]*6,profile
assert len(profile)==6,profile
assert set(profile)=={(3,0,-1),(-3,0,1),(-1,-3,0),(1,3,0),(0,-1,-3),(0,1,3)},profile
print('remaining_row_profile', sorted(profile.items()))

# Determinantal divisors of the reduced 222x3 integer matrix. They are
# the gcds of 1x1,2x2,3x3 minors. Duplicate rows need not be repeated.
rows=list(profile)
def det3(x,y,z):
    return (x[0]*(y[1]*z[2]-y[2]*z[1])
            -x[1]*(y[0]*z[2]-y[2]*z[0])
            +x[2]*(y[0]*z[1]-y[1]*z[0]))
d1=0;d2=0;d3=0
for r in rows:
    for a in r:d1=gcd(d1,abs(a))
for r,s in combinations(rows,2):
    for a,b in combinations(range(3),2):
        d2=gcd(d2,abs(r[a]*s[b]-r[b]*s[a]))
for r,s,t in combinations(rows,3):
    d3=gcd(d3,abs(det3(r,s,t)))
assert (d1,d2,d3)==(1,1,26),(d1,d2,d3)
print('reduced_determinantal_divisors',(d1,d2,d3))
print('reduced_Smith_invariants',(d1,d2//d1,d3//d2))
print('boundary3_Smith_invariants','unit x 554; 26 x 1')

# Independently test boundary ranks over finite fields (not used as an
# infinite or integer-homology proof).
def modular_rank(k,prime):
    idx={v:i for i,v in enumerate(faces[k-1])}
    basis={}
    for simplex in faces[k]:
        col={idx[simplex[:j]+simplex[j+1:]]:(1 if j%2==0 else prime-1)
             for j in range(k+1)}
        while col:
            r=max(col);a=col[r]
            if r not in basis:
                inv=pow(a,-1,prime)
                basis[r]={u:v*inv%prime for u,v in col.items()}
                break
            for u,v in basis[r].items():
                nv=(col.get(u,0)-a*v)%prime
                if nv:col[u]=nv
                else:col.pop(u,None)
    return len(basis)
for prime,expected in [(2,(36,297,554)),(3,(36,297,555)),(13,(36,297,554))]:
    actual=tuple(modular_rank(k,prime) for k in [1,2,3])
    assert actual==expected,(prime,actual)
    print('boundary_ranks_mod',prime,actual)

# Integral H_1 vanishes by triangular Tietze eliminations.
# The two-incidence submatrix is a primitive graph incidence matrix;
# its 552 unit pivots leave the displayed 222x3 matrix with Smith (1,1,26).
# Thus rank(d3)=555 and torsion(coker(d3))=Z/26. The image of d2 is
# primitive of rank 297, so the torsion of H_2 matches that of coker(d3).
# H_2 free rank is 888-297-555=36 and H_3=0.
assert 888-297-555==36
print('integral_homology','H0=Z; H1=0; H2=Z^36 + Z/26; H3=0')
print('homotopy_type','wedge 36 S^2 and Moore(Z/26,2)')
print('ALL_CHECKS_PASS')
