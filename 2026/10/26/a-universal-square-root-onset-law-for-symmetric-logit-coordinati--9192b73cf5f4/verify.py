#!/usr/bin/env python3
"""Numerical and analytic-identity checks for a symmetric logit-feedback game."""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import expit
from scipy.signal import find_peaks


def flow(t, state, alpha, lam):
    x, y = state
    return np.array([expit(lam*(x-y))-x, alpha*(x-.5)])


def lienard(t, state, alpha, lam):
    z, v = state
    sigma=expit(lam*z)
    return np.array([v, -(1-lam*sigma*(1-sigma))*v-alpha*(sigma-.5)])


def inverse(z,v,alpha,lam):
    x=(expit(lam*z)+alpha/2-v)/(1+alpha)
    return np.array([x,x-z])


def run():
    # Verify exact phase-coordinate correspondence for many parameter points.
    rng=np.random.default_rng(15426)
    for _ in range(250):
        alpha=float(rng.uniform(.1,9))
        lam=float(rng.uniform(.4,8))
        x=float(rng.uniform(.05,.95))
        y=float(rng.uniform(-1,2))
        f=flow(0,(x,y),alpha,lam)
        z=x-y; v=f[0]-f[1]
        assert np.linalg.norm(inverse(z,v,alpha,lam)-[x,y],ord=np.inf)<1e-12
        dzdv=lienard(0,(z,v),alpha,lam)
        sig=expit(lam*z)
        direct_dv=(lam*sig*(1-sig))*(f[0]-f[1])-f[0]-alpha*f[0]
        assert abs(dzdv[1]-direct_dv)<1e-11
        assert (1-lam/4*math.cosh(lam*z/2)**-2) == (1-lam/4*math.cosh(lam*z/2)**-2)
    print('Exact reduction checks: 250 passed')

    # Check the sign of the proper-energy dissipation in the damped regimes.
    for lam in (1,3.9,4):
        grid=np.linspace(-3,3,3001)
        f=1-lam/4/np.cosh(lam*grid/2)**2
        assert f.min()>-1e-13
    print('Dissipation sign checks: passed')

    # Compare the oscillation amplitude with 0.5*sqrt(lambda-4).
    for alpha in (.5,2.0,5.0):
        delta=.04
        lam=4+delta
        sol=solve_ivp(lambda t,w:lienard(t,w,alpha,lam),(0,550),(.15,0),
                      method='DOP853',rtol=2e-10,atol=1e-12,dense_output=True)
        assert sol.success
        ts=np.linspace(430,550,10001)
        zs=sol.sol(ts)[0]
        peaks,_=find_peaks(zs,distance=80)
        assert len(peaks)>5
        amp=float(np.mean(zs[peaks][-5:]))
        ratio=amp/(math.sqrt(delta)/2)
        assert .965<ratio<1.025, (alpha,amp,ratio)
        # The symmetry implies the orbit has opposite half-wave extrema.
        min_ratio=abs(float(np.min(zs)))/amp
        assert abs(min_ratio-1)<.01
        print('alpha=',alpha,'lambda=',lam,'z-max=',round(amp,9),
              'amplitude-to-leading-ratio=',round(ratio,7))
    print('All finite parameter checks passed (not a substitute for proof).')

if __name__=='__main__':
    run()
