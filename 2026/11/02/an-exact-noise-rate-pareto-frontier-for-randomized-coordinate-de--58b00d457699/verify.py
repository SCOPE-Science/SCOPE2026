#!/usr/bin/env python3
"""Reproduce finite-dimensional rate/noise Pareto design identities.

Only the Python standard library is required. These checks supplement the proof.
"""
import math
import random
from fractions import Fraction


def u_from_k(k, w):
    z = k / w
    return 2.0 / (2.0 + z + math.sqrt(z * (z + 4.0)))


def optimal_design(tau, weights):
    d = len(weights)
    assert d >= 2 and all(w > 0 for w in weights)
    assert 0 < tau <= 1.0 / d
    if tau == 1.0 / d:
        return [1.0 / d] * d, [1.0] * d, sum(weights)

    def p_and_sum(k):
        uu = [u_from_k(k, w) for w in weights]
        pp = [tau / (1.0 - u * u) for u in uu]
        return pp, uu, sum(pp)

    lo, hi = 0.0, 1.0
    while p_and_sum(hi)[2] > 1.0:
        hi *= 2.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if p_and_sum(mid)[2] > 1.0:
            lo = mid
        else:
            hi = mid
    pp, uu, _ = p_and_sum(hi)
    ss = [1.0 - u for u in uu]
    return pp, ss, sum(w * (1.0 - u) / (1.0 + u) for w, u in zip(weights, uu))


def risk_for_probabilities(tau, pp, weights):
    assert len(pp) == len(weights)
    return sum(w * (1.0 - math.sqrt(1.0 - tau / p)) /
               (1.0 + math.sqrt(1.0 - tau / p))
               for w, p in zip(weights, pp))


def run_checks():
    rng = random.Random(20231031)
    checks = 0
    for _ in range(500):
        d = rng.randrange(2, 8)
        weights = [10 ** rng.uniform(-1.2, 1.2) for j in range(d)]
        tau = (0.01 + .94 * rng.random()) / d
        p, s, val = optimal_design(tau, weights)
        assert abs(sum(p) - 1.0) < 2e-11
        assert all(pi > tau and 0 < si < 1 for pi, si in zip(p, s))
        assert all(abs(pi * si * (2-si) - tau) < 2e-11 for pi, si in zip(p, s))
        assert abs(val - risk_for_probabilities(tau, p, weights)) < 1e-10
        marginals = [w * tau / (pi*pi*math.sqrt(1-tau/pi)*(1+math.sqrt(1-tau/pi))**2)
                     for w,pi in zip(weights,p)]
        assert max(marginals)/min(marginals) < 1+2e-9
        checks += 5
        for j in range(10):
            # Randomly redistribute probability while preserving feasibility.
            z = [rng.expovariate(1) for i in range(d)]
            q = [tau + (1-d*tau) * zz / sum(z) for zz in z]
            assert risk_for_probabilities(tau, q, weights) >= val - 1e-10
            checks += 1
    for _ in range(250):
        d = rng.randrange(2, 7)
        lambdas = [Fraction(rng.randrange(1, 11),rng.randrange(1, 9)) for j in range(d)]
        sigmas2 = [Fraction(rng.randrange(1, 11),rng.randrange(1, 9)) for j in range(d)]
        pp = [Fraction(rng.randrange(1, 10), 1) for j in range(d)]
        pp = [v/sum(pp) for v in pp]
        ss = [Fraction(rng.randrange(1, 20), 10) for j in range(d)]
        for l, sig2, p, s in zip(lambdas, sigmas2, pp, ss):
            # Exact second-moment recursion and its fixed point.
            q = 1 - p*s*(2-s)
            v = s*sig2/(l*l*(2-s))
            innovation = p*s*s*sig2/(l*l)
            assert q*v + innovation == v
            assert l*v/2 == sig2*s/(2*l*(2-s))
            checks += 2
    # Sharp feasibility endpoint.
    for d in range(2, 12):
        weights = [float(i*i+1) for i in range(d)]
        p,s,val=optimal_design(1/d, weights)
        assert p == [1/d]*d and s == [1.0]*d and val == sum(weights)
        checks += 1
    # Both limiting sampling laws and value expansions.
    for d in (2, 3, 5):
        w = [float(i*i+2) for i in range(d)]
        target = [math.sqrt(z)/sum(map(math.sqrt,w)) for z in w]
        tau = 1e-5
        p,s,val=optimal_design(tau,w)
        assert max(abs(x-y) for x,y in zip(p,target)) < 2e-4
        assert abs(val/(tau/4*(sum(map(math.sqrt,w)))**2)-1) < 2e-4
        checks += 2
        delta=1e-5
        tau = (1-delta)/d
        p,s,val=optimal_design(tau,w)
        excess=[(pi-tau)/delta for pi in p]
        tgt=[x*x/sum(y*y for y in w) for x in w]
        assert max(abs(x-y) for x,y in zip(excess,tgt))<0.012
        pred=sum(w)-2*math.sqrt(delta/tau)*math.sqrt(sum(x*x for x in w))
        assert abs(val-pred)<.04
        checks += 2
    # Concrete two-coordinate asymmetry example.
    p,s,val=optimal_design(.1,[.5,4.5])
    assert .27777 < p[0] < .27779
    assert abs(val-.22314303955973805)<2e-11
    assert risk_for_probabilities(.1,[.5,.5],[.5,4.5]) / val > 1.24
    checks += 3
    print('PASS',checks,'exact and numerical tests')

if __name__ == '__main__':
    run_checks()
