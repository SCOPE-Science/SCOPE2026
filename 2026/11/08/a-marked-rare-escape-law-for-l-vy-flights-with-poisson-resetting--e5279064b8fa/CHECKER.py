"""Numerical checks of analytic constants and marked renewal formulas.

Run with: python CHECKER.py
These tests do not constitute a proof of any infinite-dimensional claim.
"""
import math
import random
from scipy.integrate import quad


def levy_density_constant(alpha, sigma):
    assert 0 < alpha < 2 and sigma > 0
    return (sigma ** alpha * alpha * 2 ** (alpha - 1)
            * math.gamma((1 + alpha) / 2)
            / (math.sqrt(math.pi) * math.gamma(1 - alpha / 2)))


def rates(alpha, sigma, lam):
    assert -1 < lam < 1
    c = levy_density_constant(alpha, sigma)
    ap = c / (alpha * (1 - lam) ** alpha)
    am = c / (alpha * (1 + lam) ** alpha)
    return ap, am


def mark_density(z, alpha, sigma, lam):
    ap, am = rates(alpha, sigma, lam)
    return (levy_density_constant(alpha, sigma) * abs(z-lam)**(-1-alpha) / (ap+am)
            if abs(z) > 1 else 0.0)


def verify():
    checks = 0
    for alpha in (0.25, 0.5, 0.8, 1.0, 1.3, 1.75, 1.95):
        for sigma in (0.3, 1.0, 2.5):
            for lam in (-0.7, -0.2, 0.0, 0.4, 0.8):
                ap, am = rates(alpha, sigma, lam)
                pplus = quad(lambda z: mark_density(z, alpha, sigma, lam), 1, math.inf,
                             epsabs=3e-11, epsrel=3e-11)[0]
                pminus = quad(lambda z: mark_density(z, alpha, sigma, lam), -math.inf, -1,
                              epsabs=3e-11, epsrel=3e-11)[0]
                assert abs((pplus + pminus)-1) < 2e-9
                assert abs(pplus-ap/(ap+am)) < 2e-9
                assert abs(pminus-am/(ap+am)) < 2e-9
                checks += 3
    for alpha in (0.25, 0.5, 1.0, 1.5, 1.9):
        for z in (1.05, 1.3, 2.0, 5.0, 17.0):
            tail=2*quad(lambda t: mark_density(t, alpha, 1.0, 0.0), z, math.inf)[0]
            assert abs(tail-z**(-alpha)) < 2e-9
            checks += 1
    for lam in (-0.8, 0.0, 0.6):
        alpha, sigma, r = 1.0, 1.3, 0.9
        a=sum(rates(alpha,sigma,lam))
        # The joint Laplace transform (time, terminal age) predicted by the proof
        # must factor, and the transform of scaled reset count is locked to time.
        for u in (0.0, 0.2, 1.5, 4.0):
            for v in (0.0, 0.4, 2.0):
                for theta in (0.0, 0.1, 1.0):
                    joint = a/(a+u+r*theta)*r/(r+v)
                    expected = (a/(a+u+r*theta))*(r/(r+v))
                    assert abs(joint-expected) < 1e-13
                    checks += 1
    c = levy_density_constant(1.0, 1.0)
    assert abs(c-1/math.pi)<1e-14; checks+=1
    a=sum(rates(1,1,0))
    assert abs(1/a-math.pi/2)<1e-14; checks+=1
    print(f"{checks} deterministic consistency assertions passed")
    print('Cauchy central mean coefficient:',1/a,'expected',math.pi/2)


def cauchy_mesh_diagnostic(seed=13579, n=1600, L=30., r=1.0, dt=0.10):
    # Independent coarse-grid diagnostic; no claim of exact first exits.
    rng=random.Random(seed)
    records=[]
    for _ in range(n):
        x=0.0; total=0.0; age=0.0
        while True:
            x+=dt*math.tan(math.pi*(rng.random()-0.5))
            total+=dt; age+=dt
            if abs(x)>=L:
                records.append((total/L,age,x/L));break
            if rng.random()<1-math.exp(-r*dt):
                x=0.0;age=0.0
    means=[sum(rec[i] for rec in records)/n for i in range(3)]
    pplus=sum(rec[2]>1 for rec in records)/n
    ptail=sum(abs(rec[2])>2 for rec in records)/n
    print('Coarse-grid Cauchy diagnostic:')
    print('mean(S/L), mean(last age), right fraction, P(|exit/L|>2):',
          round(means[0],3),round(means[1],3),round(pplus,3),round(ptail,3))
    print('asymptotic reference:',round(math.pi/2,3),1.0,0.5,0.5)
    assert abs(means[0]-math.pi/2)<0.4
    assert abs(means[1]-1.0)<0.20
    assert abs(pplus-0.5)<0.10
    assert abs(ptail-0.5)<0.13
    print('4 coarse-grid diagnostic checks passed (not a proof)')


if __name__=='__main__':
    verify()
    cauchy_mesh_diagnostic()
