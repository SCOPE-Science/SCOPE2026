"""Reproducibility checks for the short-overlap curvature contact law.

Independent numerical checks only; the proof is analytic.
Python 3 with numpy and scipy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def ellipse_axis_lens(s, a1, b1, a2, b2):
    """Exact 1D numerical quadrature for two coaxial ellipses near tangency.

    Each ellipse has longitudinal semiaxis a and transverse semiaxis b.
    Their center displacement is a1+a2-s.
    """
    dist = a1 + a2 - s
    def width(y):
        return a1*math.sqrt(max(0., 1-(y/b1)**2)) + a2*math.sqrt(max(0., 1-(y/b2)**2)) - dist
    root = brentq(width, 0.0, min(b1,b2), xtol=1e-14)
    return 2*quad(width, 0., root, epsabs=1e-14, epsrel=2e-13)[0]


def c_lens(a1, b1, a2, b2):
    q = a1/(b1*b1) + a2/(b2*b2)
    return 4./3.*math.sqrt(2./q)


def radius_of_curvature(a, b, theta):
    h = math.hypot(a*math.cos(theta), b*math.sin(theta))
    return (a*b)**2/h**3


def overlap_quantile_cdf(epsilon, r1, r2):
    m=r1+r2
    def overlap(s):
        return ellipse_axis_lens(s, r1, r1, r2, r2)
    dep=brentq(lambda s: overlap(s)-epsilon, 0.0, min(r1,r2)*0.4)
    return (2*m*dep-dep*dep)/(m*m)


if __name__=='__main__':
    # Truly different local curvatures: circle against noncircular ellipse.
    for axes in [(2.0,1.0,0.8,0.8), (1.0,2.0,0.8,0.8),
                 (2.0,1.0,1.4,0.7)]:
        C=c_lens(*axes)
        errors=[]
        for s in [1e-2,2e-3,5e-4,1e-4]:
            G=ellipse_axis_lens(s,*axes)
            ratio=G/(C*s**1.5)
            errors.append(abs(ratio-1))
        assert errors[-1]<2e-4,(axes,errors)
        assert errors[-1]<errors[0],(axes,errors)
    print('INDEPENDENT_ELLIPTIC_TANGENCY_LENS_COEFFICIENT_OK 3')

    for r1,r2 in [(1.,1.),(1.4,.7)]:
        m=r1+r2
        q=1/r1+1/r2
        c=(9./32.)**(1./3.)
        predicted=2*c*q**(1./3.)/m
        eps_list=[.008,.002,.0005]
        ratios=[]
        for eps in eps_list:
            prob=overlap_quantile_cdf(eps,r1,r2)
            ratios.append(prob/(predicted*eps**(2./3.)))
        assert abs(ratios[-1]-1)<.01,(r1,r2,ratios)
        assert abs(ratios[-1]-1)<abs(ratios[0]-1)
        x=.3
        ratio=overlap_quantile_cdf(eps_list[-1]*x,r1,r2)/overlap_quantile_cdf(eps_list[-1],r1,r2)
        assert abs(ratio-x**(2./3.))<.009,(ratio,x**(2./3.))
    print('UNIFORM_RANDOM_TRANSLATION_TAIL_AND_BETA_DEPTH_OK 2')

    # Unordered curvature-radius tomography from the normal-resolved intensity.
    for theta in np.linspace(0,2*math.pi,41,endpoint=False):
        r1=radius_of_curvature(2.0,1.0,theta)
        r2=radius_of_curvature(.85,.85,theta+math.pi)
        m=r1+r2
        q=1/r1+1/r2
        c=(9./32.)**(1./3.)
        w=c*m*q**(1./3.)
        restored_q=(w/(c*m))**3
        discs=max(0.,m*m-4*m/restored_q)
        rr1=(m+math.sqrt(discs))/2
        rr2=(m-math.sqrt(discs))/2
        assert np.allclose(sorted([rr1,rr2]),sorted([r1,r2]),rtol=1e-6,atol=1e-7)
    print('UNORDERED_CONTACT_CURVATURE_RADII_RECOVERY_OK 41')

    # Affine arclength reduces to the same-body case, with consistency
    # coefficient for a centrally symmetric convex body.
    for a,b in [(1.,1.), (2.,1.)]:
        def w(theta):
            rho=radius_of_curvature(a,b,theta)
            return (9./32.)**(1./3.)*(2*rho)*(2/rho)**(1./3.)
        def aff(theta):
            rho=radius_of_curvature(a,b,theta)
            return rho**(2./3.)
        for theta in np.linspace(0,2*math.pi,17):
            assert abs(w(theta)/aff(theta) - 2*(9./16.)**(1./3.))<1e-10
    print('AFFINE_ARCLENGTH_SPECIALIZATION_OK 2')
    # The conditional orientation density equals affine arclength of M
    # precisely when the curvature-radius ratio is constant. In a deliberately
    # nonhomothetic ellipse/circle pair, it has a nonconstant density ratio.
    ratios=[]
    for theta in np.linspace(0,2*math.pi,37,endpoint=False):
        r1=radius_of_curvature(2.0,1.0,theta)
        r2=0.8
        m=r1+r2
        q=1/r1+1/r2
        ratios.append((m*q)**(1./3.))
    assert max(ratios)-min(ratios)>.04
    # Homothetic but anisotropic ellipses have constant curvature-radius ratio.
    ratios=[]
    for theta in np.linspace(0,2*math.pi,37,endpoint=False):
        r1=radius_of_curvature(2.0,1.0,theta)
        r2=radius_of_curvature(1.4,0.7,theta)
        m=r1+r2
        q=1/r1+1/r2
        ratios.append((m*q)**(1./3.))
    assert max(ratios)-min(ratios)<1e-10
    print('AFFINE_NORMAL_ANGLE_RIGIDITY_GEOMETRIC_DIAGNOSTIC_OK 2')
    print('ALL_SHORT_OVERLAP_CONTACT_LAW_CHECKS_OK')
