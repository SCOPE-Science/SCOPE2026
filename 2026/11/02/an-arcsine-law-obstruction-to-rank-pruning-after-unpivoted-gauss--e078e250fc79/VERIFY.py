#!/usr/bin/env python3
"""Exact algebra and reproducible Gaussian checks for the rank-pruning theorem.
No external data or network access is required.
"""
from fractions import Fraction
from math import asin, atan, exp, pi, sqrt
import numpy as np
import sympy as sp


def exact_identities():
    x, y, d = sp.symbols('x y d', real=True)
    den = x*x + d*d*y*y
    # First QR unit vector proportional to (x, d*y).
    w1 = (x*x + d**4*y*y)/den
    w2 = d*d*(x*x + y*y)/den
    sin2 = d*d*y*y/den
    assert sp.cancel(w1+w2-(1+d*d)) == 0
    assert sp.cancel(w2-(d*d+(1-d*d)*sin2)) == 0
    assert sp.cancel(w1-(d*d+(1-d*d)*(1-sin2))) == 0
    t, tau = sp.symbols('t tau', positive=True)
    assert sp.cancel(((tau*tau-d*d)/(1-d*d) - t).subs(tau**2, d*d+t*(1-d*d))) == 0
    return 4


def exact_rational_samples():
    checks = 0
    for tau in [Fraction(1, 20), Fraction(1, 10), Fraction(1, 4)]:
        for c in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
            d = c*tau
            threshold = (tau*tau-d*d)/(1-d*d)
            assert 0 < threshold < Fraction(1, 2)
            for x in range(-7, 8):
                for y in range(-7, 8):
                    if x == 0 and y == 0:
                        continue
                    x, y = Fraction(x), Fraction(y)
                    den = x*x+d*d*y*y
                    w1 = (x*x+d**4*y*y)/den
                    w2 = d*d*(x*x+y*y)/den
                    sin2 = d*d*y*y/den
                    p = (w1 >= tau*tau and w2 >= tau*tau)
                    q = (threshold <= sin2 <= 1-threshold)
                    assert p == q
                    checks += 1
    return checks


def formula_prob(tau, c):
    d = c*tau
    t = (tau*tau-d*d)/(1-d*d)
    a = sqrt(t/(1-t))
    b = sqrt((1-t)/t)
    return 2/pi*(atan(b/d)-atan(a/d))


def direct_qr_checks():
    rng = np.random.default_rng(3891)
    tests = 0
    for tau, c in [(0.03,0.5),(0.07,0.7),(0.12,0.35)]:
        d=tau*c
        A=np.diag([1.0,d,0.0,0.0])
        for _ in range(60):
            G=rng.standard_normal((4,2))
            Y=A@G/np.sqrt(2)
            # All test points use the actual unpivoted QR, not a rotation fit.
            Q,_=np.linalg.qr(Y,mode='reduced')
            B=Q.T@A
            f=G[0,0]
            g=G[1,0]
            den=f*f+d*d*g*g
            direct=np.array([(f*f+d**4*g*g)/den,d*d*(f*f+g*g)/den])
            assert np.allclose(np.sum(B*B,axis=1),direct,atol=1e-12,rtol=1e-10)
            assert np.linalg.norm(A-Q@B) < 1e-12
            if np.linalg.norm(Y)>=tau:
                # Reported rank agrees with the analytical classification.
                kept=sum(np.sum(B*B,axis=1)>=tau*tau)
                t=(tau*tau-d*d)/(1-d*d)
                sin2=d*d*g*g/den
                assert (kept==2)==(t<=sin2<=1-t)
            assert np.linalg.svd(B,compute_uv=False)[1] < tau
            tests += 1
    return tests


def reproducibility():
    rng = np.random.default_rng(20261027)
    cases = [(0.03,0.5),(0.07,0.7),(0.12,0.35)]
    summary=[]
    n=160000
    for tau,c in cases:
        d=tau*c
        # Four-by-four normalized Gaussian block, only first two rows of A Omega nonzero.
        g = rng.standard_normal((n,2,2))
        first=g[:,0,0]
        second=g[:,1,0]
        den=first**2+d*d*second**2
        w1=(first**2+d**4*second**2)/den
        w2=d*d*(first**2+second**2)/den
        survived=((g[:,0,:]**2).sum(axis=1)+d*d*(g[:,1,:]**2).sum(axis=1))/2 >= tau*tau
        event=(w1>=tau*tau)&(w2>=tau*tau)
        empirical=int(np.sum(survived&event))/n
        p0=formula_prob(tau,c)
        deterministic_gap=1-exp(-tau*tau)
        # 5 standard deviations (conservative) plus analytic first-stop bound.
        assert abs(empirical-p0) < deterministic_gap+5*sqrt(0.25/n)
        summary.append((tau,c,empirical,p0,deterministic_gap))
    for c in [0.2,0.5,0.8]:
        target=2/pi*asin(c)
        err1=abs(formula_prob(0.001,c)-target)
        err2=abs(formula_prob(0.0001,c)-target)
        assert err2 < err1
        assert err2 < 1e-5
    return summary

if __name__ == '__main__':
    a=exact_identities()
    b=exact_rational_samples()
    qr=direct_qr_checks()
    c=reproducibility()
    print(f'PASS: {a} symbolic equalities, {b} exact-rational classifications, 480000 Gaussian trials, {qr} explicit QR/SVD tests')
    for t,r,p,q,bnd in c:
        print(f'tau={t:.4f} ratio={r:.2f} empirical={p:.6f} ideal={q:.6f} initial-stop-bound={bnd:.6f}')
    print(f'limit at ratio=1/2: {2/pi*asin(0.5):.12f}')
