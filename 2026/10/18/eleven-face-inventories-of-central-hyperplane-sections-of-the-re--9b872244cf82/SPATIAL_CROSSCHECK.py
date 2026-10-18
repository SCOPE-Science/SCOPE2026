import numpy as np
from scipy.spatial import ConvexHull

import EXACT_CHECK as E
P=(1+5**.5)/2
v=np.array([[a+b*P for a,b in x] for x in E.verts])
for mask in range(1,16):
 n=np.array([sum((E.Ad[k][j][0]+E.Ad[k][j][1]*P) for j in range(4) if mask&(1<<j)) for k in range(4)])
 if E.sig(E.D)<0:n=-n
 s=v@n
 inds=np.where(abs(s)<1e-7)[0]
 points=list(v[inds])
 for i,j in E.edges:
  if s[i]*s[j]<-1e-8:
   t=s[i]/(s[i]-s[j]); points.append((1-t)*v[i]+t*v[j])
 points=np.array(points)
 # orthogonal proj onto 3D; from SVD of normal
 _,_,right=np.linalg.svd(n.reshape(1,4)); points=points@right[1:].T
 hull=ConvexHull(points)
 exact=E.section(mask)
 assert len(hull.vertices)==exact['f_vector'][0],(mask,len(hull.vertices),exact['f_vector'][0])
 ntri=sum((int(k)-2)*val for k,val in exact['face_sizes'].items())
 assert len(hull.simplices)==ntri,(mask,len(hull.simplices),ntri)
print('INDEPENDENT_SPATIAL_HULL_OK 15/15 strata convex-hull vertices and triangulated faces')
