#!/usr/bin/env python3
"""Reproducible finite corroboration of tetrahedral silhouette-transfer formulas.
Requires numpy, scipy, sympy. Analytic proof is in RESULT.md.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

rng=np.random.default_rng(20260819)
base_shapes=[
 np.array([[1.,1.,1.],[1.,-1.,-1.],[-1.,1.,-1.],[-1.,-1.,1.]]),
 np.array([[0.,0.,0.],[2.,0.,0.],[.1,2.7,0.],[.4,.2,1.6]]),
 np.array([[0.,0.,0.],[3.,0.,0.],[.2,.2,0.],[.1,.02,.18]])
]
depths=np.array([.13,.23,.34,.28])
assert max(depths[i]+depths[j] for i in range(4) for j in range(i+1,4))<1


def face_normals(verts):
 out=[]
 for i in range(4):
  j,k,l=[a for a in range(4) if a!=i]
  x=verts[j];v=np.cross(verts[k]-x,verts[l]-x)
  if np.dot(v,verts[i]-x)>0:v=-v
  out.append(v/np.linalg.norm(v))
 return np.array(out)

def cut_points(verts,mask):
 pts=[]
 for i in range(4):
  if i not in mask:pts.append(verts[i])
  else:
   for j in range(4):
    if i!=j:pts.append((1-depths[i])*verts[i]+depths[i]*verts[j])
 return np.array(pts)

def hull_n(pts,u):
 a=np.array([1.,0.,0.]) if abs(u[0])<.8 else np.array([0.,1.,0.])
 v=np.cross(u,a);v/=np.linalg.norm(v)
 w=np.cross(u,v)
 return len(ConvexHull(pts@np.stack([v,w],axis=1)).vertices)

checks=0
for V in base_shapes:
 normals=face_normals(V)
 for _ in range(600):
  u=rng.normal(size=3);u/=np.linalg.norm(u)
  signs=normals@u>0
  D=sum(signs[i]!=signs[j] for i in range(4) for j in range(i+1,4))
  assert D in (3,4)
  counts={}
  for r in range(5):
   for mask in itertools.combinations(range(4),r):
    pred=D+sum(sum(signs[i]==signs[j] for j in range(4) if j!=i) for i in mask)
    n=hull_n(cut_points(V,mask),u)
    assert n==pred,(mask,signs,D,n,pred)
    counts[frozenset(mask)]=n
    checks+=1
  for mask,n in counts.items():
   assert n+counts[frozenset(set(range(4))-set(mask))]==12

p=sp.Symbol('p')
for r,expected in {
 0:{3:p,4:1-p},
 1:{3:p/4,5:1-p/4},
 2:{5:p/2,6:1-p,7:p/2},
 3:{7:1-p/4,9:p/4},
 4:{8:1-p,9:p}
}.items():
 values={}
 for signs in itertools.product((False,True),repeat=4):
  k=sum(signs)
  if k in (0,4):continue
  prob=p/8 if k in (1,3) else (1-p)/6
  D=k*(4-k)
  n=D+sum(sum(signs[i]==signs[j] for j in range(4) if j!=i) for i in range(r))
  values[n]=values.get(n,sp.Integer(0))+prob
 assert set(values)==set(expected)
 assert all(sp.simplify(values[n]-expected[n])==0 for n in expected)

pr=float(6/sp.pi*sp.acos(sp.Rational(1,3))-2)
N=250000
U=rng.normal(size=(N,3));U/=np.linalg.norm(U,axis=1)[:,None]
sgn=U@face_normals(base_shapes[0]).T>0
hist={r:{} for r in range(5)}
for r in range(5):
 k=sgn.sum(axis=1)
 D=k*(4-k)
 num=D.copy()
 for i in range(r):
  num+=np.sum(sgn[:,i:i+1]==sgn,axis=1)-1
 for n in np.unique(num):hist[r][int(n)]=int((num==n).sum())
 assert all(abs(hist[r].get(k,0)/N-float(v.subs(p,pr) if hasattr(v,'subs') else v))<.005 for k,v in {
 0:{3:p,4:1-p},1:{3:p/4,5:1-p/4},2:{5:p/2,6:1-p,7:p/2},
 3:{7:1-p/4,9:p/4},4:{8:1-p,9:p}
 }[r].items())
print('PASS:',checks,'independent projected-convex-hull checks; 5 symbolic distributions; 250000 orientation samples per distribution.')
print('regular tetra p=',pr,'empirical stage counts=',hist)
