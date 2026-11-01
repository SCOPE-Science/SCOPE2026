#!/usr/bin/env python3
"""Exact Q(sqrt(5)) incidence/sign certificate for icosahedron shadow counts.
Pure standard library. Numerical angles and simulations are secondary checks.
"""
from fractions import Fraction as F
import itertools, math, random

class K:
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,x):
        if not isinstance(x,K): x=K(x)
        return K(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,x):return self+-x if isinstance(x,K) else self+(-K(x))
    def __rsub__(self,x):return K(x)-self
    def __mul__(self,x):
        if not isinstance(x,K):x=K(x)
        return K(self.a*x.a+5*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        if not isinstance(x,K): x=K(x)
        den=x.a*x.a-5*x.b*x.b
        assert den
        return self*K(x.a/den,-x.b/den)
    def sign(self):
        a,b=self.a,self.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if (a>0)==(b>0):return (a>0)-(a<0)
        t=a*a-5*b*b
        if not t:return 0
        return ((a>0)-(a<0)) *((t>0)-(t<0))
    def __eq__(self,x):return (self-x).sign()==0
    def __lt__(self,x):return (self-x).sign()<0
    def __float__(self):return float(self.a)+float(self.b)*math.sqrt(5)
    def __repr__(self):return f'({self.a})+({self.b})sqrt5'
zero=K(0); one=K(1); root5=K(0,1);phi=(one+root5)/2;invphi=phi-one
assert (phi*invphi)==one

def V(*x):return tuple(x)
def scale(a,k):return tuple(k*y for y in a)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return V(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

# Icosahedron vertices; all coordinates lie in Q(sqrt5).
verts=[]
for s,t in itertools.product([-1,1],repeat=2):
    verts.extend([V(zero,K(s),K(t)*phi),V(K(s),K(t)*phi,zero),V(K(s)*phi,zero,K(t))])
assert len(verts)==12
# Outward normals to the twenty triangular facets, up to positive normalization sqrt(3).
normals=[]
for s,t,u in itertools.product([-1,1],repeat=3):normals.append(V(K(s),K(t),K(u)))
for s,t in itertools.product([-1,1],repeat=2):
    normals.extend([V(zero,K(s)*phi,K(t)*invphi),V(K(s)*invphi,zero,K(t)*phi),V(K(s)*phi,K(t)*invphi,zero)])
assert len(normals)==20 and len(set(map(str,normals)))==20
assert all(dot(n,n)==K(3) for n in normals)

facets=[]
for n in normals:
    h=max([dot(n,v) for v in verts])
    face=frozenset(i for i,v in enumerate(verts) if dot(n,v)==h)
    assert len(face)==3
    assert all((h-dot(n,v)).sign()>=0 for v in verts)
    facets.append(face)
assert len(set(facets))==20
edges=[(i,j) for i in range(20) for j in range(i+1,20) if len(facets[i]&facets[j])==2]
assert len(edges)==30
assert all(sum(i in z for z in edges)==3 for i in range(20))

# A is a fivefold icosahedron vertex axis; B is a threefold facet axis;
# C is the twofold midpoint of their incident edge. All UNNORMALIZED:
A0=V(zero,-one,-phi)
B0=V(-one,-one,-one)
C0=V(-invphi,-phi,-one)
assert dot(A0,A0)==phi+K(2)
assert dot(B0,B0)==K(3)
assert dot(C0,C0)==K(4)
assert A0 in verts and B0 in normals
assert any(set(face)>={verts.index(A0),verts.index(V(-one,-phi,zero))} for face in facets)

# Exactly ten oppositely paired facet normals have positive dot with B.
posB=[n for n in normals if dot(n,B0).sign()>0]
assert len(posB)==10
pattern_counts={}
for n in posB:
    pat=tuple(dot(n,z).sign() for z in [A0,B0,C0])
    pattern_counts[pat]=pattern_counts.get(pat,0)+1
assert pattern_counts=={(1,1,1):7,(1,1,0):1,(-1,1,0):1,(-1,1,1):1},pattern_counts
n7=V(-phi,invphi,zero)
n9=V(-one,-one,one)
assert n7 in posB and n9 in posB
assert dot(n7,A0).sign()<0 and dot(n7,C0)==zero
assert dot(n9,A0).sign()<0 and dot(n9,C0).sign()>0
# P is on the arc AB; D on AC. Two active great circles meet at P.
P0=add(A0,scale(B0,invphi))
D0=add(scale(A0,K(2)),C0)
assert dot(P0,P0)==K(8)
assert dot(D0,D0)==K(12)*phi*phi
assert dot(n7,P0)==zero and dot(n9,P0)==zero and dot(n9,D0)==zero

def cut_count(x):
    sg=[dot(n,x).sign() for n in normals]
    assert all(s!=0 for s in sg)
    return sum(sg[i]!=sg[j] for i,j in edges)

# Positive cones on three open spherical subtriangles A-D-P, D-C-P, C-B-P.
assert cut_count(add(add(A0,D0),P0))==10
assert cut_count(add(add(D0,C0),P0))==8
assert cut_count(add(add(C0,B0),P0))==6

# Three areas from spherical excess and exact trigonometric cosines.
phif=float(phi)
q=math.acos(1/math.sqrt(3))
r=math.acos(1/(phif*math.sqrt(3)))
omega10=q-3*math.pi/10
omega6=r+q-2*math.pi/3
omega8=math.pi/30-omega6-omega10
probs={6:30*omega6/math.pi,8:30*omega8/math.pi,10:30*omega10/math.pi}
assert all(p>0 for p in probs.values())
assert abs(sum(probs.values())-1)<2e-14

def uvec(x):
    a=[float(t) for t in x]
    norm=math.sqrt(sum(z*z for z in a))
    return tuple(t/norm for t in a)
def dfloat(x,y):return sum(a*b for a,b in zip(x,y))
def det3(x,y,z):
    return dfloat(x,(y[1]*z[2]-y[2]*z[1],y[2]*z[0]-y[0]*z[2],y[0]*z[1]-y[1]*z[0]))
def solid(x,y,z):
    return 2*math.atan2(abs(det3(x,y,z)),1+dfloat(x,y)+dfloat(y,z)+dfloat(z,x))
A,B,C,P,D=map(uvec,(A0,B0,C0,P0,D0))
assert abs(solid(A,B,C)-math.pi/30)<3e-14
for w,val in [(solid(A,D,P),omega10),(solid(D,C,P),omega8),(solid(C,B,P),omega6)]:
    assert abs(w-val)<3e-14,(w,val)
# Independently expected shadow polygon size from dihedral exterior angle.
expect=sum(k*p for k,p in probs.items())
assert abs(expect-30*math.acos(math.sqrt(5)/3)/math.pi)<1e-12

# Independent diagnostic: ordinary 2D convex-hull size of projected vertices,
# compared with the 30-edge signed dual cut, for 2000 reproducible directions.
def projected_count(direction):
    z=direction
    w=(1.,0.,0.) if abs(z[0])<.8 else (0.,1.,0.)
    ux=(z[1]*w[2]-z[2]*w[1],z[2]*w[0]-z[0]*w[2],z[0]*w[1]-z[1]*w[0])
    t=math.sqrt(dfloat(ux,ux));ux=tuple(a/t for a in ux)
    uy=(z[1]*ux[2]-z[2]*ux[1],z[2]*ux[0]-z[0]*ux[2],z[0]*ux[1]-z[1]*ux[0])
    pts=sorted((dfloat(uvec_:=tuple(float(a) for a in v),ux), dfloat(uvec_,uy)) for v in verts)
    def turn(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and turn(lo[-2],lo[-1],p)<=1e-12:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and turn(hi[-2],hi[-1],p)<=1e-12:hi.pop()
        hi.append(p)
    return len(lo)+len(hi)-2
rng=random.Random(170619)
freq={6:0,8:0,10:0}
for i in range(2000):
    z0=2*rng.random()-1;theta=2*math.pi*rng.random()
    rad=math.sqrt(1-z0*z0);z=(rad*math.cos(theta),rad*math.sin(theta),z0)
    hull_n=projected_count(z)
    sgn=[(dfloat(uvec(n),z)>0) for n in normals]
    cut_n=sum(sgn[j]!=sgn[k] for j,k in edges)
    assert hull_n==cut_n,(i,hull_n,cut_n)
    freq[hull_n]+=1
# Exact spherical angle certificates: both squared cosines and their signs
# belong to the quadratic field Q(sqrt5), even when actual cosines do not.
def angle_cos_sq(x,y,z):
    yy=dot(y,y)
    numer=dot(x,z)*yy-dot(x,y)*dot(y,z)
    den=(dot(x,x)*yy-dot(x,y)*dot(x,y))*(dot(z,z)*yy-dot(z,y)*dot(z,y))
    assert den.sign()>0
    return numer*numer/den, numer.sign()
for x,y,z,want_sq,want_sign in [
    (B0,A0,C0,phi*phi/K(4),1),
    (A0,B0,C0,one/K(4),1),
    (A0,C0,B0,zero,0),
    (D0,A0,P0,phi*phi/K(4),1),
    (A0,D0,P0,zero,0),
    (A0,P0,D0,one/K(3),1),
    (C0,B0,P0,one/K(4),1),
    (B0,C0,P0,one/(K(3)*phi*phi),1),
    (C0,P0,B0,one/K(3),1),
]:
    got,sgn=angle_cos_sq(x,y,z)
    assert got==want_sq and sgn==want_sign,(got,want_sq,sgn,want_sign)

print('EXACT_Q5_CHAMBERS_AND_SHADOW_COUNTS_OK')
print('20_facets_30_edges_exact, 10_signed_axes_exact, chamber_counts=[10,8,6]')
print('probs=',probs,'E=',expect,'simulation=',freq)
