"""Independent numerical checks for an unbiased run-and-tumble current-cumulant theorem.

Requires Python >=3.10, numpy and scipy. Run: python verify.py
This script checks identities and finite examples; it is not an infinite-parameter proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, erfc, i0e, i1e
from scipy.stats import poisson
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq


def bernoulli_third(p):
    return p * (1.0 - p) * (1.0 - 2.0*p)


def beta_crossing(g, y):
    """Initial +/- crossing probabilities at distance z=v*t*y; g=gamma*t."""
    y = np.asarray(y, dtype=float)
    nmax = max(12, int(poisson.ppf(1.0-1.0e-13, g))+2)
    n = np.arange(nmax+1)
    pn = poisson.pmf(n, g)
    u = (1.0+y)/2.0
    plus = np.full(y.shape, pn[0])
    minus = np.zeros_like(plus)
    for j in range(1, nmax+1):
        a, b = j//2+1, (j+1)//2
        plus += pn[j]*betainc(b, a, 1.0-u)
        minus += pn[j]*betainc(a, b, 1.0-u)
    return plus, minus


def bessel_crossing(g, y):
    """Independent propagation-density integral, including the + ballistic atom."""
    y = np.asarray(y, dtype=float)
    def continuous_density(u):
        rad = math.sqrt(max(0.0, 1.0-u*u))
        arg = g*rad
        return 0.5*g*math.exp(-g*(1.0-rad))*(
            i0e(arg)+(1.0+u)*i1e(arg)/max(rad, 1e-14))
    plus = np.array([math.exp(-g)+quad(continuous_density, float(q), 1.0,
                          epsabs=2e-12)[0] for q in y])
    minus = np.array([quad(continuous_density, -1.0, -float(q),
                           epsabs=2e-12)[0] for q in y])
    return plus, minus


def dimensionless_third(g, nodes=320):
    """Returns third cumulants divided by rho*v/gamma."""
    x, w = leggauss(nodes)
    y = (x+1.0)/2.0
    weights = w/2.0
    plus, minus = beta_crossing(g, y)
    mean = (plus+minus)/2.0
    qq = g*np.dot(weights, (bernoulli_third(plus)+bernoulli_third(minus))/2.0)
    qa = g*np.dot(weights, bernoulli_third(mean))
    gap = 0.75*g*np.dot(weights, (1.0-2.0*mean)*(plus-minus)**2)
    return qq, qa, gap


def gaussian_constant():
    return (3.0*math.sqrt(2.0)*math.atan(1.0/math.sqrt(2.0))
            /(2.0*math.pi)-0.25)/math.sqrt(math.pi)


def run():
    checks = 0
    for g in (0.03, 0.7, 3.0, 12.0):
        points = np.array((0.05, 0.3, 0.65, 0.95))
        bp, bm = beta_crossing(g, points)
        dp, dm = bessel_crossing(g, points)
        for a, b in zip(np.r_[bp,bm], np.r_[dp,dm]):
            assert abs(a-b) < 4e-10, (g,a,b)
            checks += 1

    for g in (0.0002, 0.001, 0.005, 0.01, 0.03, 0.1,
              0.3, 0.5, 0.7, 1.0, 2.0, 3.0, 5.0, 10.0, 30.0, 80.0):
        qq, qa, gap = dimensionless_third(g)
        assert qa > 0.0 and qa > qq
        assert abs((qa-qq)-gap) < 1e-11*max(1.0,abs(qa))
        checks += 3

    for g in (0.0002, 0.0005, 0.001):
        qq, qa, _ = dimensionless_third(g)
        assert abs(qq/(-g*g/4.0)-1.0) < 0.02
        assert abs(qa/(g*g/8.0)-1.0) < 0.02
        checks += 2

    c3=gaussian_constant()
    q=quad(lambda y: bernoulli_third(0.5*erfc(y)), 0, 10,
           epsabs=1e-13)[0]
    assert abs(c3-q)<1e-12 and c3>0
    checks += 2

    for g in (30.0, 80.0, 200.0):
        qq, qa, _ = dimensionless_third(g, nodes=410)
        pred=2.0*math.sqrt(g/2.0)*c3
        assert abs(qq/pred-1.0) < 0.06
        assert abs(qa/pred-1.0) < 0.06
        checks += 2

    assert dimensionless_third(0.1)[0] < 0.0
    assert dimensionless_third(1.0)[0] > 0.0
    checks += 2
    root=brentq(lambda g: dimensionless_third(g)[0], 0.5, 1.0, xtol=1e-11)
    assert 0.66 < root < 0.68
    checks += 1
    print(f"PASS: {checks} deterministic comparisons/inequalities")
    print(f"Gaussian coefficient C3 = {c3:.14f}")
    print(f"Illustrative zero: gamma*t = {root:.9f}; no uniqueness claimed")

if __name__ == '__main__':
    run()
