#!/usr/bin/env python3
"""Numerical tests for the finite-dimensional simplex-width first-overlap theorem.
No external service; Python 3, NumPy and SciPy are used for numerical integration."""
from itertools import permutations
from math import acos, gamma, pi, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc
C=sqrt(3)/2
T0=sqrt(2/3)

def cap(d,t):
    return 0.5*betainc((d-1)/2,.5,1-t*t)
def lens(d,t):
    if t >= C: return 0.
    if d==2: return (2*acos(t)-pi/3)/(2*pi)
    def f(z):
        w=min(1.,max(0.,((C*z-t)/(.5*sqrt(max(1e-300,1-z*z))))**2))
        return (gamma(d/2)/(sqrt(pi)*gamma((d-1)/2)) * (1-z*z)**((d-3)/2) * betainc(.5,(d-2)/2,w))
    z_split=C*t+.5*sqrt(1-t*t)
    return quad(f,t/C,1.,points=[z_split],epsabs=1e-12)[0]
def tail(d,t):
    return d*(d+1)*cap(d,t)-d*(d*d-1)*lens(d,t)
def coefficient(d):
    return 4*(d*d-1)/pi * (4/sqrt(3))**((d-2)/2)
def roots(d):
    m=d+1
    # Oriented roots in hyperplane orthogonal to (1,...,1).
    a=[]
    for i,j in permutations(range(m),2):
        u=np.zeros(m); u[i]=1/sqrt(2); u[j]=-1/sqrt(2); a.append(u)
    return np.asarray(a)
def run():
    tests=0
    for d in range(2,9):
        a=roots(d);g=a@a.T
        M=d*(d+1)
        assert len(a)==M
        assert np.allclose(np.diag(g),1,atol=1e-14)
        assert all(np.sum(np.isclose(g[i],0.5,atol=1e-13)) ==2*(d-1) for i in range(M))
        # Any three distinct roots have average norm at most sqrt(2/3).
        assert max(g[i,j] for i in range(M) for j in range(M) if i!=j) < .50000000001
        tests+=3
        for t in [C, C-.001, C-.008]:
            val=tail(d,t)
            assert 0 <= val <= 1+2e-12,(d,t,val)
            tests+=1
        dlt=1e-4
        corr=M*cap(d,C-dlt)-tail(d,C-dlt)
        assert abs(corr/dlt**(d/2)/coefficient(d)-1)<.001,(d,corr)
        tests+=1
    # Independent Monte Carlo: sample uniform directions in sum-zero hyperplane.
    rng=np.random.default_rng(20261029)
    for d in [2,3,4,5]:
        m=d+1
        N=360000
        z=rng.normal(size=(N,m))
        z-=z.mean(axis=1,keepdims=True)
        z/=np.linalg.norm(z,axis=1,keepdims=True)
        widths=(z.max(axis=1)-z.min(axis=1))/sqrt(2)
        for t in [C+.02, C-.02, C-.04]:
            if t<T0:continue
            empirical=float((widths>=t).mean()); exact=tail(d,t)
            se=sqrt(max(exact*(1-exact),.0001)/N)
            assert abs(empirical-exact)<=6*se+0.0005,(d,t,empirical,exact,se)
            print('MC d=%d t=%.6f empirical=%.6f exact=%.6f 6sigma=%.6f'%(d,t,empirical,exact,6*se))
            tests+=1
    # Spherical lens Gauss-Bonnet formula in three dimensions.
    for t in [.82,.83,.84,.85,.86]:
        phi=acos(t/(sqrt(3)*sqrt(1-t*t)))
        gam=acos((.5-t*t)/(1-t*t))
        j=(2*pi-2*gam-4*t*phi)/(4*pi)
        assert abs(j-lens(3,t))<1e-11,(j,t)
        tests+=1
    print('PASS',tests,'grouped tests; cap-lens exact and first-overlap checks')
if __name__=='__main__':run()
