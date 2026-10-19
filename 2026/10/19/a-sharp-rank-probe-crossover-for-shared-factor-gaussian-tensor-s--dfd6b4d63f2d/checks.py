#!/usr/bin/env python3
"""Numerical cross-checks for the shared-left Gaussian tensor-probe theorem.

Requires Python 3 and SciPy. Computes exact one-dimensional integrals; no
simulation or fitted scaling exponent is used for assertions.
"""
from math import gamma, sqrt, pi, log, isclose
from scipy.integrate import quad
from scipy.stats import chi2
from scipy.special import k1


def constant_isotropic(r, ell):
    """The exact asymptotic coefficient for nonzero singular values 1/sqrt(r)."""
    sq_norm = 1.0
    prod_s = r ** (-r / 2)
    if r < ell:
        return (ell * sq_norm) ** (r / 2) * gamma((ell-r)/2) / (2**r * gamma(1+r/2)*gamma(ell/2)*prod_s)
    if r == ell:
        return r**(1+r/2) / (2**r * gamma(1+r/2)**2 * prod_s)
    # S=(chi-square_r)/r and negative moment exists precisely when r>ell.
    return ell**(ell/2) * r**(ell/2) * gamma((r-ell)/2) / (2**ell * gamma(1+ell/2)*gamma(r/2))


def exact_probability_isotropic(r, ell, tau):
    """For S=chi-square_r/r, integrate P(W < r*ell/(tau^2*x))."""
    def integrand(t):
        x = __import__('math').exp(t)
        return chi2.pdf(x, r)*chi2.cdf(r*ell/(tau*tau*x),ell)*x
    return quad(integrand, -45, 12, epsabs=1.e-11, epsrel=1.e-10, limit=200)[0]


def leading_probability(r, ell, tau):
    k=min(r,ell)
    return constant_isotropic(r,ell)*tau**(-k)*(log(tau) if r==ell else 1)


def main():
    cases=[(1,3,100),(2,2,500),(2,3,500),(3,2,500)]
    for r,ell,tau in cases:
        p=exact_probability_isotropic(r,ell,tau)
        q=leading_probability(r,ell,tau)
        ratio=p/q
        assert 0.95<ratio<1.05, (r,ell,tau,ratio)
        print(f'rank={r}, probes={ell}, threshold={tau}: exact={p:.12g}, leading={q:.12g}, ratio={ratio:.6f}')
    assert isclose(constant_isotropic(2,2),2.0,rel_tol=1.e-12)
    assert isclose(constant_isotropic(2,3),3.0,rel_tol=1.e-12)
    assert isclose(constant_isotropic(3,2),3.0,rel_tol=1.e-12)
    assert isclose(constant_isotropic(1,3),2*sqrt(3)/pi,rel_tol=1.e-12)
    for tau in [5,10,20,100]:
        # E1,E2~Exp(1), Q_2^2=(E1*E2)^(-1).
        exact_closed=1-(2/tau)*k1(2/tau)
        integ=exact_probability_isotropic(2,2,tau)
        assert abs(integ-exact_closed)<1.e-9,(tau,integ,exact_closed)
    print('PASS: exact integrals, four asymptotic constants, and Bessel example agree.')

if __name__=='__main__':
    main()
