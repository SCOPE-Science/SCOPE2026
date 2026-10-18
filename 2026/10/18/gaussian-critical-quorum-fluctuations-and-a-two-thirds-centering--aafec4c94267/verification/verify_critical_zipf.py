#!/usr/bin/env python3
"""Reproduce finite checks for a harmonic Zipf quorum-time fluctuation law.

These tests are finite numerical checks, not proofs of asymptotic claims.
Requires Python 3.9+ standard library only.
"""
import math
import random
import statistics

GAMMA = 0.577215664901532860606512090082402431


def array_statistics(n, a):
    f = 0.0
    d = 0.0
    v = 0.0
    for j in range(1, n + 1):
        z = a / j
        q = math.exp(-z)
        one_minus_q = -math.expm1(-z)
        f += one_minus_q / j
        d += q / (j*j)
        v += q * one_minus_q / (j*j)
    return f, d, v


def harmonic(n):
    return math.fsum(1.0/j for j in range(1, n+1))


def mean_root(n, theta):
    goal = theta * harmonic(n)
    base = math.exp((theta - 2.0)*GAMMA) * n**theta
    low = base/2.0
    high = base*2.0
    while array_statistics(n, low)[0] >= goal:
        low *= 0.5
    while array_statistics(n, high)[0] <= goal:
        high *= 2.0
    for _ in range(33):
        mid = (low + high)/2.0
        if array_statistics(n, mid)[0] < goal:
            low = mid
        else:
            high = mid
    return (low + high)/2.0


def simulate(n, theta, repetitions=1000, seed=20261017):
    rnd = random.Random(seed)
    h = harmonic(n)
    root = mean_root(n, theta)
    threshold = theta*h
    vals = []
    for _ in range(repetitions):
        visits = [(j * (-math.log1p(-rnd.random())), j) for j in range(1, n+1)]
        visits.sort()
        seen_weight = 0.0
        for at, j in visits:
            seen_weight += 1.0/j
            if seen_weight > threshold:
                vals.append(math.sqrt(root)*(at/root - 1.0))
                break
        else:
            raise AssertionError('missing absorption')
    return statistics.mean(vals), statistics.pvariance(vals), sum(x <= 0 for x in vals)/len(vals)


def main():
    count = 0
    for n in (10000, 100000):
        for theta in (0.5, 2.0/3.0, 0.8):
            root = mean_root(n, theta)
            f,d,v = array_statistics(n,root)
            goal = theta*harmonic(n)
            assert abs(f-goal) < 1e-8
            assert abs(root*d - 1.0) < 2.0*root/n + 0.02
            assert abs(root*v - 0.5) < 0.025
            count += 3
            a0 = math.exp((theta-2.0)*GAMMA)*n**theta
            drift = math.sqrt(a0)*(root/a0 - 1.0)
            predicted = a0**1.5/n
            assert drift > 0
            assert abs(drift/predicted - 1.0) < 0.13
            count += 2
    # Stronger high-N precision check at the boundary theta = 2/3.
    n = 200000
    theta = 2.0/3.0
    root = mean_root(n,theta)
    a0 = math.exp((theta-2.0)*GAMMA)*n**theta
    drift = math.sqrt(a0)*(root/a0 - 1.0)
    assert abs(drift - math.exp(1.5*(theta-2.0)*GAMMA)) < 0.008
    count += 1
    # A separate first-arrival simulation checks the time change and scaling,
    # without asserting that finite sampling proves a central limit theorem.
    sample_mean,sample_variance,sample_cdf0 = simulate(2000, 0.5)
    print('finite simulation: mean=%.5f variance=%.5f P(Z<=0)=%.5f'%(
        sample_mean,sample_variance,sample_cdf0))
    assert abs(sample_mean) < 0.14
    assert 0.32 < sample_variance < 0.72
    assert 0.40 < sample_cdf0 < 0.60
    count += 3
    print('SUCCESS: %d deterministic analytic/numeric and simulation assertions passed'%count)


if __name__ == '__main__':
    main()
