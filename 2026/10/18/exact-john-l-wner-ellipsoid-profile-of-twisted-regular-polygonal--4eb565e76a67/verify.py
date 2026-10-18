import numpy as np, math
from scipy.spatial import ConvexHull
for n in range(3,18):
 beta=math.pi/n
 for frac in (0.02,0.25,0.5,0.83,0.99):
  phi=2*beta*frac
  h=0.2+0.5*n
  p=np.array([[math.cos(2*math.pi*k/n),math.sin(2*math.pi*k/n),0] for k in range(n)])
  q=np.array([[math.cos(2*math.pi*k/n+phi),math.sin(2*math.pi*k/n+phi),h] for k in range(n)])
  hull=ConvexHull(np.vstack((p,q)))
  a2=math.cos(beta)*math.cos(beta-min(phi,2*beta-phi))
  b=h/2
  c=np.array([0.,0.,b]);A=np.diag([math.sqrt(a2),math.sqrt(a2),b])
  margins=[]
  for plane in hull.equations:
   sup=plane[:3]@c +np.linalg.norm(A@plane[:3])+plane[3]
   margins.append(sup)
  assert max(margins)<2e-8,(n,frac,max(margins))
  assert min(abs(x) for x in margins)<1e-8,(n,frac,margins)
  assert sum(abs(x)<1e-8 for x in margins) >=2*n, (n,frac,margins)
print('PASS: all n 3..17 and five twist fractions: John candidate tangent to all supporting facets')
for n in range(3,18):
 beta=math.pi/n
 for frac in (0,0.19,0.5,0.77,1):
  phi=beta*frac;R=1.3;h=0.3+n/13
  v=np.array([[R*math.cos(2*math.pi*k/n+th),R*math.sin(2*math.pi*k/n+th),z] for z,th in ((0,0),(h,phi)) for k in range(n)])
  observed=ConvexHull(v).volume
  A=math.cos(beta);B=math.cos(beta-phi)
  expected=h*n*R*R*math.sin(beta)*(2*A+B)/3
  assert abs(observed-expected)<3e-10,(n,frac,observed,expected)
print('PASS: 75 convex-hull volumes match exact mixed-area formula')
