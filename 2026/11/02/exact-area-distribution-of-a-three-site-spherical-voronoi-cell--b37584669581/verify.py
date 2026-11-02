"""Independent symbolic and Monte Carlo checks for a three-site spherical Voronoi area law."""
import numpy as np
from math import pi
import sympy as s

A, t = s.symbols('a t', real=True)
F = (A*(2+s.cos(A))-3*s.sin(A))/(6*s.pi)
f = s.diff(F,A)
f2 = (2/(3*s.pi))*s.sin(A/2)*(s.sin(A/2)-(A/2)*s.cos(A/2))
assert s.simplify(s.expand_trig(f-f2))==0
assert s.simplify(F.subs(A,0))==0 and s.simplify(F.subs(A,2*s.pi))==1
mu = s.simplify(s.integrate(A*f,(A,0,2*s.pi)))
m2 = s.simplify(s.integrate(A**2*f,(A,0,2*s.pi)))
assert s.simplify(mu-4*s.pi/3)==0
assert s.simplify(m2-(20*s.pi**2/9-s.Rational(10,3)))==0
assert s.simplify(m2-mu**2-(4*s.pi**2/9-s.Rational(10,3)))==0
assert s.simplify(F.subs(A,s.pi)-s.Rational(1,6))==0
print('EXACT_CDF_PDF_NORMALIZATION_AND_MOMENTS_PASSED')

# Differential derivation of the angular kernel from a Gaussian polar integral.
theta, psi = s.symbols('theta psi',real=True)
J = s.integrate(s.cos(psi)*s.cos(psi-theta),(psi,theta-s.pi/2,s.pi/2))
assert s.trigsimp(J-(s.sin(theta)+(s.pi-theta)*s.cos(theta))/2)==0
fth = 4/(3*s.pi)*s.sin(theta)*(s.sin(theta)+(s.pi-theta)*s.cos(theta))
assert s.simplify(s.integrate(fth,(theta,0,s.pi))-1)==0
assert s.simplify(s.integrate(theta*fth,(theta,0,s.pi))-s.pi/3)==0
assert s.simplify(s.integrate(theta**2*fth,(theta,0,s.pi))-(2*s.pi**2/9-s.Rational(5,6)))==0
print('GAUSSIAN_ANGULAR_CONVOLUTION_AND_EXACT_MOMENTS_PASSED')

# Independent site generation, conditional on tagged site fixed at north pole.
rng=np.random.default_rng(20261030)
n=260000
h=rng.uniform(-1,1,size=(n,2))
az=rng.uniform(0,2*pi,size=(n,2))
r=np.sqrt(1-h*h)
x=np.stack((r*np.cos(az),r*np.sin(az),h),axis=-1)
normals=np.empty_like(x)
normals[...,0]=-x[...,0]
normals[...,1]=-x[...,1]
normals[...,2]=1-x[...,2]
normals /= np.linalg.norm(normals,axis=-1,keepdims=True)
ang=np.arccos(np.clip(np.einsum('ij,ij->i',normals[:,0,:],normals[:,1,:]),-1,1))
areas=2*(pi-ang)
assert abs(np.mean(areas)-4*pi/3)<.018
assert abs(np.var(areas)-(4*pi*pi/9-10/3))<.021
for a in [pi/2,pi,4*pi/3,3*pi/2]:
 empirical=np.mean(areas<=a)
 formula=(a*(2+np.cos(a))-3*np.sin(a))/(6*pi)
 assert abs(empirical-formula)<.009,(a,empirical,formula)
print('DIRECT_INDEPENDENT_UNIFORM_SPHERICAL_SITES_PASSED',n)

# Independent Voronoi membership-area estimate, not using the lune area formula.
# For a set of sampled triplets, the tagged cell can be counted by random probes.
N, probes = 150,22000
xsmall=x[:N,:,:]
phi_probe=rng.uniform(0,2*pi,size=probes)
z_probe=rng.uniform(-1,1,size=probes)
u_probe=np.column_stack((np.sqrt(1-z_probe*z_probe)*np.cos(phi_probe),np.sqrt(1-z_probe*z_probe)*np.sin(phi_probe),z_probe))
cos_others=np.einsum('mk,njk->mnj',u_probe,xsmall)
inside=(u_probe[:,None,2]>=np.max(cos_others,axis=2))
mc_areas=4*pi*np.mean(inside,axis=0)
assert np.max(np.abs(mc_areas-areas[:N]))<0.16,np.max(np.abs(mc_areas-areas[:N]))
print('INDEPENDENT_VORONOI_MEMBERSHIP_AREA_INTEGRATION_PASSED',N,probes)
print('ALL_CHECKS_PASSED')
