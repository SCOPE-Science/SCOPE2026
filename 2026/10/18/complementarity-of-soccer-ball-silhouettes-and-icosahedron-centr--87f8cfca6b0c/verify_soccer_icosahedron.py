#!/usr/bin/env python3
"""Exact sign-chamber certificate and independent projected-hull tests."""
import itertools, math, random
from collections import Counter, defaultdict

# Work in Z[sqrt(5)]. A pair (a,b) means a+b sqrt(5).
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sgn(a):
 p,q=a
 if q==0:return (p>0)-(p<0)
 if p==0:return (q>0)-(q<0)
 if (p>0)==(q>0):return (p>0)-(p<0)
 # Magnitude comparison is between p^2 and 5 q^2.
 if p*p==5*q*q:return 0
 return ((p>0)-(p<0)) if p*p>5*q*q else ((q>0)-(q<0))
def val(a):return a[0]+a[1]*math.sqrt(5)
Z=(0,0);two=(2,0);phi2=(1,1)
def dot(x,y):
 z=Z
 for a,b in zip(x,y):z=add(z,mul(a,b))
 return z
def addv(x,y):return tuple(add(a,b) for a,b in zip(x,y))
def subv(x,y):return tuple(add(a,neg(b)) for a,b in zip(x,y))
def cross(x,y):return (add(mul(x[1],y[2]),neg(mul(x[2],y[1]))),add(mul(x[2],y[0]),neg(mul(x[0],y[2]))),add(mul(x[0],y[1]),neg(mul(x[1],y[0]))))
def det(x,y,z):return dot(x,cross(y,z))
def numv(x):return tuple(val(a) for a in x)
def scale(x,k):
 if isinstance(x[0],int):return (x[0]*k,x[1]*k)
 return tuple((a[0]*k,a[1]*k) for a in x)
V=[]
for e in (-1,1):
 for f in (-1,1):
  V += [(Z,scale((1,0),2*e),scale(phi2,f)),(scale(two,e),scale(phi2,f),Z),(scale(phi2,f),Z,scale(two,e))]
assert len(V)==12 and len(set(V))==12
norms={dot(v,v) for v in V}
assert norms=={(10,2)},norms
# Edge criterion exact: dot=2+2 sqrt(5).
E=[(i,j) for i,j in itertools.combinations(range(12),2) if dot(V[i],V[j])==(2,2)]
assert len(E)==30 and all(sum(i in e for e in E)==5 for i in range(12))
Es=set(E)
F=[f for f in itertools.combinations(range(12),3) if all(tuple(sorted(e)) in Es for e in itertools.combinations(f,2))]
assert len(F)==20
W=[addv(addv(V[i],V[j]),V[k]) for i,j,k in F]
# Exactly 12 pentagons and 20 hexagons. Each original edge has two faces.
inc=defaultdict(list)
for fi,f in enumerate(F):
 for e in itertools.combinations(f,2):inc[tuple(sorted(e))].append(fi)
assert all(len(fs)==2 for fs in inc.values())
scored_edges=[(12+a,12+b) for a,b in inc.values()]+[(i,12+fi) for fi,f in enumerate(F) for i in f]
assert len(scored_edges)==90
# Representative antipodal vertex axes and 32 chamber centers.
axis=[]
for v in V:
 if all(v!=scale(w,-1) and v!=w for w in axis):axis.append(v)
assert len(axis)==6
assert all(sgn(det(*q))!=0 for q in itertools.combinations(axis,3))
centers=[('pentagon',v) for v in V]+[('hexagon',w) for w in W]
masks=set();records=[]
for kind,u in centers:
 ax=tuple(sgn(dot(u,w)) for w in axis)
 assert all(x!=0 for x in ax)
 assert ax not in masks,('duplicate region',kind,ax)
 masks.add(ax)
 normals=V+W
 nsg=[sgn(dot(u,w)) for w in normals]
 assert all(s!=0 for s in nsg)
 Nshadow=sum(nsg[i]!=nsg[j] for i,j in scored_edges)
 Vsg=nsg[:12];Nsection=sum(Vsg[i]!=Vsg[j] for i,j in E)
 records.append((kind,Nshadow,Nsection))
assert len(masks)==32
assert Counter(records)==Counter({('pentagon',20,10):12,('hexagon',18,12):20}), Counter(records)
print('EXACT_FACE_EDGE_GRAPH_OK',len(V),len(E),len(F),len(scored_edges))
print('EXACT_SIX_AXES_GENERAL_POSITION_OK',len(axis))
print('EXACT_32_CHAMBER_REPRESENTATIVES_AND_COMPLEMENTARITY_OK',Counter(records))
# Verify each hexagon is a centrally symmetric polygon: the six vertices
# (2 vertex_i + vertex_j)/3 over ordered pairs of its three original vertices.
for face in F:
 d=[addv(scale(V[i],2),V[j]) for i,j in itertools.permutations(face,2)]
 center=scale(W[F.index(face)],2)  # common sum of paired numerators
 assert all(any(addv(x,y)==center for y in d if x!=y) for x in d)
print('EXACT_20_CENTRALLY_SYMMETRIC_HEXAGON_FACES_OK')
# Normalized pairwise axis dot absolute value is 1/sqrt(5): (2+2sqrt5)/(10+2sqrt5).
assert all(dot(w,w)==(10,2) for w in axis)
for a,b in itertools.combinations(axis,2):
 t=dot(a,b)
 assert t in ((2,2),(-2,-2)),t
angle=math.acos(1/math.sqrt(5))
p=15*angle/math.pi-5
assert abs(p-0.28624573524350067)<1e-13
print('EXACT_SPHERICAL_CHAMBER_LAW_OK','Pr18=',f'{p:.15f}','Pr20=',f'{1-p:.15f}')
# Independent convex-hull projection of the actual 60 truncation vertices.
Q=[addv(scale(V[i],2),V[j]) for i,j in E for (i,j) in [(i,j),(j,i)]]
assert len(Q)==60 and len(set(Q))==60
Qf=[numv(x) for x in Q]
Vf=[numv(x) for x in V]
Wf=[numv(x) for x in W]
def hull_count(coords):
 p=sorted(coords)
 def cc(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lo=[]
 for x in p:
  while len(lo)>1 and cc(lo[-2],lo[-1],x)<=1e-11:lo.pop()
  lo.append(x)
 hi=[]
 for x in reversed(p):
  while len(hi)>1 and cc(hi[-2],hi[-1],x)<=1e-11:hi.pop()
  hi.append(x)
 return len(lo)+len(hi)-2
rng=random.Random(314159)
count=Counter()
for z in range(4000):
 u=[rng.gauss(0,1) for _ in range(3)];r=math.sqrt(sum(t*t for t in u));u=[t/r for t in u]
 j=min(range(3),key=lambda k:abs(u[k]));e=[0.,0.,0.];e[j]=1.
 e=[e[k]-sum(e[l]*u[l] for l in range(3))*u[k] for k in range(3)]
 t=math.sqrt(sum(v*v for v in e)); e=[v/t for v in e]
 g=[u[1]*e[2]-u[2]*e[1],u[2]*e[0]-u[0]*e[2],u[0]*e[1]-u[1]*e[0]]
 proj=[(sum(x[k]*e[k] for k in range(3)),sum(x[k]*g[k] for k in range(3))) for x in Qf]
 H=hull_count(proj)
 ss=[sum(u[k]*n[k] for k in range(3))>0 for n in Vf+Wf]
 S=sum(ss[i]!=ss[j] for i,j in scored_edges)
 T=sum(ss[i]!=ss[j] for i,j in E)
 assert H==S and S+T==30,(H,S,T,u)
 assert H in (18,20)
 count[H]+=1
assert abs(count[18]/4000-p)<.035,(count,p)
print('INDEPENDENT_4000_PROJECTED_CONVEX_HULLS_OK',dict(count))
print('ALL_SOCCER_SILHOUETTE_CHECKS_OK')
