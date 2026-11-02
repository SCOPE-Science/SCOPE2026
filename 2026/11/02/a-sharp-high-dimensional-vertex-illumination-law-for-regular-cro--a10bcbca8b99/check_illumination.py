"""Standalone numerical checks for random illumination of cross-polytopes.

Numerically integrates the elementary two-dimensional Dirichlet case and
compares Gaussian direction simulation with the closed asymptotic factor.
"""
import math
import numpy as np
from scipy.integrate import dblquad
from scipy.special import gammaln

RNG = np.random.default_rng(20261027)

def prefactor(d):
    return math.exp(math.log(d) + (1-d)*math.log(math.pi)/2 - math.lgamma((d+1)/2))

def exp_dirichlet(d, total=100000, chunk=2000):
    sw=sw2=sy=0.
    done=0
    while done < total:
        n=min(chunk,total-done)
        t=RNG.exponential(size=(n,d))
        t/=t.sum(axis=1,keepdims=True)
        s=(t[:,:-1]**2).sum(axis=1)
        w=(1+s)**(-d/2)
        sw+=w.sum(); sw2+=(w*d*t[:,0]).sum(); sy+=(w*d*s/2).sum()
        done+=n
    return sw/total,sw2/sw,sy/sw

def gaussian_check(d,total=600000,chunk=10000):
    count=0;done=0
    while done<total:
        n=min(chunk,total-done)
        x=np.abs(RNG.standard_normal(size=(n,d)))
        top=np.max(x,axis=1)
        count+=(top > x.sum(axis=1)-top).sum()
        done+=n
    return count/total

if __name__ == '__main__':
    assert math.isclose(prefactor(2)*math.pi/4,1,rel_tol=1e-14)
    w3,err3=dblquad(lambda t2,t1:2*(1+t1*t1+t2*t2)**(-1.5),0,1,
                     lambda t1:0,lambda t1:1-t1,epsabs=1e-11,epsrel=1e-11)
    p3=prefactor(3)*w3
    target=6*math.asin(1/3)/math.pi
    assert abs(p3-target)<1e-12, (p3,target)
    print(f'd=2: exact full-sphere illumination = 1')
    print(f'd=3: integral={p3:.12f}, octahedral solid angle={target:.12f}, quadrature error={err3:.2g}')
    for d in [3,4,5,8]:
        eg=gaussian_check(d)
        ew,m1,ys=exp_dirichlet(d,total=90000)
        pred=prefactor(d)*ew
        err=abs(eg-pred)
        tol=5*math.sqrt(max(eg*(1-eg),1e-12)/600000)+.013*pred
        print(f'd={d}: Gaussian={eg:.8g}, Dirichlet={pred:.8g}, discrepancy={err:.3g}, tolerance={tol:.3g}')
        assert err<tol, (d,err,tol)
    for d in [12,30,80,160,320]:
        ew,m1,ys=exp_dirichlet(d,total=50000)
        print(f'd={d}: ratio-to-asymptotic={math.e*ew:.7f}, E[d*T1|event]={m1:.7f}, E[d*S2/2|event]={ys:.7f}')
        if d>=160: assert abs(math.e*ew-1)<.05 and abs(m1-1)<.1 and abs(ys-1)<.1
    print('PASS: analytic special cases, Gaussian simulation, and large-d limit checks')
