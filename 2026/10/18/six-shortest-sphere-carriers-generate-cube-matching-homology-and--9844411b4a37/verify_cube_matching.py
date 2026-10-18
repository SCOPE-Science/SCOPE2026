"""Exact checks for minimal induced 2-sphere carriers of the cube matching complex.

Run: python verify_cube_matching.py  (requires SymPy)
All vertex, edge, simplex, and orientation conventions are specified here.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import gcd
from sympy import Matrix, zeros, ilcm
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

VERTICES = tuple(product((0, 1), repeat=3))
VINDEX = {v:i for i,v in enumerate(VERTICES)}
EDGES = tuple((i,j) for i in range(8) for j in range(i+1,8)
              if sum(a!=b for a,b in zip(VERTICES[i],VERTICES[j]))==1)
EINDEX = {e:i for i,e in enumerate(EDGES)}
F = {r: tuple(s for s in combinations(range(12),r+1)
               if len(set(v for e in s for v in EDGES[e]))==2*(r+1))
     for r in range(4)}
assert [len(F[i]) for i in range(4)] == [12,42,44,9]
FIDX = {r:{s:i for i,s in enumerate(F[r])} for r in range(4)}

def boundary(dim):
    res = zeros(len(F[dim-1]),len(F[dim]))
    for j,s in enumerate(F[dim]):
        for k in range(len(s)):
            res[FIDX[dim-1][s[:k]+s[k+1:]],j] = (-1)**k
    return res

D1,D2,D3 = (boundary(i) for i in (1,2,3))
assert D1*D2 == zeros(12,44) and D2*D3 == zeros(42,9)
assert [D1.rank(),D2.rank(),D3.rank()] == [11,31,9]

def smith_units(mat,expected):
    result = smith_normal_form(mat, domain=ZZ)
    nonzero = [int(result[i,i]) for i in range(min(result.rows,result.cols))
               if result[i,i]!=0]
    assert len(nonzero)==expected, (expected,nonzero)
    assert all(abs(x)==1 for x in nonzero), nonzero

# The image of D2 is primitive in C1; hence H1 vanishes integrally.
smith_units(D2,31)

def gf2_rank(cols):
    pivots={}
    for x in cols:
        while x:
            bit=x.bit_length()-1
            if bit in pivots: x ^= pivots[bit]
            else:
                pivots[bit]=x
                break
    return len(pivots)

def dim_h2_mod2(s):
    allowed=set(s)
    tri=tuple(t for t in F[2] if set(t)<=allowed)
    edges=tuple(t for t in F[1] if set(t)<=allowed)
    tet=tuple(t for t in F[3] if set(t)<=allowed)
    eidx={e:i for i,e in enumerate(edges)}
    tidx={t:i for i,t in enumerate(tri)}
    b2=[sum(1<<eidx[t[:i]+t[i+1:]] for i in range(3)) for t in tri]
    b3=[sum(1<<tidx[s[:i]+s[i+1:]] for i in range(4)) for s in tet]
    return len(tri)-gf2_rank(b2)-gf2_rank(b3)

by_size=defaultdict(list)
for n in range(13):
    for s in combinations(range(12),n):
        h=dim_h2_mod2(s)
        if h:by_size[n].append((s,h))
assert [(n,len(by_size[n])) for n in range(13) if by_size[n]] == [
    (8,6),(9,24),(10,42),(11,12),(12,1)]
assert all(h==1 for s,h in by_size[8])
CARRIERS=tuple(s for s,h in by_size[8])

def perfect_matching(mm):
    return len(mm)==4 and len({v for j in mm for v in EDGES[j]})==8

perfects=tuple(s for s in combinations(range(12),4) if perfect_matching(s))
assert len(perfects)==9
assert all(perfect_matching(tuple(e for e in range(12) if e not in s)) for s in CARRIERS)
assert all(len({next(i for i in range(3) if VERTICES[a][i]!=VERTICES[b][i])
                for e in range(12) if e not in s for a,b in [EDGES[e]]})==2
           for s in CARRIERS)

# Four elementary free-face collapses on the first carrier give a closed 2-sphere.
PAIRS = (
    ((0,6,7),(0,6,7,8)),
    ((1,3,9),(1,3,9,10)),
    ((3,9),(3,9,10)),
    ((6,7),(6,7,8)),
)
R = set(x for n in range(1,5) for x in combinations(CARRIERS[0],n)
        if x in F[n-1])
for small,large in PAIRS:
    assert small in R and large in R and len(large)==len(small)+1
    assert {g for g in R if set(small)<set(g)} == {large}
    R.remove(small);R.remove(large)
assert Counter(map(len,R)) == {1:8,2:18,3:12}
triangles={x for x in R if len(x)==3}
incidence=Counter(e for t in triangles for e in combinations(t,2))
assert set(incidence.values())=={2}
assert set(e for e in R if len(e)==2)==set(incidence)
assert len({t[0] for t in R if len(t)==1})==8
assert 8-18+12==2
remaining_neighbors=defaultdict(set)
for a,b in (f for f in R if len(f)==2):
    remaining_neighbors[a].add(b)
    remaining_neighbors[b].add(a)
seen_vertices=set();todo=[CARRIERS[0][0]]
while todo:
    v=todo.pop()
    if v in seen_vertices:continue
    seen_vertices.add(v);todo.extend(remaining_neighbors[v]-seen_vertices)
assert seen_vertices==set(CARRIERS[0])
for v in CARRIERS[0]:
    link_edges=[tuple(x for x in t if x!=v) for t in triangles if v in t]
    nb=defaultdict(set)
    for a,b in link_edges:nb[a].add(b);nb[b].add(a)
    assert nb and all(len(q)==2 for q in nb.values())
    seen=set();stack=[next(iter(nb))]
    while stack:
        x=stack.pop()
        if x in seen:continue
        seen.add(x);stack.extend(nb[x]-seen)
    assert seen==set(nb)
# The remaining connected closed surface has Euler characteristic two, hence S2.

# Build automorphism group and its S4 x C2 class labels.
DIAGONALS=tuple(sorted({tuple(sorted((i,VINDEX[tuple(1-x for x in v)])))
                       for i,v in enumerate(VERTICES)}))
DINDEX={x:i for i,x in enumerate(DIAGONALS)}

def sign(perm):
    return (-1)**sum(a>b for i,a in enumerate(perm) for b in perm[i+1:])

def cycle_type(perm):
    visited=set();lens=[]
    for i in range(len(perm)):
        if i not in visited:
            j=i;n=0
            while j not in visited:
                visited.add(j);j=perm[j];n+=1
            lens.append(n)
    return tuple(sorted(lens,reverse=True))

AUT=[]; chars={}; orbit=set()
for perm in permutations(range(3)):
    for flip in VERTICES:
        gv=[VINDEX[tuple(v[perm[i]] ^ flip[i] for i in range(3))]
            for v in VERTICES]
        ge=[EINDEX[tuple(sorted((gv[a],gv[b])))] for a,b in EDGES]
        gd=[DINDEX[tuple(sorted((gv[a],gv[b])))] for a,b in DIAGONALS]
        parity=(-1)**sum(flip)
        label=(cycle_type(gd),parity)
        fixed_reduced_lefschetz=-1
        for size in range(1,5):
            for s in F[size-1]:
                if set(ge[i] for i in s)==set(s):
                    fixed_reduced_lefschetz += (-1)**(size-1)*sign([s.index(ge[i]) for i in s])
        if label in chars:assert chars[label]==fixed_reduced_lefschetz
        chars[label]=fixed_reduced_lefschetz
        orbit.add(tuple(sorted(ge[i] for i in CARRIERS[0])))
        AUT.append((gv,ge,gd,label))
assert len(AUT)==48 and orbit==set(CARRIERS)
CLASSES=((1,1,1,1),(2,1,1),(2,2),(3,1),(4,))
assert [chars[(c,1)] for c in CLASSES]==[4,0,0,1,2]
assert [chars[(c,-1)] for c in CLASSES]==[2,-2,-2,-1,0]
# Rational irreducible S4 table with the standard S4 x central-inversion splitting.
CHAR_TABLE={(4,):(1,1,1,1,1),(3,1):(3,1,-1,0,-1),
            (2,2):(2,0,2,-1,0),(2,1,1):(3,-1,-1,0,1),
            (1,1,1,1):(1,-1,1,1,-1)}
CLASS_SIZES=(1,6,3,8,6)
DECOMP={}
for parity in (1,-1):
    values=[(chars[(c,1)]+parity*chars[(c,-1)])//2 for c in CLASSES]
    for irrep,row in CHAR_TABLE.items():
        total=sum(n*x*y for n,x,y in zip(CLASS_SIZES,values,row))
        assert total%24==0
        if total:
            assert total>0
            DECOMP[(irrep,parity)]=total//24
assert DECOMP=={((2,1,1),1):1, ((4,),-1):1}

# Pick natural primitive cycles on each induced sphere, then use Smith forms.
CYCLES=[]
for carrier in CARRIERS:
    tri_cols=[i for i,s in enumerate(F[2]) if set(s)<=set(carrier)]
    tet_cols=[i for i,s in enumerate(F[3]) if set(s)<=set(carrier)]
    small_d2=D2[:,tri_cols]
    small_d3=D3.extract(tri_cols,tet_cols)
    assert small_d3.rank()==2
    assert len(small_d2.nullspace())==3
    for raw in small_d2.nullspace():
        candidate=zeros(len(F[2]),1)
        for i,val in zip(tri_cols,raw):candidate[i]=val
        if Matrix.hstack(D3,candidate).rank()>D3.rank():
            factor=1
            for val in candidate:factor=ilcm(factor,int(val.q))
            candidate=candidate*factor
            g=gcd(*(int(val) for val in candidate))
            candidate=candidate/g
            assert D2*candidate==zeros(len(F[1]),1)
            assert all(val.q==1 for val in candidate)
            CYCLES.append(candidate)
            break
    else:raise AssertionError('No nonboundary local generator found')
assert len(CYCLES)==6
combined=Matrix.hstack(D3,*CYCLES[:4])
assert combined.rank()==13
smith_units(combined,13)
assert Matrix.hstack(D3,*CYCLES).rank()==13
assert [Matrix.hstack(D3,z).rank() for z in CYCLES]==[10]*6
# The primitive rank-13 lattice generated by these columns equals ker(D2)
# because ker(D2) is a saturated rank-13 subgroup of Z^44.

# There are exactly two primitive relations among the six classes.
relation_kernel=Matrix.hstack(D3,*CYCLES).nullspace()
assert len(relation_kernel)==2
relations=[tuple(int(t) for t in v[9:]) for v in relation_kernel]
assert relations==[(-1,-1,-1,0,1,0),(0,-1,-1,1,0,1)]
print('VERIFY_OK FACE_VECTOR_12_42_44_9 NINE_PERFECT_MATCHINGS')
print('SIX_MINIMUM_8_EDGE_CARRIERS S2_BY_FOUR_COLLAPSES ORBIT_48')
print('H2_Z4 INTEGRAL_SPAN_BY_FOUR_OF_SIX SNF_13_UNITS')
print('S4_C2_CHARACTER EVEN_4_0_0_1_2 ODD_2_-2_-2_-1_0')
print('TWO_GENERATOR_RELATION_LATTICE_OK')
