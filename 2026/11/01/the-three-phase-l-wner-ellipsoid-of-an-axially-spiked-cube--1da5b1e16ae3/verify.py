#!/usr/bin/env python3
"""Reproduce candidate containment/contact certificates and convex numerical optimization.

No external data.  The numerical experiments only corroborate the analytic proof.
"""
import math
import numpy as np
from scipy.optimize import minimize


def candidate(d, a):
    assert isinstance(d,int) and d>=2 and a>=1.0
    if a<=math.sqrt(d):
        c,b,r=0.0,math.sqrt(d),math.sqrt(d)
        regime=1
    elif a<=d:
        c,b,r=0.0,a,a*math.sqrt((d-1)/(a*a-1))
        regime=2
    else:
        c,b,r=(a-d)/(d+1), d*(a+1)/(d+1), d/math.sqrt(d+1)
        regime=3
    return c,b,r,regime


def contact_probabilities(d,a):
    c,b,r,k=candidate(d,a)
    if k==1:
        return {'apex':0.0,'cube_minus':0.5,'cube_plus':0.5}
    if k==2:
        p=(a*a-d)/(d*(a*a-1))
        q=(d-1)*a*a/(d*(a*a-1))
        m=-(a*a-d)/(a*(d-1))
        return {'apex':p,'cube_minus':q*(1-m)/2,'cube_plus':q*(1+m)/2}
    return {'apex':1/(d+1),'cube_minus':d/(d+1),'cube_plus':0.0}


def check(d,a):
    c,b,r,k=candidate(d,a)
    p=contact_probabilities(d,a)
    assert min(p.values())>=-2e-12
    assert abs(sum(p.values())-1)<2e-12
    apex=(a-c)/b
    uplus=(1-c)/b
    uminus=(-1-c)/b
    v=1/r
    norms={'apex':apex*apex,'cube_minus':uminus**2+(d-1)*v*v,
           'cube_plus':uplus**2+(d-1)*v*v}
    assert max(norms.values())<=1+5e-12,(d,a,norms)
    mean=p['apex']*apex+p['cube_minus']*uminus+p['cube_plus']*uplus
    var1=p['apex']*apex**2+p['cube_minus']*uminus**2+p['cube_plus']*uplus**2
    varperp=(p['cube_minus']+p['cube_plus'])*v*v
    assert abs(mean)<5e-12, (d,a,mean)
    assert abs(var1-1/d)<5e-12,(d,a,var1)
    assert abs(varperp-1/d)<5e-12,(d,a,varperp)
    for type_,w in p.items():
        if w>1e-10:
            assert abs(norms[type_]-1)<5e-12,(d,a,type_,norms)
    return c,b,r,norms


def opt(d,a):
    c,b,r,_=candidate(d,a)
    u0,v0,z0=1/b,1/r,-c/b
    def obj(t):
        u,v,z=t
        return -(math.log(u)+(d-1)*math.log(v)) if u>0 and v>0 else 1e12
    def cons(t):
        u,v,z=t
        return np.array([1-(z-u)**2-(d-1)*v*v,
                         1-(z+u)**2-(d-1)*v*v,
                         1-(a*u+z)**2])
    res=minimize(obj,[u0,v0,z0],method='SLSQP',bounds=[(1e-9,None),(1e-9,None),(None,None)],
                 constraints={'type':'ineq','fun':cons},
                 options={'ftol':1e-11,'maxiter':300})
    assert res.success or abs(res.fun-obj([u0,v0,z0]))<2e-9,(d,a,res.message)
    assert np.min(cons(res.x))>=-2e-7,(d,a,cons(res.x))
    # The optimizer is the independent convex primal; its objective must agree.
    assert abs(res.fun-obj([u0,v0,z0]))<3e-7,(d,a,res.fun,obj([u0,v0,z0]))
    return abs(res.fun-obj([u0,v0,z0]))


def verify():
    count=0;errs=[]
    for d in list(range(2,21))+[25,40,60,100]:
        grid=[1,1.01, math.sqrt(d)*(1-1e-7),math.sqrt(d),math.sqrt(d)*(1+1e-7),
              (math.sqrt(d)+d)/2,d*(1-1e-7),d,d*(1+1e-7),2*d,5*d]
        grid += [1.0+(5*d-1)*j/31 for j in range(32)]
        for a in grid:
            check(d,a)
            count+=1
    for d in [2,3,4,5,8,12,20]:
        for a in [1,math.sqrt(d)*.96,math.sqrt(d),math.sqrt(d)*1.04,
                  (math.sqrt(d)+d)/2,d*.99,d,d*1.01,1.5*d,3*d]:
            errs.append(opt(d,a))
    print('PASS: %d containment-and-isotropic-certificate cases, %d independent convex optimizations, maximum log-volume discrepancy %.3g' % (count,len(errs),max(errs)))

if __name__=='__main__':
    verify()
