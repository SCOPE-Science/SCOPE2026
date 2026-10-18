#!/usr/bin/env python3
"""Exact standalone census of the singular torus-orbit closures of the Fano matroid polytope.
Only Python's standard library is needed.  All matrices are integral and all tests exact.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import gcd

E = tuple(range(7))
POINTS = tuple(range(1, 8))  # nonzero vectors in F_2^3, with point i labelled i+1
LINES = {triple for triple in combinations(E, 3)
         if (triple[0]+1) ^ (triple[1]+1) ^ (triple[2]+1) == 0}
BASES = tuple(t for t in combinations(E, 3) if t not in LINES)
assert len(LINES) == 7 and len(BASES) == 28


def rational_rank(rows):
    if not rows: return 0
    a = [[Fraction(v) for v in row] for row in rows]
    h, w = len(a), len(a[0]); piv = 0
    for j in range(w):
        q = next((k for k in range(piv, h) if a[k][j]), None)
        if q is None: continue
        a[piv],a[q] = a[q],a[piv]
        t=a[piv][j]; a[piv]=[v/t for v in a[piv]]
        for i in range(piv+1,h):
            if a[i][j]:
                t=a[i][j]
                a[i]=[u-t*v for u,v in zip(a[i],a[piv])]
        piv+=1
        if piv==h:break
    return piv


def det(rows):
    """Exact determinant via fraction-free Bareiss elimination."""
    n=len(rows)
    if n==0:return 1
    a=[list(r) for r in rows]
    assert all(len(r)==n for r in a)
    sign=1;old=1
    for k in range(n-1):
        if a[k][k]==0:
            u=next((i for i in range(k+1,n) if a[i][k]),None)
            if u is None:return 0
            a[k],a[u]=a[u],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=a[i][j]*p-a[i][k]*a[k][j]
                assert t%old==0
                a[i][j]=t//old
        for i in range(k+1,n):a[i][k]=0
        old=p
    return sign*a[n-1][n-1]


def dimension(face):
    if not face: return -1
    b=BASES[(face&-face).bit_length()-1]
    vec0=[int(i in b) for i in range(6)]
    rows=[]
    for j,c in enumerate(BASES):
        if (face>>j)&1:
            rows.append([int(i in c)-vec0[i] for i in range(6)])
    return rational_rank(rows)


def rk(S):
    if len(S)<=2:return len(S)
    return 2 if tuple(S) in LINES else 3

# Edmonds' rank-inequality description gives all supporting halfspaces.
# Test all proper nonempty subsets, retain exactly codimension-one faces.
FACETS=[]
for mask in range(1,(1<<7)-1):
    S=tuple(i for i in E if (mask>>i)&1)
    r=rk(S)
    supported=sum((1<<j) for j,b in enumerate(BASES)
                  if sum(i in b for i in S)==r)
    if dimension(supported)==5:
        FACETS.append((S,r,supported))
assert len(FACETS)==21
assert Counter((len(S),r) for S,r,_ in FACETS)=={(1,1):7,(3,2):7,(6,3):7}

# Every face is an intersection of facets (the full polytope included).
FULL=(1<<len(BASES))-1
FACES={FULL}
for _,_,facet_mask in FACETS:
    FACES |= {f&facet_mask for f in tuple(FACES)}
assert len(FACES)==772
DIMS={f:dimension(f) for f in FACES}
assert Counter(DIMS.values()) == {-1:1,0:28,1:126,2:245,3:238,4:112,5:21,6:1}

# Ambient affine lattice is {sum x_i=3} with coordinates x_0,...,x_5.
# Primitive dual ray for x(S)<=r(S) has components 1_(i in S)-1_(6 in S).
NORMALS=[tuple(int(i in S)-int(6 in S) for i in range(6)) for S,_,_ in FACETS]


def determinant_divisor(normals,k):
    """GCD of full-size minors of the integer matrix of column rays."""
    if k==0:return 1
    value=0
    for indices in combinations(range(6),k):
        M=[[normals[j][i] for j in range(k)] for i in indices]
        value=gcd(value,abs(det(M)))
    return value


ACTIVE={f:tuple(j for j,(_,_,mask) in enumerate(FACETS) if f&mask==f)
        for f in FACES if DIMS[f]>=0}
SINGULAR=set()
for f,act in ACTIVE.items():
    codim=6-DIMS[f]
    if len(act)!=codim or determinant_divisor([NORMALS[j] for j in act],codim)!=1:
        SINGULAR.add(f)
assert len(SINGULAR)==308

# A singular torus orbit is contained in the closure of a higher-dimensional
# singular orbit iff its face lies in the larger face.  Keep maximal faces.
COMPONENTS={f for f in SINGULAR if not any(f!=g and f&g==f for g in SINGULAR)}
assert len(COMPONENTS)==70
SIG=Counter((DIMS[f],f.bit_count(),len(ACTIVE[f])) for f in COMPONENTS)
assert SIG=={(3,4,4):21,(2,4,5):21,(2,3,5):28}

# All 70 generic transverse cones are saturated and have one more ray than
# their dimensions: their divisor class group is free of rank one.
for f in COMPONENTS:
    k=6-DIMS[f]
    assert len(ACTIVE[f])==k+1
    vv=[NORMALS[j] for j in ACTIVE[f]]
    div=0
    for sub in combinations(vv,k):div=gcd(div,determinant_divisor(sub,k))
    assert div==1

# All 168 automorphisms of the Fano plane act on the face lattice.
def lin_image(x,a,b,c):
    return ((a if x&1 else 0) ^ (b if x&2 else 0) ^ (c if x&4 else 0))
AUT=[]
for a,b,c in ((a,b,c) for a in POINTS for b in POINTS for c in POINTS):
    im=[lin_image(i,a,b,c) for i in POINTS]
    if len(set(im))==7:
        AUT.append(tuple(v-1 for v in im))
assert len(AUT)==168
INDEX={b:i for i,b in enumerate(BASES)}
def act_on_face(f,perm):
    res=0
    for i,b in enumerate(BASES):
        if (f>>i)&1:
            new=tuple(sorted(perm[j] for j in b))
            res |= 1<<INDEX[new]
    return res
orbits=[];unseen=set(COMPONENTS)
while unseen:
    f=min(unseen)
    orbit={act_on_face(f,p) for p in AUT}
    assert orbit<=COMPONENTS
    orbits.append((DIMS[f],f.bit_count(),len(orbit)))
    unseen-=orbit
assert sorted(orbits)==[(2,3,28),(2,4,21),(3,4,21)]
print('VERIFY_OK')
print('vertices=28 facets=21 faces=772 singular_orbits=308')
print('face_vector=(28,126,245,238,112,21)')
print('irreducible_singular_components=70')
print('component_orbits=(dim2 triangular 28, dim2 quadrilateral 21, dim3 tetrahedral 21)')
print('generic_local_class_groups=Z')
