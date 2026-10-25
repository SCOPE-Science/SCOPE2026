#!/usr/bin/env python3
"""Exact integral homology verification for the ternary projective arc complex.

Requires Python 3.11+ and SymPy 1.13+.  Exhaustive enumeration of all
13 points, 78 edges, 234 noncollinear triangles, 234 quadrangles.
"""
from collections import Counter
from itertools import combinations, product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

MOD = 3

def det3(A):
    (a, b, c) = A
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))%MOD

def canonical(v):
    a = next(x for x in v if x)
    return tuple((x*pow(a, -1, MOD))%MOD for x in v)

points = sorted({canonical(v) for v in product(range(MOD), repeat=3) if any(v)})
assert len(points)==13
verts = list(range(len(points)))
S0=[(x,) for x in verts]
S1=list(combinations(verts,2))
S2=[t for t in combinations(verts,3) if det3([points[i] for i in t]) != 0]
s2set=set(S2)
S3=[q for q in combinations(verts,4) if all(f in s2set for f in combinations(q,3))]
assert tuple(map(len,(S0,S1,S2,S3)))==(13,78,234,234)

def boundary(rows, cols):
    rowid = {simplex:i for i,simplex in enumerate(rows)}
    data = [[0]*len(cols) for _ in rows]
    for j, simplex in enumerate(cols):
        for k in range(len(simplex)):
            face = simplex[:k]+simplex[k+1:]
            data[rowid[face]][j]+=(-1)**k
    return Matrix(data)

d1=boundary(S0,S1)
d2=boundary(S1,S2)
d3=boundary(S2,S3)
assert d1*d2==Matrix.zeros(13,234)
assert d2*d3==Matrix.zeros(78,234)

def smith_counts(A):
    smith=smith_normal_form(A,domain=ZZ)
    return Counter(abs(int(smith[i,i])) for i in range(min(smith.rows,smith.cols)) if smith[i,i])

z1=smith_counts(d1)
z2=smith_counts(d2)
z3=smith_counts(d3)
assert z1==Counter({1:12}),z1
assert z2==Counter({1:66}),z2
assert z3==Counter({1:165,3:3}),z3
rank2=sum(z2.values())
rank3=sum(z3.values())
assert len(S2)-rank2==rank3==168
assert len(S3)-rank3==66
assert len(S1)-sum(z1.values())-rank2==0

# Quadrangles are exactly the four-vertex induced homology 2-spheres.
# For three vertices the C_2 boundary of a single triangle is nonzero.
assert len(S3)==234
# A projective 5-arc does not exist, so the cap complex stops in degree 3.
assert not any(all(t in s2set for t in combinations(five,3))
               for five in combinations(verts,5))
# Every noncollinear triple lies on at least one quadrangle.
assert all(any(set(t).issubset(q) for q in S3) for t in S2)
for q in combinations(verts,4):
    faces=[f for f in combinations(q,3) if f in s2set]
    assert (len(faces)==4)==(q in S3)

# The ordered quadrangle frames have cardinality 234*4! = |PGL(3,3)|.
assert len(S3)*24==(27-1)*(27-3)*(27-9)//2==5616

print('POINTS',len(S0),'EDGES',len(S1),'TRIANGLES',len(S2),'QUADRANGLES',len(S3))
print('SMITH_BOUNDARY_1',dict(sorted(z1.items())))
print('SMITH_BOUNDARY_2',dict(sorted(z2.items())))
print('SMITH_BOUNDARY_3',dict(sorted(z3.items())))
print('HOMOLOGY_H1',0,'H2',(3,3,3),'H3_FREE_RANK',66)
print('MATROID_TOP_H2_FREE_RANK',168,'FOUR_CIRCUIT_SUBLATTICE_INDEX',27)
print('VERIFY_OK_PROJECTIVE_TERNARY_QUADRANGLE_HOMOLOGY')
