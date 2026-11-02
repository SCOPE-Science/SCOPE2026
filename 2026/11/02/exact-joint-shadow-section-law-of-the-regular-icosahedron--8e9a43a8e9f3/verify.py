#!/usr/bin/env python3
"""Exact Q(sqrt(5)) certificate for the icosahedral shadow--section coupling.
Only the Python standard library is needed. No floating-point arithmetic is used
in graph, chamber, or containment certification.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
from math import acos, pi, sqrt

class Q:
    __slots__ = ('a','b')
    def __init__(self, a=0, b=0): self.a, self.b = F(a), F(b)
    def __add__(self, z):
        z = cv(z); return Q(self.a+z.a, self.b+z.b)
    __radd__ = __add__
    def __neg__(self): return Q(-self.a, -self.b)
    def __sub__(self, z): return self+-cv(z)
    def __rsub__(self,z): return cv(z)+-self
    def __mul__(self, z):
        z=cv(z); return Q(self.a*z.a+5*self.b*z.b, self.a*z.b+self.b*z.a)
    __rmul__ = __mul__
    def __eq__(self,z):
        z=cv(z); return self.a == z.a and self.b == z.b
    def sign(self):
        a,b=self.a,self.b
        if a==0:return (b>0)-(b<0)
        if b==0:return (a>0)-(a<0)
        if (a>0)==(b>0):return (a>0)-(a<0)
        z=a*a-5*b*b
        if z==0:raise AssertionError('sqrt5 rational contradiction')
        return ((a>0)-(a<0))*((z>0)-(z<0))
    def __hash__(self):return hash((self.a,self.b))
    def __repr__(self):return f'({self.a}+{self.b}sqrt5)'
def cv(x):return x if isinstance(x,Q) else Q(x)
Z=Q(); O=Q(1); T=Q(0,1); p=(O+T)*F(1,2); q=(T-O)*F(1,2)

def vec(*v):return tuple(map(cv,v))
def neg(v):return tuple(-x for x in v)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def triple(a,b,c):return dot(a,cross(b,c))
def add(*vv):return tuple(sum((v[i] for v in vv),Z) for i in range(3))
def sgn(x):return x.sign()

# One representative of each antipodal pair of icosahedron vertices
V=[vec(0,1,s*p) for s in (-1,1)]+[vec(1,s*p,0) for s in (-1,1)]+[vec(p,0,s) for s in (-1,1)]
# One representative of each antipodal pair of outward face normals
A=[vec(1,s,t) for s,t in product((-1,1),repeat=2)]+[vec(0,p,s*q) for s in (-1,1)]+[vec(p,s*q,0) for s in (-1,1)]+[vec(q,0,s*p) for s in (-1,1)]
assert len(V)==6 and len(A)==10
assert len(set(map(repr,V)))==6 and len(set(map(repr,A)))==10
assert all(dot(x,x)==p+2 for x in V)
assert all(dot(x,x)==3 for x in A)
assert all(triple(*t).sign()!=0 for t in combinations(V,3))
assert all(triple(*t).sign()!=0 for t in combinations(A,3))

vertices=V+[neg(x) for x in V]
faces=A+[neg(x) for x in A]
assert len(vertices)==12 and len(faces)==20
# Each supporting plane touches exactly three icosahedron vertices.
facets=[]
for a in faces:
    vals=[dot(a,v) for v in vertices]
    h=next(w for w in vals if all((w-v).sign()>=0 for v in vals))
    hit=tuple(i for i,w in enumerate(vals) if w==h)
    assert h==p+1 and len(hit)==3
    facets.append(hit)
assert len(set(tuple(sorted(x)) for x in facets))==20
Evertex={tuple(sorted(e)) for tri in facets for e in combinations(tri,2)}
assert len(Evertex)==30
assert all(sum(1 for e in Evertex if i in e)==5 for i in range(12))
# Dodecahedral dual graph, hence the set of silhouette edges.
Eface={tuple(sorted((i,j))) for i,j in combinations(range(20),2) if dot(faces[i],faces[j])==T}
assert len(Eface)==30
assert all(sum(1 for e in Eface if i in e)==3 for i in range(20))
assert Eface=={tuple(sorted((i,j))) for i,j in combinations(range(20),2) if len(set(facets[i])&set(facets[j]))==2}

def arrangement(normals):
    m=len(normals)
    corners=[]
    for i,j in combinations(range(m),2):
        r=cross(normals[i],normals[j]);assert any(z.sign() for z in r)
        for z in (r,neg(r)):
            signs=[sgn(dot(w,z)) for w in normals]
            assert signs.count(0)==2 and signs[i]==signs[j]==0
            corners.append((i,j,z,signs))
    assert len(corners)==m*(m-1)
    seen=set()
    for i,j,z,sg in corners:
        for si,sj in product((-1,1),repeat=2):
            ss=list(sg);ss[i]=si;ss[j]=sj
            seen.add(tuple(ss))
    assert len(seen)==m*(m-1)+2,(m,len(seen))
    regions={}
    for ss in seen:
        vv=[(i,j,z) for i,j,z,sg in corners if all(t*c>=0 for t,c in zip(ss,sg))]
        assert len(vv)>=3
        x=add(*(z for i,j,z in vv))
        assert all(sgn(dot(n,x))==s for n,s in zip(normals,ss)),(m,ss)
        regs=(ss,vv,x)
        regions[ss]=regs
    return regions

def silhouette(u):
    fsg=[sgn(dot(a,u)) for a in faces]
    assert all(fsg)
    return sum(fsg[i]!=fsg[j] for i,j in Eface)
def section(u):
    vsg=[sgn(dot(a,u)) for a in vertices]
    assert all(vsg)
    return sum(vsg[i]!=vsg[j] for i,j in Evertex)

RA=arrangement(A)
RV=arrangement(V)
assert len(RA)==92 and len(RV)==32
TA=Counter((len(vv),silhouette(x)) for ss,vv,x in RA.values())
TV=Counter((len(vv),section(x)) for ss,vv,x in RV.values())
assert TA=={(6,6):20,(3,8):60,(5,10):12},TA
assert TV=={(3,12):20,(5,10):12},TV
print('EXACT_12_VERTICES_20_FACES_30_EDGES_AND_DUAL_GRAPH_PASSED')
print('EXACT_NO_TRIPLE_GREAT_CIRCLE_CONCURRENCES_PASSED')
print('EXACT_SHADOW_92_CHAMBERS_20_HEX_60_TRI_12_PENT_PASSED')
print('EXACT_SECTION_32_CHAMBERS_20_TRI_12_PENT_PASSED')

# Establish each section-12 triangular normal cone is contained in one shadow-6 cone.
# Homogeneous linear inequalities can be tested on all extreme rays.
all_triangle_chambers=[]
for ss,vv,x in RV.values():
    if len(vv)!=3:continue
    all_triangle_chambers.append((ss,vv,x))
    signs=[sgn(dot(a,x)) for a in A]
    assert all(signs)
    for i,j,r in vv:
        assert all(sign*sgn(dot(a,r))>=0 for sign,a in zip(signs,A))
    assert silhouette(x)==6
assert len(all_triangle_chambers)==20
print('EXACT_ALL_20_SECTION_TWELVE_CONES_NESTED_IN_SHADOW_SIX_CONES_PASSED')

# Every interior angle comes from exactly two active halfspace normals.
# spherical angle = arccos(-s_i*s_j*(a_i.a_j)/||a_i||||a_j||).
def cornersignature(normals, reg, normsq):
    ss, vv, x=reg
    return Counter(-ss[i]*ss[j]*dot(normals[i],normals[j]) for i,j,r in vv)
SA=Counter()
for reg in RA.values():
    n=silhouette(reg[2]); sig=cornersignature(A,reg,3)
    SA[(n,tuple(sorted((str(k),c) for k,c in sig.items())))]+=1
SV=Counter()
for reg in RV.values():
    n=section(reg[2]);sig=cornersignature(V,reg,p+2)
    SV[(n,tuple(sorted((str(k),c) for k,c in sig.items())))]+=1
assert len(SA)==3 and len(SV)==2
for n in (6,8,10): assert sum(k[0]==n for k in SA)==1
for n in (10,12):assert sum(k[0]==n for k in SV)==1
# Mathematically exact angle signatures, without inverse-trig numerical classification.
assert all(cornersignature(A,r,3)==({Q(-1):3,Q(0,-1):3} if silhouette(r[2])==6 else {Q(1):2,Q(0,1):1} if silhouette(r[2])==8 else {Q(-1):5}) for r in RA.values())
# Check signatures for vertex-normal arrangement explicitly by algebraic equality.
for reg in RV.values():
    vals=cornersignature(V,reg,p+2)
    if section(reg[2])==12:
        assert vals=={p:3},vals
    else:
        assert vals=={-p:5},vals
print('EXACT_SPHERICAL_POLYGON_CORNER_ANGLE_SIGNATURES_PASSED')

# These are genuine exact analytic formulas for surface-area fractions via Girard.
alpha=acos(-1/3)
beta=acos(-sqrt(5)/3)
small=acos(1/sqrt(5))
S6=3*alpha+3*beta-4*pi
S8=2*acos(1/3)+acos(sqrt(5)/3)-pi
S10=5*alpha-3*pi
S12=3*small-pi
p6=20*S6/(4*pi)
p8=60*S8/(4*pi)
p10=12*S10/(4*pi)
p12=20*S12/(4*pi)
joint={(6,12):p12,(6,10):p6-p12,(8,10):p8,(10,10):p10}
assert all(z>0 for z in joint.values())
assert abs(sum(joint.values())-1)<1e-12
# Independent mean-angle check: 30 edge indicators each have probability delta/pi.
delta=acos(sqrt(5)/3)
assert abs(6*p6+8*p8+10*p10-30*delta/pi)<1e-12
print('EXACT_GIRARD_JOINT_PROBABILITY_FORMULAS_AND_CROFTON_EXPECTATION_PASSED')
for k,w in sorted(joint.items()):print('JOINT',k,format(w,'.12f'))
# Rational generic normals give strict nonempty interiors for all four joint events.
witness={}
for ix,iy,iz in product(range(-3,4),repeat=3):
    if (ix,iy,iz)==(0,0,0):continue
    u=vec(ix,iy,iz)
    if any(dot(u,z).sign()==0 for z in V+A):continue
    key=(silhouette(u),section(u))
    if key in joint and key not in witness:witness[key]=(ix,iy,iz)
assert set(witness)==set(joint),witness
print('EXACT_OPEN_INTERIOR_WITNESSES_FOR_ALL_FOUR_JOINT_CLASSES_PASSED',sorted(witness.items()))
print('ALL_CHECKS_PASSED')
