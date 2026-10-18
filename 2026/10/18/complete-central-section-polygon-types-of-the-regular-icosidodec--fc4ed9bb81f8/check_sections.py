#!/usr/bin/env python3
"""Exact rational-quadratic verification for central sections of a convex polyhedron.

Requires only Python's standard library.  Every algebraic sign decision is made
in Q(sqrt(5)) by integer/rational comparisons, never floating point.
"""
from fractions import Fraction
from itertools import product, combinations
from collections import Counter

class F:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=co(o);return F(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return F(-self.a,-self.b)
    def __sub__(self,o):return self+(-co(o))
    def __rsub__(self,o):return co(o)+(-self)
    def __mul__(self,o):
        o=co(o);return F(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=co(o);den=o.a*o.a-5*o.b*o.b
        assert den!=0
        return F((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=co(o);return self.a==o.a and self.b==o.b
    def __hash__(self):return hash((self.a,self.b))
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if (a>0)==(b>0):return (a>0)-(a<0)
        if a*a>5*b*b:return (a>0)-(a<0)
        if a*a<5*b*b:return (b>0)-(b<0)
        raise AssertionError('sqrt5 irrational')
    def __repr__(self):return f'({self.a}+{self.b}*sqrt5)'

def co(x):return x if isinstance(x,F) else F(x)
Z=F(); ONE=F(1); PHI=F(Fraction(1,2),Fraction(1,2))
def vadd(u,v):return tuple(a+b for a,b in zip(u,v))
def vsub(u,v):return tuple(a-b for a,b in zip(u,v))
def scale(t,v):return tuple(t*a for a in v)
def dot(u,v):return sum((a*b for a,b in zip(u,v)),Z)
def cross(u,v):return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def neg(v):return tuple(-a for a in v)
def sqdist(u,v):return dot(vsub(u,v),vsub(u,v))
def iszero(v):return all(a==Z for a in v)
def projkey(v):
    a=next(t for t in v if t!=Z)
    return tuple(t/a for t in v)

# Circumradius sqrt(1+phi^2), icosahedron edge length 2.
I=[]
for x,y in product((-1,1),repeat=2):
    I.extend(((Z,F(x),F(y)*PHI), (F(x),F(y)*PHI,Z), (F(y)*PHI,Z,F(x))))
assert len(set(I))==12
IE=[(i,j) for i,j in combinations(range(12),2) if sqdist(I[i],I[j])==F(4)]
assert len(IE)==30
P=[scale(F(Fraction(1,2)),vadd(I[i],I[j])) for i,j in IE]
assert len(set(P))==30
PE=[(i,j) for i,j in combinations(range(30),2) if sqdist(P[i],P[j])==F(1)]
assert len(PE)==60
assert Counter(k for ij in PE for k in ij)=={i:4 for i in range(30)}

# Verify the entire facet structure, rather than merely assuming that every
# shortest midpoint segment is a polytope edge. Each icosahedral triangle
# contributes a triangular facet; each icosahedral vertex contributes a
# pentagonal facet. Support inequalities and incidence are checked exactly.
iedges={frozenset(e):k for k,e in enumerate(IE)}
triangles=[t for t in combinations(range(12),3)
           if all(frozenset(e) in iedges for e in combinations(t,2))]
assert len(triangles)==20
faces=[]
for tri in triangles:
    face=tuple(iedges[frozenset(e)] for e in combinations(tri,2))
    p,q,r=(P[k] for k in face)
    normal=cross(vsub(q,p),vsub(r,p))
    assert not iszero(normal)
    bound=dot(normal,p)
    if bound.sign()<0:normal=neg(normal);bound=-bound
    assert all((dot(normal,v)-bound).sign()<=0 for v in P)
    assert {k for k,v in enumerate(P) if dot(normal,v)==bound}==set(face)
    faces.append(set(face))
for i in range(12):
    face={k for k,(j,l) in enumerate(IE) if i in (j,l)}
    assert len(face)==5
    normal=I[i]
    bound=dot(normal,P[next(iter(face))])
    assert {k for k,v in enumerate(P) if dot(normal,v)==bound}==face
    assert all((dot(normal,v)-bound).sign()<=0 for v in P)
    faces.append(face)
assert len(faces)==32
incidence=Counter()
for face in faces:
    side_edges=[(i,j) for i,j in PE if i in face and j in face]
    assert len(side_edges)==len(face)  # 3-cycle or 5-cycle
    assert Counter(i for e in side_edges for i in e)=={k:2 for k in face}
    incidence.update(map(frozenset,side_edges))
assert len(incidence)==60 and set(incidence.values())=={2}
assert set(incidence)==set(map(frozenset,PE))

# Each antipodal pair of midpoint vertices determines one mirror plane.
roots=[]; visited=set()
for i in range(30):
    if i in visited:continue
    j=next(j for j in range(30) if P[j]==neg(P[i]))
    roots.append(P[i]); visited.update((i,j))
assert len(roots)==15 and len(visited)==30

# Check all 15 reflections preserve the entire polyhedron vertex set;
# hence each is an exact geometric symmetry of the edge graph.
Pset=set(P)
for r in roots:
    den=dot(r,r)
    reflected={vsub(v,scale(F(2)*dot(v,r)/den,r)) for v in P}
    assert reflected==Pset

# The section-vertex formula counts strict edge crossings plus vertices on the plane.
def section_sides(u):
    a=[dot(v,u).sign() for v in P]
    strict=sum(a[i]*a[j]<0 for i,j in PE)
    zero=a.count(0)
    return strict+zero,strict,zero

# Exhaust the projective intersection lines of all distinct mirror planes.
axes={}
for i,j in combinations(range(15),2):
    x=cross(roots[i],roots[j])
    assert not iszero(x)
    key=projkey(x)
    axes.setdefault(key,set()).add((i,j))
assert len(axes)==31
axis_table=Counter(); sum_pairs=0
for x,pair_indices in axes.items():
    mirrors=[j for j,r in enumerate(roots) if dot(x,r)==Z]
    m=len(mirrors)
    assert len(pair_indices)==m*(m-1)//2
    sides,strict,zeros=section_sides(x)
    axis_table[(m,sides,strict,zeros)]+=1
    sum_pairs+=len(pair_indices)
assert sum_pairs==105
assert axis_table==Counter({(2,8,4,4):15,(3,6,0,6):10,(5,10,0,10):6}),axis_table

# The arrangement has 62 spherical vertices, 180 arcs and 120 chambers.
V=2*len(axes)
E=sum(2*m*cnt for (m,*_),cnt in axis_table.items())
FACES=2-V+E
assert (V,E,FACES)==(62,180,120)

# An exact interior direction has twelve edge crossings and no zero vertex.
u=(F(1),F(2),F(4))
assert all(dot(r,u)!=Z for r in roots)
assert section_sides(u)==(12,12,0)

# The spherical chamber containing u is a triangle with one 2-fold,
# one 3-fold and one 5-fold axial corner, checked by exact inequalities.
sign=[dot(r,u).sign() for r in roots]
corners=[]
for axis in axes:
    for x in (axis,neg(axis)):
        if all(s*dot(x,r).sign()>=0 for s,r in zip(sign,roots)):
            corners.append((x,sum(dot(x,r)==Z for r in roots)))
assert len(corners)==3 and sorted(m for _,m in corners)==[2,3,5],corners

# A typical mirror direction contains precisely one antipodal vertex pair.
wall=None
for r in roots:
    for vec in ((F(1),F(2),F(3)),(F(1),F(3),F(7)),(F(2),F(5),F(11))):
        x=cross(r,vec)
        if not iszero(x) and sum(dot(x,t)==Z for t in roots)==1:
            wall=x;break
    if wall is not None:break
assert wall is not None
assert section_sides(wall)==(10,8,2)

print('EXACT_SECTION_CERT_OK')
print('icosahedral_vertices=12 icosahedral_edges=30')
print('icosidodecahedral_vertices=30 icosidodecahedral_edges=60 mirrors=15')
print('spherical_arrangement=(62 vertices,180 arcs,120 triangular chambers)')
print('axis_orbits={(2fold,15 axes,8 sides),(3fold,10 axes,6 sides),(5fold,6 axes,10 sides)}')
print('generic=12 mirror_regular=10')
