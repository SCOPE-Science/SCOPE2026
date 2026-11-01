"""Self-contained exact certificate for square-antiprism central sections.
Run: python verify.py .  Requires sympy, numpy (only for independent numerical diagnostic).
"""
import itertools,math,collections
from fractions import Fraction
from sympy import Matrix,sqrt,simplify,sign

s=sqrt(2)/2
V=[(1,0,1),(0,1,1),(-1,0,1),(0,-1,1),(s,s,-1),(-s,s,-1),(-s,-s,-1),(s,-s,-1)]
E=[(j,(j+1)%4) for j in range(4)]+[(4+j,4+(j+1)%4) for j in range(4)]+[(0,4),(0,7),(1,4),(1,5),(2,5),(2,6),(3,6),(3,7)]
assert len(E)==16 and len(set(tuple(sorted(e)) for e in E))==16
# Sign of determinant in Q(sqrt 2); rescale z to unit height, preserving the oriented matroid.
S={}
for i,j,k in itertools.combinations(range(8),3):
 d=simplify(Matrix([V[i],V[j],V[k]]).det())
 assert d!=0,(i,j,k)
 sg=sign(d)
 assert sg in (-1,1),(i,j,k,d,sg)
 S[(i,j,k)]=int(sg)
def detsign(i,j,k):
 if len({i,j,k})<3:return 0
 p=[i,j,k]; q=sorted(p)
 v=S[tuple(q)]
 inv=sum(p[a]>p[b] for a in range(3) for b in range(a+1,3))
 return (-1 if inv%2 else 1)*v
regions=set()
for i,j in itertools.combinations(range(8),2):
 for pole in (-1,1):
  side={k:pole*detsign(i,j,k) for k in range(8) if k not in (i,j)}
  for ai,aj in itertools.product((-1,1),repeat=2):
   side[i]=ai;side[j]=aj
   regions.add(tuple(side[k] for k in range(8)))
assert len(regions)==58,len(regions)
classes=collections.Counter(sum(a[i]!=a[j] for i,j in E) for a in regions)
assert classes=={6:24,8:34},classes
# Equidistant origin and 16 equal edges: physical height h=2^(-3/4).
h=2**(-.75)
import numpy as np
W=np.array([[float(x),float(y),h if i<4 else -h] for i,(x,y,z) in enumerate(V)])
radius2=1+h*h
assert max(abs(np.dot(v,v)-radius2) for v in W)<1e-12
assert max(abs(np.dot(W[i]-W[j],W[i]-W[j])-2) for i,j in E)<1e-12
cosangle=(2*sqrt(2)-1)/7
assert abs(float(cosangle)-(h*h/radius2))<1e-14
alpha=math.acos(float(cosangle))
p8=8*alpha/math.pi-3;p6=1-p8
assert 0<p8<1 and abs(p8-.3270440971384683)<1e-12
# Independent uniform-sphere diagnostic of crossing count and probability.
rg=np.random.default_rng(45791)
normals=rg.standard_normal((250000,3));vals=normals@W.T
counts=sum(((vals[:,i]>0)!=(vals[:,j]>0)).astype(int) for i,j in E)
assert set(np.unique(counts))=={6,8},set(np.unique(counts))
assert abs(np.mean(counts==8)-p8)<.005,(np.mean(counts==8),p8)
print('EXACT_56_TRIPLE_DETERMINANT_SIGNS_PASSED')
print('EXACT_58_SPHERICAL_SIGN_CHAMBERS_PASSED')
print('EXACT_6_OR_8_EDGE_CROSSING_CLASSIFICATION_PASSED',classes)
print('EXACT_EQUILATERAL_COSINE_IDENTITY_PASSED')
print('INDEPENDENT_GAUSSIAN_DIAGNOSTIC_PASSED',np.mean(counts==8),p8)
print('ALL_CHECKS_PASSED')
