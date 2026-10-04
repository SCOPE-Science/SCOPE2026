#!/usr/bin/env python3
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import chi, norm

def exact_size(n,rho,alpha=0.05):
    z=norm.ppf(1-alpha/2); s=math.sqrt(1-rho*rho)
    lo=max(0.0,chi.ppf(1e-12,n)); hi=chi.ppf(1-1e-12,n)
    f=lambda q:(norm.sf((z-rho*q)/s)+norm.sf((z+rho*q)/s))*chi.pdf(q,n)
    return quad(f,lo,hi,epsabs=1e-12,epsrel=1e-12,limit=400)[0]
alpha=0.05
v=exact_size(100,0.1,alpha)
assert abs(v-0.16881556417835863)<2e-11
z=norm.ppf(1-alpha/2); lim=norm.sf(z-1)+norm.sf(z+1)
assert abs(lim-0.17007504575308752)<2e-13
assert abs(exact_size(1,0.7,alpha)-alpha)<3e-10
Sigma=np.array([[2.0,0.4,0.2],[0.4,1.5,0.3],[0.2,0.3,1.2]])
A=np.array([[1.0],[0.5],[-0.25]]); beta=np.array([0.8,-0.4,0.6]); theta=np.array([-0.3,0.9,0.5])
perp=Sigma-Sigma@A@np.linalg.inv(A.T@Sigma@A)@A.T@Sigma
dx2=beta@perp@beta; dy2=theta@perp@theta; cov=beta@perp@theta
rho=cov/math.sqrt((0.7**2+dx2)*(1.1**2+dy2))
assert dx2>=-1e-12 and dy2>=-1e-12 and abs(rho)<1 and cov*cov<=dx2*dy2+1e-12
print(f"exact_size_n100_rho0.1={v:.15f}")
print(f"local_limit_kappa1={lim:.15f}")
print(f"geometry_rho={rho:.15f}")
print("VERIFY_OK")
