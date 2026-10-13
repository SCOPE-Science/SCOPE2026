#!/usr/bin/env python3
"""Independent exact-arithmetic and angular-quadrature checks of the
one-probe resolvent effective-dimension bias identity.
Standard library only; finite tests supplement the analytical proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import cos, pi, sin, sqrt, isclose


def closed_mean(a, b, z, s, t):
    return (a*a*(1 + 2*t/s) + 2*a*b + b*b*(1 + 2*s/t)) / (s+t)**2


def closed_bias(a, b, z, s, t):
    return a*b*(a-b)**2 / ((a+z)*(b+z)*(s+t)**2)


def matrix_sample(a, b, z, x, y):
    q = a*x*x + b*y*y
    if not q:
        raise ValueError('zero Gaussian probe is excluded')
    m11, m12, m22 = (a*x)**2/q, a*b*x*y/q, (b*y)**2/q
    eigen = m11 + m22
    # A_nys is rank one, and f_z(A_nys)=A_nys/(eigen+z).
    return (m11*x*x + 2*m12*x*y + m22*y*y)/(eigen+z)


def direct_sample(a, b, z, x, y):
    q = a*x*x + b*y*y
    return q*q / (a*(a+z)*x*x + b*(b+z)*y*y)


rational_checks = 0
matrix_checks = 0
# Rational parametrization: for each u>1, a=z(u-1)^2/(4u)
# and sqrt(a(a+z))=z(u^2-1)/(4u), both rational.
for z in [Q(1, 3), Q(1), Q(2), Q(3, 2)]:
    eigenpairs = []
    for u in [Q(3, 2), Q(2), Q(5, 2), Q(3), Q(4), Q(7), Q(11)]:
        a = z*(u-1)**2/(4*u)
        s = z*(u*u-1)/(4*u)
        assert s*s == a*(a+z)
        eigenpairs.append((a, s))
    for (a, s), (b, t) in combinations(eigenpairs, 2):
        if b>a:
            a, b, s, t = b, a, t, s
        mean = closed_mean(a,b,z,s,t)
        bias = closed_bias(a,b,z,s,t)
        target = a/(a+z)+b/(b+z)
        assert target-mean == bias
        assert 0 < bias < b/(b+z)
        ratio = bias / (b/(b+z))
        assert ratio == a*(a-b)**2/((a+z)*(s+t)**2)
        assert ratio < (a-b)**2/(a+z)**2
        rational_checks += 1
        for x,y in product([Q(-3),Q(1, 2),Q(2)], [Q(-2),Q(1),Q(5, 3)]):
            assert matrix_sample(a,b,z,x,y) == direct_sample(a,b,z,x,y)
            matrix_checks += 1

# Independent numerical evaluation of the original polar-angle integral.
angular_checks = 0
n_angles = 32000
for a,b,z in [(4.,1.,2.), (3.,1.,0.5), (2.,0.5,1.),
              (0.1,0.03,3.), (1.,1.,0.3), (0.7,0.2,2.5),
              (11.,3.,8.), (1.2,0.2,1.4)]:
    s, t = sqrt(a*(a+z)), sqrt(b*(b+z))
    mean = closed_mean(a,b,z,s,t)
    via_integral = 0.
    for j in range(n_angles):
        theta = 2*pi*(j+0.5)/n_angles
        c2, d2 = cos(theta)**2, sin(theta)**2
        via_integral += 2*(a*c2+b*d2)**2/(a*(a+z)*c2+b*(b+z)*d2)
    via_integral /= n_angles
    assert isclose(via_integral,mean,rel_tol=2e-11,abs_tol=2e-11)
    assert isclose((a/(a+z)+b/(b+z))-via_integral,
                   closed_bias(a,b,z,s,t),rel_tol=1e-9,abs_tol=2e-11)
    angular_checks += 1

# The crossover is an asymptotic, not an assertion of exact equality at b>0.
matched_checks = 0
for a in [0.6, 3., 10.]:
    for gamma in [0.1, 0.5, 1., 3., 7.]:
        b = 1e-8*a
        z = gamma*b
        s, t = sqrt(a*(a+z)), sqrt(b*(b+z))
        B = closed_bias(a,b,z,s,t)
        assert abs(B-1/(1+gamma)) < 1e-5
        assert abs(closed_mean(a,b,z,s,t)-1) < 1e-5
        matched_checks += 1
print('VERIFY_OK rational_bias_identities=',rational_checks,
      'exact_matrix_reconstructions=',matrix_checks,
      'independent_angular_integrals=',angular_checks,
      'matched_scale_checks=',matched_checks)
