#!/usr/bin/env python3
"""Reproducible finite checks of formulas for Gaussian polar-response benchmark.
This is a finite numerical check, not a proof of universal claims.
Requires numpy, scipy, mpmath.
"""
import math
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.special import ellipk, ellipe

C = math.sqrt(2/math.pi)
H = math.sqrt(math.pi/2)/2
checks = 0

def checked(c, desc):
    global checks
    assert c, desc
    checks += 1

def ellipse_coeffs(r):
    if abs(r-1)<1e-12:
        return H, H
    k2 = 1-1/r**2
    K,E = ellipk(k2),ellipe(k2)
    return C*(r*r*E-K)/(r*(r*r-1)), C*r*(K-E)/(r*r-1)

def angle_coeffs(r):
    er=math.sqrt(math.pi/2)/(2*math.pi)
    def Qa(phi):
        c,s=math.cos(phi),math.sin(phi)
        q=r*r*c*c+s*s
        return s*s/q**1.5
    def Qb(phi):
        c,s=math.cos(phi),math.sin(phi)
        q=r*r*c*c+s*s
        return r*r*c*c/q**1.5
    return er*quad(Qa,0,2*math.pi,epsabs=1e-11,limit=350,points=[math.pi/2,3*math.pi/2])[0], er*quad(Qb,0,2*math.pi,epsabs=1e-11,limit=350,points=[math.pi/2,3*math.pi/2])[0]

for r in [1,1.01,1.1,1.5,2,3,8,25,100,300]:
    a,b=ellipse_coeffs(r)
    ac,bc=angle_coeffs(r)
    checked(abs(a-ac)<3e-8 and abs(b-bc)<3e-8, f'elliptic/angle r={r}')
    checked(a>0 and b>0 and (r==1 or b>a), f'ordering r={r}')
    q=(r*r*(a-b)**2)/((r*r+1)*(r*r*a*a+b*b))
    checked(0<=q<1, f'scalar residual r={r}')
    s=(r*r*a+b)/(r*r+1)
    weighted_error=r*r*(a-s)**2+(b-s)**2
    checked(abs(q-weighted_error/(r*r*a*a+b*b))<1e-12, f'scalar minimization {r}')
    if r>1:
        h=np.array([(1+b/a)/2,1.0])
        checked(1<h[0]<b/a, f'positive inversion interval r={r}')
        checked((b*h[1])>(a*h[0]), f'linear order inversion r={r}')

mp.mp.dps=70
for r in [mp.mpf(10)**k for k in [2,4,6,8,12,18]]:
    k2=1-1/r**2
    K=mp.ellipk(k2);E=mp.ellipe(k2)
    a=mp.sqrt(2/mp.pi)*(r*r*E-K)/(r*(r*r-1))
    b=mp.sqrt(2/mp.pi)*r*(K-E)/(r*r-1)
    ratio=b/a
    diagnostic=(r*r*(a-b)**2)/((r*r+1)*(r*r*a*a+b*b))
    checked(abs(r*a/mp.sqrt(2/mp.pi)-1)<mp.mpf('0.0005'), f'a asymptotic r={r}')
    checked(abs(r*b/mp.sqrt(2/mp.pi)-(mp.log(4*r)-1))<mp.mpf('0.002'),f'b asymptotic r={r}')
    checked(abs(ratio-(mp.log(4*r)-1))<mp.mpf('0.002'),f'ratio asymptotic r={r}')
    checked(abs(diagnostic*r*r/(mp.log(r)**2)-1)<mp.mpf('0.35'),f'diagnostic asymptotic r={r}')

# Monte Carlo symmetric finite difference of smoothed direction map (separate check).
rng=np.random.default_rng(3465)
n=400000
z=rng.normal(size=(n,2))
for r in [1.5,3,10]:
    noisy=z*np.array([r,1.])
    a,b=ellipse_coeffs(r)
    # Gaussian score identity avoids singular direct-difference sampling variance
    radius=np.linalg.norm(noisy,axis=1)
    unit=noisy/radius[:,None]
    J_est=np.mean(unit*noisy/np.array([r*r,1]),axis=0)
    checked(abs(J_est[0]-a)<0.011, f'score first r={r}: {J_est[0]} {a}')
    checked(abs(J_est[1]-b)<0.011, f'score second r={r}: {J_est[1]} {b}')

print(f'PASS: {checks} deterministic high-precision/quadrature/formula/Monte-Carlo tolerance assertions')
print('At r=10: coefficient pair, amplification, scalar weighted mismatch')
a,b=ellipse_coeffs(10)
print(f'a={a:.12f}; b={b:.12f}; b/a={b/a:.12f}; min_relative_scalar_mse={100*(a-b)**2/((101)*(100*a*a+b*b)):.12f}')
