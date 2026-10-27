"""Numerical corroboration of local nodal-ray counts for real harmonic Steklov kernels.
Not a substitute for the all-parameter analytic proof.
"""
import math
import mpmath as mp
from scipy.optimize import brentq
mp.mp.dps=35

def kernel(sig,rho,theta):
    z=1-mp.mpf(rho)*mp.e**(1j*mp.mpf(theta))
    return float(2*mp.re(mp.polylog(mp.mpf(sig),z)/z)-1)

def expected_angles(sig):
    mu=1-sig
    return [(2*j+1)*math.pi/(2*mu) for j in range(64) if (2*j+1)<mu]

runs=0
for sig in (-0.5,-1.0,-2.5,-3.4,-4.6):
    mu=1-sig
    e=expected_angles(sig)
    for rho in (.025,.006):
        theta_max=math.acos(rho/2)
        xs=[theta_max*k/80 for k in range(81)]
        fs=[kernel(sig,rho,x) for x in xs]
        brackets=[(xs[k],xs[k+1]) for k in range(80) if fs[k]*fs[k+1]<0]
        roots=[brentq(lambda th:kernel(sig,rho,th),a,b,xtol=1e-12) for a,b in brackets]
        assert len(roots)==len(e),(sig,rho,roots,e)
        assert max(abs(kernel(sig,rho,root))*rho**mu for root in roots)<1e-7
        for i,(theta,t0) in enumerate(zip(roots,e)):
            a=(1/mu-0.5)*math.sin(t0)
            if rho==.006:
                assert abs((theta-t0)/rho-a)<0.08,(sig,rho,theta,t0,a)
        print(f'sigma={sig:5.1f} rho={rho:.3f} upper_roots={len(roots)}',
              'angles='+','.join(f'{th:.7f}' for th in roots))
        runs+=1
for sig in (0.0,.15,1.,2.,5.):
    for z in (-.9,.4,.3+.65j,-.85j):
        val=float(2*mp.re(mp.polylog(sig,z)/z)-1)
        assert val>0,(sig,z,val)
        runs+=1
print('PASS cases:',runs)
