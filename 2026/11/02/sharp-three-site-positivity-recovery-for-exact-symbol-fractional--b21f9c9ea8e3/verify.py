"""Reproduction checks for the three-site exact-symbol fractional diffusion semigroup.

Run: python verify.py
Dependencies: numpy >= 1.23; scipy >= 1.9.
This is numerical corroboration, not a substitute for the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.optimize import brentq, minimize_scalar
from scipy.special import sici


def coeff(alpha, k):
    assert 0 < alpha <= 2 and k in (0, 1, 2)
    v, err = quad(lambda x: x ** alpha * math.cos(k * x), 0,
                  math.pi, epsabs=2e-13, epsrel=2e-13, limit=200)
    assert err < 3e-10
    return v / math.pi


def parameters(alpha):
    a, b_signed, gamma = (coeff(alpha, k) for k in range(3))
    beta = -b_signed
    delta = math.sqrt(2 * beta ** 2 + gamma ** 2 / 4)
    return a, beta, gamma, delta


def stiffness(alpha, h=1):
    a, beta, gamma, _ = parameters(alpha)
    return h ** (-alpha) * np.array(
        [[a, -beta, gamma], [-beta, a, -beta], [gamma, -beta, a]],
        dtype=float)


def exact_entrywise(alpha, tau):
    a, beta, gamma, delta = parameters(alpha)
    z = math.exp(-a * tau - gamma * tau / 2)
    ct, st = math.cosh(delta * tau), math.sinh(delta * tau)
    even_outer = z * (ct - gamma * st / (2 * delta))
    anti = math.exp(-a * tau + gamma * tau)
    outer_diag = (even_outer + anti) / 2
    outer_cross = (even_outer - anti) / 2
    inner_diag = z * (ct + gamma * st / (2 * delta))
    adjacent = z * beta * st / delta
    return np.array([[outer_diag, adjacent, outer_cross],
                     [adjacent, inner_diag, adjacent],
                     [outer_cross, adjacent, outer_diag]])


def onset(alpha):
    assert 1 < alpha <= 2
    _, beta, gamma, delta = parameters(alpha)
    assert 0 < gamma < beta and delta > 1.5 * gamma
    q = gamma / (2 * delta)
    def H(t):
        return (1-q)/2 * math.expm1((delta-1.5*gamma)*t) + \
               (1+q)/2 * math.expm1(-(delta+1.5*gamma)*t)
    lo = max(1e-13, gamma * 1e-4)
    hi = 2.0
    assert H(lo) < 0 and H(hi) > 0
    return brentq(H, lo, hi, xtol=4e-15, rtol=9e-15)


def run():
    tests=0
    alphas=(.07,.15,.5,.9,1.,1.001,1.01,1.1,1.3,1.5,1.7,1.9,2.)
    for alpha in alphas:
        a, b, g, delta = parameters(alpha)
        assert b > 0 and (g < 0 if alpha < 1 else (g > 0 if alpha > 1 else abs(g) < 1e-12)); tests+=1
        assert np.linalg.eigvalsh(stiffness(alpha))[0] > 0; tests+=1
        for h in (.65,1.,2.):
            for tau in (0.,1e-4,.002,.04,.15,.4,1.,2.):
                observed=expm(-tau * h**alpha * stiffness(alpha,h))
                derived=exact_entrywise(alpha,tau)
                assert np.max(np.abs(observed-derived)) < 2e-10, (alpha,h,tau)
                tests+=1
        if alpha <= 1:
            for tau in (1e-4,.01,.1,.5,2.):
                assert np.min(exact_entrywise(alpha,tau)) > -3e-12
                tests+=1
        else:
            t0=onset(alpha)
            assert t0>0
            for fraction in (.05,.2,.5,.9):
                P=exact_entrywise(alpha,t0*fraction)
                assert P[0,2] < 0 and np.min(P[np.array([[0,1],[1,0],[1,2],[2,1]])[:,0],np.array([[0,1],[1,0],[1,2],[2,1]])[:,1]])>0
                tests+=1
            for fraction in (1.05,1.2,2,4,8):
                assert np.min(exact_entrywise(alpha,t0*fraction)) > 0
                tests+=1
            assert abs(exact_entrywise(alpha,t0)[0,2])<2e-12; tests+=1
    a,b,g,_=parameters(2)
    assert abs(a-math.pi**2/3)<2e-13 and abs(b-2)<2e-13 and abs(g-.5)<2e-13;tests+=1
    assert abs(onset(2)-0.26118517326098534)<1e-11;tests+=1
    ci=sici(2*math.pi)[1]
    zeta=0.5772156649015328606+math.log(2*math.pi)-ci
    kappa=math.pi*zeta/8
    dip_const=zeta**2/128
    for eps in (.01,.005,.001,.0005):
        alpha=1+eps
        t0=onset(alpha)
        assert abs(t0/eps-kappa)<2.3*eps
        q=minimize_scalar(lambda t:exact_entrywise(alpha,t)[0,2],bounds=(0,t0),method='bounded',options={'xatol':1e-14})
        assert q.success and q.fun<0
        assert abs(q.x/eps-kappa/2)<2.5*eps
        assert abs(-q.fun/eps**2-dip_const)<.15*eps
        tests+=4
    print('PASS',tests,'check groups')
    print('alpha=2: threshold =',onset(2))
    print('alpha down to 1: threshold slope =',kappa)
    print('alpha down to 1: negative dip coefficient =',dip_const)

if __name__=='__main__':
    run()
