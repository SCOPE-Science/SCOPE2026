"""Numerical cross-checks of the affine-circle acute-triangle identity.

This program checks analytic identities and independently samples triangles.
The all-parameter theorem rests on the accompanying mathematical proof,
not on these finite computations.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spence


def p_dilog(ratio):
    assert ratio >= 1
    k = (ratio**2 - 1)/(ratio**2 + 1)
    return .25 - 3/(2*math.pi**2)*spence(1-k*k)


def p_independent_integral(ratio):
    k = (ratio**2 - 1)/(ratio**2 + 1)
    integral = quad(lambda x: math.asin(k*math.sin(x))**2,
                    0, math.pi/2, epsabs=3e-13, epsrel=3e-13)[0]
    return .25 - 6/math.pi**3*integral


def sample_probability(ratio, random_angles):
    points = np.stack((ratio*np.cos(random_angles),np.sin(random_angles)),axis=2)
    signs=[]
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        d=points[:,j]-points[:,i]
        e=points[:,k]-points[:,i]
        signs.append(np.einsum('ij,ij->i',d,e)>0)
    return float(np.mean(signs[0]&signs[1]&signs[2]))


def main():
    ratios=(1.,1.1,2.,3.,10.,100.)
    for a in ratios:
        p1=p_dilog(a)
        p2=p_independent_integral(a)
        assert abs(p1-p2)<1e-11,(a,p1,p2)
        assert 0<p1<=.25
    print('DILOGARITHM_MATCHES_INDEPENDENT_SPHERICAL_ANGLE_QUADRATURE_OK')
    assert abs(p_dilog(1)-.25)<1e-15
    last=1.
    for ratio in np.geomspace(1,1000,80):
        p=p_dilog(ratio)
        assert p<=last+1e-14 and p>0
        last=p
    print('STRICT_ANISOTROPY_MONOTONICITY_SAMPLED_OK')
    for r in (1.00001,1.0001,1.001):
        s=math.log(r)
        leading=.25-3/(2*math.pi**2)*s*s
        assert abs(p_dilog(r)-leading)<1e-9
    for t in (1e-2,1e-3):
        p=p_dilog(1/t)
        asym=6/math.pi**2*t*t*(1-math.log(4*t*t))
        assert abs(p/asym-1)<.002,(t,p,asym)
    print('NEAR_CIRCLE_AND_THIN_ELLIPSE_ASYMPTOTICS_OK')
    rng=np.random.default_rng(4131)
    n=220000
    theta=rng.uniform(0,2*math.pi,size=(n,3))
    for ratio in (1.,1.1,2.,3.,10.):
        prob=p_dilog(ratio)
        observed=sample_probability(ratio,theta)
        standard_error=math.sqrt(prob*(1-prob)/n)
        assert abs(observed-prob)<5*standard_error,(ratio,observed,prob)
    print(f'INDEPENDENT_CARTESIAN_THREE_VERTEX_MONTE_CARLO_OK_{n}')
    print('ALL_AFFINE_ELLIPSE_ACUTENESS_CHECKS_OK')

if __name__=='__main__':main()
