#!/usr/bin/env python3
"""Reproducibility checks for a two-dimensional compressed uniform diagonal spacing law."""
import numpy as np
import sympy as sp

p,q=sp.symbols('p q',positive=True)
r=1-p-q
xx,yy=sp.symbols('x y',real=True)
D=[xx,yy,0]; P=[p,q,r]
tr=sum((1-P[i])*D[i] for i in range(3))
tr2=sum((1-P[i])**2*D[i]**2 for i in range(3))+sum(P[i]*P[j]*D[i]*D[j] for i in range(3) for j in range(3) if i!=j)
Q=sp.expand(2*tr2-tr**2)
M=sp.hessian(Q,(xx,yy))/2
assert sp.simplify(M.det()-4*p*q*r)==0
Minv=M.inv(); terms=[]
for L in [sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([1,-1])]:
    terms.append(sp.factor((L.T*Minv*L)[0]))
assert sp.simplify(terms[0]-(1-q)**2/(4*p*q*r))==0
assert sp.simplify(terms[1]-(1-p)**2/(4*p*q*r))==0
assert sp.simplify(terms[2]-(1-r)**2/(4*p*q*r))==0
print('symbolic quadratic form, determinant, and three support-width identities: PASS')

rng=np.random.default_rng(2107)
checks=0
for probs in [(1/3,1/3,1/3),(.2,.3,.5),(.05,.25,.7),(.47,.43,.1)]:
    p,q,r=probs
    Mv=np.array([[(1-p)**2,p*q-r],[p*q-r,(1-q)**2]])
    t0=2*np.sqrt(p*q*r)/(1-min(probs))
    for tt in [t0*.15,t0*.4,t0*.7]:
        pred=np.pi*tt**2/(2*np.sqrt(p*q*r))-tt**3/(3*p*q*r)
        # Deterministic angular quadrature after ellipse-variable polar transform.
        L=np.linalg.cholesky(Mv)
        theta=np.arange(131072)*(2*np.pi/131072)
        radial=np.stack((np.cos(theta),np.sin(theta)))
        z=np.linalg.solve(L.T,radial)
        widths=(np.abs(z[0])+np.abs(z[1])+np.abs(z[0]-z[1]))/2
        integ=(tt**2/2-tt**3*widths.mean()/3)*2*np.pi/np.sqrt(np.linalg.det(Mv))
        assert abs(integ-pred)<5e-8,(probs,tt,pred,integ)
        checks+=1
    tt=.45*t0
    samples=rng.random((450000,3))
    x=samples[:,0]-samples[:,2];y=samples[:,1]-samples[:,2]
    gap=np.sqrt(np.maximum(0, Mv[0,0]*x*x+2*Mv[0,1]*x*y+Mv[1,1]*y*y))
    pred=np.pi*tt**2/(2*np.sqrt(p*q*r))-tt**3/(3*p*q*r)
    emp=np.mean(gap<=tt)
    sig=np.sqrt(pred*(1-pred)/len(gap))
    assert abs(emp-pred)<6*sig,(probs,tt,emp,pred)
    checks+=1
    print('interior',probs,'max exact threshold',round(t0,6),'test t',round(tt,6),'cdf',round(pred,8),'empirical',round(emp,8))

for p,q in [(0.5,0.5),(.2,.8),(.01,.99)]:
    tt=.4*min(p,q)
    d=rng.random((550000,3))
    z=p*d[:,0]+q*d[:,1]
    emp=np.mean(abs(z-d[:,2])<=tt)
    exact=2*tt-tt**3/(3*p*q)
    assert abs(emp-exact)<6*np.sqrt(exact*(1-exact)/len(z)),(p,q,tt,emp,exact)
    checks+=1
    print('one zero coordinate',p,q,'cdf',exact,'empirical',emp)

tt=.34
d=rng.random((600000,2)); emp=np.mean(abs(d[:,0]-d[:,1])<=tt)
assert abs(emp-(2*tt-tt**2))<6*np.sqrt((2*tt-tt**2)*(1-(2*tt-tt**2))/len(d))
checks+=1
print('two zero coordinates CDF: PASS')

# Degenerate perturbation and the uniform Schur-complement splitting bound.
a=np.array([.5,.6,np.sqrt(.39)]);a=a/np.linalg.norm(a)
D=np.diag([.2,.9,.7]);P=np.eye(3)-np.outer(a,a)
U=np.linalg.eigh(P)[1][:,1:]
mu=np.linalg.eigvalsh(U.T@D@U)
for eta in [0.01,0.001,0.0001]:
    eigen=np.linalg.eigvalsh(np.outer(a,a)+eta*D)
    assert all(-eta**2/(1-eta)-1e-12<=eigen[i]-eta*mu[i]<=1e-12 for i in (0,1))
    checks+=1
print('finite-perturbation eigenvalue splitting (uniform bound): PASS')
print('VERIFICATION_PASS',checks)
