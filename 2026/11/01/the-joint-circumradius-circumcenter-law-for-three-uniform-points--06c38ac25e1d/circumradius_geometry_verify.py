#!/usr/bin/env python3
"""Independent numerical and algebraic checks of a random-circumcircle law.

Requires numpy and scipy. Runs as `python circumradius_geometry_verify.py`.
The analytic change-of-variables proof, not these finite tests, is the theorem.
"""
from math import acos, cos, pi, sin
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc


def angular_kernel(alpha):
    return 24.0 * (alpha**2 + alpha * sin(2*alpha) / 2.0 + cos(2*alpha) - 1.0)


def gap_quadrature(alpha):
    def outer(u):
        return quad(lambda v: 192.0 * (alpha-u-v) * sin(u) * sin(v) * sin(u+v),
                    0., alpha-u, epsabs=1e-11)[0]
    return quad(outer, 0., alpha, epsabs=1e-11)[0]


def cap_half_angle(s, r):
    if s+r <= 1.0:
        return pi
    if abs(s-r) >= 1.0:
        return 0.0
    return acos(np.clip((s*s+r*r-1.0)/(2*s*r), -1., 1.))


def joint_density(r, s):
    if r <= 0 or s <= 0:
        return 0.0
    return 2*r**3*s/(pi*pi)*angular_kernel(cap_half_angle(s, r))


def exterior_density(r):
    if r <= 0:
        return 0.
    return quad(lambda s: joint_density(r,s), abs(1-r), 1+r,
                epsabs=2e-10, epsrel=2e-10, limit=200)[0]


def density(r):
    return 24*r**3*max(1-r,0)**2 + exterior_density(r) if r > 0 else 0.0


def check():
    n = 0
    for alpha in [pi/6, pi/4, pi/2, 2*pi/3, 5*pi/6, pi]:
        a, b = angular_kernel(alpha), gap_quadrature(alpha)
        assert abs(a-b) < 5e-9, (alpha, a, b)
        assert a > 0
        n += 2
    assert abs(angular_kernel(pi)-24*pi*pi) < 1e-10
    assert abs(quad(lambda r: 24*r**3*(1-r)**2, 0, 1)[0] - 0.4) < 1e-12
    n += 2
    p1 = quad(density, 0, 1, epsabs=2e-9, epsrel=2e-9)[0]
    p1_known = 4 - 32/(pi*pi)
    assert abs(p1-p1_known) < 2e-8, (p1,p1_known)
    n += 1
    extmass=p1-0.4
    assert abs(extmass-(18/5-32/(pi*pi))) < 2e-8
    assert exterior_density(0.5)>0
    assert exterior_density(1.5)>0
    n += 3
    # Exact small-radius noncontained coefficient from an independent angular integral.
    small_coeff = 48 - 1024/(3*pi*pi)
    a = quad(lambda alpha: angular_kernel(alpha)*sin(alpha),0,pi,epsabs=1e-10)[0]
    assert abs(2*a/(pi*pi)-small_coeff)<1e-10
    assert abs(exterior_density(0.005)/0.005**4 - small_coeff) < 0.2
    n += 2
    # Sampling check uses quasi-random triples and directly computes circumcentres.
    U=qmc.Sobol(d=6, scramble=True, seed=20261026).random_base2(m=19)
    angles=2*pi*U[:,[1,3,5]]
    radii=np.sqrt(U[:,[0,2,4]])
    xs=radii*np.cos(angles)
    ys=radii*np.sin(angles)
    ax=xs[:,1]-xs[:,0];ay=ys[:,1]-ys[:,0]
    bx=xs[:,2]-xs[:,0];by=ys[:,2]-ys[:,0]
    cross=ax*by-ay*bx
    side_a=np.hypot(ax,ay)
    side_b=np.hypot(bx,by)
    side_c=np.hypot(xs[:,2]-xs[:,1],ys[:,2]-ys[:,1])
    rho=side_a*side_b*side_c/(2*np.abs(cross))
    q1=(xs[:,1]**2+ys[:,1]**2-xs[:,0]**2-ys[:,0]**2)/2
    q2=(xs[:,2]**2+ys[:,2]**2-xs[:,0]**2-ys[:,0]**2)/2
    cx=(q1*by-q2*ay)/cross
    cy=(ax*q2-bx*q1)/cross
    s=np.hypot(cx,cy)
    cover=np.mean(rho+s<1)
    p_below=np.mean(rho<=1)
    assert abs(cover-.4)<.004, cover
    assert abs(p_below-p1_known)<.004, (p_below,p1_known)
    n += 2
    for r,h,tol in [(0.5,0.03,0.045),(0.75,0.025,0.045),
                    (0.95,0.03,0.055),(1.5,0.07,0.022)]:
        empirical=np.mean((rho>=r-h)&(rho<r+h))/(2*h)
        expected=density(r)
        assert abs(empirical-expected)<tol,(r,empirical,expected)
        n += 1
    print(f'PASS {n} substantive exact/numerical comparisons')
    print(f'P(rho < 1): quadrature {p1:.12f}, established value {p1_known:.12f}')
    print(f'P(rho < 1, circle crosses boundary): {extmass:.12f}')
    print(f'P(contained circle): quadrature 0.4, sampled {cover:.5f}')
    print(f'P(rho < 1): sampled {p_below:.5f}')
    print(f'exterior density small-r coefficient: {small_coeff:.12f}')
    for r in [0.25,0.5,0.75,0.9,1.0,1.5,2.,5.]:
        print(f'  density({r:g}) = {density(r):.12f}')

if __name__=='__main__':
    check()
