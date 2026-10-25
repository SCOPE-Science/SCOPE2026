"""Exact arithmetic reproducibility for a two-orbit icosahedral brightness-variance optimizer.
Requires only Python 3 standard library. Fractions certify all interval inequalities.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import isqrt

class Q:
    def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
    def __add__(x,y):
        y=q(y);return Q(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x):return Q(-x.a,-x.b)
    def __sub__(x,y):return x+-q(y)
    def __rsub__(x,y):return q(y)+-x
    def __mul__(x,y):
        y=q(y);return Q(x.a*y.a+x.b*y.b,x.a*y.b+x.b*y.a+x.b*y.b)
    __rmul__=__mul__
    def __truediv__(x,y):
        y=q(y); norm=y.a*y.a+y.a*y.b-y.b*y.b
        assert norm
        return x*Q((y.a+y.b)/norm,-y.b/norm)
    def __eq__(x,y):y=q(y);return x.a==y.a and x.b==y.b
    def __hash__(x):return hash((x.a,x.b))
    def __repr__(x):return '(%s)+(%s)phi'%(x.a,x.b)

def q(x):return x if isinstance(x,Q) else Q(x)
Z=Q(0);ONE=Q(1);PHI=Q(0,1)
def dot(a,b):return sum((i*j for i,j in zip(a,b)),Z)
V=[]
for s,t in product((-1,1),repeat=2):
    V.extend(((Z,q(s),t*PHI),(q(s),t*PHI,Z),(s*PHI,Z,q(t))))
assert len(V)==12 and len(set(map(str,V)))==12
edges=[(i,j) for i,j in combinations(range(12),2) if dot([a-b for a,b in zip(V[i],V[j])],[a-b for a,b in zip(V[i],V[j])])==q(4)]
assert len(edges)==30
E={frozenset(e) for e in edges}
tri=[tr for tr in combinations(range(12),3) if all(frozenset(e) in E for e in combinations(tr,2))]
assert len(tri)==20
W=[tuple(sum((V[k][j] for k in t),Z) for j in range(3)) for t in tri]

def cos2(a,b):return dot(a,b)*dot(a,b)/(dot(a,a)*dot(b,b))
AA={Q(1):24,Q(F(1,5)):120}
BB={Q(1):40,Q(F(1,9)):240,Q(F(5,9)):120}
AB={Q(F(7,15),F(-4,15)):120,Q(F(3,15),F(4,15)):120}
for A,B,hist in [(V,V,AA),(W,W,BB),(V,W,AB)]:
    actual={}
    for a in A:
        for b in B:
            t=cos2(a,b);actual[t]=actual.get(t,0)+1
    assert actual==hist,(actual,hist)
print('EXACT_TWO_NORMAL_ORBITS_FACES_12_20_EDGES_30_OK')
print('EXACT_ALL_144_400_240_PAIR_COSINES_OK')

# Rational interval helpers. Every transcendental or radical is enclosed by two Fractions.
N=10**35
def sqrt_lower(r):
    assert r>=0
    return F(isqrt((r.numerator*N*N)//r.denominator),N)
def sqrt_interval(r):
    if isinstance(r,tuple):lo,hi=r
    else:lo=hi=r
    a=sqrt_lower(lo);b=sqrt_lower(hi)+F(1,N)
    assert a*a<=lo<=hi<=b*b
    return a,b

def atan_interval(x,n):
    assert 0<x<1
    s=F(0)
    for k in range(n):s+=(-1)**k*x**(2*k+1)/F(2*k+1)
    d=x**(2*n+1)/F(2*n+1)
    if n%2: return s-d,s
    return s,s+d

p5=atan_interval(F(1,5),50)
p239=atan_interval(F(1,239),16)
PI=(16*p5[0]-4*p239[1],16*p5[1]-4*p239[0])
assert PI[0]>F(31415926535897932384,10**19) and PI[1]<F(31415926535897932386,10**19)
sqrt5=sqrt_interval(F(5))
phi=((1+sqrt5[0])/2,(1+sqrt5[1])/2)

def arc_interval(r,n=75):
    xlo,xhi=sqrt_interval(r)
    lo=hi=F(0); coefficient=F(1)
    for k in range(n):
        term=coefficient/F(2*k+1)
        lo+=term*xlo**(2*k+1)
        hi+=term*xhi**(2*k+1)
        coefficient*=F(2*k+1,2*k+2)
    hi+=xhi**(2*n+1)/(1-xhi*xhi)
    return lo,hi

def kernel_interval(r):
    if isinstance(r,Q):
        xlo=r.a+(r.b*(phi[0] if r.b>=0 else phi[1]))
        xhi=r.a+(r.b*(phi[1] if r.b>=0 else phi[0]))
    else:xlo=xhi=F(r)
    assert F(0)<=xlo<=xhi<F(1)
    s=sqrt_interval((1-xhi,1-xlo))
    al,ah=arc_interval((xlo,xhi))
    xl,xh=sqrt_interval((xlo,xhi))
    num=(s[0]+xl*al,s[1]+xh*ah)
    return (2*num[0]/(3*PI[1]),2*num[1]/(3*PI[0]))

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (c*a[0],c*a[1]) if c>=0 else(c*a[1],c*a[0])
def sub(a,b):return a[0]-b[1],a[1]-b[0]
G1=(F(1,3),F(1,3))
G5=kernel_interval(F(1,5)); G19=kernel_interval(F(1,9));G59=kernel_interval(F(5,9))
Gl=kernel_interval(Q(F(7,15),F(-4,15))); Gh=kernel_interval(Q(F(3,15),F(4,15)))
x=sub(scale(add(G1,scale(G5,5)),F(1,6)),(F(1,4),F(1,4)))
y=sub(scale(add(Gl,Gh),F(1,2)),(F(1,4),F(1,4)))
z=sub(scale(add(add(G1,scale(G19,6)),scale(G59,3)),F(1,10)),(F(1,4),F(1,4)))
assert F(3924,10**7)<x[0]<=x[1]<F(3925,10**7),x
assert F(-1745,10**7)<y[0]<=y[1]<F(-1743,10**7),y
assert F(1493,10**7)<z[0]<=z[1]<F(1495,10**7),z
print('CERTIFIED_EXACT_NEGATIVE_ORBIT_COVARIANCE_AND_POSITIVE_SELF_VARIANCES_OK')

denom=sub(add(x,z),scale(y,2));numer=sub(z,y)
plo=numer[0]/denom[1]; phi=numer[1]/denom[0]
assert F(3635,10000)<plo<=phi<F(3636,10000),(float(plo),float(phi))
print('CERTIFIED_INTERIOR_UNIQUE_OPTIMUM_AND_STABILITY_OK')
print('optimal_p_interval',float(plo),float(phi))
print('variance_coefficients_intervals',[(float(a),float(b)) for a,b in [x,y,z]])
print('ALL_EXACT_CERTIFICATES_OK')
