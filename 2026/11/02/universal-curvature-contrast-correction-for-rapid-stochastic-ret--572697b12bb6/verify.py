"""Finite-difference consistency test for a two-phase stochastic-return MFPT.

Requires NumPy and SciPy. Computes two independent killed resolvents:
probability of success in a search/return cycle, and the Dynkin
comparison integral. These numerical checks do not certify continuum limits.
"""
from math import exp, log, cosh, sqrt
import numpy as np
from scipy import sparse, special, integrate
from scipy.sparse.linalg import spsolve

def solve(k1,c1,k2,c2,r,step=0.0004):
    left=-3.0; right=1.0
    n=int(round((right-left)/step)); h=(right-left)/n
    x=left+h*np.arange(1,n); b1=-k1*x-c1*np.tanh(x)
    b2=-k2*x-c2*np.tanh(x)
    dx=0.00025
    xx=np.arange(-10,1.0005,dx)
    J=np.exp(-k2*xx**2/2-c2*np.log(np.cosh(xx)))
    I=integrate.cumulative_trapezoid(J,xx,initial=0)
    yprime=-np.interp(x,xx,I)/np.exp(-k2*x*x/2-c2*np.log(np.cosh(x)))
    xp=np.arange(0,1.0005,dx)
    sp=np.exp(k2*xp**2/2+c2*np.log(np.cosh(xp)))
    si=integrate.cumulative_trapezoid(sp,xp,initial=0)
    S=si[-1]
    hret=np.interp(x,xp,si,left=0,right=S)/S
    forcing=(b1-b2)*yprime
    upper=np.ones_like(x)/h**2 +b1/(2*h)
    lower=np.ones_like(x)/h**2 -b1/(2*h)
    diagonal=(-2/h**2-r)*np.ones_like(x)
    A=sparse.diags((lower[1:],diagonal,upper[:-1]),(-1,0,1),format='csc')
    rp=-r*hret;rp[-1]-=upper[-1]
    rw=-forcing
    p=np.interp(0,x,spsolve(A,rp));w=np.interp(0,x,spsolve(A,rw))
    difference=w/p
    prediction=4*((k1+c1)-(k2+c2))*S*r**(-1.5)
    return difference,p,prediction,S

if __name__ == "__main__":
    tests=0
    for pair in [(1.8,0.6,1.0,0.2), (0.6,0.1,1.2,0.7), (1.0,0.1,1.0,0.1)]:
        for r in [100,400,900]:
            delta, p, prediction, S=solve(*pair,r)
            assert np.isfinite([delta,p,prediction,S]).all()
            assert 0<p<1 and S>0
            if abs(prediction)>1e-12:
                ratio=delta/prediction
                assert abs(ratio-1)<0.04
                if r>=400: assert abs(ratio-1)<0.012
                assert delta*prediction>0
            else:
                assert abs(delta)<1e-12
                ratio=float("nan")
            tests+=1
            print("parameters", pair, "reset rate", r, "cycle success",round(p,9),
                  "mean correction",round(delta,10), "asymptotic",round(prediction,10),
                  "ratio",round(ratio,8))
    print("PASS:",tests,"independent numerical resolvent consistency cases")
