"""Standalone elementary checks for finite-memory sigmoidal Rulkov equilibria.

Requirements: Python 3, numpy, scipy, sympy.
This finite check is diagnostic; the accompanying theorem has an analytic proof.
"""
import math
import numpy as np
from scipy.optimize import brentq
import sympy as sp


def sigma_root(k):
    if k <= 1:
        return 0.0
    return brentq(lambda s: math.tanh(k*s)-s, 1e-8, 1-1e-12, xtol=1e-15)


def matrix(m, k, mu, s):
    tau = m/(2*k)
    a = 5/(2-s)**2
    eta = (1-s*s)/(2*tau)
    B = np.zeros((m+2,m+2))
    B[0,:2] = [a,1.]
    B[1,0]=-mu
    B[1,1]=1.
    B[1,2:]=mu*eta
    B[2,0]=1.
    for j in range(1,m):
        B[j+2,j+1]=1.
    return B


def polynomial_coeffs(m,k,mu,s):
    a=5/(2-s)**2
    eta = k*(1-s*s)/m
    p = np.zeros(m+3)
    p[0]=1
    p[1]=-(1+a)
    p[2]=(a+mu)
    p[3:]= -mu*eta
    return p

# Formal characteristic identity independent of eigenvalues and numeric conditioning.
m=3
z,a,mu,eta=sp.symbols('z a mu eta')
J=sp.zeros(m+2)
J[0,0]=a;J[0,1]=1;J[1,0]=-mu;J[1,1]=1
for j in range(m):
    J[1,j+2]=mu*eta
J[2,0]=1
for j in range(1,m):
    J[j+2,j+1]=1
p=sp.expand(z**m*((z-1)*(z-a)+mu)-mu*eta*sum(z**j for j in range(m)))
assert sp.expand(J.charpoly(z).as_expr()-p)==0

for m in [1,2,3,4,6]:
    for k in [.9,1.,1.005,1.05,1.1,1.3,2.]:
        s=sigma_root(k)
        for sigma in ([0.] if k<=1 else [-s,0.,s]):
            mu0=1e-5
            B=matrix(m,k,mu0,sigma)
            coeff=polynomial_coeffs(m,k,mu0,sigma)
            eig=np.linalg.eigvals(B)
            assert all(abs(np.polyval(coeff,v))<1e-7 for v in eig)
            eigen_max=max(abs(eig))
            if sigma>=0 or (sigma<0 and k<math.atanh(math.sqrt(5)-2)/(math.sqrt(5)-2)):
                assert eigen_max>1.+1e-7, (m,k,sigma,eigen_max)
            if sigma<0 and k>math.atanh(math.sqrt(5)-2)/(math.sqrt(5)-2):
                assert eigen_max<1., (m,k,sigma,eigen_max)

# At the double-fast-root boundary, a complex pair becomes damped
# for every memory length; this validates the boundary expansion numerically.
s_star = math.sqrt(5)-2
k_star = math.atanh(s_star)/s_star
rho_star = k_star*(1-s_star*s_star)
assert .5 < rho_star < 1
for m in [1,2,3,5,12]:
    for mu0 in [1e-4,1e-5]:
        B = matrix(m,k_star,mu0,-s_star)
        radius = max(abs(np.linalg.eigvals(B)))
        assert radius < 1., (m,mu0,radius)
        coeff = (1-rho_star*(m+3)/2)/2
        assert abs((radius-1)/mu0-coeff)<0.04, (m,mu0,radius,coeff)

m=150;k=150/140;mu=.001;s=sigma_root(k)
for sigma in [-s,0.,s]:
    B=matrix(m,k,mu,sigma)
    roots=np.linalg.eigvals(B)
    print('m=150 k=150/140 s=',sigma,'largest abs eig=',max(abs(roots)))
print('All symbolic characteristic, finite-size, and small-mu stability checks passed.')
