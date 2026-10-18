#!/usr/bin/env python3
"""Exact Q(sqrt(5)) chamber/flux certificate for icosahedral shadows.
No floating point or external libraries are used in the certification.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter, defaultdict

def Q(a=0,b=0):return (F(a),F(b))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def div(a,b):
    den=b[0]*b[0]-5*b[1]*b[1]
    c=mul(a,(b[0],-b[1]));return(c[0]/den,c[1]/den)
def sg(a):
    x,y=a
    if x==0:return (y>0)-(y<0)
    if y==0:return (x>0)-(x<0)
    if (x>0)==(y>0):return (x>0)-(x<0)
    d=x*x-5*y*y
    assert d!=0
    return ((x>0)-(x<0)) if d>0 else ((y>0)-(y<0))
def dot(u,v):
    s=Q()
    for a,b in zip(u,v):s=add(s,mul(a,b))
    return s
def cross(u,v):
    return [sub(mul(u[1],v[2]),mul(u[2],v[1])),sub(mul(u[2],v[0]),mul(u[0],v[2])),sub(mul(u[0],v[1]),mul(u[1],v[0]))]
def scale(s,v):return [mul(s,x) for x in v]
def same(a,b):return a==b
def iszero(a):return a==Q()
def fmt(a):return f'({a[0]})+({a[1]})*sqrt(5)'

one=Q(1); zero=Q(); r=Q(F(-1,2),F(1,2));phi=Q(F(1,2),F(1,2))
axes=[]
for s,t in product([-1,1],repeat=2):axes.append([one,scale(Q(s),[one])[0],scale(Q(t),[one])[0]])
for t in [-1,1]:axes.append([zero,phi,mul(Q(t),r)])
for t in [-1,1]:axes.append([phi,mul(Q(t),r),zero])
for t in [-1,1]:axes.append([r,zero,mul(Q(t),phi)])
assert len(axes)==10 and all(dot(x,x)==Q(3) for x in axes)
faces=axes+[scale(Q(-1),x) for x in axes]
# Independently reconstruct the twenty supporting triangles of the regular icosahedron.
ico_vertices=[]
for s,t in product([-1,1], repeat=2):
    ico_vertices.extend([[zero,Q(s),mul(Q(t),phi)], [Q(s),mul(Q(t),phi),zero], [mul(Q(s),phi),zero,Q(t)]])
assert len(ico_vertices)==12
support=mul(phi,phi)
triangles=[]
for a in faces:
    vals=[dot(a,v) for v in ico_vertices]
    assert all(sg(sub(support,z))>=0 for z in vals)
    face_tri=tuple(i for i,z in enumerate(vals) if z==support)
    assert len(face_tri)==3
    for i,j in combinations(face_tri,2):
        delta=[sub(ico_vertices[i][k],ico_vertices[j][k]) for k in range(3)]
        assert dot(delta,delta)==Q(4)
    triangles.append(set(face_tri))
assert len({tuple(sorted(x)) for x in triangles})==20

pairs=list(combinations(range(10),2))
raw=[]
for i,j in pairs:
    z=cross(axes[i],axes[j]);assert any(not iszero(x) for x in z)
    for t in [-1,1]:
        w=scale(Q(t),z)
        d=[sg(dot(x,w)) for x in axes]
        assert d[i]==d[j]==0 and all(d[k]!=0 for k in range(10) if k not in (i,j))
        raw.append((i,j,w,tuple(d)))
assert len(raw)==90
cells=set()
for i,j,w,d in raw:
    for a,b in product([-1,1],repeat=2):
        s=list(d);s[i]=a;s[j]=b;cells.add(tuple(s))
assert len(cells)==92
icosa_edges=[(i,j) for i,j in combinations(range(20),2) if dot(faces[i],faces[j])==Q(0,1)]
assert len(icosa_edges)==30
facet_adj=[(i,j) for i,j in combinations(range(20),2) if len(triangles[i]&triangles[j])==2]
assert set(facet_adj)==set(icosa_edges)

assert Counter(x for ij in icosa_edges for x in ij)==Counter({i:3 for i in range(20)})

COS_H2=Q(F(7,16),F(3,16)) # ((3+sqrt(5))/(4sqrt(2)))^2
COS_P2=Q(F(23,32),F(3,32)) # ((1+3sqrt(5))/8)^2
CATS=Counter(); TYPES=Counter(); SUMS=defaultdict(lambda:[Q(),Q()]); EXAMPLES={}
angle_cats=defaultdict(Counter)
for s in cells:
    verts=[(i,j,w,d) for i,j,w,d in raw if all(s[k]*d[k]>=0 for k in range(10))]
    m=len(verts)
    # adjacency: each active great-circle side exactly two endpoints
    active=defaultdict(list)
    for vix,(i,j,w,d) in enumerate(verts):
        active[i].append(vix);active[j].append(vix)
        p=mul(Q(s[i]*s[j]),div(dot(axes[i],axes[j]),Q(3)))
        if p==Q(F(1,3)):angle_cats[s]['pi-alpha']+=1
        elif p==Q(F(-1,3)):angle_cats[s]['alpha']+=1
        elif p==Q(0,F(1,3)):angle_cats[s]['pi-beta']+=1
        elif p==Q(0,F(-1,3)):angle_cats[s]['beta']+=1
        else:raise AssertionError((p,s,i,j))
    assert len(active)==m and all(len(vs)==2 for vs in active.values())
    # Front/back normal signs indexed by signed facet representatives
    fs=list(s)+[-a for a in s]
    N=sum(fs[i]!=fs[j] for i,j in icosa_edges)
    TYPES[(N,m)]+=1
    for k,ends in active.items():
        a,b=verts[ends[0]][2],verts[ends[1]][2]
        z=div(mul(dot(a,b),dot(a,b)),mul(dot(a,a),dot(b,b)))
        assert sg(dot(a,b))>0
        if z==COS_H2:classkey='H'
        elif z==COS_P2:classkey='P'
        else:raise AssertionError(('bad edge cos^2',z))
        V=[Q() for _ in range(3)]
        for sig,axis in zip(s,axes):
            V=[add(x,mul(Q(sig),y)) for x,y in zip(V,axis)]
        coeff=div(mul(Q(s[k]),dot(V,axes[k])),Q(3))
        assert sg(coeff)>0
        SUMS[N][0 if classkey=='H' else 1]=add(SUMS[N][0 if classkey=='H' else 1],coeff)
        CATS[(N,classkey,coeff)]+=1
    EXAMPLES.setdefault(N,(s,m,angle_cats[s]))
assert TYPES==Counter({(6,6):20,(8,3):60,(10,5):12}),TYPES
assert Counter(tuple(sorted(v.items())) for v in angle_cats.values())==Counter({(('pi-alpha',3),('pi-beta',3)):20,(('alpha',2),('beta',1)):60,(('pi-alpha',5),):12})
# coefficients summed across all chambers, suitable for (1/2)(4*pi) flux factor
expected={
6: (mul(Q(20),Q(6+2*F(0),2)),Q()),
}
print('CHAMBERS_EXACT_OK',TYPES)
for N in [6,8,10]:
    print('CLASS',N,'spherical-angle-exemplar',EXAMPLES[N][2],
          'aggregate_H_coeff',fmt(SUMS[N][0]),'aggregate_P_coeff',fmt(SUMS[N][1]))
# From all 20 hexagons: coefficient H 20*(6*(3+sqrt5)/3)=40*(3+sqrt5)
assert SUMS[6]==[Q(120,40),Q()]
# From 60 triangles: H 60*(2*(3-sqrt5)/3)=40*(3-sqrt5), P 60*((1+sqrt5)/3)=20*(1+sqrt5)
assert SUMS[8]==[Q(120,-40),Q(20,20)]
# From 12 pentagons: P 12*(5*(5-sqrt5)/3)=20*(5-sqrt5)
assert SUMS[10]==[Q(),Q(100,-20)]
# Total formula: E[W1_{N=j}] = (H_sum*h+P_sum*p)/(8*pi).
# 6h+3p=pi, and E[W]=5 by Cauchy; exact coefficient balance:
assert add(add(SUMS[6][0],SUMS[8][0]),SUMS[10][0])==Q(240)
assert add(add(SUMS[6][1],SUMS[8][1]),SUMS[10][1])==Q(120)
print('EXACT_ICO_SHADOW_FLUX_CERTIFICATE_OK cells=92 plane_intersections=90')
