#!/usr/bin/env python3
"""Reproduce the exact central-section side-count law of a regular truncated tetrahedron.

Only the Python standard library is required. Integer arithmetic determines
all spherical chambers and their angle signatures; floating point arithmetic
is used solely to evaluate the resulting exact arccosine expressions and to
perform independent geometric spot checks.
"""
import itertools
import math
import random
from collections import Counter, defaultdict


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a, b, c):
    return dot(a, cross(b, c))


def neg(a):
    return tuple(-x for x in a)


def primitive(a):
    g = math.gcd(*a)
    return None if g == 0 else tuple(x//g for x in a)


def sq(a):
    return dot(a, a)


V = sorted({tuple((3 if j == i else 1)*s[j] for j in range(3))
            for s in itertools.product((-1, 1), repeat=3)
            if math.prod(s) == 1 for i in range(3)})
assert len(V) == 12 and {sq(v) for v in V} == {11}
E = [(i,j) for i,j in itertools.combinations(range(12),2)
     if sq(tuple(V[i][k]-V[j][k] for k in range(3))) == 8]
assert len(E) == 18
T = [s for s in itertools.product((-1,1),repeat=3) if math.prod(s) == 1]
assert len(T) == 4
assert all(-3 <= dot(v,t) <= 5 for v in V for t in T)
assert all(sum(dot(v,t) == 5 for t in T) == 1 and
           sum(dot(v,t) == -3 for t in T) == 2 for v in V)
# Verify the eight half-space inequalities have no additional vertices.
from fractions import Fraction
halfspaces=[(t,5) for t in T]+[(t,-3) for t in T]
extreme=set()
for (a,h),(b,k),(c,l) in itertools.combinations(halfspaces,3):
    denominator=det(a,b,c)
    if denominator==0:continue
    ca,cb,cc=cross(b,c),cross(c,a),cross(a,b)
    point=tuple(Fraction(h*ca[j]+k*cb[j]+l*cc[j],denominator)
                for j in range(3))
    if all(-3<=dot(t,point)<=5 for t in T):extreme.add(point)
assert extreme==set(V)
print('EIGHT_HALFSPACE_FACETS_RECONSTRUCT_EXACTLY_TWELVE_VERTICES_OK')
assert all(det(*trip) != 0 for trip in itertools.combinations(V,3))
print('TWELVE_VERTICES_EIGHT_FACETS_EIGHTEEN_EDGES_NO_TRIPLE_GREAT_CIRCLE_INTERSECTIONS_OK')

rays = sorted({d for i,j in itertools.combinations(range(12),2)
               for p in [primitive(cross(V[i],V[j]))]
               if p is not None for d in (p,neg(p))})
assert len(rays) == 132
# Each admissible signed chamber is represented by its sign mask.
# Every extreme ray is an intersection of two of the great circles.
compatible = defaultdict(set)
for d in rays:
    signs = [1 if dot(v,d)>0 else -1 if dot(v,d)<0 else 0 for v in V]
    free = [i for i,s in enumerate(signs) if s == 0]
    fixed = sum(1<<i for i,s in enumerate(signs) if s < 0)
    for r in range(1<<len(free)):
        mask = fixed | sum(1<<i for j,i in enumerate(free) if r>>j & 1)
        compatible[mask].add(d)


def cyclic_order(points, center):
    # Exact polar sort in the plane perpendicular to the integer interior ray.
    from functools import cmp_to_key
    first = next(p for p in points if sq(cross(center,p)))
    cc=sq(center)
    axis=cross(center,first)
    def xy(p):
        return (dot(p,first)*cc-dot(p,center)*dot(first,center),
                dot(p,axis))
    def half(x,y):return 0 if y>0 or (y==0 and x>=0) else 1
    def compare(p,q):
        x,y=xy(p);X,Y=xy(q)
        hp,hq=half(x,y),half(X,Y)
        if hp!=hq:return -1 if hp<hq else 1
        z=x*Y-y*X
        assert z!=0 or p==q
        return -1 if z>0 else (1 if z<0 else 0)
    ordered=sorted(points,key=cmp_to_key(compare))
    assert all(det(center,ordered[j],ordered[(j+1)%len(ordered)])>0
               for j in range(len(ordered)))
    return ordered


def chamber(mask):
    candidates = compatible.get(mask,())
    if len(candidates)<3:
        return None
    c = tuple(sum(p[k] for p in candidates) for k in range(3))
    if not all(dot(v,c)*(-1 if (mask>>i)&1 else 1)>0
               for i,v in enumerate(V)):
        return None
    pts = cyclic_order(candidates,c)
    walls = []
    for j in range(len(pts)):
        x,y=pts[j],pts[(j+1)%len(pts)]
        wall=[i for i,v in enumerate(V) if dot(v,x)==0 and dot(v,y)==0]
        assert len(wall)==1
        walls.append(wall[0])
    angles=Counter()
    for j in range(len(pts)):
        i,k=walls[j-1],walls[j]
        ni=-1 if (mask>>i)&1 else 1
        nk=-1 if (mask>>k)&1 else 1
        angles[ni*nk*dot(V[i],V[k])]+=1
    n=sum(bool(mask>>i&1)!=bool(mask>>j&1) for i,j in E)
    area=2*math.pi-sum(h*math.acos(a/11) for a,h in angles.items())
    assert area>1e-10
    return n,len(pts),tuple(sorted(angles.items())),area


classes=Counter()
areas=defaultdict(float)
for mask in range(1<<12):
    out=chamber(mask)
    if out is None:continue
    n,m,sig,area=out
    classes[(n,m,sig)]+=1
    areas[n]+=area
EXPECTED={
 (4,4,((-5,1),(-1,2),(7,1))):24,
 (4,8,((7,4),(9,4))):6,
 (5,3,((-9,1),(-7,1),(1,1))):48,
 (5,5,((1,2),(5,2),(7,1))):24,
 (6,3,((-5,3),)):8,
 (6,4,((-7,1),(-1,2),(9,1))):24,
}
assert classes==EXPECTED, (classes, EXPECTED)
assert sum(classes.values())==134
assert abs(sum(areas.values())-4*math.pi)<1e-10
print('EXHAUSTIVE_4096_SIGN_MASKS_134_CHAMBERS_SIX_ANGLE_CLASSES_OK')
for (n,m,sig),count in sorted(classes.items()):
    area=2*math.pi-sum(k*math.acos(q/11) for q,k in sig)
    print('CLASS',n,'chamber_vertices',m,'count',count,
          'angle_signature',sig,'area',f'{area:.14f}')
p={n:areas[n]/(4*math.pi) for n in (4,5,6)}
assert abs(sum(p.values())-1)<1e-12
exact_mean=18*math.acos(7/11)/math.pi
assert abs(sum(n*p[n] for n in p)-exact_mean)<1e-12
print('EXACT_SPHERICAL_GIRARD_AREAS_AND_INDEPENDENT_EDGE_EXPECTATION_OK')
for n in (4,5,6):print('P',n,f'{p[n]:.15f}')
print('MEAN',f'{exact_mean:.15f}')

# Independently intersect the section plane with all pairs of the eight
# distinct supporting planes; never use the edge-based signs in this test.
facets=[(t,5) for t in T]+[(t,-3) for t in T]
def section_vertices(u):
    vals=[]
    for (a,h),(b,k) in itertools.combinations(facets,2):
        den=det(a,b,u)
        if abs(den)<1e-12:continue
        ca,cb=cross(b,u),cross(u,a)
        x=[(h*ca[i]+k*cb[i])/den for i in range(3)]
        if all(-3-1e-8<=dot(t,x)<=5+1e-8 for t in T):
            if not any(sum((x[j]-y[j])**2 for j in range(3))<1e-14 for y in vals):
                vals.append(x)
    return vals

rng=random.Random(108123)
for _ in range(600):
    u=[rng.gauss(0,1) for _ in range(3)]
    x=section_vertices(u)
    signs=[dot(v,u) for v in V]
    n=sum(signs[i]*signs[j]<0 for i,j in E)
    assert len(x)==n and n in p, (u,n,len(x))
print('INDEPENDENT_EIGHT_FACET_PAIR_SECTION_VERTEX_RECONSTRUCTION_OK_600')
counts=Counter()
for _ in range(80000):
    u=[rng.gauss(0,1) for _ in range(3)]
    s=[dot(v,u) for v in V]
    counts[sum(s[i]*s[j]<0 for i,j in E)]+=1
assert set(counts)=={4,5,6}
assert all(abs(counts[n]/80000-p[n])<0.008 for n in p)
print('INDEPENDENT_GAUSSIAN_SPHERE_MONTE_CARLO_OK_80000',dict(sorted(counts.items())))
print('ALL_REGULAR_TRUNCATED_TETRAHEDRON_CENTRAL_SECTION_CHECKS_OK')
