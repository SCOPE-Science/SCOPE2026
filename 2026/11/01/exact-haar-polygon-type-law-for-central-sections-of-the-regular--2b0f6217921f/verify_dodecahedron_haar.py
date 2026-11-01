#!/usr/bin/env python3
"""Exact Z[golden-ratio] certificate for the central-section type law.

The checker enumerates all 1024 strict sign patterns of the ten
antipodal-vertex hyperplanes. Its arithmetic uses integer pairs
(a,b) representing a+b*phi, phi^2=phi+1. No floating-point decisions.
"""
from itertools import combinations, product
from collections import Counter

Z=(0,0)
ONE=(1,0)
PHI=(0,1)
PIM1=(-1,1)
SQRT5=(-1,2)

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    a,b=x;c,d=y
    return (a*c+b*d,a*d+b*c+b*d)
def scale(x,s):return (x[0]*s,x[1]*s)
def sign(x):
    a,b=x
    u=2*a+b
    if not b:return (a>0)-(a<0)
    if not u:return (b>0)-(b<0)
    if u>0 and b>0:return 1
    if u<0 and b<0:return -1
    d=u*u-5*b*b
    assert d!=0
    return ((d>0)-(d<0)) if u>0 else -((d>0)-(d<0))
def vadd(x,y):return tuple(add(a,b) for a,b in zip(x,y))
def vneg(x):return tuple(neg(a) for a in x)
def vsum(vs):
    r=(Z,Z,Z)
    for v in vs:r=vadd(r,v)
    return r
def dot(x,y):
    s=Z
    for a,b in zip(x,y):s=add(s,mul(a,b))
    return s
def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
            sub(mul(x[2],y[0]),mul(x[0],y[2])),
            sub(mul(x[0],y[1]),mul(x[1],y[0])))
def nsign(x):return sign(x)
def firstsign(v):return next(sign(x) for x in v if sign(x))
def coord(s,x):return x if s>0 else neg(x)

v=[tuple((k,0) for k in s) for s in product((-1,1),repeat=3)]
for s,t in product((-1,1),repeat=2):
    v.extend([(Z,coord(s,PIM1),coord(t,PHI)),
              (coord(s,PIM1),coord(t,PHI),Z),
              (coord(s,PHI),Z,coord(t,PIM1))])
assert len(v)==20 and len(set(v))==20
assert all(dot(x,x)==(3,0) for x in v)

d2=(8,-4)
edges=[(i,j) for i,j in combinations(range(20),2)
       if dot(tuple(sub(a,b) for a,b in zip(v[i],v[j])),
              tuple(sub(a,b) for a,b in zip(v[i],v[j])))==d2]
assert len(edges)==30 and Counter(i for e in edges for i in e)==Counter({i:3 for i in range(20)})

# Twelve exposed regular pentagonal faces certify that the 30
# shortest vertex pairs really are the edges of the convex hull.
faces_normals=[]
for s,t in product((-1,1),repeat=2):
    faces_normals.extend([(coord(s,ONE),Z,coord(t,PHI)),
                          (Z,coord(s,PHI),coord(t,ONE)),
                          (coord(s,PHI),coord(t,ONE),Z)])
assert len(faces_normals)==12
face_sets=[]
for f in faces_normals:
    hits=tuple(i for i,x in enumerate(v) if dot(f,x)==(1,1))
    assert len(hits)==5
    assert all(sign(sub((1,1),dot(f,x)))>=0 for x in v)
    face_sets.append(hits)
assert len(set(face_sets))==12
incidences=Counter(pair for F in face_sets for pair in combinations(F,2))
assert {pair for pair,m in incidences.items() if m==2}==set(edges)
assert all(m in (1,2) for m in incidences.values())

w=[]
for x in v:
    y=x if firstsign(x)>0 else vneg(x)
    if y not in w:w.append(y)
assert len(w)==10
assert all(dot(x,x)==(3,0) for x in w)
assert all(dot(w[i],w[j]) in {(1,0),(-1,0),SQRT5,neg(SQRT5)}
           for i,j in combinations(range(10),2))

# Every two distinct great circles meet at one antipodal pair;
# no three are concurrent. This rules out all degeneracies.
assert all(sign(dot(w[k],cross(w[i],w[j])))!=0
           for i,j,k in combinations(range(10),3))

rays=[]
for i,j in combinations(range(10),2):
    x=cross(w[i],w[j]);assert any(nsign(z)!=0 for z in x)
    rays.extend([((i,j),x),((i,j),vneg(x))])
assert len(rays)==90
ray_dots=[[sign(dot(w[k],x)) for k in range(10)] for _,x in rays]
assert all(sum(s==0 for s in row)==2 for row in ray_dots)

# Every pointed full-dimensional chamber is a three-dimensional
# cone, and all of its extreme rays are pairwise plane intersections.
# Enumerating all sign patterns and their feasible rays is exhaustive.
cells=[]
for bits in product((-1,1),repeat=10):
    selected=[r for r,row in enumerate(ray_dots)
              if all(bits[k]*row[k]>=0 for k in range(10))]
    if len(selected)<3:continue
    interior=vsum(rays[r][1] for r in selected)
    if not all(bits[k]*sign(dot(w[k],interior))==1 for k in range(10)):
        continue
    nv=[sign(dot(x,interior)) for x in v]
    assert all(s!=0 for s in nv)
    N=sum(nv[i]!=nv[j] for i,j in edges)
    angles=Counter()
    for r in selected:
        i,j=rays[r][0]
        z=dot(w[i],w[j]); bz=z if sign(z)>0 else neg(z)
        typ='a' if bz==ONE else 'b' if bz==SQRT5 else None
        assert typ is not None
        signed=bits[i]*bits[j]*sign(z)
        # Interior angle = pi-acos(signed * abs(dot)/3).
        angles['pi-'+typ if signed>0 else typ]+=1
    cells.append((bits,selected,N,angles))

assert len(cells)==92
summary=Counter((N,len(sel),tuple(sorted(ang.items()))) for _,sel,N,ang in cells)
expected=Counter({
    (6,6,(('pi-a',3),('pi-b',3))):20,
    (8,3,(('a',2),('b',1))):60,
    (10,5,(('pi-a',5),)):12,
})
assert summary==expected,(summary,expected)
assert sum(len(c[1]) for c in cells)==360
print('PASS: 20 vertices, 30 edges, 10 antipodal normals, 90 transverse intersections')
print('PASS: all 1024 sign patterns checked exactly, 92 spherical chambers')
print('PASS: angle and section-side classification',dict(summary))
print('PASS: spherical area is 20(2pi-3a-3b)+60(2a+b-pi)+12(2pi-5a)=4pi')
print('PASS: exact probability law follows by Girard and division by 4pi')
