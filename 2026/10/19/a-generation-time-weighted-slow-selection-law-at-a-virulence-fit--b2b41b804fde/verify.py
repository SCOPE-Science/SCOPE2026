#!/usr/bin/env python3
"""Exact coefficient and supplemental finite-perturbation checks for a two-stage epidemic model."""
from fractions import Fraction as Q
from math import log
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

a = [Q(1,2),Q(1,2)]
d = [[Q(2),Q(2)],[Q(2),Q(3)]]
k = [[Q(2),Q(2)],[Q(1),Q(9,2)]]
K=[sum((a[j]*k[i][j]/d[i][j] for j in range(2)),Q(0)) for i in range(2)]
T=[sum((a[j]*k[i][j]/(d[i][j]**2) for j in range(2)),Q(0)) for i in range(2)]
assert K==[Q(1),Q(1)] and T==[Q(1,2),Q(3,8)]
H=Q(2)
for v in [Q(1,5),Q(1,2),Q(4,5)]:
    h=[H*v,H*(1-v)]
    I=[[a[j]*h[i]/d[i][j] for j in range(2)] for i in range(2)]
    F=[sum((k[i][j]*I[i][j] for j in range(2)),Q(0)) for i in range(2)]
    assert F==h
    assert Q(3)-Q(1)-sum(F)==0
    for i in range(2):
        for j in range(2):
            assert a[j]*F[i]-d[i][j]*I[i][j]==0
    i=np.asarray([[float(z) for z in line] for line in I]);kk=np.asarray([[float(z) for z in line] for line in k]);dd=np.asarray([[float(z) for z in line] for line in d]);aa=np.array([.5,.5])
    J=np.zeros((5,5));J[0,0]=-1-sum(F)
    for ii in range(2):
        for jj in range(2):
            row=1+2*ii+jj
            J[0,row]=-kk[ii,jj]
            J[row,0]=aa[jj]*float(F[ii])
            for ll in range(2):
                J[row,1+2*ii+ll]+=aa[jj]*kk[ii,ll]
            J[row,row]-=dd[ii,jj]
    eig=np.linalg.eigvals(J)
    assert sum(abs(z)<1e-8 for z in eig)==1, eig
    assert all(z.real < -1e-6 for z in eig if abs(z)>1e-8), eig

u0=.5
root=brentq(lambda u:.5*log(u/u0)-.375*log((1-u)/(1-u0))+1.,1e-8,1-1e-8,xtol=1e-14)
assert abs(root-0.1047406326247829)<1e-10
kk=np.asarray([[float(z) for z in line] for line in k]);dd=np.asarray([[float(z) for z in line] for line in d]);aa=np.array([.5,.5])
initial=np.array([1.,.25,.25,.25,1/6])
def rhs(t,x,eps):
   S=x[0];I=x[1:].reshape(2,2)
   Fs=np.sum(kk*(1+eps*np.array([0.,1.]))[:,None]*I,axis=1)
   return np.r_[3-S-S*sum(Fs),(aa[None,:]*S*Fs[:,None]-dd*I).ravel()]
errors=[]
for eps in [0.04,0.02,0.01,0.005]:
   sol=solve_ivp(lambda t,x:rhs(t,x,eps),(0,1/eps),initial,rtol=1e-10,atol=1e-12)
   assert sol.success
   I=sol.y[1:,-1].reshape(2,2)
   Fs=np.sum(kk*(1+eps*np.array([0.,1.]))[:,None]*I,axis=1)
   u=Fs[0]/sum(Fs)
   errors.append(abs(u-root))
assert all(errors[i+1]<errors[i] for i in range(3)),errors
assert errors[-1]<2.5e-4,errors
print('PASS: rational coefficients, neutral equilibria, spectral samples, four numerical singular-limit checks; errors',errors)
