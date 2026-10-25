"""Independent direct torus metric Monte Carlo comparison with radial Voronoi areas."""
import math
import numpy as np
from verify_geometry import facets, intersection_area
rng=np.random.default_rng(381)
N=75000
u=np.array((1.,0.));v=np.array((.42,1.2)); area=abs(np.linalg.det(np.column_stack((u,v))))
xy=(rng.random((N,2))-rng.random((N,2)))
z=xy[:,0,None]*u+xy[:,1,None]*v
sq=np.full(N,np.inf)
for i in range(-2,3):
 for j in range(-2,3):
  w=z-i*u-j*v
  sq=np.minimum(sq, np.sum(w*w,axis=1))
d=np.sqrt(sq)
print('Direct independent Haar pair Monte Carlo (n=%d)'%N)
for r in (.2,.4,.55,.65,.7):
 obs=np.mean(d<=r);pred=intersection_area(facets(u,v),r,N=18000)/area
 tol=5*math.sqrt(max(pred*(1-pred),0)/N)+.0005
 print(f'r={r:.2f} observed={obs:.6f} predicted={pred:.6f} tol={tol:.6f} pass={abs(obs-pred)<tol}')
 assert abs(obs-pred)<tol
