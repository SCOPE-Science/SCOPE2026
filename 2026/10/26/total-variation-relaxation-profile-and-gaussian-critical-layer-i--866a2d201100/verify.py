#!/usr/bin/env python3
"""Standalone deterministic checks for the finite-chain relaxation theorem.
No sampling; finite quadrature is not used as a proof of limiting statements.
"""
from math import sqrt, pi, exp, erf, log
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtr, gammainc, gammaincc
from scipy.stats import gamma
import numpy as np

SQRT2PI=sqrt(2*pi)

def phi(z): return exp(-z*z/2)/SQRT2PI

def profile(s): return phi(1)*(phi(s)-s*(1-ndtr(s)))

def exact_fourier(n,c,k):
    return exp(-.5*k*k*c)*gammaincc(n,n*c)+(1/(1+k*k/(2*n)))**n * gammainc(n,n*c+.5*k*k*c)
    # Dimensionless Y=X/sqrt(2Dn/r).  E exp(ikY)=E exp(-k^2 min(U,c)/2).

def exact_fourier_quad(n,c,k):
    f=lambda u: gamma.pdf(u,a=n,scale=1/n)*exp(-.5*k*k*min(u,c))
    return quad(f,0,c,epsabs=2e-12,limit=200)[0]+quad(f,c,np.inf,epsabs=2e-12,limit=200)[0]

def tv_exact(n,c):
    """One-crossing identity; integral over U>c only."""
    assert c>0
    surv=gammaincc(n,n*c)
    upper=gamma.ppf(1-2e-14,a=n,scale=1/n)
    if c>=upper:
        return 0., float('nan')
    def tail_expect(h):
        return quad(lambda u: gamma.pdf(u,a=n,scale=1/n)*h(u),c,upper,epsabs=5e-11,epsrel=5e-11,limit=300)[0]
    def signed(y):
        gc=phi(y/sqrt(c))/sqrt(c)
        return gc*surv-tail_expect(lambda u:phi(y/sqrt(u))/sqrt(u))
    yhi=1.
    while signed(yhi)>0 and yhi<100: yhi*=2
    root=brentq(signed,0,yhi,xtol=2e-11)
    mass=tail_expect(lambda u:erf(root/sqrt(2*c))-erf(root/sqrt(2*u)))
    assert mass>0
    return mass,root

def normal_tv(theta):
    a=sqrt(theta*log(1/theta)/(1-theta))
    return 2*(ndtr(a/sqrt(theta))-ndtr(a))

def main():
    checks=0
    for n in [1,2,4,11,37]:
      for c in [.2,.6,1.1,2.]:
       for k in [.3,.9,1.6]:
        d=abs(exact_fourier(n,c,k)-exact_fourier_quad(n,c,k))
        assert d<5e-10,(n,c,k,d)
        checks+=1
    print('Fourier identity: 60 quadrature checks passed')
    for n in [30,80,180,480]:
        for theta in [.4,.75]:
            val,a=tv_exact(n,theta)
            target=normal_tv(theta)
            print(f'precritical n={n}, theta={theta}: TV={val:.8f}, target={target:.8f}, single-crossing x={a:.6f}')
            assert 0<val<1 and a>0
            if n==480: assert abs(val-target)<.002
            checks+=1
    for s in [-1.,0.,1.]:
        tgt=profile(s)
        for n in [40,120,360,900]:
            c=1+s/sqrt(n)
            tv,a=tv_exact(n,c)
            obs=sqrt(n)*tv
            print(f'critical s={s},n={n}: sqrt(n) TV={obs:.8f}, theory={tgt:.8f}')
            assert tv>0 and a>0
            if n==900: assert abs(obs-tgt)<.009,(s,obs,tgt)
            checks+=1
    for n in [30,80,200]:
        val,a=tv_exact(n,1.3)
        assert val<=gammaincc(n,1.3*n)+1e-12
        checks+=1
    assert abs(profile(0)-exp(-.5)/(2*pi))<1e-14
    checks+=1
    print(f'PASS: {checks} deterministic checks')

if __name__=='__main__': main()
