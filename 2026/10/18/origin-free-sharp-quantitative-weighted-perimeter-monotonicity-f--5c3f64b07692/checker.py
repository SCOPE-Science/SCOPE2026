"""Numerical supplementary checks for radial-exponential surface-area monotonicity.
Requires Python 3 with scipy and numpy. The analytical proof is in RESULT.md.
"""
import math
import random
from scipy.special import ive, gammaln, roots_jacobi, logsumexp
import numpy as np


def log_energy(n, lam, center, radius):
    assert n >= 2 and lam >= 0 and radius > 0
    s = float(np.linalg.norm(center))
    nu = n/2 - 1
    z = 2*lam*s*radius
    if z < 1e-12:
        log_ang = 0.0
    else:
        log_ang = nu*math.log(2/z) + gammaln(nu+1) + math.log(ive(nu,z)) + z
    log_sphere = math.log(2) + (n/2)*math.log(math.pi) - gammaln(n/2)
    return log_sphere + (n-1)*math.log(radius) + lam*(s*s+radius*radius) + log_ang


def direct_energy(n, lam, s, r):
    x,w = roots_jacobi(240,(n-3)/2,(n-3)/2)
    rho2=s*s+r*r+2*s*r*x
    log_mean=logsumexp(np.log(w)+lam*rho2)-math.log(np.sum(w))
    log_sphere=math.log(2)+(n/2)*math.log(math.pi)-gammaln(n/2)
    return log_sphere+(n-1)*math.log(r)+log_mean


def check():
    rnd=random.Random(193206)
    comparisons=0
    for n in (2,3,4,7):
        for lam in (0,0.02,0.2,1.,3.):
            for _ in range(36):
                a=np.array([rnd.uniform(-2,2) for _ in range(n)])
                shift=np.array([rnd.uniform(-1,1) for _ in range(n)])
                r=rnd.uniform(.1,2.5)
                R=r+float(np.linalg.norm(shift))+rnd.uniform(.03,1.2)
                b=a+shift
                left=log_energy(n,lam,a,r)
                right=log_energy(n,lam,b,R)
                M=max(R,float(np.linalg.norm(a)),float(np.linalg.norm(b)))
                assert right-left >= (n-1)*(R-r)/M -1e-9, (n,lam,left,right)
                if rnd.random()<.07:
                    s=float(np.linalg.norm(a))
                    assert abs(log_energy(n,lam,a,r)-direct_energy(n,lam,s,r))<5e-9
                comparisons+=1
    for n in (2,3,4,7):
        nu=n/2-1
        for z in np.geomspace(.02,300,200):
            m=ive(nu+1,z)/ive(nu,z)
            assert m>=max(0,1-(n-1)/z)-1e-10
            assert 0<m<1
    print('PASS:',comparisons,'nested-ball inequalities; direct spherical quadratures; 800 Bessel barriers.')

if __name__=='__main__':
    check()
