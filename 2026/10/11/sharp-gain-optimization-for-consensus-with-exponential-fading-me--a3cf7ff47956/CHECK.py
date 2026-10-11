#!/usr/bin/env python3
"""Standalone arithmetic examples for exact exponential-memory consensus rates.

The universally quantified proof is in RESULT.md; these bounded tests are diagnostic.
"""
from fractions import Fraction as Q
from math import sqrt
from random import Random


def modal_rate(a, u, lam, b):
    discriminant = (lam - a*u)**2 - 4*lam*b*u
    return (lam + a*u - sqrt(max(discriminant, 0.0))) / 2


def optimal_gain(alpha, beta, lam, b):
    if alpha == beta:
        return (lam + 2*sqrt(lam*b*alpha))/alpha
    return (lam*beta + sqrt(lam**2*(beta-alpha)**2
            + 4*lam*b*alpha*beta*(2*beta-alpha))) / (alpha*(2*beta-alpha))


def exact_path_certificate():
    alpha, beta, lam, b = Q(1), Q(3), Q(1), Q(1)
    a = Q(11, 5)
    d_alpha = (lam-a*alpha)**2-4*lam*b*alpha
    d_beta = (lam-a*beta)**2-4*lam*b*beta
    assert d_alpha == Q(-64,25)
    assert d_beta == Q(484,25)
    assert (lam+a*alpha)/2 == Q(8,5)
    assert (lam+a*beta-Q(22,5))/2 == Q(8,5)
    assert Q(11,5) == Q(3+8,5)
    return 'Exact path certificate: OK'


def randomized_diagnostics():
    rng=Random(280914)
    for _ in range(1000):
        lam=10**rng.uniform(-2,2)
        b=10**rng.uniform(-2,2)
        alpha=10**rng.uniform(-2,1)
        beta=alpha*10**rng.uniform(.05,2)
        a=optimal_gain(alpha,beta,lam,b)
        ra=modal_rate(a,alpha,lam,b)
        rb=modal_rate(a,beta,lam,b)
        assert abs(ra-rb)<1e-8*max(1,ra,rb)
        assert (lam+2*sqrt(lam*b*beta))/beta < a
        assert a < (lam+2*sqrt(lam*b*alpha))/alpha
        q=10**rng.uniform(-2,2)
        end=min(modal_rate(q,alpha,lam,b),modal_rate(q,beta,lam,b))
        for k in range(1,20):
            u=alpha+(beta-alpha)*k/20
            assert modal_rate(q,u,lam,b)>=end-1e-9*max(1,end)
    return '1000 crossover and 19000 endpoint diagnostics: OK'

if __name__=='__main__':
    print(exact_path_certificate())
    print(randomized_diagnostics())
