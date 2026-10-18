#!/usr/bin/env python3
"""Exact, standard-library certificate for the silhouette polygon-type law.
All incidence and angle comparisons take place in Z[phi], phi^2=phi+1.
No sampling, numerical tolerances, or external datasets are used.
"""
from itertools import combinations
from collections import Counter

Z=(0,0); ONE=(1,0); PHI=(0,1)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def sm(x,k):return (x[0]*k,x[1]*k)
def sign(x):
    a,b=x; p=2*a+b
    if b==0:return (p>0)-(p<0)
    if p==0:return (b>0)-(b<0)
    if (p>0)==(b>0):return (p>0)-(p<0)
    d=p*p-5*b*b
    assert d!=0 or (p==0 and b==0) # irrationality: equality is impossible otherwise
    return ((p>0)-(p<0)) if d>0 else ((b>0)-(b<0))
def vadd(x,y):return tuple(add(a,b) for a,b in zip(x,y))
def vneg(x):return tuple(neg(a) for a in x)
def vsub(x,y):return vadd(x,vneg(y))
def dot(x,y):
    r=Z
    for a,b in zip(x,y):r=add(r,mul(a,b))
    return r
def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),sub(mul(x[2],y[0]),mul(x[0],y[2])),sub(mul(x[0],y[1]),mul(x[1],y[0])))
def iszero(x):return all(t==Z for t in x)
def norm2(x):return dot(x,x)
def canon(x):
    return x if next(sign(t) for t in x if t!=Z)>0 else vneg(x)
def sd(x,y):return dot(vsub(x,y),vsub(x,y))

# Vertices of an icosahedron of edge length 2.
verts=[]
for y in (-1,1):
    for z in (-1,1):verts.append((Z,sm(ONE,y),sm(PHI,z)))
for x in (-1,1):
    for y in (-1,1):verts.append((sm(ONE,x),sm(PHI,y),Z))
for x in (-1,1):
    for z in (-1,1):verts.append((sm(PHI,x),Z,sm(ONE,z)))
assert len(set(verts))==12
edges=[(i,j) for i,j in combinations(range(12),2) if sd(verts[i],verts[j])==(4,0)]
assert len(edges)==30 and Counter(i for e in edges for i in e)==Counter({i:5 for i in range(12)})
edge_set=set(edges)
facets=[tri for tri in combinations(range(12),3) if all((min(i,j),max(i,j)) in edge_set for i,j in combinations(tri,2))]
assert len(facets)==20
tri_norm=[vadd(vadd(verts[i],verts[j]),verts[k]) for i,j,k in facets]
all_norm=verts+tri_norm
assert len(all_norm)==32
# The rectification has 12 pentagonal and 20 triangular faces, with
# one edge per incidence of a face and one of its three vertices.
incidences=[(12+j,i) for j,tri in enumerate(facets) for i in tri]
assert len(incidences)==60
norms=[]
for v in all_norm:
    q=canon(v)
    if not any(iszero(cross(q,w)) for w in norms):norms.append(q)
assert len(norms)==16
assert all(any(iszero(cross(q,n)) for q in norms) for n in all_norm)

# Pairwise intersections of great circles, as 90 oriented spherical rays.
rays=[]
for a,b in combinations(range(16),2):
    v=cross(norms[a],norms[b]); assert not iszero(v)
    for w in (v,vneg(v)):
        if not any(iszero(cross(w,r)) and sign(dot(w,r))>0 for r in rays):rays.append(w)
assert len(rays)==90
sigma=[]
for r in rays:
    signs=tuple(sign(dot(q,r)) for q in norms)
    assert signs.count(0) in (2,4)
    sigma.append(signs)
assert Counter(z.count(0) for z in sigma)==Counter({2:60,4:30})

# Testing 2^16 possible open cells against exactly computed extreme rays.
ray_masks=[]
for ss in sigma:
    pm=mm=0
    for i,z in enumerate(ss):
        if z==1:pm|=1<<i
        if z==-1:mm|=1<<i
    ray_masks.append((pm,mm))
profiles=Counter(); polygons=Counter(); all_cells=0; total_edges=0; shared_sides={}
for mask in range(1<<16):
    eligible=[j for j,(pm,mm) in enumerate(ray_masks) if not (pm &~mask or mm &mask)]
    if len(eligible)<3:continue
    center=(Z,Z,Z)
    for j in eligible:center=vadd(center,rays[j])
    # The sum of the extreme rays is a strictly feasible cell direction.
    ss=[sign(dot(q,center)) for q in norms]
    if any(ss[i]!=(1 if mask & (1<<i) else -1) for i in range(16)):
        raise AssertionError('unexpected degenerate feasible region')
    n=len(eligible)
    assert n in (3,5),('nonpolygonal cell',n)
    nsign=[sign(dot(q,center)) for q in all_norm]
    assert set(nsign)<={1,-1}
    k=sum(nsign[i]!=nsign[j] for i,j in incidences)
    assert k in (10,12,14)
    # At each polygon vertex, two and only two incident boundary sides;
    # a boundary side is identified by the circle carrying its endpoints.
    angles=[]
    for j in eligible:
        active=[]
        for i in range(16):
            if sigma[j][i]==0 and sum(sigma[t][i]==0 for t in eligible)==2:
                active.append(i)
        assert len(active)==2,(n,k,active)
        i,h=active
        di=dot(norms[i],norms[h]);
        if bool(mask & (1<<i)) == bool(mask & (1<<h)):
            di=di
        else:di=neg(di)
        cosine_sign=-sign(di)
        lhs=mul(di,di); den=mul(norm2(norms[i]),norm2(norms[h]))
        if cosine_sign==-1 and sm(lhs,9)==den:ang='minus_third'
        elif cosine_sign==1 and sm(lhs,9)==den:ang='plus_third'
        elif cosine_sign==1 and sm(lhs,9)==sm(den,5):ang='plus_sqrt5_over3'
        elif cosine_sign==1 and sm(lhs,5)==den:ang='plus_inv_sqrt5'
        elif cosine_sign==1 and sm(lhs,15)==mul((3,4),den):ang='plus_gamma_cos'
        else:raise AssertionError(('unrecognized exact angular type',k,lhs,den,cosine_sign))
        angles.append(ang)
    shape=tuple(sorted(angles))
    tag=(k,n,shape)
    for i in range(16):
        endpoints=[j for j in eligible if sigma[j][i]==0]
        if len(endpoints)==2:
            key=(i,tuple(sorted(endpoints)))
            shared_sides.setdefault(key,[]).append(tag)
    profiles[(k,n,shape)]+=1
    polygons[k]+=1
    all_cells+=1;total_edges+=n
assert all_cells==152 and total_edges==480
expected={
 (10,5,('minus_third',)*5):12,
 (12,3,('plus_inv_sqrt5',)*3):20,
 (12,3,('plus_sqrt5_over3','plus_third','plus_third')):60,
 (14,3,('minus_third','plus_gamma_cos','plus_gamma_cos')):60,
}
assert dict(profiles)==expected,(profiles,expected)
assert len(shared_sides)==240 and all(len(x)==2 for x in shared_sides.values())
transition_counts=Counter(tuple(sorted(x[0] for x in v)) for v in shared_sides.values())
full_transitions=Counter(tuple(sorted((x[0],x[2]) for x in v)) for v in shared_sides.values())
print('TRANSITIONS:',sorted(transition_counts.items()))
print('FOUR_CLASS_TRANSITIONS:',sorted((str(k),v) for k,v in full_transitions.items()))
assert dict(polygons)=={10:12,12:80,14:60}
print('EXACT_CERTIFICATE_OK icosahedron_vertices=12 edges=30 faces=20')
print('facet_normals=32 great_circles=16 arrangement_vertices=90 double=60 quadruple=30')
print('chambers=152 total_spherical_polygon_sides=480')
for key,count in sorted(profiles.items()):print(count,key)
print('COVERAGE: 2^16 sign patterns exhausted; Z[phi] sign & angle tests only')
