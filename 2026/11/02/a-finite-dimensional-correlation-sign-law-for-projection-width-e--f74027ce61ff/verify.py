"""Reproducibility checks for exact covariance of directional projection-width energies.

Run: python verify.py
Only the Python standard library is required.
"""
from math import gamma, log, exp, pi
from random import Random
import math


def rf(z, t):
    return exp(math.lgamma(z + t) - math.lgamma(z))


def covariance_direct(d, a, m, alpha=0.5):
    """Mixed Dirichlet moments, WITHOUT using the new telescoping identity."""
    D = d * alpha
    one = rf(alpha, a)
    two = rf(alpha, m)
    product = d * rf(alpha, a + m) + d * (d - 1) * one * two
    expect_product = product / rf(D, a + m)
    expect_a = d * one / rf(D, a)
    expect_m = d * two / rf(D, m)
    return expect_product - expect_a * expect_m


def covariance_telescoped(d, a, m, alpha=0.5):
    """New factorization, evaluation at the two Dirichlet concentrations."""
    D = d * alpha
    def F(z):
        return a * sum(math.prod((z+a+j)/(z+1+j) for j in range(k))
                       for k in range(m))
    return (d * rf(alpha, a) * rf(alpha, m) / (alpha * rf(D, a+m))) * (F(alpha) - F(D))


def covariance_m2(d, a, alpha=0.5):
    D=d*alpha
    return d*rf(alpha,a)*a*(a-1)*(D-alpha)/(rf(D,a+2)*(D+1))


def independent_spherical_quadrature(d, a, m, grid=20000):
    """Independent deterministic midpoint integration for the circle d=2."""
    assert d == 2
    vals=[]
    for i in range(grid):
        theta=2*pi*(i+0.5)/grid
        x=math.cos(theta)**2
        y=math.sin(theta)**2
        vals.append((x**a+y**a, x**m+y**m))
    n=float(grid)
    avg1=sum(x for x,y in vals)/n
    avg2=sum(y for x,y in vals)/n
    return sum(x*y for x,y in vals)/n - avg1*avg2


def main():
    checks=0
    for alpha in (0.25, 0.5, 1., 1.8, 3.):
        for d in (2, 3, 5, 8):
            for m in (2, 3, 4, 6):
                for a in (0.4, 0.5, 0.75, 1., 1.2, 1.5, 2., 2.8, 4.):
                    first=covariance_direct(d,a,m,alpha)
                    second=covariance_telescoped(d,a,m,alpha)
                    assert abs(first-second) < 2e-9*(1+abs(first)), (alpha,d,m,a,first,second)
                    assert (abs(second)<1e-11 if a==1 else second*(a-1)>0), (alpha,d,m,a,second)
                    checks+=2
    for d in (2, 3, 5, 10, 15):
        for a in (0.5,0.8,1.,1.2,2.,3.7):
            first=covariance_telescoped(d,a,2)
            second=covariance_m2(d,a)
            assert abs(first-second)<2e-11
            checks+=1
    for a,m in ((0.5,2),(1.4,2),(0.6,3),(2.3,4)):
        exact=covariance_telescoped(2,a,m)
        quad=independent_spherical_quadrature(2,a,m)
        assert abs(exact-quad)<2e-9,(a,m,exact,quad)
        checks+=1
    # Explicit independent pseudo-random Gaussian normalization, not an analytical proof.
    rng=Random(84127)
    for d,a,m in ((3,0.5,2),(4,1.5,2),(6,0.7,3),(5,2.1,2)):
        n=130000
        sx=sy=sxy=0.
        for i in range(n):
            z=[rng.gauss(0.,1.) for j in range(d)]
            total=sum(w*w for w in z)
            x=sum((w*w/total)**a for w in z)
            y=sum((w*w/total)**m for w in z)
            sx+=x;sy+=y;sxy+=x*y
        empirical=sxy/n-(sx/n)*(sy/n)
        theory=covariance_telescoped(d,a,m)
        # MC standard error is order n^-1/2; loose independent check.
        assert abs(empirical-theory) < max(0.0015,0.22*abs(theory)),(d,a,m,theory,empirical)
        checks+=1
    print(f'VERIFY_OK {checks} checks (Dirichlet exact moment and independent spherical tests)')


if __name__=='__main__':
    main()
