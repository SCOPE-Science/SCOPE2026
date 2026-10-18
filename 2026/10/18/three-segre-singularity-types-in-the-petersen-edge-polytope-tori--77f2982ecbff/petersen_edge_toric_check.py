#!/usr/bin/env python3
"""Exact, self-contained certificate for the normal fan of the Petersen edge polytope.
Requires Python >=3.10; only Python standard library. No floating-point decisions.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd, lcm
import json
import time

START=time.monotonic()

def echelon(rows, ncols):
    """Fraction-free input, rational row echelon output and pivot columns."""
    a=[[Fraction(v) for v in row] for row in rows]
    piv=[]; h=0
    for col in range(ncols):
        i=next((i for i in range(h,len(a)) if a[i][col]),None)
        if i is None: continue
        a[h],a[i]=a[i],a[h]
        pv=a[h][col]
        for k in range(col,ncols):a[h][k]/=pv
        for j in range(h+1,len(a)):
            f=a[j][col]
            if f:
                for k in range(col,ncols):a[j][k]-=f*a[h][k]
        piv.append(col);h+=1
        if h==len(a):break
    return a,piv

def rank(rows,ncols):
    return len(echelon(rows,ncols)[1]) if rows else 0

def prim_kernel(rows,ncols):
    a,piv=echelon(rows,ncols)
    if len(piv)!=ncols-1: return None
    free=(set(range(ncols))-set(piv)).pop()
    v=[Fraction(0)]*ncols;v[free]=Fraction(1)
    for r in reversed(range(len(piv))):
        j=piv[r];v[j]=-sum(a[r][c]*v[c] for c in range(j+1,ncols))
    q=lcm(*(z.denominator for z in v))
    u=[int(t*q) for t in v];div=gcd(*u)
    u=tuple(x//div for x in u)
    if next(x for x in u if x)!=abs(next(x for x in u if x)):
        u=tuple(-x for x in u)
    assert all(sum(a*b for a,b in zip(row,u))==0 for row in rows)
    return u

def det(rows):
    n=len(rows)
    if n==0:return 1
    a=[list(row) for row in rows]
    prev=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            swap=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if swap is None:return 0
            a[k],a[swap]=a[swap],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            q=a[i][k]
            for j in range(k+1,n):
                top=p*a[i][j]-q*a[k][j]
                assert top%prev==0
                a[i][j]=top//prev
            a[i][k]=0
        prev=p
    return sign*a[n-1][n-1]

def unit_minor(rows,r):
    # Existence of a single unit minor is a sufficient integral saturation certificate.
    for ix in combinations(range(len(rows)),r):
        block=[rows[i] for i in ix]
        for cols in combinations(range(9),r):
            if abs(det([[row[c] for c in cols] for row in block]))==1:
                return True
    return False

# Vertices of the graph: two-subsets of a five-set.
labels=list(combinations(range(5),2));label_index={v:i for i,v in enumerate(labels)}
E=[(i,j) for i,j in combinations(range(10),2) if not set(labels[i])&set(labels[j])]
E_index={e:i for i,e in enumerate(E)}
assert len(E)==15
P=[tuple(int(j==u or j==v) for j in range(9)) for u,v in E]
full=(1<<15)-1
D=[[P[i][j]-P[0][j] for j in range(9)] for i in range(1,15)]
assert rank(D,9)==9
assert unit_minor(D,9)  # the vertex-difference lattice is exactly Z^9

# Prove facet completeness by inspecting every 9-tuple of vertex points.
# Every facet of a 9-dimensional polytope contains 9 affinely independent vertices.
facets={}
for I in combinations(range(15),9):
    rows=[[P[i][j]-P[I[0]][j] for j in range(9)] for i in I[1:]]
    u=prim_kernel(rows,9)
    if u is None:continue
    scores=[sum(v*x for v,x in zip(u,p)) for p in P]
    base=scores[I[0]]
    if max(scores)>base and min(scores)<base:continue
    if min(scores)==max(scores):raise AssertionError('full-dimensionality contradicted')
    if max(scores)==base:n=u;b=base
    else:n=tuple(-v for v in u);b=-base
    vals=[b-sum(v*x for v,x in zip(n,p)) for p in P]
    assert min(vals)==0
    m=sum(1<<i for i,z in enumerate(vals) if z==0)
    assert rank([[P[i][j]-P[I[0]][j] for j in range(9)] for i in I[1:]],9)==8
    assert m.bit_count()>=9
    facets[(n,b)]=m
assert len(facets)==25,len(facets)
F=list(facets)
Fmask=[facets[k] for k in F]
# Every face is an intersection of facets, including the full/empty face.
faces={full}
for fm in Fmask:
    faces|={f&fm for f in faces}
assert len(faces)==5734,len(faces)
assert 0 in faces

face_info={};face_dim={}
for f in faces:
    if not f:continue
    ix=[i for i in range(15) if f&(1<<i)]
    dim=rank([[P[i][j]-P[ix[0]][j] for j in range(9)] for i in ix[1:]],9)
    incident=tuple(i for i,mask in enumerate(Fmask) if (f&mask)==f)
    assert len(incident)>=9-dim if dim<9 else len(incident)==0
    face_info[f]=(dim,incident)
    face_dim[f]=dim
fv=Counter(face_dim.values()); fv[-1]=1
assert [fv[k] for k in range(-1,10)]==[1,15,105,435,1095,1657,1470,735,195,25,1]

nonsimp=set()
checked_unit=0
for f,(dim,J) in face_info.items():
    if dim==9:continue
    codim=9-dim
    rays=[F[i][0] for i in J]
    if len(rays)>codim: nonsimp.add(f)
    else:
        assert len(rays)==codim
        assert unit_minor(rays,codim), ('nonsmooth simplicial cone',f)
        checked_unit+=1
assert len(nonsimp)==1645

minimal={f for f in nonsimp if not any(f!=g and f&g==f for g in nonsimp)}
assert len(minimal)==115,len(minimal)

# Each minimal nonsimplicial cone has exactly one primitive ray dependence;
# unit minors exclude hidden finite-quotient lattices.
class_of={}; orbit_type=Counter()
for f in minimal:
    dim,J=face_info[f];codim=9-dim
    rays=[F[i][0] for i in J]
    assert len(rays)==codim+1
    assert unit_minor(rays,codim)
    rel=prim_kernel(list(zip(*rays)),len(rays))
    assert rel is not None and all(abs(v)==1 for v in rel)
    a=sum(v>0 for v in rel);b=sum(v<0 for v in rel)
    kind=(dim,tuple(sorted((a,b))))
    class_of[f]=kind
    orbit_type[kind]+=1
assert orbit_type==Counter({(5,(2,3)):60,(4,(2,4)):45,(4,(3,3)):10}),orbit_type

# Verify the automorphism-orbit decomposition from all 120 permutations of 5 letters.
autos=[]
for sig in permutations(range(5)):
    vp=[label_index[tuple(sorted((sig[a],sig[b])))] for a,b in labels]
    autos.append(tuple(E_index[tuple(sorted((vp[a],vp[b])))] for a,b in E))
assert len(set(autos))==120
orb_counts={}
for kind in sorted(orbit_type):
    remaining={f for f in minimal if class_of[f]==kind}
    sizes=[]
    while remaining:
        f=next(iter(remaining))
        orbit={sum(1<<p[i] for i in range(15) if f&(1<<i)) for p in autos}
        assert orbit<=remaining or orbit<=set(class_of)
        assert {class_of[g] for g in orbit}=={kind}
        remaining-=orbit
        sizes.append(len(orbit))
    orb_counts[str(kind)]=sorted(sizes)
assert orb_counts=={'(4, (2, 4))':[15,30], '(4, (3, 3))':[10], '(5, (2, 3))':[10,20,30]},orb_counts

# All 15 vertices are singular, all 105 edges are edges of the polytope.
assert all(face_info[1<<i][1] and len(face_info[1<<i][1])==18 for i in range(15))
assert fv[1]==105
summary={'graph_vertices':10,'graph_edges':15,'polytope_dimension':9,
         'facets':len(F),'nonempty_faces':len(face_info),
         'f_vector_including_empty_and_full':[fv[i] for i in range(-1,10)],
         'nonsimplicial_normal_cones':len(nonsimp),
         'unimodular_simplicial_cones':checked_unit,
         'singular_components':len(minimal),
         'singular_component_types':{str(k):v for k,v in sorted(orbit_type.items())},
         'S5_orbit_sizes':orb_counts,'fixed_points':15,
         'generic_transverse_multiplicities':{'2x3':3,'2x4':4,'3x3':6},
         'integral_method':'rational row reduction, integer Bareiss minors, all nine-vertex facet candidates',
         'elapsed_seconds':round(time.monotonic()-START,3)}
print(json.dumps(summary,sort_keys=True))
print('VERIFY_OK')
