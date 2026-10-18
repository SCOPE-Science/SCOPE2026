"""Exact reproducible face-lattice and toric-singularity certificate for K4 spanning-tree base polytope."""
from itertools import combinations, permutations
from functools import reduce
from fractions import Fraction
from math import gcd
from collections import Counter

EDGES=list(combinations(range(4),2)); NE=len(EDGES)

def rank_integer(rows):
    if not rows:return 0
    a=[[Fraction(z) for z in row] for row in rows]
    n=len(a); m=len(a[0]); i=0
    for j in range(m):
        pivot=next((p for p in range(i,n) if a[p][j]),None)
        if pivot is None:continue
        a[i],a[pivot]=a[pivot],a[i]
        val=a[i][j]; a[i]=[t/val for t in a[i]]
        for p in range(i+1,n):
            val=a[p][j]
            if val:a[p]=[a[p][l]-val*a[i][l] for l in range(m)]
        i+=1
        if i==n:break
    return i

def det_int(mat):
    n=len(mat)
    if n==0:return 1
    if n==1:return mat[0][0]
    return sum(((-1)**j)*mat[0][j]*det_int([r[:j]+r[j+1:] for r in mat[1:]]) for j in range(n))

def graph_rank(Eset):
    parent=list(range(4))
    def find(x):
        while x!=parent[x]:x=parent[x]
        return x
    edges=0
    for i in Eset:
        a,b=EDGES[i];a,b=find(a),find(b)
        if a!=b:parent[a]=b;edges+=1
    return edges

bases=sorted(tuple(1 if i in S else 0 for i in range(NE)) for S in combinations(range(NE),3) if graph_rank(S)==3)
coords=[b[:5] for b in bases]
assert len(bases)==16
assert rank_integer([[z[i]-coords[0][i] for i in range(5)] for z in coords[1:]])==5

facets=[]
for bits in range(1,(1<<6)-1):
    S=[i for i in range(6) if bits>>i&1]
    r=graph_rank(S)
    tight=frozenset(j for j,b in enumerate(bases) if sum(b[i] for i in S)==r)
    if not tight:continue
    t=next(iter(tight))
    d=rank_integer([[coords[j][i]-coords[t][i] for i in range(5)] for j in tight if j!=t])
    if d==4:
        normal=tuple(int(i in S)-int(5 in S) for i in range(5))
        facets.append((bits,normal,tight,r))
assert len(facets)==16 and len({f[2] for f in facets})==16

faces={frozenset(range(len(bases)))}
for bits,normal,mask,r in facets:
    faces|={f&mask for f in faces if f&mask}
assert len(faces)==219

def dim_face(face):
    t=next(iter(face))
    return rank_integer([[coords[j][i]-coords[t][i] for i in range(5)] for j in face if j!=t])

def saturated_index(vectors):
    c=len(vectors)
    if c==0:return 1
    if c>5:return 0
    minors=(abs(det_int([[v[i] for i in sub] for v in vectors])) for sub in combinations(range(5),c))
    return reduce(gcd,minors,0)

faces_by_dim=Counter()
singular=set()
for face in faces:
    dim=dim_face(face);faces_by_dim[dim]+=1
    normals=[f[1] for f in facets if face<=f[2]]
    c=5-dim
    if len(normals)!=c or saturated_index(normals)!=1:singular.add(face)
assert dict(faces_by_dim)=={0:16,1:54,2:78,3:54,4:16,5:1}
assert len(singular)==94
assert Counter(dim_face(f) for f in singular)=={0:16,1:48,2:30}
maximal={f for f in singular if not any(f<g for g in singular)}
assert len(maximal)==30 and all(dim_face(f)==2 for f in maximal)
assert Counter(len(f) for f in maximal)=={3:24,4:6}

edge_to_index={e:i for i,e in enumerate(EDGES)}
base_to_index={b:i for i,b in enumerate(bases)}
permutations_on_bases=[]
for p in permutations(range(4)):
    edge_perm=[edge_to_index[tuple(sorted((p[a],p[b])))] for a,b in EDGES]
    j_map=[]
    for b in bases:
        image=[0]*6
        for e,v in enumerate(b):image[edge_perm[e]]=v
        j_map.append(base_to_index[tuple(image)])
    permutations_on_bases.append(j_map)
remaining=set(maximal);orbits=[]
while remaining:
    f=next(iter(remaining))
    orbit={frozenset(p[j] for j in f) for p in permutations_on_bases}
    assert orbit<=maximal
    orbits.append(orbit);remaining-=orbit
assert sorted((len(o),len(next(iter(o)))) for o in orbits)==[(6,4),(12,3),(12,3)]

# Generic codimension-three singularities: primitive 4-ray cones, all 3x3 minors gcd 1.
for face in maximal:
    normals=[f[1] for f in facets if face<=f[2]]
    assert len(normals)==4
    for three in combinations(normals,3):
        assert saturated_index(three)==1
    # Any one primitive relation has coefficients with absolute value 1:
    # compute its signs using one nonzero 3x3 coordinate projection.
    full=[list(x) for x in normals]
    rel=None
    for projection in combinations(range(5),3):
        a=[[v[i] for i in projection] for v in normals]
        if rank_integer(a)!=3:continue
        cofs=[(-1)**j*det_int([a[t] for t in range(4) if t!=j]) for j in range(4)]
        g=reduce(gcd,map(abs,cofs))
        if g and rank_integer([cofs])==1:
            cofs=[c//g for c in cofs]
            if all(abs(c)==1 for c in cofs):
                rel=cofs;break
    assert rel is not None
    assert sum(rel)==0 and all(sum(rel[i]*normals[i][j] for i in range(4))==0 for j in range(5))
print('VERIFY_OK bases=16 facets=16 faces=219 f=(16,54,78,54,16,1) singular_orbits=94 components=30 triangles=24 squares=6 automorphism_orbits=(6,12,12) generic_conifold=30')
# Check the orbit closures are standard simplex/square toric surfaces (no lattice index).
for f in maximal:
    vs=[coords[j] for j in sorted(f)]
    diffs=[[v[i]-vs[0][i] for i in range(5)] for v in vs[1:]]
    for two in combinations(diffs,2):
        assert saturated_index(two)==1
    if len(f)==4:
        # In a parallelogram one of the four is the sum of two others minus the fourth.
        assert any(tuple(a[i]+b[i]-c[i] for i in range(5)) in vs for a,b,c in permutations(vs,3))
print('FACE_SURFACES_OK')
