"""Standalone numerical checks for planar renewal swimmers with constant curvature.

Dependencies: Python 3, numpy, scipy. Run `python checks/verify.py`.
The theorem's infinite-time claims use analytic arguments, not finite tests.
"""
from math import cos, gamma, pi
import numpy as np
from scipy.integrate import quad
import mpmath as mp


def diffusivity_from_cycles(v, mu, omega, expected_cos):
    return v*v*(1.0-expected_cos)/(2.0*mu*omega*omega)


def lomax_cos(alpha, ell, omega):
    # Exact characteristic function via a generalized exponential integral.
    mp.mp.dps=55
    a, h, w=mp.mpf(str(alpha)),mp.mpf(str(ell)),mp.mpf(str(omega))
    integral=mp.im(h*mp.exp(-1j*w*h)*mp.expint(a,-1j*w*h))
    return float(1-w*integral)


def direct_msd_zero(alpha, ell, v, t):
    value, err=quad(lambda s: (t-s)*(1+s/ell)**(1-alpha), 0, t,
                    epsabs=1e-7, epsrel=1e-10, limit=400)
    return 2*v*v*value


def run():
    checks=0
    rng=np.random.default_rng(20261028)
    for alpha in (1.2,1.5,1.8):
        ell=1.3;v=1.7;mu=ell/(alpha-1)
        pref=(v*v*ell**(alpha-1)/2)*gamma(2-alpha)*(-cos(pi*alpha/2))
        for omega in (1e-7,1e-8,1e-9):
            cos_avg=lomax_cos(alpha,ell,omega)
            d=diffusivity_from_cycles(v,mu,omega,cos_avg)
            approximate=pref*omega**(alpha-2)
            assert np.isfinite(d) and d>0
            # convergence of the singular prefactor, with finite-frequency corrections
            assert abs(d/approximate-1)<0.055,(alpha,omega,d,approximate,d/approximate)
            checks+=1
        for t in (1e6,1e7,1e8):
            U=1+t/ell
            exact=2*v*v*(ell*(t+ell)*(U**(2-alpha)-1)/(2-alpha) - ell**2*(U**(3-alpha)-1)/(3-alpha))
            asym=2*v*v*ell**(alpha-1)*t**(3-alpha)/((2-alpha)*(3-alpha))
            assert abs(exact/asym-1)<0.085,(alpha,t,exact/asym)
            checks+=1
        direct=direct_msd_zero(alpha,ell,v,1000)
        U=1+1000/ell
        exact=2*v*v*(ell*(1000+ell)*(U**(2-alpha)-1)/(2-alpha)-ell*ell*(U**(3-alpha)-1)/(3-alpha))
        assert abs(direct/exact-1)<1e-8
        checks+=1
    # Standalone cycle Monte Carlo checks full-flight covariance, for two distinct nonzero angular speeds
    alpha=1.5;ell=1.0;v=1.0;mu=ell/(alpha-1)
    L=ell*rng.pareto(alpha,size=400000)
    Theta=rng.uniform(0,2*pi,size=len(L))
    for omega in (0.2,0.8,2.3):
        Y=v/(1j*omega)*np.exp(1j*Theta)*(np.exp(1j*omega*L)-1)
        # Starting headings are uniform; per-cycle displacement is bounded by 2v/|omega|.
        assert np.max(np.abs(Y)) <=2*v/abs(omega)+1e-12
        d_emp=np.mean(np.abs(Y)**2)/(4*mu)
        d_exact=diffusivity_from_cycles(v,mu,omega,lomax_cos(alpha,ell,omega))
        assert abs(d_emp/d_exact-1)<0.02, (omega,d_emp,d_exact)
        assert abs(np.mean(Y))<0.025
        checks+=3
    # Negative control: full circles close exactly at deterministic integer periods.
    for ell in (2*pi,4*pi,6*pi):
        Y=(np.exp(1j*ell)-1)/1j
        assert abs(Y)<1e-14
        checks+=1
    print('PASS',checks,'standalone numerical/structural checks')

if __name__=='__main__':run()
