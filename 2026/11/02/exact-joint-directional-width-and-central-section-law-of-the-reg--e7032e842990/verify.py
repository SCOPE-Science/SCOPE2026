"""Exact arrangement checks and numerical quadrature for the icosahedral joint width--section law."""
import itertools
import math
import random
import sympy as sp
from scipy.integrate import quad

phi=(1+sp.sqrt(5))/2
V=[]
for a in (-1,1):
    for b in (-1,1):
        V.extend(((sp.Integer(0),sp.Integer(a),b*phi),
                  (sp.Integer(a),b*phi,sp.Integer(0)),
                  (a*phi,sp.Integer(0),sp.Integer(b))))
V=list(dict.fromkeys(V))
assert len(V)==12
R2=sp.simplify(sum(x*x for x in V[0]))
assert all(sp.simplify(sum(x*x for x in v)-R2)==0 for v in V)

def dot(u,v):return sum(a*b for a,b in zip(u,v))
def subsimp(x):return sp.simplify(sp.expand(x))
def sgn(x):
    v=sp.sign(subsimp(x))
    assert v in (-1,0,1), (x,v)
    return int(v)
E=[(i,j) for i,j in itertools.combinations(range(12),2) if subsimp(sum((V[i][k]-V[j][k])**2 for k in range(3))-4)==0]
assert len(E)==30
F=[(i,j,k) for i,j,k in itertools.combinations(range(12),3) if all(tuple(sorted(p)) in E for p in ((i,j),(i,k),(j,k)))]
assert len(F)==20
# Vertex-neighbor rings, the nested spherical pentagon, and the Voronoi-side midpoints.
for q in V:
    nbr=[w for w in V if subsimp(dot(q,w)-phi)==0]
    assert len(nbr)==5 and all(subsimp(dot(q,w)/R2-1/sp.sqrt(5))==0 for w in nbr)
    assert all(subsimp(sum(w[k] for w in nbr)-sp.sqrt(5)*q[k])==0 for k in range(3))
    for w in nbr:
        mid=tuple(q[k]+w[k] for k in range(3))
        assert sgn(dot(mid,q)-dot(mid,w))==0
        assert all(sgn(dot(mid,q)-dot(mid,v))>=0 for v in V)
        assert all(sgn(dot(mid,v))>=0 for v in nbr)
        assert sum(sgn(dot(mid,v))==0 for v in nbr)==2
reps=[]
for v in V:
    if tuple(-x for x in v) not in reps:reps.append(v)
assert len(reps)==6
assert all(sgn(sp.det(sp.Matrix([reps[i] for i in ids])))!=0 for ids in itertools.combinations(range(6),3))

def pat(u):
    ss=tuple(sgn(dot(u,v)) for v in reps)
    assert all(t!=0 for t in ss)
    return ss

def cut(u):
    ss=[sgn(dot(u,v)) for v in V]
    assert all(t!=0 for t in ss)
    return sum(ss[i]!=ss[j] for i,j in E)

chambers={}
for q in V:
    p=pat(q)
    assert p not in chambers
    chambers[p]=10
    assert cut(q)==10
for i,j,k in F:
    u=tuple(V[i][p]+V[j][p]+V[k][p] for p in range(3))
    p=pat(u)
    assert p not in chambers
    chambers[p]=12
    assert cut(u)==12
assert len(chambers)==32
# Six great circles in general position produce exactly 6*5+2=32 cells.
# Every nonzero sign pattern identifies one convex spherical chamber.

h0=math.asin(1/math.sqrt(5))
h1=math.acos(math.sqrt((1+1/math.sqrt(5))/2))
c5=math.cos(math.pi/5)
def outradius(h):return math.atan(math.tan(h)/c5)
def segment(z,h):
    if z>=math.cos(h):return 0.
    return 2*(math.acos(max(-1,min(1,math.sin(h)/math.sqrt(1-z*z))))
              -z*math.acos(max(-1,min(1,z*math.tan(h)/math.sqrt(1-z*z)))))
def C(z,h):
    b=outradius(h)
    zb=math.cos(b)
    if z>=1:return 0.
    if z<=zb:return 2*math.pi*(1-zb)-5*segment(zb,h)
    if z>=math.cos(h):return 2*math.pi*(1-z)
    return 2*math.pi*(1-z)-5*segment(z,h)

assert abs(outradius(h0)-h1)<1e-12
assert abs(C(-1,h1)-math.pi/3)<1e-12
P10=3*C(-1,h0)/math.pi
P12=3*(C(-1,h1)-C(-1,h0))/math.pi
P12lit=15*math.acos(1/math.sqrt(5))/math.pi-5
assert abs(P12-P12lit)<1e-12 and abs(P10+P12-1)<1e-12
# Compare cap intersection to a wholly separate radial/angular integral.
def numerical_cap(z,h):
    rad=outradius(h)
    rho=min(rad,math.acos(max(-1,min(1,z))))
    if rho<=0:return 0.
    def ang(t):
        if t<=h:return 2*math.pi
        zz=math.tan(h)/math.tan(t)
        return 2*math.pi-10*math.acos(max(-1,min(1,zz)))
    return quad(lambda t:ang(t)*math.sin(t),0,rho,points=[h] if 0<h<rho else None,epsabs=1e-11)[0]
for h in (h0,h1):
    for z in (-0.5,0,0.7,0.8,0.84,0.87,0.89,0.93,0.99,1.01):
        assert abs(C(z,h)-numerical_cap(z,h))<5e-10,(h,z,C(z,h),numerical_cap(z,h))
# Monte Carlo direct edge crossing and independent normalized width on same sampled normals.
rng=random.Random(20310930)
vf=[tuple(float(t) for t in v) for v in V]
R=math.sqrt(float(R2))
Nsim=30000
bins={(10,0):0,(10,1):0,(12,0):0,(12,1):0}
threshold=0.87
for _ in range(Nsim):
    xyz=[rng.gauss(0,1) for i in range(3)]
    nn=math.sqrt(sum(t*t for t in xyz));xyz=[t/nn for t in xyz]
    ss=[sum(a*b for a,b in zip(xyz,v)) for v in vf]
    n=sum((ss[i]>0)!=(ss[j]>0) for i,j in E)
    assert n in (10,12)
    w=max(ss)/R
    bins[n,int(w>=threshold)]+=1
p10hi=3*C(threshold,h0)/math.pi
p12hi=3*(C(threshold,h1)-C(threshold,h0))/math.pi
assert abs(bins[10,1]/Nsim-p10hi)<0.02
assert abs(bins[12,1]/Nsim-p12hi)<0.02
print('ALL_EXACT_ARRANGEMENT_AND_AREA_CHECKS_PASSED')
print('vertices=',len(V),'edges=',len(E),'faces=',len(F),'sign_cells=',len(chambers))
print('inradii=',h0,h1,'outer circ=',outradius(h1))
print('joint class masses=',P10,P12,'threshold=',threshold,'joint survival=',p10hi,p12hi)
print('empirical joint survival=',bins[10,1]/Nsim,bins[12,1]/Nsim)
