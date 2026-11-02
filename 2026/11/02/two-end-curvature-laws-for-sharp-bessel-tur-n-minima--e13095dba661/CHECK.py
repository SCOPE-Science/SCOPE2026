#!/usr/bin/env python3
"""Supplementary numeric checks for two-end Bessel Turan curvature asymptotics.
Run: python CHECK.py (requires scipy and numpy). Numerical checks are not proofs.
"""
import math
from scipy.special import jv, jvp, jn_zeros, ai_zeros, airy
from scipy.optimize import minimize_scalar

checks=0

def insist(condition, description):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(description)


def phi(mu,x):
    j=jv(mu,x)
    jd=jvp(mu,x)
    return 1.0+(jd/j)**2-(mu/x)**2

def small_order_check():
    import mpmath as mp
    mp.mp.dps=45
    for n in (1,2,3):
        j=jn_zeros(1,n)[-1]
        c3=2.0/(j**4*jv(0,j)**2)
        for mu in (0.01,0.03,0.06):
            left=float(mp.besseljzero(mu,n)); right=float(mp.besseljzero(mu,n+1))
            opt=minimize_scalar(lambda x:phi(mu,x),bounds=(left+0.15*(right-left),right-0.15*(right-left)),method='bounded',options={'xatol':1e-13})
            approx=1-mu**2/j**2+c3*mu**3
            insist(abs(opt.fun-approx) < (0.07 if n==1 else 0.01)*mu**4, 'cubic remainder small mu n='+str(n))
            insist(left<opt.x<right,'minimizer between zeros')
            insist(0<opt.fun<1,'positive less than one')


def airy_F(s):
    A,Ap,_,_=airy(-2**(1/3)*s)
    q=-2**(1/3)*Ap/A
    return 2*s+q*q

def large_order_check():
    ss=-ai_zeros(4)[0]/2**(1/3)
    for n in (1,2,3):
        a,b=ss[n-1:n+1]
        sol=minimize_scalar(airy_F,bounds=(a+0.08,b-0.08),method='bounded',options={'xatol':1e-13})
        c=sol.fun
        insist(c>0,'Airy positive minimum')
        insist(a<sol.x<b,'Airy min lies within nodal interval')
        errs=[]
        for mu in (100,200,400):
            scale=mu**(1/3)
            left=mu+(a+0.1)*scale
            right=mu+(b-0.1)*scale
            sol2=minimize_scalar(lambda x:phi(mu,x),bounds=(left,right),method='bounded',options={'xatol':1e-11})
            scaled=sol2.fun*mu**(2/3)
            errs.append(abs(scaled-c))
            insist(abs(scaled-c) < 65.0*mu**(-2/3),'large-order remainder')
        insist(errs[-1]<errs[0],'large-order convergence')
    return ss

if __name__=='__main__':
    small_order_check()
    large_order_check()
    print('CHECKS_OK',checks)
