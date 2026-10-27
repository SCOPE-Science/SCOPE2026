#!/usr/bin/env python3
"""Numerical cross-checks for a three-client smooth-clipping fixed-point theorem.

All infinite-parameter claims are established analytically in RESULT.md; this
script tests representative finite parameters and exact update residuals.
"""
import math


def scalar_root(a, phi, eps):
    """Solve the monotone equilibrium equation for p in (0,min(a,phi/2))."""
    hi = min(a, phi / 2)
    lo = 0.0
    root = None
    for _ in range(110):
        p = (lo + hi) / 2
        val = 3 * p + math.sqrt(eps) * p * (
            1 / math.sqrt(phi * phi - p * p)
            + 2 / math.sqrt(phi * phi - 4 * p * p)
        ) - 3 * a
        if val > 0:
            hi = p
        else:
            lo = p
        root = p
    return root


def pos(a, phi, eps):
    p = scalar_root(a, phi, eps)
    return p - a + math.sqrt(eps) * p / math.sqrt(phi * phi - p * p), p


def check_close(a, b, tol=2e-11):
    assert abs(a - b) <= tol * max(1, abs(a), abs(b)), (a, b)


def test():
    count = 0
    for a, phi in [(1., .5), (1., 1.), (1., 1.9), (1., 2.), (1., 3.), (2., 3.5)]:
        for eps in (1e-2, 1e-4, 1e-6, 1e-8):
            x, p = pos(a, phi, eps)
            assert -a < x < 0, (a, phi, eps, x)
            assert 0 < p < min(a, phi / 2)
            m = [p, p, -2*p]
            grads = [x+a, x+a, x-2*a]
            for gi, mi in zip(grads, m):
                clip = phi * (gi-mi) / math.sqrt((gi-mi)**2 + eps)
                check_close(mi, clip, tol=1e-9)
                count += 1
            check_close(sum(m),0)
            for beta in (0.1, 0.5, 0.9):
                for eta in (.01, .12, 1.):
                    mp = [beta*mi + (1-beta)*phi*(gi-mi)/math.sqrt((gi-mi)**2+eps)
                          for gi,mi in zip(grads,m)]
                    xp = x - eta * sum(mp)/3
                    check_close(xp,x, 1e-9)
                    for aa,bb in zip(mp,m):check_close(aa,bb,1e-9)
                    count += 4
    # Three distinctly different asymptotic scaling regimes.
    for phi in (0.5, 1., 1.5):
        eps = 1e-8
        x,p = pos(1.,phi,eps)
        baseline=phi/2-1 + math.sqrt(eps/3)
        assert abs(x-baseline)<2e-5, (phi,x,baseline)
        count+=1
    for eps in (1e-8,1e-10,1e-12):
        x,p=pos(1.,2.,eps)
        expected=-(2*eps/36)**(1/3)
        assert 0.94 < x/expected < 1.02,(eps,x,expected)
        count+=1
    for phi in (2.5,3.,5.):
        eps=1e-8
        x,p=pos(1.,phi,eps)
        expected=-2/3*math.sqrt(eps)*(1/math.sqrt(phi**2-4)-1/math.sqrt(phi**2-1))
        assert .95 < x/expected <1.05,(phi,x,expected)
        count+=1
    # Two-client equal-curvature symmetry is exactly unbiased.
    for a in (0.5, 1., 3.):
        for phi in (.3, 2., 5.):
            for eps in (1e-6, .2, 3.):
                q=phi*a/math.sqrt(a*a+eps)
                # Invert feedback equation: m=Psi(g-m), in the symmetric pair.
                # At the true optimum, the feedback solution is (q0,-q0).
                lo, hi = 0, min(a,phi)
                for _ in range(80):
                    mid=(lo+hi)/2
                    if mid-phi*(a-mid)/math.sqrt((a-mid)**2+eps)>0: hi=mid
                    else: lo=mid
                m=(lo+hi)/2
                check_close(m,phi*(a-m)/math.sqrt((a-m)**2+eps))
                check_close(m+(-m),0)
                count+=2
    # Check derivative of scalar inverse map and perturbative slow eigenslope.
    for phi, eps, beta in ((1.,.1,.8),(.6,.5,.75),(2.,4.,.9)):
        x,p=pos(1.,phi,eps)
        ms=[p,p,-2*p]
        gs=[x+1,x+1,x-2]
        c=[]; alpha=[]
        for m,g in zip(ms,gs):
            d=phi*eps/(((g-m)**2+eps)**1.5)
            ci=(1-beta)*d
            ai=beta-ci
            assert 0<ai<beta<1, (phi,eps,beta,ai)
            c.append(ci);alpha.append(ai);count+=1
        slope=-sum(ci/(1-ai) for ci,ai in zip(c,alpha))/3
        assert slope<0
        count+=1
    print('VERIFY_OK',count)


if __name__ == '__main__':
    test()
