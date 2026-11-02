#!/usr/bin/env python3
"""Exact and numerical checks of finite-dimensional phase-map spectra."""
import math, random
import sympy as sp
import numpy as np

def state(m,phis):
    return np.array([t for p in phis for t in (p,p+np.pi)],dtype=float)

def jac(theta,alpha,K):
    N=len(theta)
    Z=np.exp(1j*theta).mean()
    A=np.cos(theta[None,:]-theta[:,None]-alpha)
    D=np.diag(np.real(Z*np.exp(-1j*theta-1j*alpha)))
    return np.eye(N)+(K/N)*A-K*D

def spectral(theta,alpha,K):
    rho=abs(np.exp(2j*theta).mean())
    c=np.cos(alpha)
    root=np.lib.scimath.sqrt(rho*rho-np.sin(alpha)**2)
    return [1+K*(c+root)/2,1+K*(c-root)/2]

def kcrit(alpha,rho):
    c=math.cos(alpha)
    if c>=0 or rho>=1: return 0
    q=1-rho*rho
    if rho<=abs(math.sin(alpha))+1e-14:
        return -4*c/q
    return 4/(-c+math.sqrt(max(0,rho*rho-math.sin(alpha)**2)))

random.seed(2831)
err=0.0
count=0
for m in [2,3,4,6,10]:
  for _ in range(150):
    phis=[random.uniform(-math.pi,math.pi) for j in range(m)]
    theta=state(m,phis)
    rho=abs(np.exp(2j*theta).mean())
    if rho>.9999999999:continue
    alpha=random.uniform(0,2*math.pi)
    K=random.uniform(.01,12)
    J=jac(theta,alpha,K)
    e=np.linalg.eigvals(J)
    pred=np.array(spectral(theta,alpha,K),dtype=complex)
    for p in pred:
      err=max(err,min(abs(e-p)))
    # Compare characteristic trace/product instead of repeated eigenvalues.
    B=J-np.eye(2*m)
    assert abs(np.trace(B)-K*np.cos(alpha))<2e-11
    assert abs((np.trace(B)**2-np.trace(B@B))/2-K*K*(1-rho*rho)/4)<2e-10
    count+=1
assert err<2e-6,(err,count)
# Exact exceptional point and nilpotence
c=-sp.Rational(1,2); s=sp.sqrt(3)/2
angles=[sp.Integer(0), sp.pi/6, sp.pi, 7*sp.pi/6]
C=sp.Matrix([sp.cos(t) for t in angles]);S=sp.Matrix([sp.sin(t) for t in angles]);Q=C.row_join(S)
R=sp.Matrix([[c,s],[-s,c]])
G=sp.simplify(Q.T*Q/4)
B=sp.simplify(R*G)
A=sp.simplify(sp.eye(2)+4*B)
assert sp.simplify(A.trace())==0
assert sp.simplify(A.det())==0
assert A!=sp.zeros(2)
assert sp.simplify(A*A)==sp.zeros(2)
assert sp.simplify(sp.eye(2)+8*B+sp.eye(2))==2*A
# Ordinary exact phase examples alpha=pi, rho=0 and rho=sqrt3/2
assert sp.simplify(G.det()-sp.Rational(1,16))==0 # q/4 = (1-3/4)/4 = 1/16
assert sp.simplify(B.trace()+sp.Rational(1,2))==0
assert sp.simplify(B.det()-sp.Rational(1,16))==0
# Assert Schur threshold with direct eigenvalues and no boundary acceptance
schur=0
for a in [math.pi*.51, math.pi*.62, math.pi*.75, math.pi*.95, math.pi]:
    for rho in [0,.2,.5,.8,.93,.99]:
        crit=kcrit(a,rho)
        for mult in [.33,.98,1.02,1.5]:
            k=crit*mult
            vals=np.array([1+k*(math.cos(a)+complex(np.lib.scimath.sqrt(rho*rho-math.sin(a)**2)))/2,1+k*(math.cos(a)-complex(np.lib.scimath.sqrt(rho*rho-math.sin(a)**2)))/2])
            isstable=np.max(np.abs(vals))<1-1e-10
            assert isstable==(mult<1),(a,rho,k,vals,crit)
            schur+=1
print('PASS exact nilpotent example; random spectral comparisons:', count, 'max eigen residual:',err,'Schur cases:',schur)
print('Exact Gram=',G,'normal block at K=4=',A)


# Verify the nonzero nonlinear remainder after two nilpotent normal steps.
def next_phases(theta, alpha, K):
    return theta + K*np.sin(theta[None,:]-theta[:,None]-alpha).mean(axis=1)
base=np.array([0.,np.pi/6,np.pi,7*np.pi/6])
nonlinear_coeff=[]
for d in [1e-2,1e-3]:
    theta=base.copy();theta[0]+=d
    theta=next_phases(next_phases(theta,2*np.pi/3,4),2*np.pi/3,4)
    z1=abs(np.exp(1j*theta).mean())
    assert 0<z1<0.5*d*d,(d,z1)
    nonlinear_coeff.append(z1/(d*d))
print('Two-step nonlinear residual scales quadratically; coefficients:',nonlinear_coeff)
