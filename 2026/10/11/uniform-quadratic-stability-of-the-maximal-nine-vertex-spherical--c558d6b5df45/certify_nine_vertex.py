#!/usr/bin/env python3
"""Exact rational outward-interval proof for the 9-point volume Hessian.
Uses only Python's integer arithmetic; each interval contains its exact real value.
"""
from math import isqrt
from collections import Counter
S=10**18
class IV:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def rational(a,b=1):
        assert b>0
        return IV(a*S//b,-(-a*S//b))
    def __add__(self,b):
        b=asiv(b);return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,b): return self+-asiv(b)
    def __rsub__(self,b): return asiv(b)+-self
    def __mul__(self,b):
        b=asiv(b);a=[i*j for i in (self.lo,self.hi) for j in (b.lo,b.hi)]
        return IV(min(a)//S,-(-max(a)//S))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=asiv(b);assert b.lo>0 or b.hi<0
        vals=[(i*S,j) for i in (self.lo,self.hi) for j in (b.lo,b.hi)]
        return IV(min(a//b for a,b in vals),max(-(-a//b) for a,b in vals))
    def __repr__(self):return f'[{self.lo/S:.14g},{self.hi/S:.14g}]'
def asiv(x):return x if isinstance(x,IV) else IV.rational(x)
def vsub(a,b):return [x-y for x,y in zip(a,b)]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),IV.rational(0))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(a,b,c):return dot(a,cross(b,c))
def addto(a,b):return [x+y for x,y in zip(a,b)]
# For integer bounds A/S<sqrt(3)<(A+1)/S, every comparison is exact.
A=isqrt(3*S*S);assert A*A<3*S*S<(A+1)**2
sq3=IV(A,A+1); r=sq3-1
# Lower/upper rational enclosures of sqrt(2 sqrt(3)-3).
Nlo=2*A-3*S;Nhi=2*(A+1)-3*S
B=isqrt(Nlo*S);C=isqrt(Nhi*S)+1
assert B*B<=Nlo*S and C*C>Nhi*S
h=IV(B,C)
zero=IV.rational(0);one=IV.rational(1);half=IV.rational(1,2);sqrt3half=sq3*half
# a = equator triangle; u = midpoint-radius triangles, equilateral.
a=[[one,zero,zero],[-half,sqrt3half,zero],[-half,-sqrt3half,zero]]
u=[[half,sqrt3half,zero],[-one,zero,zero],[half,-sqrt3half,zero]]
p=a+[[r*t[0],r*t[1],h] for t in u]+[[r*t[0],r*t[1],-h] for t in u]
# T[i] two tangent unit vectors; all algebraic identities follow from r²+h²=1.
T=[]
for i in range(9):
 if i<3:
  x,y,_=p[i];T.append([[-y,x,zero],[zero,zero,one]])
 else:
  ux,uy,_=u[(i-3)%3];eps=1 if i<6 else -1
  T.append([[-uy,ux,zero],[-eps*h*ux,-eps*h*uy,r]])
# Listed outward facets; certify support, nondegeneracy, and 14 facets.
faces=[(7,2,4),(5,4,2),(3,0,6),(3,4,5),(3,5,0),
 (8,6,0),(8,7,6),(8,2,7),(8,0,5),(8,5,2),
 (1,6,7),(1,7,4),(1,3,6),(1,4,3)]
assert len(faces)==14 and len(set(map(frozenset,faces)))==14
# Euler/edge-incidence test: the 14 triangles form a closed two-sphere on 9 vertices.
edges=Counter(tuple(sorted(pair)) for f in faces for pair in
              [(f[0],f[1]),(f[1],f[2]),(f[2],f[0])])
assert set(sum((list(f) for f in faces),[]))==set(range(9))
assert len(edges)==21 and set(edges.values())=={2}
assert 9-len(edges)+len(faces)==2
margin=10**100
for i,j,k in faces:
 orient=det(p[i],p[j],p[k]);assert orient.lo>0
 for l in range(9):
  if l in (i,j,k):continue
  d=det(vsub(p[j],p[i]),vsub(p[k],p[i]),vsub(p[l],p[i]))
  assert d.hi<0,('facet support',i,j,k,l,d)
  margin=min(margin,-d.hi)
assert margin>5476*S//10000
# 14 triangular strict facets are the entire boundary because every triangulated
# convex polyhedral sphere on nine vertices has exactly 2V-4=14 triangles.
# Signed volume polynomial F=(1/6) sum det(v_i,v_j,v_k).
H=[[zero for _ in range(18)] for _ in range(18)]
grad=[[zero,zero,zero] for _ in range(9)]
for i,j,k in faces:
 for ii,jj,kk in [(i,j,k),(j,k,i),(k,i,j)]:
  grad[ii]=addto(grad[ii],[x/6 for x in cross(p[jj],p[kk])])
  for alpha in range(2):
   for beta in range(2):
    x=det(T[ii][alpha],T[jj][beta],p[kk])/6
    H[2*ii+alpha][2*jj+beta]=H[2*ii+alpha][2*jj+beta]+x
    H[2*jj+beta][2*ii+alpha]=H[2*jj+beta][2*ii+alpha]+x
for i in range(9):
 lam=dot(p[i],grad[i])
 for alpha in range(2):H[2*i+alpha][2*i+alpha]=H[2*i+alpha][2*i+alpha]-lam
# Verify first variation tangent-zero is symbolically exact separately in the argument.
# Interval output gives high-precision independent numerical cross-check.
max_grad_t=max(max(abs(dot(e,grad[i]).lo),abs(dot(e,grad[i]).hi)) for i in range(9) for e in T[i])
print("grad",max_grad_t,max_grad_t/S)
assert max_grad_t<2000  # all tangent gradients within 2e-15.
# Infinitesimal rotations columns W_a; by rotational invariance and stationarity
# they lie in kernel of H. Their Gram matrix is diag(g,g,k) by 3-fold symmetry.
W=[[zero for _ in range(3)] for _ in range(18)]
unit=[[one,zero,zero],[zero,one,zero],[zero,zero,one]]
for i in range(9):
 for alpha in range(2):
  for j in range(3):W[2*i+alpha][j]=dot(T[i][alpha],cross(unit[j],p[i]))
g=IV.rational(15,2)-3*r*r
k=IV.rational(3)+6*r*r
# Verify the Gram identities to high precision, and explicit exactness follows
# from roots-of-unity cancellation and r²+h²=1.
for i in range(3):
 for j in range(3):
  q=sum((W[x][i]*W[x][j] for x in range(18)),zero)
  target=([g,g,k][i] if i==j else zero)
  assert max(abs((q-target).lo),abs((q-target).hi))<4000
# Rational interval certificate of PSD with gap 39/100 on rotation complement.
# C=-H+Proj_rot-(39/100)*I, where Proj_rot=W diag(1/g,1/g,1/k) W^T.
Cmat=[[zero for _ in range(18)] for _ in range(18)]
for i in range(18):
 for j in range(18):
  proj=sum((W[i][a]*W[j][a]/[g,g,k][a] for a in range(3)),zero)
  Cmat[i][j]=-H[i][j]+proj-(IV.rational(39,100) if i==j else zero)
# Interval LDL^T decomposition. Every pivot must be positive.
L=[[zero for j in range(18)] for i in range(18)]
D=[None]*18
for i in range(18):
 diag=Cmat[i][i]-sum((L[i][j]*L[i][j]*D[j] for j in range(i)),zero)
 assert diag.lo>0,(i,diag)
 D[i]=diag;L[i][i]=one
 for z in range(i+1,18):
  numer=Cmat[z][i]-sum((L[z][j]*L[i][j]*D[j] for j in range(i)),zero)
  L[z][i]=numer/diag
assert min(x.lo for x in D)>5575*S//100000
# Validate its interval decomposition contains each corresponding matrix coefficient.
for i in range(18):
 for j in range(i+1):
  reconstructed=sum((L[i][k]*D[k]*L[j][k] for k in range(j+1)),zero)
  assert reconstructed.lo<=Cmat[i][j].hi and reconstructed.hi>=Cmat[i][j].lo
print('VERIFY_OK')
print('facet support minimum strictly larger than',margin/S)
print('rotational Gram entries',g,k)
print('min rational interval LDL pivot >',min(x.lo for x in D)/S)
print('max first derivative tangent residual <=',max_grad_t/S)
print('negative Hessian spectral gap (rotation complement) > 0.39')
