#!/usr/bin/env python3
"""Numerical cross-checks of a stationary three-state run-rest skewness theorem."""
import numpy as np
from scipy.optimize import brentq
from numpy.linalg import solve

def expression(a,b,w):
    P=a*(a+1)*(a+2)*(a-b)-(1-w*w)*b*b*(7*a*a+12*a+4+(7*a+6)*b+2*b*b)
    return 2*b*w*P/((a+1)*(a+2)*(a+b)**3*(a+b+1)*(a+b+2))

def direct_generator(a,b,w,d=0):
    # Dimensionless Ornstein-Uhlenbeck thermal diffusivity d >= 0.
    Q=np.array([[-a,a,0],[b*(1+w)/2,-b,b*(1-w)/2],[0,a,-a]],float)
    stationary=np.array([b*(1+w)/(2*(a+b)),a/(a+b),b*(1-w)/(2*(a+b))])
    velocities=np.array([1.,0.,-1.]);m=[stationary]
    for n in (1,2,3):
        rhs=n*velocities*m[n-1]
        if n>=2: rhs+=n*(n-1)*d*m[n-2]
        m.append(solve(n*np.eye(3)-Q.T,rhs))
    u=[v.sum() for v in m]
    return u[3]-3*u[1]*u[2]+2*u[1]**3

def main():
    r=np.random.default_rng(42)
    n=0
    for _ in range(60):
        a,b=10**r.uniform(-1,1.5,2);w=r.uniform(.03,.97)
        expected=expression(a,b,w)
        assert abs(direct_generator(a,b,w)-expected)<3e-12*max(1,abs(expected))
        assert abs(direct_generator(a,b,w,.27)-expected)<3e-12*max(1,abs(expected))
        n+=2
    for a in [.2,1.,5.]:
        prev=-1
        for w in [.1,.5,.9]:
            h=lambda b:expression(a,b,w)
            root=brentq(h,1e-10,a)
            assert 0<root<a and root>prev
            assert h(root*.99)>0 and h(root*1.01)<0
            prev=root
            print('a=%.3g w=%.3g threshold=%.9f'%(a,w,root))
            n+=1
    print('PASS:',n,'independent generator/thermal/threshold cases (each transition checks both signs)')
if __name__=='__main__':main()
