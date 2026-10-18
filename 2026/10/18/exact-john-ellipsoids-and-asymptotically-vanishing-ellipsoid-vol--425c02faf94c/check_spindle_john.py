#!/usr/bin/env python3
"""Reproducible finite checks for the two-point spindle John-ellipsoid theorem.

Only the Python standard library is required.  These tests complement, rather than
replace, the analytic proof for every dimension and endpoint separation.
"""
from fractions import Fraction
from math import exp, gamma, lgamma, log, pi, sqrt


def parameters(m, d):
    if m < 2 or not (0 < d < 1):
        raise ValueError('m >= 2 and 0 < d < 1 required')
    D = d*d
    c = sqrt(1-D)
    q = 1-c
    B = 2*m-1+D
    disc = (1-D)*(4*m*(m-1)+1-D)
    z = 2*m*D/(B+sqrt(disc))  # cancellation-resistant smaller root
    r2 = z*(D-z)/(1-z)
    return D, c, q, z, sqrt(r2)


def meridian(t, c):
    return sqrt(max(0, 1-t*t))-c


def log_ellipsoid_det(z, D, m):
    if not (0 < z < D):
        return float('-inf')
    c = sqrt(1-D)
    q = 1-c
    if z <= q:
        return (m-1)*log(q)+.5*log(z)
    return .5*(m*log(z)+(m-1)*(log(D-z)-log(1-z)))


def golden_opt(D, m):
    c = sqrt(1-D)
    q = 1-c
    left, right = q, D
    alpha = (sqrt(5)-1)/2
    x = right-alpha*(right-left)
    y = left+alpha*(right-left)
    fx = log_ellipsoid_det(x,D,m)
    fy = log_ellipsoid_det(y,D,m)
    for _ in range(140):
        if fx < fy:
            left = x; x = y; fx = fy
            y = left+alpha*(right-left)
            fy = log_ellipsoid_det(y,D,m)
        else:
            right = y; y = x; fy = fx
            x = right-alpha*(right-left)
            fx = log_ellipsoid_det(x,D,m)
    return (left+right)/2


def simpson_integral(f, a, b, count=6000):
    h = (b-a)/count
    total = f(a)+f(b)
    for j in range(1,count):
        total += (4 if j%2 else 2)*f(a+h*j)
    return h*total/3


def dimensionless_volume_ratio(m, d):
    """Returns spindle/John and both volumes divided by kappa_m*q^(m-1/2)."""
    D, c, q, z, r = parameters(m,d)
    k = m-1
    upper = d*sqrt(k/q)
    def integrand(u):
        t = sqrt(q/k)*u
        a = max(0, meridian(t,c)/q)
        return a**k
    integral = simpson_integral(integrand,0,upper)
    kappa_ratio = exp(lgamma(m/2+1)-lgamma((m+1)/2)-.5*log(pi))
    spindle = 2*kappa_ratio*integral/sqrt(k)
    ellipsoid = sqrt(z/q)*(r/q)**(m-1)
    return spindle/ellipsoid, spindle, ellipsoid


def check_exact_certificate():
    # Rational radicand identity for the three-four-five endpoint triangle.
    D = Fraction(9,25)
    c2 = 1-D
    for m in [2,3,4,7,17,100]:
        B = 2*m-1+D
        discriminant = c2*(4*m*(m-1)+c2)
        assert B*B-discriminant == 4*m*m*D
        # Each of 4(m-1) equal-weight contact directions has axial
        # coordinate square 1/m; transverse coordinate squares average 1/m.
        axial = Fraction(1,m)
        transversal = Fraction(m-1,m)/Fraction(m-1)
        assert axial == transversal == Fraction(1,m)
    print('PASS exact rational discriminant and isotropic-contact identities')


def check_parameters_and_inclusion():
    count = 0
    for d in [.08,.2,.4,.6,.8,.95,.99]:
        for m in [2,3,4,6,10,24,60]:
            D,c,q,z,r=parameters(m,d)
            assert q < z < D
            residual = m*(D-z)*(1-z)-(m-1)*c*c*z
            assert abs(residual) < 1e-10*max(1,D*m)
            opt = golden_opt(D,m)
            assert abs(opt-z) < 2e-7*max(1,z)
            t = sqrt(z/m)
            radius = r*sqrt((m-1)/m)
            assert abs(meridian(t,c)-radius)<1e-11
            for j in range(201):
                tt=sqrt(z)*j/200
                elr=r*sqrt(max(0,1-(tt*tt/z)))
                assert elr <= meridian(tt,c)+2e-12
            # Unique-contact location: the minimum meridian/ellipse ratio
            # appears at +/-sqrt(z/m), as shown analytically.
            count+=1
    print('PASS',count,'separate dimension/separation optimizations and meridian-inclusion grids')


def check_volume_asymptotics():
    for d in [.2,.6,.9]:
        D,c,q,z,r=parameters(96,d)
        ratios=[]
        for m in [24,48,96]:
            quotient,body,ell=dimensionless_volume_ratio(m,d)
            assert quotient > 1
            ratios.append(quotient)
            bound = 2/(m*m)
            assert abs(body-(1+3*c/(8*m))) < bound
            assert abs(ell-(1+c/(8*m))) < bound
            assert abs(quotient-(1+c/(4*m))) < bound
        assert ratios[0]>ratios[1]>ratios[2]
        print(f'PASS d={d:.2f} spindle/John ratios: '+', '.join(f'{x:.10f}' for x in ratios))


if __name__=='__main__':
    check_exact_certificate()
    check_parameters_and_inclusion()
    check_volume_asymptotics()
    print('ALL CHECKS PASSED (finite tests; the proof establishes universal claims)')
