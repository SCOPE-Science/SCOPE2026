"""Independent finite diagnostics for cuboctahedral random-shadow area conditioning.
Run: python cuboctahedron_verify.py (requires numpy, scipy, mpmath).
"""
from itertools import product
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.stats import qmc, norm
import mpmath as mp

VERTICES=np.array(sorted({tuple(v) for v in product((-1,0,1),repeat=3) if sum(int(w!=0) for w in v)==2}),dtype=float)
assert len(VERTICES)==12

def area_and_vertices_from_points(direction):
    u=direction/np.linalg.norm(direction)
    ref=np.eye(3)[np.argmin(np.abs(u))]
    e=np.cross(u,ref); e/=np.linalg.norm(e)
    f=np.cross(u,e)
    hull=ConvexHull(np.stack((VERTICES@e,VERTICES@f),axis=1))
    return float(hull.volume),len(hull.vertices)

def formula(direction):
    a,b,c=sorted(map(abs,direction),reverse=True)
    return (4*a+2*b+2*c if a>b+c else 3*(a+b+c)), (8 if a>b+c else 6)

rng=np.random.default_rng(20261019)
for _ in range(2400):
    d=rng.standard_normal(3);d/=np.linalg.norm(d)
    v,n=area_and_vertices_from_points(d)
    fv,fn=formula(d)
    assert n==fn, (n,fn,d)
    assert abs(v-fv)<3e-12, (v,fv,d)
print('INDEPENDENT_PROJECTED_HULL_AREAS_AND_SILHOUETTE_VERTEX_COUNTS_OK 2400')

mp.mp.dps=50
pi=mp.pi
limit=lambda ph:mp.atan(1/(mp.cos(ph)+mp.sin(ph)))
# x=cos t,y=sin t cos phi,z=sin t sin phi, dOmega=sin t dt dphi.
def inner_omega(ph):return 1-mp.cos(limit(ph))
def inner_x(ph):return (mp.sin(limit(ph))**2)/2
def inner_y(ph):
    t=limit(ph)
    return mp.cos(ph)*(t/2-mp.sin(2*t)/4)
def inner_z(ph):
    t=limit(ph)
    return mp.sin(ph)*(t/2-mp.sin(2*t)/4)
O=mp.quad(inner_omega,[0,pi/4,pi/2])
Ix=mp.quad(inner_x,[0,pi/4,pi/2])
Iy=mp.quad(inner_y,[0,pi/4,pi/2])
Iz=mp.quad(inner_z,[0,pi/4,pi/2])
assert abs(O-mp.asin(mp.mpf(1)/3))<mp.mpf('1e-44')
assert abs(Ix-pi/(6*mp.sqrt(3)))<mp.mpf('1e-44')
assert abs(Iy-(pi/8-pi/(6*mp.sqrt(3))))<mp.mpf('1e-44')
assert abs(Iy-Iz)<mp.mpf('1e-44')
assert abs((4*Ix+2*Iy+2*Iz)-pi/2)<mp.mpf('1e-44')
print('INDEPENDENT_SPHERICAL_TRIANGLE_QUADRATURE_MOMENT_OK')

# Scrambled Sobol on [0,1]^2; map to Haar sphere, avoiding Gaussian normalization.
sampler=qmc.Sobol(2,scramble=True,seed=21)
x=sampler.random_base2(19)
z=2*x[:,0]-1;th=2*np.pi*x[:,1];r=np.sqrt(np.maximum(0,1-z*z))
u=np.stack((r*np.cos(th),r*np.sin(th),z),axis=1)
s=np.sort(np.abs(u),axis=1)
oct_mask=s[:,2]>s[:,1]+s[:,0]
a=np.where(oct_mask,4*s[:,2]+2*s[:,1]+2*s[:,0],3*s.sum(axis=1))
p8=6/math.pi*math.asin(1/3)
assert abs(np.mean(oct_mask)-p8)<.0015
assert abs(np.mean(a*oct_mask)-3)<.008
assert abs(np.mean(a*(~oct_mask))-math.sqrt(3))<.008
assert abs(np.mean(a)-(3+math.sqrt(3)))<.008
print('SOBOL_AREA_WEIGHTED_SILHOUETTE_MOMENTS_OK',np.mean(oct_mask),np.mean(a*oct_mask),np.mean(a*(~oct_mask)))

p6=1-p8
m8=3/p8;m6=math.sqrt(3)/p6
cov=6-2*(3+math.sqrt(3))*p8
assert m6>m8 and cov<0
assert 3/(3+math.sqrt(3))<p8
print('EXACT_NEGATIVE_AREA_VERTEX_COUNT_COVARIANCE_OK',m6,m8,cov)
print('ALL_CUBOCTAHEDRON_SHADOW_BRIGHTNESS_CHECKS_OK')
