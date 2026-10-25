"""Exact support-face and viewing-cell verification for the Miller–Aškinuze solid.
Standard Python 3 only. Algebraic field arithmetic is exact; metric angles are
numerical checks of independently derived finite solid-angle expressions.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import sqrt,atan,atan2,acos,pi
import random

class K:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        self.a=F(a);self.b=F(b)
    def __add__(self,y):
        y=K.of(y);return K(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,y):return self+-K.of(y)
    def __rsub__(self,y):return K.of(y)+-self
    def __mul__(self,y):
        y=K.of(y);return K(self.a*y.a+2*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,y):
        y=K.of(y);den=y.a*y.a-2*y.b*y.b
        assert den
        z=self*K(y.a,-y.b)
        return K(z.a/den,z.b/den)
    def __lt__(self,y):return (self-K.of(y)).sign()<0
    def __gt__(self,y):return (self-K.of(y)).sign()>0
    def __eq__(self,y):
        try:y=K.of(y);return self.a==y.a and self.b==y.b
        except:return False
    def __hash__(self):return hash((self.a,self.b))
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if (a>0)==(b>0):return (a>0)-(a<0)
        return ((a>0)-(a<0)) * ((a*a>2*b*b)-(a*a<2*b*b))
    def __float__(self):return float(self.a)+float(self.b)*sqrt(2)
    @staticmethod
    def of(y):return y if isinstance(y,K) else K(y)

Z=K();O=K(1);R=K(0,1);E=O+R

def sub(v,w):return tuple(x-y for x,y in zip(v,w))
def dot(v,w):return sum((x*y for x,y in zip(v,w)),Z)
def cross(v,w):return (v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])
def vec(*s):return tuple(K.of(z) for z in s)

V=[vec(E,0,s*R) for s in (-1,1)] + [vec(E,s*R,0) for s in (-1,1)]
V += [vec(a,b,c*E) for a,b,c in product((-1,1),repeat=3)]
V += [vec(a,b*E,c) for a,b,c in product((-1,1),repeat=3)]
V += [vec(-E,b,c) for b,c in product((-1,1),repeat=2)]
assert len(V)==24 and len(set(V))==24
# Fundamental-wedge reductions: quarter-turn, mirror, and gyro-reflection.
assert {vec(x,-z,y) for x,y,z in V}==set(V)
assert {vec(x,z,y) for x,y,z in V}==set(V)
assert {vec(-x,(y-z)/R,(y+z)/R) for x,y,z in V}==set(V)
print('EXACT_ORDER_16_GYROBICUPOLA_SYMMETRY_WEDGE_OK')

# Reconstruct every supporting plane independently from all vertex triples.
faces={}
for i,j,k in combinations(range(24),3):
    n=cross(sub(V[j],V[i]),sub(V[k],V[i]))
    if all(x==Z for x in n):continue
    signs=[dot(n,sub(v,V[i])).sign() for v in V]
    if max(signs)>0 and min(signs)<0:continue
    if min(signs)<0:n=tuple(-x for x in n);signs=[-x for x in signs]
    f=tuple(i for i,s in enumerate(signs) if s==0)
    faces.setdefault(f,n)
assert len(faces)==26 and sorted(map(len,faces))==[3]*8+[4]*18
flist=list(faces);normals=[faces[f] for f in flist]
edges=[]
for i,j in combinations(range(26),2):
    s=set(flist[i]).intersection(flist[j])
    if len(s)==2:edges.append((i,j,tuple(sorted(s))))
assert len(edges)==48 and len({z for _,_,z in edges})==48
assert {x for f in flist for x in f}==set(range(24))
print('EXACT_HULL_SUPPORT_24_VERTICES_26_FACETS_48_EDGES_OK')

# No other event lines occur within the fundamental spherical wedge.
fun=lambda q:[q,R*q,(O-q)/R,(O+q)/R,O-q,O,O+q,R]
qtest=K(F(1,5))
vals=fun(qtest)
for n in normals:
    if n[0]==Z:
        assert (n[1]+qtest*n[2]).sign()!=0
        # A zero can enter only through q=0 or q=1 in the closed wedge.
        if n[2]!=Z:
            qt=-n[1]/n[2]
            assert not (Z<qt<O)
    else:
        t0=-n[1]/n[0];t1=-n[2]/n[0]
        p=t0+t1*qtest
        # An affine event has positive p somewhere in (0,1) iff its
        # maximum at an endpoint is positive.
        if max(t0,t0+t1)>Z:
            branches=[(Z,O),(Z,R),(O/R,-O/R),(O/R,O/R),
                      (O,-O),(O,Z),(O,O),(R,Z)]
            assert any(t0==a and t1==b for a,b in branches),(tuple(map(float,n)),float(t0),float(t1))
            assert p in vals,(tuple(map(float,n)),float(p))
print('EXACT_EIGHT_FACET_THRESHOLD_FAMILIES_OK')

qcuts=[Z,K(3,-2),K(F(1,3)),E-K(2),K(F(1,2)),R/2,O]
assert all(qcuts[i]<qcuts[i+1] for i in range(len(qcuts)-1))

def count(n):
    signs=[dot(x,n).sign() for x in normals]
    assert all(signs)
    return sum(signs[i]*signs[j]<0 for i,j,_ in edges)

def predicted(p,q):
    a=min(R*q,O-q);b=max(R*q,O-q)
    c=min(R,O+q);d=max(R,O+q)
    if p<a or p>d:return 10
    if a<p<b or c<p<d:return 11
    if b<p<c:return 12
    raise AssertionError('boundary direction')

samples=[]
for lo,hi in zip(qcuts,qcuts[1:]):
    q=(lo+hi)/2
    fs=sorted(fun(q))
    assert len(set(fs))==8,(float(q),[float(v) for v in fs])
    ps=[fs[0]/2]+[(x+y)/2 for x,y in zip(fs,fs[1:])]+[fs[-1]+O]
    for p in ps:
        got=count(vec(p,O,q));target=predicted(p,q)
        assert got==target,(float(p),float(q),got,target)
        samples.append((float(p),float(q),got))
assert len(samples)==54
print('EXACT_54_FUNDAMENTAL_CHAMBERS_AND_PIECEWISE_LAW_OK')

# The first moment is independently forced by the dihedral-normal angles.
angles=[]
for i,j,_ in edges:
    nn=normals[i];mm=normals[j]
    co=float(dot(nn,mm))/sqrt(float(dot(nn,nn))*float(dot(mm,mm)))
    angles.append(acos(max(-1,min(1,co))))
classes=(pi/4,atan(1/sqrt(2)))
assert sum(abs(a-classes[0])<1e-12 for a in angles)==24
assert sum(abs(a-classes[1])<1e-12 for a in angles)==24
assert all(min(abs(a-x) for x in classes)<1e-12 for a in angles)
print('TWENTY_FOUR_OF_EACH_DIHEDRAL_NORMAL_ANGLE_OK')

# Each event is an affine great-circle line in (p,q). The checked cells
# therefore cover all generic rays in the wedge, by continuity of signs.

def vv(x):return tuple(float(z) for z in x)
def area_triangle(x,y,z):
    import math
    triple=abs(x[0]*(y[1]*z[2]-y[2]*z[1])+x[1]*(y[2]*z[0]-y[0]*z[2])+x[2]*(y[0]*z[1]-y[1]*z[0]))
    def norm(a):return math.sqrt(sum(z*z for z in a))
    def prod(a,b):return sum(s*t for s,t in zip(a,b))
    den=norm(x)*norm(y)*norm(z)+prod(x,y)*norm(z)+prod(y,z)*norm(x)+prod(z,x)*norm(y)
    return 2*atan2(triple,den)

def strip(a,b,s,t):
    X=vv(vec(0,1,s));Y=vv(vec(a+b*s,1,s));Zp=vv(vec(a+b*t,1,t));W=vv(vec(0,1,t))
    return area_triangle(X,Y,Zp)+area_triangle(X,Zp,W)

r=float(E-K(2))
s=lambda a,b,lo,hi:strip(float(K.of(a)),float(K.of(b)),lo,hi)
p10=1+4/pi*(s(0,R,0,r)+s(1,-1,r,1)-s(R,0,0,r)-s(1,1,r,1))
p12=4/pi*(s(1,1,0,r)-s(1,-1,0,r)+s(R,0,r,1)-s(0,R,r,1))
p11=1-p10-p12
assert all(0<x<1 for x in (p10,p11,p12))
mean=10*p10+11*p11+12*p12
expected=6+24/pi*atan(1/sqrt(2))
assert abs(mean-expected)<2e-13,(mean,expected)
print('EXACT_SOLID_ANGLE_DECOMPOSITION_AND_EQUAL_MEAN_OK',p10,p11,p12,mean)

# Completely independent 2D projected convex hulls for generic directions.
random.seed(43945)
def hull_size(points):
    arr=sorted(set(points))
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    low=[]
    for p in arr:
        while len(low)>1 and turn(low[-2],low[-1],p)<=1e-10:low.pop()
        low.append(p)
    high=[]
    for p in reversed(arr):
        while len(high)>1 and turn(high[-2],high[-1],p)<=1e-10:high.pop()
        high.append(p)
    return len(low)+len(high)-2
for _ in range(1800):
    p=random.uniform(.001,3);q=random.uniform(.001,.999)
    nx,ny,nz=p,1.,q
    norm=sqrt(nx*nx+ny*ny+nz*nz);nx/=norm;ny/=norm;nz/=norm
    ax,ay,az=-ny,nx,0;an=sqrt(ax*ax+ay*ay);ax/=an;ay/=an
    bx,by,bz=ny*az-nz*ay,nz*ax-nx*az,nx*ay-ny*ax
    pts=[(float(v[0])*ax+float(v[1])*ay,float(v[0])*bx+float(v[1])*by+float(v[2])*bz) for v in V]
    got=hull_size(pts)
    pr=predicted(K(F(str(p))),K(F(str(q))))
    assert got==pr,(got,pr,p,q)
print('INDEPENDENT_1800_PROJECTED_HULLS_OK')
print('ALL_J37_SILHOUETTE_CHECKS_OK')
