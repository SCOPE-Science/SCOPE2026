"""Exact golden-field chamber certificate for central rhombic-triacontahedron sections.

Run: python check_geometry.py
Dependencies: numpy, mpmath. Integer-pair arithmetic represents a+b*phi in Z[phi].
"""
import itertools
import math
import numpy as np
import mpmath as mp

Z=(0,0); I=(1,0); PH=(0,1)
def sadd(a,b): return (a[0]+b[0],a[1]+b[1])
def sneg(a): return (-a[0],-a[1])
def ssub(a,b): return sadd(a,sneg(b))
def smul(a,b): return (a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def sint(k): return (k,0)
def sgn(a):
    c=2*a[0]+a[1];d=a[1]
    if c==d==0: return 0
    if c>=0 and d>=0: return 1
    if c<=0 and d<=0: return -1
    if d>0: return 1 if 5*d*d>c*c else -1
    return 1 if c*c>5*d*d else -1

def va(*entries): return tuple(entries)
def vneg(x): return tuple(map(sneg,x))
def vadd(x,y): return tuple(sadd(a,b) for a,b in zip(x,y))
def vsub(x,y): return tuple(ssub(a,b) for a,b in zip(x,y))
def vscale(t,x): return tuple(smul(t,a) for a in x)
def dot(x,y):
    t=Z
    for a,b in zip(x,y):t=sadd(t,smul(a,b))
    return t
def cross(x,y):
    return va(ssub(smul(x[1],y[2]),smul(x[2],y[1])),ssub(smul(x[2],y[0]),smul(x[0],y[2])),ssub(smul(x[0],y[1]),smul(x[1],y[0])))
def det(x,y,z):return dot(x,cross(y,z))
def fl(a):return a[0]+a[1]*(1+5**.5)/2
def fv(v):return np.array([fl(x) for x in v])

g=[va(Z,I,PH),va(Z,sneg(I),PH),va(I,PH,Z),va(sneg(I),PH,Z),va(PH,Z,I),va(PH,Z,sneg(I))]
assert all(sgn(det(g[i],g[j],g[k])) for i,j,k in itertools.combinations(range(6),3))
assert len(set(g))==6
assert all(dot(x,x)==(2,1) for x in g)
assert all(dot(g[i],g[j]) in (PH,sneg(PH)) for i,j in itertools.combinations(range(6),2))
print('ALL_TWENTY_GENERATOR_TRIPLES_INDEPENDENT_EXACT')

# For each generator, ten arcs cut the circle of normals perpendicular to it.
# Arc mid-rays provide exact supporting normals and hence every true edge.
edges=set()
for i,vi in enumerate(g):
    rays=[vscale(sint(e),cross(vi,g[j])) for j in range(6) if j!=i for e in (-1,1)]
    assert len(set(rays))==10
    axis=fv(vi)
    e1=fv(rays[0]);e1=e1/np.linalg.norm(e1)
    e2=np.cross(axis,e1);e2/=np.linalg.norm(e2)
    rays.sort(key=lambda r:math.atan2(np.dot(fv(r),e2),np.dot(fv(r),e1)))
    patterns=set()
    for k in range(10):
        r0,r1=rays[k],rays[(k+1)%10]
        assert sgn(det(vi,r0,r1))==1, (i,k,'bad cyclic order')
        u=vadd(r0,r1)
        assert dot(u,vi)==Z
        signs=tuple(sgn(dot(u,g[j])) for j in range(6) if j!=i)
        assert all(s!=0 for s in signs)
        assert signs not in patterns
        patterns.add(signs)
        base=(Z,Z,Z)
        for j in range(6):
            if j!=i: base=vadd(base,vscale(sint(sgn(dot(u,g[j]))),g[j]))
        a=vsub(base,vi);b=vadd(base,vi)
        edges.add(frozenset((a,b)))
    assert len(patterns)==10
assert len(edges)==60
verts={v for e in edges for v in e}
assert len(verts)==32 and {vneg(x) for x in verts}==verts
radii={dot(v,v) for v in verts}
assert len(radii)==2 and sorted([sum(dot(v,v)==r for v in verts) for r in radii])==[12,20]
assert all(len({dot(v,v) for v in e})==2 for e in edges)
assert len({dot(*tuple(e)) for e in edges})==1
print('EXACT_32_VERTICES_60_EDGES_TWO_RADIAL_ORBITS_AND_EDGE_TRANSITIVITY')

# Standard spherical Coxeter triangle for the full icosahedral reflection group.
f=va(Z,I,PH)
g3=va(I,I,I)
h=va(I,sadd(I,PH),PH)
T=(f,g3,h)
borders=[]
for i in range(3):
    n=cross(T[i],T[(i+1)%3])
    if sgn(dot(n,T[(i+2)%3]))==-1:n=vneg(n)
    assert sgn(dot(n,T[(i+2)%3]))==1
    borders.append(n)
for n in borders:
    denominator=dot(n,n)
    for vi in g:
        numerator=vsub(vscale(denominator,vi),vscale(smul(sint(2),dot(n,vi)),n))
        assert any(numerator==vscale(denominator,x) or numerator==vscale(sneg(denominator),x) for x in g)
print('THREE_GOLDEN_REFLECTIONS_PRESERVE_ALL_SIX_GENERATORS')

A=va(sadd(I,PH),Z,sneg(PH))        # (phi^2,0,-phi)
B=va(I,I,sneg(I))                 # (1,1,-1)
C=va(sadd(I,PH),sneg(I),Z)        # (phi^2,-1,0)
P=va(I,sadd(sint(1),smul(sint(3),PH)),sadd(sint(2),smul(sint(3),PH)))
Q=va(I,sadd(I,PH),sadd(sint(2),PH))
R=va(I,ssub(sint(3),PH),PH)
assert dot(P,B)==Z and dot(P,borders[2])==Z
assert dot(Q,B)==Z and dot(Q,C)==Z and dot(Q,borders[0])==Z
assert dot(R,A)==Z and dot(R,borders[0])==Z
assert dot(h,A)==Z and dot(h,C)==Z

# Only three of sixteen antipodal vertex-normal circles cut the open Coxeter triangle.
axes=set()
for x in verts:
    if vneg(x) not in axes: axes.add(x)
assert len(axes)==16
crossers=[x for x in axes if -1 in [sgn(dot(x,t)) for t in T] and 1 in [sgn(dot(x,t)) for t in T]]
assert len(crossers)==3
for a in (A,B,C):assert any(cross(a,x)==(Z,Z,Z) for x in crossers)
for x in axes:
    if x not in crossers:
        signs=[sgn(dot(x,t)) for t in T]
        assert not (-1 in signs and 1 in signs)
print('EXACT_SIXTEEN_VERTEX_AXES_ONLY_THREE_INTERIOR_CUTTING_CIRCLES')

triangles=[(f,P,Q),(P,Q,h),(Q,R,h),(R,g3,h)]
expected=[(-1,-1,-1),(-1,1,-1),(-1,1,1),(1,1,1)]
for k,tri in enumerate(triangles):
    for vi in tri:
        assert all(sgn(dot(n,vi))>=0 for n in borders)
    u=vadd(vadd(tri[0],tri[1]),tri[2])
    assert tuple(sgn(dot(a,u)) for a in (A,B,C))==expected[k]
    assert all(sgn(dot(u,v))!=0 for v in verts)
    c=sum(sgn(dot(u,x))*sgn(dot(u,y))<0 for x,y in (tuple(e) for e in edges))
    assert c==[10,12,14,12][k],(k,c)
print('FOUR_COMPLETE_GOLDEN_SPHERICAL_TRIANGLES_HAVE_10_12_14_12_SIDES')

mp.mp.dps=75
ph=(1+mp.sqrt(5))/2
def mv(v):return mp.matrix([mp.mpf(a)+mp.mpf(b)*ph for a,b in v])
def mdt(a,b):return sum(x*y for x,y in zip(a,b))
def nor(a):return mp.sqrt(mdt(a,a))
def omega(X,Y,Z):
    a,b,c=map(mv,(X,Y,Z))
    num=abs(mdt(a,mp.matrix([b[1]*c[2]-b[2]*c[1],b[2]*c[0]-b[0]*c[2],b[0]*c[1]-b[1]*c[0]])))
    den=nor(a)*nor(b)*nor(c)+mdt(a,b)*nor(c)+mdt(b,c)*nor(a)+mdt(c,a)*nor(b)
    return 2*mp.atan2(num,den)
areas=[omega(*tri) for tri in triangles]
assert abs(sum(areas)-mp.pi/30)<mp.mpf('1e-65')
ps=[mp.mpf(30)/mp.pi*(areas[0]),mp.mpf(30)/mp.pi*(areas[1]+areas[3]),mp.mpf(30)/mp.pi*(areas[2])]
assert abs(sum(ps)-1)<mp.mpf('1e-65')
mean=10*ps[0]+12*ps[1]+14*ps[2]
xx,yy=tuple(next(iter(edges)))
ct=mdt(mv(xx),mv(yy))/(nor(mv(xx))*nor(mv(yy)))
edge_mean=60/mp.pi*mp.acos(ct)
assert abs(mean-edge_mean)<mp.mpf('1e-65'),(str(mean),str(edge_mean))
assert abs(ct-ph**3/mp.sqrt((1+ph**2)*(1+ph**4)))<mp.mpf('1e-65')
print('ALL_SPHERICAL_EXCESS_AND_INDEPENDENT_SIXTY_EDGE_EXPECTATIONS_MATCH')
print('P10',mp.nstr(ps[0],30));print('P12',mp.nstr(ps[1],30));print('P14',mp.nstr(ps[2],30))
print('MEAN',mp.nstr(mean,30))

# Independent sampled normals, using the sixty exact combinatorial edges.
rng=np.random.default_rng(116083)
sample=rng.normal(size=(180000,3))
S=sample/np.linalg.norm(sample,axis=1)[:,None]
V={x:i for i,x in enumerate(verts)};Vlist=list(verts)
EV=np.array([[V[v] for v in e] for e in edges],dtype=int)
W=np.array([fv(x) for x in Vlist]);vsign=(S@W.T)>0
counts=(vsign[:,EV[:,0]]!=vsign[:,EV[:,1]]).sum(axis=1)
actual=np.array([(counts==n).mean() for n in (10,12,14)])
ideal=np.array([float(x) for x in ps]);assert set(np.unique(counts))=={10,12,14}
assert np.max(np.abs(actual-ideal))<0.006,(actual,ideal)
print('INDEPENDENT_UNIFORM_DIRECTION_180000_TRIAL_CHECK',actual)
print('ALL_GOLDEN_ZONOHEDRAL_SECTION_LAW_CHECKS_OK')
