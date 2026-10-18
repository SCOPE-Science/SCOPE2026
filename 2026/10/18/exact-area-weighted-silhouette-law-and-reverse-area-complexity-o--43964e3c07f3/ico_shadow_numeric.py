#!/usr/bin/env python3
"""Independent projected-hull and Haar checks for regular icosahedron."""
import math
import numpy as np
from scipy.spatial import ConvexHull
rng=np.random.default_rng(548021)
phi=(1+math.sqrt(5))/2
r=1/phi
axes=np.array([[1,s,t] for s in (-1,1) for t in (-1,1)]+[[0,phi,t*r] for t in (-1,1)]+[[phi,t*r,0] for t in (-1,1)]+[[r,0,t*phi] for t in (-1,1)],dtype=float)/math.sqrt(3)
vertices=[]
for s in (-1,1):
 for t in (-1,1):
  vertices.extend([[0,s,t*phi],[s,t*phi,0],[s*phi,0,t]])
vertices=np.array(vertices)
assert len(vertices)==12
normals=ConvexHull(vertices).equations[:,:3]
face_edge_to_normals={}
for ix,tri in enumerate(ConvexHull(vertices).simplices):
 for j in range(3):
  edge=tuple(sorted((int(tri[j]),int(tri[(j+1)%3]))))
  face_edge_to_normals.setdefault(edge,[]).append(ix)
assert len(face_edge_to_normals)==30

def shadow(u):
    z=np.array([1.,0.,0.]) if abs(u[0])<0.8 else np.array([0.,1.,0.])
    v=np.cross(u,z);v/=np.linalg.norm(v);w=np.cross(u,v)
    pr=np.stack((vertices@v,vertices@w),axis=1)
    hull=ConvexHull(pr)
    W=hull.volume/math.sqrt(3)
    return len(hull.vertices),W

for u in rng.normal(size=(1800,3)):
 u=u/np.linalg.norm(u)
 N,W=shadow(u)
 assert N in (6,8,10)
 assert abs(W-np.abs(axes@u).sum())<1e-9,(N,W,np.abs(axes@u).sum())
 face_front=normals@u>0
 Nedge=sum(face_front[j]!=face_front[k] for j,k in face_edge_to_normals.values())
 assert N==Nedge,(N,Nedge)
print('INDEPENDENT_HULL_CAUCHY_AND_SILHOUETTES_OK 1800')

alpha=math.acos(1/3);beta=math.acos(math.sqrt(5)/3)
H=math.acos((3+math.sqrt(5))/(4*math.sqrt(2)))
P=math.acos((1+3*math.sqrt(5))/8)
predp=np.array([5*(2*math.pi-3*(alpha+beta))/math.pi,15*(2*alpha+beta-math.pi)/math.pi,3*(2*math.pi-5*alpha)/math.pi])
predm=np.array([5*(3+math.sqrt(5))*H/math.pi,5*((1+math.sqrt(5))*P+2*(3-math.sqrt(5))*H)/(2*math.pi),5*(5-math.sqrt(5))*P/(2*math.pi)])
U=rng.normal(size=(300000,3));U/=np.linalg.norm(U,axis=1)[:,None]
F=U@normals.T
# Silhouette count via crossing exactly once per icosahedron edge
N=np.zeros(len(U),dtype=np.int32)
for j,k in face_edge_to_normals.values():N+=(F[:,j]*F[:,k]<0)
W=np.abs(U@axes.T).sum(axis=1)
obs_p=np.array([(N==n).mean() for n in (6,8,10)])
obs_m=np.array([np.mean(np.where(N==n,W,0)) for n in (6,8,10)])
assert np.max(abs(obs_p-predp))<0.004
assert np.max(abs(obs_m-predm))<0.02
assert abs(predm.sum()-5)<2e-14
print('HAAR_MIXED_MOMENTS_OK observations=',obs_m.tolist(),'predictions=',predm.tolist())
print('NUMERIC_ICO_SHADOW_CHECKS_OK')
