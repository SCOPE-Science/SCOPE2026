#!/usr/bin/env python3
"""Exact finite certificate for icosahedral vertex-tetrahedron volume and equality loci.
Run with Python 3; integer-pair arithmetic in Z[phi], phi^2=phi+1.
"""
from itertools import combinations, product
from collections import Counter

Z=(0,0)
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def minus(a,b): return (a[0]-b[0],a[1]-b[1])
def times(a,b):
    x,y=a;u,v=b
    return (x*u+y*v,x*v+y*u+y*v)
def scal(a,s): return (s*a[0],s*a[1])
def sign(a):
    # a + b*phi = ((2a+b)+b*sqrt(5))/2.
    u,v=2*a[0]+a[1],a[1]
    if u==0: return (v>0)-(v<0)
    if v==0: return (u>0)-(u<0)
    if u*v>0: return (u>0)-(u<0)
    c=u*u-5*v*v
    if c==0: raise AssertionError('Unexpected sqrt(5) rationality')
    return ((c>0)-(c<0)) * ((u>0)-(u<0))
def absolute(a): return a if sign(a)>=0 else scal(a,-1)
def vecminus(x,y): return tuple(minus(a,b) for a,b in zip(x,y))
def cross(x,y): return (
    minus(times(x[1],y[2]),times(x[2],y[1])),
    minus(times(x[2],y[0]),times(x[0],y[2])),
    minus(times(x[0],y[1]),times(x[1],y[0])))
def dot(x,y):
    s=Z
    for a,b in zip(x,y): s=plus(s,times(a,b))
    return s
def determinant(x,y,z): return dot(x,cross(y,z))
def determinant2(x,y,z):
    # Algebraically independent six-term determinant implementation.
    a,b,c=x; d,e,f=y; g,h,i=z
    positive=plus(plus(times(a,times(e,i)),times(b,times(f,g))),times(c,times(d,h)))
    negative=plus(plus(times(c,times(e,g)),times(a,times(f,h))),times(b,times(d,i)))
    return minus(positive,negative)

one=(1,0); phi=(0,1)
V=[]
for a,b in product((-1,1),repeat=2):
    V += [(Z,scal(one,a),scal(phi,b)),
          (scal(one,a),scal(phi,b),Z),
          (scal(phi,a),Z,scal(one,b))]
assert len(V)==len(set(V))==12

volume_counts=Counter(); maxsets=set(); maxima_det=(4,8)
for ids in combinations(range(12),4):
    p,q,r,s=[V[i] for i in ids]
    x,y,z=vecminus(q,p),vecminus(r,p),vecminus(s,p)
    d=determinant(x,y,z)
    assert d==determinant2(x,y,z)
    d=absolute(d)
    volume_counts[d]+=1
    if d==maxima_det: maxsets.add(ids)
assert volume_counts==Counter({(0,0):75,(4,0):30,(0,4):180,(4,4):180,(4,8):30}),volume_counts
assert len(maxsets)==30

# Verify the 12-vertex configuration has precisely 20 triangular supporting facets.
def supporting_triangle(t):
    a,b,c=[V[i] for i in t]
    normal=cross(vecminus(b,a),vecminus(c,a))
    signs=[sign(dot(normal,vecminus(v,a))) for j,v in enumerate(V) if j not in t]
    return len(set(signs))==1 and signs[0]!=0
facets={t for t in combinations(range(12),3) if supporting_triangle(t)}
assert len(facets)==20

# The 20 movable-apex families: a rigid three-vertex base and an opposite facet.
apex_sets={t:tuple(j for j in range(12) if j not in t and tuple(sorted((*t,j))) in maxsets)
           for t in combinations(range(12),3)}
assert Counter(map(len,apex_sets.values()))==Counter({0:140,1:60,3:20})
families={t:tuple(sorted(v)) for t,v in apex_sets.items() if len(v)==3}
assert len(families)==20
assert set(families.values())==facets
assert all(tuple(sorted(f)) in facets for f in families.values())
assert all(tuple(sorted((*t,j))) in maxsets for t,f in families.items() for j in f)
assert all(len({determinant(vecminus(V[t[1]],V[t[0]]), vecminus(V[t[2]],V[t[0]]), vecminus(V[j],V[t[0]])) for j in f})==1 for t,f in families.items())
assert all(sum(set(t).issubset(s) for t in families)==2 for s in maxsets)

# Two independently movable vertices would force a 2x2 rectangle of maximizing
# four-vertex selections.  Verify that the finite maximum-set hypergraph has none.
grid_count=0
for base in combinations(range(12),2):
    leftover=[i for i in range(12) if i not in base]
    for a,b,c,d in combinations(leftover,4):
        for (u,v,w,z) in ((a,b,c,d),(a,c,b,d),(a,d,b,c)):
            if all(tuple(sorted((*base,i,j))) in maxsets for i in (u,v) for j in (w,z)):
                grid_count+=1
assert grid_count==0

# Independent numerical check of determinant levels at higher precision.
from decimal import Decimal,localcontext
with localcontext() as ctx:
    ctx.prec=60
    golden=(Decimal(1)+Decimal(5).sqrt())/Decimal(2)
    levels=sorted([Decimal(a)+Decimal(b)*golden for a,b in volume_counts])
    assert levels[0]==0 and levels[-1]==4*golden**3

# Representative supporting-pair witness.
example=min(maxsets)
print('VERIFY_OK vertex_sets=495 volume_levels=5 histogram=75,30,180,180,30 maxsets=30 families=20 facets=20 grids=0 witness='+str(example))
