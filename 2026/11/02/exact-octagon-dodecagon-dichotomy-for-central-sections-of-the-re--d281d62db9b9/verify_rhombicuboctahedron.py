"""Exact Q(sqrt(2)) certificate for central-plane section sidedness.

Run: python3 rhombicuboctahedron_verify.py
No nonstandard dependencies are required for the exact certificate.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import acos, pi, sqrt

class Q:
    __slots__=('p','q')
    def __init__(self,p=0,q=0):
        self.p=F(p);self.q=F(q)
    @staticmethod
    def coerce(x): return x if isinstance(x,Q) else Q(x)
    def __add__(self,x):
        x=self.coerce(x);return Q(self.p+x.p,self.q+x.q)
    __radd__=__add__
    def __neg__(self):return Q(-self.p,-self.q)
    def __sub__(self,x):return self+(-self.coerce(x))
    def __rsub__(self,x):return self.coerce(x)-self
    def __mul__(self,x):
        x=self.coerce(x);return Q(self.p*x.p+2*self.q*x.q,self.p*x.q+self.q*x.p)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.coerce(x);den=x.p*x.p-2*x.q*x.q
        assert den!=0
        return Q((self.p*x.p-2*self.q*x.q)/den,(self.q*x.p-self.p*x.q)/den)
    def __eq__(self,x):
        x=self.coerce(x);return self.p==x.p and self.q==x.q
    def sign(self):
        p,q=self.p,self.q
        if not q:return (p>0)-(p<0)
        if not p:return (q>0)-(q<0)
        if (p>0)==(q>0):return (p>0)-(p<0)
        t=p*p-2*q*q
        assert t!=0 # irrational sqrt(2) makes this automatic if p,q nonzero
        return ((p>0)-(p<0)) if t>0 else ((q>0)-(q<0))
    def __hash__(self):return hash((self.p,self.q))
    def __repr__(self):return f'({self.p}+{self.q}*sqrt2)'

Z=Q(0);ONE=Q(1);A=Q(1,1)

def vdot(p,q):return sum((a*b for a,b in zip(p,q)),Z)
def vsub(p,q):return tuple(a-b for a,b in zip(p,q))
def squared(p):return vdot(p,p)

# All signed coordinate permutations of (A,1,1), 24 unique vertices.
V=[]
for i in range(3):
    for s in product([-1,1],repeat=3):
        v=[Q(s[j]) for j in range(3)]
        v[i]=A*s[i]
        V.append(tuple(v))
assert len(V)==24 and len(set(map(str,V)))==24

# Equal-length edges, their degrees, and supporting facets.
E=[(i,j) for i,j in combinations(range(24),2) if squared(vsub(V[i],V[j]))==Q(4)]
assert len(E)==48
assert {sum(i in e for e in E) for i in range(24)}=={4}
print('EXACT_RHOMBICUBOCTAHEDRON_24_VERTICES_48_EDGES_PASSED')

# Fundamental chamber: normal (1,v,w), 0 <= w <= v <= 1.
# Only potentially sign-changing vertex-plane equations, up to sign:
# L1=A*v-w-1; L2=A*v+w-1; L3=A*w-v-1; L4=A*w+v-1.
LINES=((A,Q(-1),Q(-1)),(A,ONE,Q(-1)),(Q(-1),A,Q(-1)),(ONE,A,Q(-1)))
T=[(Z,Z),(ONE,Z),(ONE,ONE)]

def line(L,p):return L[0]*p[0]+L[1]*p[1]+L[2]
def clip(poly,L,s):
    if not poly:return []
    out=[]
    for k,p in enumerate(poly):
        q=poly[(k+1)%len(poly)]
        ap=line(L,p)*s;aq=line(L,q)*s
        if ap.sign()>=0:out.append(p)
        if ap.sign()*aq.sign()<0:
            z=tuple(p[i]+(q[i]-p[i])*ap/(ap-aq) for i in range(2))
            out.append(z)
    unique=[]
    for p in out:
        if not unique or unique[-1]!=p:unique.append(p)
    if len(unique)>1 and unique[0]==unique[-1]:unique.pop()
    return unique

def polygon_area(poly):
    return sum((poly[i][0]*poly[(i+1)%len(poly)][1] - poly[(i+1)%len(poly)][0]*poly[i][1]
                for i in range(len(poly))),Z)/2

regions=[]
for signs in product([-1,1],repeat=4):
    P=T[:]
    for L,s in zip(LINES,signs):P=clip(P,L,s)
    if len(P)<3 or polygon_area(P).sign()<=0:continue
    # For every original vertex, its dot product with (1,v,w) cannot change
    # sign inside a cell, since the entire boundary polygon is checked exactly.
    vertex_signs=[]
    for xyz in V:
        vals=[(xyz[0]+xyz[1]*v+xyz[2]*w).sign() for v,w in P]
        assert not(min(vals)<0 and max(vals)>0), (signs,xyz,vals)
        assert max(vals)>0 or min(vals)<0
        sg=1 if max(vals)>0 else -1
        vertex_signs.append(sg)
    N=sum(vertex_signs[i]!=vertex_signs[j] for i,j in E)
    regions.append((signs,N,P))

assert len(regions)==6
assert {(s,N) for s,N,_ in regions}=={
    ((-1,-1,-1,-1),8),
    ((-1,1,-1,-1),12),
    ((-1,1,-1,1),12),
    ((1,1,-1,-1),12),
    ((1,1,-1,1),12),
    ((1,1,1,1),12),
}
# The unique octagonal chamber has triangular planar coordinates,
# so its spherical area can be calculated by Girard's formula.
octagon=next(P for s,N,P in regions if N==8)
expected={(Z,Z),(ONE/A,Z),(ONE/(A+ONE),ONE/(A+ONE))}
assert set(octagon)==expected
print('EXACT_SIX_FUNDAMENTAL_SIGN_CHAMBERS_AND_8_OR_12_DICHOTOMY_PASSED')

# For the unique 8-sided cone the three inward normals are:
# g1=(0,0,1), g2=(0,1,-1), g3=(1,-A,-1).
g1=(Z,Z,ONE);g2=(Z,ONE,Q(-1));g3=(ONE,-A,Q(-1))
assert vdot(g1,g2)==Q(-1)
assert vdot(g1,g3)==Q(-1)
assert vdot(g2,g3)==ONE-A
assert squared(g1)==ONE and squared(g2)==Q(2)
assert squared(g3)==A*A+Q(2)
# Girard: angles pi/4, theta, theta where cos(theta)=1/sqrt(5+2sqrt(2)).
assert squared(g3)==Q(5,2)
assert (A-ONE)*(A-ONE)==Q(2)
alpha=acos(1/sqrt(5+2*sqrt(2)))
omega=2*alpha-3*pi/4
p8=12*omega/pi
p12=1-p8
assert 0<p8<1 and 0<p12<1
assert abs(p8-0.20786393703415587)<1e-13
print('EXACT_SPHERICAL_TRIANGLE_ANGLE_IDENTITIES_AND_PROBABILITY_PASSED')
print(f'P8={p8:.15f} P12={p12:.15f} E_SIDES={8*p8+12*p12:.15f}')
# Independent randomly oriented Gaussian normals, using a separate float evaluation.
import random
rng=random.Random(20261030)
vv=[tuple(float(c.p)+float(c.q)*sqrt(2) for c in row) for row in V]
trials=80000
cnt=0
for _ in range(trials):
    xyz=[rng.gauss(0,1) for j in range(3)]
    signs=[sum(x*y for x,y in zip(row,xyz))>0 for row in vv]
    sides=sum(signs[i]!=signs[j] for i,j in E)
    a0,a1,a2=sorted(map(abs,xyz),reverse=True)
    rule=8 if a0>(1+sqrt(2))*a1+a2 else 12
    assert sides==rule
    cnt+=(sides==8)
assert abs(cnt/trials-p8)<0.012
print('INDEPENDENT_GAUSSIAN_ORIENTATION_DIAGNOSTIC_PASSED',trials,cnt)
print('ALL_EXACT_CHECKS_PASSED')
