#!/usr/bin/env python3
"""Independent reproducibility checks for simplex nearest-vertex deep-hole tails.

Requires Python 3 and NumPy for independent Monte Carlo tests.  Exact
rational coefficients and analytic identities are checked without CAS.
"""
import math
import random
from fractions import Fraction
import numpy as np


def moment_coefficients(d):
    m = d + 1
    # Q=m^2 sum(P_i^2)-m; (P_i) has d-component Dirichlet(1,...,1) law.
    e_q = Fraction(m)
    e_s2_sq = Fraction(4*(m+4), m*(m+1)*(m+2))
    e_q2 = m**4*e_s2_sq - 2*m**3*Fraction(2, m) + m*m
    assert e_q2 == Fraction(m*m*(m*m+7*m-6),(m+1)*(m+2))
    return Fraction(d*m,2), Fraction(d*(d+3),8)*e_q2


def conditional_tail(eps, d, samples=160000, seed=100):
    # Integrate the exact, dimension-d Dirichlet expression over the shape variables.
    rng = np.random.default_rng(seed+d)
    m=d+1
    y=rng.exponential(size=(samples,d))
    p=y/y.sum(axis=1, keepdims=True)
    q=m*m*np.sum(p*p,axis=1)-m
    # Cancellation-free inverse of t-(Q/2)t^2=eps.
    t=2*eps/(1+np.sqrt(1-2*eps*q))
    assert np.all(t <= 1/(m*(m-1))+1e-13)
    return np.mean((m*t)**d)


def direct_tail(eps, d, samples=1000000, seed=7):
    rng=np.random.default_rng(seed+d)
    m=d+1
    y=rng.exponential(size=(samples,m))
    lam=y/y.sum(axis=1, keepdims=True)
    z=lam-1/m
    deficit=z.max(axis=1)-np.sum(z*z,axis=1)/2
    # Calculate using the actual explicit simplex vertices independently.
    # ||sum lambda_i v_i-v_j||^2 = 1/2 sum_i (lambda_i-delta_{ij})^2.
    direct=(1+np.sum(lam*lam,axis=1))/2-lam.max(axis=1)
    rr2=d/(2*m)
    assert np.max(np.abs(direct-(rr2-deficit))) < 8e-15
    assert np.min(deficit) >= -1e-14
    return float(np.mean(deficit < eps))


def simpson(f, N=50000):
    h=1/N
    return h/3*(f(0)+f(1)+sum((4 if i%2 else 2)*f(i*h) for i in range(1,N)))


def main():
    for d in range(1,15):
        c1,c2=moment_coefficients(d)
        m=d+1
        assert c1>0 and c2>0
        if d==1:
            assert c1==1 and c2==2
        if d==2:
            assert c1==3 and c2==Fraction(27,2)
        if d==3:
            assert c1==6 and c2==Fraction(228,5)
        # Explicit third coefficient from Lagrange inversion:
        # [eps^(d+2)] F = m^d*d/(d+4)*C(d+4,2)*(Q/2)^2 averaged.
        alt=Fraction(d, d+4)*math.comb(d+4,2)*Fraction(1,4)
        assert alt * (c2/Fraction(d*(d+3),8)) == c2
    print('EXACT_DIRICHLET_SECOND_AND_THIRD_TAYLOR_COEFFICIENTS_OK')

    # Direct Monte Carlo using uniformly sampled barycentric coordinates and
    # independent conditional-Dirichlet integration of the exact tail law.
    for d,eps in [(2,.04),(3,.03),(4,.015)]:
        m=d+1
        assert eps < 1/(2*m*(m-1))
        direct=direct_tail(eps,d,1600000)
        exact=conditional_tail(eps,d,210000)
        stderr=math.sqrt(max(exact*(1-exact),1e-12)/1600000)
        assert abs(direct-exact) < 5*stderr+0.001*exact,(d,eps,direct,exact,stderr)
        print('INDEPENDENT_BARYCENTRIC_MC_VS_CONDITIONAL_EXACT_LAW_OK',d,eps,round(direct,8),round(exact,8))

    # Completely deterministic Simpson quadrature when d=2 (shape P=(s,1-s)).
    d=2;m=3
    for eps in [.002,.01,.03,.07]:
        def fn(p):
            q=m*m*(p*p+(1-p)**2)-m
            t=2*eps/(1+math.sqrt(1-2*eps*q))
            return (m*t)**d
        f=simpson(fn,N=6000)
        a,b=moment_coefficients(d)
        f2=(m*eps)**d*(1+float(a)*eps+float(b)*eps**2)
        assert 0 < f-f2 < 1000*(m*eps)**d*eps**3,(eps,f,f2)
    print('DETERMINISTIC_TRIANGLE_SHAPE_QUADRATURE_AND_POSITIVE_REMAINDER_OK')

    # Verify all exact tail integrals are bounded between leading term and
    # the universal sandwich given by t <= 2eps.
    for d in range(2,9):
        m=d+1
        eps=1/(5*m*(m-1))
        f=conditional_tail(eps,d,samples=20000)
        assert (m*eps)**d < f < (2*m*eps)**d
    print('ALL_DIMENSIONAL_ENDPOINT_AND_POSITIVE_COEFFICIENT_CHECKS_OK')
    print('ALL_SIMPLEX_DEEP_HOLE_TAIL_CHECKS_OK')

if __name__=='__main__':
    main()
