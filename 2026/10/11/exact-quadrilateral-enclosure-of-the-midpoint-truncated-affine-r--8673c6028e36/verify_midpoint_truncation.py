"""Exact algebraic enumeration of minimum-area enclosing quadrilaterals.
Requires SymPy. Uses DePano's three-edge flush and midpoint lemmas.
"""
from sympy import QQ, sqrt, S, simplify
from itertools import combinations
from functools import lru_cache
K=QQ.algebraic_field(sqrt(5))
T=K.from_sympy(S(1)/2)
ONE=K.one; ZERO=K.zero
PHI=K.from_sympy((1+sqrt(5))/2)
P=((ZERO,ONE-T),(-ONE,ZERO),(ONE-PHI,-PHI),(PHI-ONE,-PHI),(ONE,ZERO))
L=( ((T-ONE,ONE),ONE-T), ((-PHI,PHI-2),PHI), ((ZERO,-ONE),PHI), ((PHI,PHI-2),PHI), ((ONE-T,ONE),ONE-T) )

def dot(x,y):return x[0]*y[0]+x[1]*y[1]
def cross(x,y):return x[0]*y[1]-x[1]*y[0]
def sign(x):
 if x==ZERO:return 0
 z=K.to_sympy(x);i=z.is_positive
 if i is None:
  s=simplify(z).is_positive
  assert s is not None,(z,'undecidable sign')
  i=s
 return 1 if i else -1

def xyinter(l,r):
 (a,b),h=l;(c,d),k=r;den=a*d-b*c
 if sign(den)==0:return None
 return ((h*d-b*k)/den,(a*k-h*c)/den)

def polyarea(lines):
 # Compute cyclic order numerically only to select permutation.
 # All geometric predicates, including strict adjacent-angle determinants,
 # are subsequently verified exactly in Q(sqrt5).
 import math
 n=[(float(K.to_sympy(l[0][0])),float(K.to_sympy(l[0][1]))) for l in lines]
 ids=sorted(range(4),key=lambda i:math.atan2(n[i][1],n[i][0]))
 ls=[lines[i] for i in ids]
 if any(sign(cross(ls[i][0],ls[(i+1)%4][0]))<=0 for i in range(4)):return None
 v=[xyinter(ls[i],ls[(i+1)%4]) for i in range(4)]
 if any(x is None for x in v):return None
 if any(sign(dot(l[0],p)-l[1])>0 for l in ls for p in v):return None
 area=sum((cross(v[i],v[(i+1)%4]) for i in range(4)),ZERO)/2
 if sign(area)<=0:return None
 return area

# Exact Q0 upper construction: normals of edges 1,2,3 and horizontal top.
q=(ONE+PHI-T)*(PHI+PHI**(-3)*(ONE-T))
assert sign(q)>0
# Input hexagon is P with original apex replaced by two half-edge points.
PHEX=(( -T,ONE-T),P[1],P[2],P[3],P[4],(T,ONE-T))
hexarea=sum((cross(PHEX[i],PHEX[(i+1)%6]) for i in range(6)),ZERO)/2
assert sign(hexarea)>0
assert sign(hexarea-((2+PHI)-T*T))==0
# Every candidate comes from 3 original edges and either fourth edge or
# contact vertex as midpoint. There are 10*2+10*3*5*2 algebraic candidates.
counts={'total':0,'valid':0,'edge':0,'vertex':0,'equal':0}
minarea=None;minobj=[]
for triple in combinations(range(5),3):
 fixed=[L[i] for i in triple]
 for k in range(5):
  if k in triple:continue
  counts['total']+=1
  lines=fixed+[L[k]]
  a=polyarea(lines)
  if a is None:continue
  counts['valid']+=1;counts['edge']+=1
  assert sign(a-q)>=0,('EDGE violates',triple,k,K.to_sympy(a-q))
  if sign(a-q)==0:counts['equal']+=1;minobj.append((triple,('edge',k)))
 for i,j in combinations(range(3),2):
  ni,hi=fixed[i];nj,hj=fixed[j]
  for k in range(5):
   V=P[k];di=hi-dot(ni,V);dj=hj-dot(nj,V)
   assert sign(di)>=0 and sign(dj)>=0
   for sg in [1,-1]:
    counts['total']+=1
    nm=tuple(sg*(dj*ni[z]+di*nj[z]) for z in range(2))
    if nm==(ZERO,ZERO):continue
    hm=dot(nm,V)
    if any(sign(dot(nm,W)-hm)>0 for W in P):continue
    a=polyarea(fixed+[(nm,hm)])
    if a is None:continue
    counts['valid']+=1;counts['vertex']+=1
    assert sign(a-q)>=0,('VERTEX violates',triple,i,j,k,sg,K.to_sympy(a-q))
    if sign(a-q)==0:counts['equal']+=1;minobj.append((triple,('vertex',(i,j),k,sg)))
assert counts['total']==320
assert counts['valid']>0 and counts['equal']>0
print('VERIFY_OK',counts)
print('q=',simplify(K.to_sympy(q)),'hexarea=',simplify(K.to_sympy(hexarea)),'ratio=',simplify(K.to_sympy(q/hexarea)))
print('equality_candidates=',minobj)
