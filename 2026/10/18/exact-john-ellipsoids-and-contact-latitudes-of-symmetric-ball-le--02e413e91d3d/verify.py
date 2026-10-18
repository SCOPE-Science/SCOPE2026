#!/usr/bin/env python3
"""Standalone numerical diagnostics for the all-dimensional symmetric lens ellipsoid theorem.
The analytic proof, not these finite checks, establishes the infinite parameter range.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import sqrt, gamma, pi

getcontext().prec = 55
pairs = 0
support_cases = 0
frame_cases = 0

for n in (2, 3, 4, 5, 8, 13):
    for numerator, denominator in ((0, 1), (1, 16), (1, 4), (1, 2), (3, 4), (7, 8), (99, 100)):
        s_q = Fraction(numerator, denominator)
        # The radicand factorization behind the positive quadratic root is exact.
        left = Fraction(4*n, 1) + (n-1)**2 * s_q*s_q
        right = Fraction((n+1)**2, 1) * s_q*s_q + 4*n*(1-s_q*s_q)
        assert left == right
        N = Decimal(n)
        s = Decimal(numerator)/Decimal(denominator)
        a = ((4*N + (N-1)**2 * s*s).sqrt() - (N+1)*s)/(2*N.sqrt())
        b2 = a*(a + N.sqrt()*s)
        b = b2.sqrt()
        assert a > 0 and b > 0
        tol = Decimal('1e-45')
        assert abs(a*a + (N+1)*s*a/N.sqrt() + s*s-1) < tol
        assert abs(b2-a*a-N.sqrt()*s*a) < tol
        c0 = 1/N.sqrt()
        for j in range(1001):
            c = Decimal(j)/Decimal(1000)
            f = (a*c+s)**2+b2*(1-c*c)
            bound = Decimal(1)-N.sqrt()*s*a*(c-c0)**2
            assert abs(f-bound) < tol
            assert f <= 1+tol
            support_cases += 1
        assert abs((a*c0+s)**2+b2*(1-c0*c0)-1) < tol
        pairs += 1
    # A regular-simplex frame in the hyperplane sum(v_j)=0 in R^n.
    # The physical dimension is n: one axial coordinate plus this hyperplane.
    v = [[sqrt(n/(n-1)) * ((1 if j==k else 0)-1/n)
          for k in range(n)] for j in range(n)]
    c0f = 1/sqrt(n)
    r0f = sqrt((n-1)/n)
    contacts = [(sgn*c0f, *[r0f*q for q in v[j]])
                for sgn in (1,-1) for j in range(n)]
    ambient = n+1
    sums = [sum(.5*u[k] for u in contacts) for k in range(ambient)]
    assert max(abs(x) for x in sums) < 2e-13
    for i in range(ambient):
        for j in range(ambient):
            covariance = sum(.5*u[i]*u[j] for u in contacts)
            expected = (1.0 if i==j==0 else
                        (0.0 if i==0 or j==0 else
                         (1.0 if i==j else 0.0)-1/n))
            assert abs(covariance-expected) < 2e-13
            frame_cases += 1

# The thin-lens occupied-volume constant is an independent asymptotic diagnostic.
limits = 0
for n in (2,3,4,5,8,13):
    s = .999
    aa = (sqrt(4*n+(n-1)**2*s*s)-(n+1)*s)/(2*sqrt(n))
    bb = sqrt(aa*(aa+sqrt(n)*s))
    k_n=pi**(n/2)/gamma(1+n/2)
    k_n1=pi**((n-1)/2)/gamma(1+(n-1)/2)
    # Simpson integral in the rescaled thin coordinate to avoid cancellation.
    subdivisions=2000
    epsilon=1-s
    vals=[(2*y-y*y)**((n-1)/2) for y in
          [epsilon*j/subdivisions for j in range(subdivisions+1)]]
    integral=epsilon/(3*subdivisions)*(vals[0]+vals[-1]+4*sum(vals[1:-1:2])+2*sum(vals[2:-1:2]))
    lens_volume=2*k_n1*integral
    john_fraction=k_n*aa*bb**(n-1)/lens_volume
    predicted=k_n/(2*k_n1)*n**(n/2)/(n+1)**((n-1)/2)
    assert abs(john_fraction-predicted)<.003
    limits += 1

print('VERIFY_OK exact_radicand_pairs=',pairs,
      'support_grid_checks=',support_cases,
      'contact_frame_entries=',frame_cases,
      'thin_lens_limits=',limits)
