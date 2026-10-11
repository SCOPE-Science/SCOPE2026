#!/usr/bin/env python3
import sympy as sp
from itertools import combinations

rt5=sp.sqrt(5)
phi=(1+rt5)/2
verts=[]
for y in (sp.Integer(1),sp.Integer(-1)):
    for z in (phi,-phi):
        verts.append(sp.Matrix([0,y,z]))
for x in (sp.Integer(1),sp.Integer(-1)):
    for y in (phi,-phi):
        verts.append(sp.Matrix([x,y,0]))
for x in (phi,-phi):
    for z in (sp.Integer(1),sp.Integer(-1)):
        verts.append(sp.Matrix([x,0,z]))
assert len(verts)==12 and len({tuple(v) for v in verts})==12

def d2(a,b):
    q=a-b
    return sp.simplify(q.dot(q))

edges=set()
for i,j in combinations(range(12),2):
    if sp.simplify(d2(verts[i],verts[j])-4)==0:
        edges.add((i,j))
assert len(edges)==30

def isedge(i,j):
    return tuple(sorted((i,j))) in edges

faces=[]
for a,b,c in combinations(range(12),3):
    if isedge(a,b) and isedge(a,c) and isedge(b,c):
        faces.append((a,b,c))
assert len(faces)==20

facet_normals=[]
for f in faces:
    a,b,c=(verts[i] for i in f)
    n=(b-a).cross(c-a)
    # For this centered regular polytope, all vertices of a supporting facet
    # have one common nonzero support value. Orient that value positive.
    s=sp.simplify(n.dot(a))
    assert s!=0
    if s<0:
        n=-n; s=-s
    # Verify support: every vertex is on or below this plane.
    for w in verts:
        assert sp.simplify(s-n.dot(w)) >= 0
    facet_normals.append(n)

incident=[[] for _ in range(12)]
for k,f in enumerate(faces):
    for i in f:
        incident[i].append(facet_normals[k])
assert all(len(x)==5 for x in incident)

axes=[sp.Matrix([1,0,0]),sp.Matrix([0,1,0]),sp.Matrix([0,0,1])]
axis_for=[]
for i,v in enumerate(verts):
    good=[]
    for j,e in enumerate(axes):
        vals=[sp.simplify(n.dot(e)) for n in incident[i]]
        if all(x>0 for x in vals) or all(x<0 for x in vals):
            good.append(j)
    assert good, (i,v)
    # One coordinate has magnitude phi; that coordinate axis must work.
    big=[j for j,x in enumerate(v) if sp.simplify(x*x-phi*phi)==0]
    assert len(big)==1 and big[0] in good
    axis_for.append(big[0])
assert set(axis_for)=={0,1,2}

# Exact almost-smooth obstruction: minimum cosine over incident facet normals.
cosines=[]
for ns in incident:
    for a,b in combinations(ns,2):
        c=sp.simplify(a.dot(b)/sp.sqrt(a.dot(a)*b.dot(b)))
        cosines.append(c)
# Compare symbolically against 1/3 and ensure it occurs.
assert any(sp.simplify(c-sp.Rational(1,3))==0 for c in cosines)
assert all(sp.simplify(c-sp.Rational(1,3))>=0 for c in cosines)
assert sp.Rational(1,3) < sp.Rational(1,2)

# Representative normals stated in the proof are incident and all x-positive.
v=sp.Matrix([phi,0,1])
i=next(k for k,w in enumerate(verts) if w==v)
assert all(sp.simplify(n[0])>0 for n in incident[i])

print('VERIFY_OK')
print('vertices = 12')
print('edges = 30')
print('facets = 20')
print('incident_facets_per_vertex = 5')
print('coordinate_axis_vertex_coverage = 12/12')
print('minimum_incident_normal_cosine = 1/3')
