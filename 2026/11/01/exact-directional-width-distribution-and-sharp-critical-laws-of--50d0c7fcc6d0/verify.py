#!/usr/bin/env python3
"""Independent coordinate and quadrature tests for the icosahedral width CDF."""
import math
import numpy as np
from scipy.stats import qmc
from scipy.integrate import quad
phi = (1 + math.sqrt(5)) / 2
scale = math.sqrt(1 + phi**2)
V = []
for a in (-1,1):
 for b in (-1,1):
  V.extend([(0,a,b*phi),(a,b*phi,0),(a*phi,0,b)])
V=np.array(V,dtype=float)/scale
assert V.shape==(12,3)
# Finite vertex checks, not exhaustive proof.
P=V@V.T
for i in range(12):
 dots=np.sort(P[i,:])
 assert np.allclose(dots[-6:-1],np.ones(5)/math.sqrt(5))
 assert np.allclose(dots[0],-1)
c=1/math.sqrt(5)
r=math.acos(math.sqrt((1+c)/2))
rho=math.acos(math.sqrt((1+2*c)/3))
wmin,w0=2*math.cos(rho),2*math.cos(r)

def F(w):
 if w<=wmin:return 0.
 if w>=2:return 1.
 if w>=w0:return 3*w-5
 theta=math.acos(w/2)
 a=math.acos(max(-1,min(1,math.sin(r)/math.sin(theta))))
 b=math.acos(max(-1,min(1,math.tan(r)/math.tan(theta))))
 S=2*(a-math.cos(theta)*b)
 return 3*w-5+15*S/math.pi

# Simultaneous direct-coordinate width evaluations using a fixed Sobol point set.
engine=qmc.Sobol(d=2,scramble=True,seed=1729)
unit=engine.random_base2(m=20)
z=2*unit[:,0]-1
a=2*np.pi*unit[:,1]
t=np.sqrt(1-z*z)
U=np.stack([t*np.cos(a),t*np.sin(a),z],axis=1)
W=2*np.max(U@V.T,axis=1)
ws=[wmin+.015,1.62,1.65,1.68,w0-.008,w0+.03,1.8,1.9]
for x in ws:
 empirical=np.mean(W<=x)
 expected=F(x)
 print(f'CDF w={x:.12f} predicted={expected:.9f} sampled={empirical:.9f} delta={empirical-expected:+.8f}')
 assert abs(empirical-expected)<.0015
assert abs(F(wmin))<1e-10 and abs(F(2)-1)<1e-10
assert abs(F(w0)-(3*w0-5))<1e-9
M=quad(lambda w: 1-F(w),wmin,2,epsabs=1e-11,points=[w0])[0]+wmin
known_mean_unit_edge=15*math.asin(2/3)/(2*math.pi)
edge=math.sqrt(2-2*c)
print('mean radius-one',M,'mean normalized-to-unit-edge',M/edge,'known unit-edge',known_mean_unit_edge)
assert abs(M/edge-known_mean_unit_edge)<1e-9
coef=10/(math.pi*math.sin(r)*math.sqrt(math.cos(r)))
for e in [1e-3,1e-4,1e-5]:
 quotient=(F(w0-e)-(3*(w0-e)-5))/e**1.5
 print(f'cusp e={e:.0e} ratio={quotient:.8f} coefficient={coef:.8f}')
 assert abs(quotient/coef-1)<.02
print('checks_passed')
