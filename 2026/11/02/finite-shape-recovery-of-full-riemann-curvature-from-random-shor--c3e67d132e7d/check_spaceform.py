"""Independent 2D unit-sphere geometric-pair quadrature sanity test."""
import numpy as np
from scipy.stats import qmc
from scipy.integrate import simpson
n=2
Q=np.diag([4.0,1.0]); a,b=4.0,1.0
scal=2.; ric=np.eye(2)
# constant curvature +1: R(Q,Q)=(trace Q)^2-tr Q^2
RQ=np.trace(Q)**2-np.trace(Q@Q)
Ktheory=RQ/(3*(n+2)**2)+2/(3*(n+2)*(n+4))*(np.trace(ric@Q@Q)-np.trace(Q)*np.trace(ric@Q)/(n+2))
# independent area moment via radial/angular trapezoidal product
rho=(np.arange(160)+.5)/160
th=np.arange(720)*2*np.pi/720
rhos,theta=np.meshgrid(rho,th,indexing='ij')
rad2=rhos**2*(a*np.cos(theta)**2+b*np.sin(theta)**2)
# J(x) spherical exp at North pole
N=2**18
z=qmc.Sobol(4,scramble=True,seed=45321).random_base2(18)
x0=np.column_stack([np.sqrt(z[:,0])*np.cos(2*np.pi*z[:,1]),np.sqrt(z[:,0])*np.sin(2*np.pi*z[:,1])])
y0=np.column_stack([np.sqrt(z[:,2])*np.cos(2*np.pi*z[:,3]),np.sqrt(z[:,2])*np.sin(2*np.pi*z[:,3])])
A=np.diag([2,1])
for r in [0.22,0.16,0.12]:
 rad=r*np.sqrt(rad2)
 J=np.sinc(rad/np.pi)
 zm=np.sum(J*rhos)/np.sum(rhos)
 z2=np.sum(rad2*J*rhos)/np.sum(J*rhos)
 baseline=2*r*r*z2
 x=r*x0@A;y=r*y0@A
 nx=np.linalg.norm(x,axis=1);ny=np.linalg.norm(y,axis=1)
 C=np.cos(nx)*np.cos(ny)+np.sin(nx)/nx*np.sin(ny)/ny*np.sum(x*y,axis=1)
 d=np.arccos(np.clip(C,-1,1))
 flat=np.sum((x-y)**2,axis=1)
 Jx=np.sinc(nx/np.pi);Jy=np.sinc(ny/np.pi)
 delta=np.mean(Jx*Jy*(d*d-flat))/(np.mean(Jx)*np.mean(Jy))
 K=(2*r*r*np.trace(Q)/(n+2) -baseline-delta)/(r**4)
 assert abs(K-Ktheory)<0.12,(K,Ktheory)
 print('INDEPENDENT_SPHERICAL_DISTANCE_QUADRATURE',r,round(K,6),'target',round(Ktheory,6))
print('SPHERE_CHECK_PASSED')
