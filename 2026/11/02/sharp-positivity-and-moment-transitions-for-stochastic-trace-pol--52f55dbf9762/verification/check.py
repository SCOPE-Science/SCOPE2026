#!/usr/bin/env python3
"""Reproduce exact trace-preconditioner identities and finite numerical checks."""
import math
import random


def single_probe_cdf(n, kappa):
    """P(n*u^T B u - lambda_max(B) <= 0), for n=2 or 3."""
    if kappa <= n:
        return 0.0
    x = (kappa - n) / (n * (kappa - 1))
    if n == 2:  # Beta(1/2,1/2) distribution
        return 2.0 / math.pi * math.asin(math.sqrt(x))
    if n == 3:  # Beta(1/2,1) distribution
        return math.sqrt(x)
    raise ValueError("Closed-form branch only for n=2,3")


def sample_u1_squared(n, rng):
    x = rng.gauss(0.0, 1.0)
    total = x*x
    for _ in range(n - 1):
        v = rng.gauss(0.0, 1.0)
        total += v*v
    return x*x/total


def measure(n, kappa, r, count, rng):
    threshold = (kappa - n) / (kappa - 1)
    failures = 0
    for _ in range(count):
        z = sum(n * sample_u1_squared(n, rng) for j in range(r)) / r
        failures += (z <= threshold)
    return failures / count




def critical_tail_constant(n,r):
    return (r**(r/2) / (n**r * math.gamma(1+r/2))
            * (math.gamma(n/2)/math.gamma((n-1)/2))**r)

def critical_cond(n,mean_u):
    ratio=(1+n*mean_u)/(n*n*mean_u)
    return max(ratio,1/ratio)

def check():
    # Eigenvalue identities for the exact trace-based first polynomial preconditioner.
    for n in (2,3,4,9,30):
        for k in (1.0001, 1.2, 2.0, 9.0, 1e4):
            eigen_hi = k * (n - 1)
            eigen_lo = k + n - 2
            assert eigen_hi + 1e-10*eigen_lo >= eigen_lo > 0
            cond = eigen_hi/eigen_lo
            assert abs(cond - (k*(n-1)/(k+n-2))) < 1e-12*cond
            assert 1-1e-10 <= cond <= n-1+1e-10
    assert abs(single_probe_cdf(3, 9) - 0.5) < 1e-14
    assert single_probe_cdf(2, 2) == 0.0
    assert single_probe_cdf(3, 3) == 0.0

    # Independent spherical draws: exact Beta CDF at n=2 and n=3.
    rng = random.Random(20261027)
    trials = 30000
    for n,k in ((2,2.1),(2,8.0),(3,3.2),(3,9.0),(3,30.0)):
        empirical=measure(n,k,1,trials,rng)
        expected=single_probe_cdf(n,k)
        assert abs(empirical-expected) < 0.018, (n,k,empirical,expected)

    # Each fixed finite kappa has an eventually vanishing failure probability.
    # This is a numerical check, not the proof of the law of large numbers.
    for n,k in ((3,9.0),(4,12.0)):
        small=measure(n,k,1,16000,rng)
        large=measure(n,k,100,5000,rng)
        assert large < small, (n,k,small,large)

    # High-dimensional large-spike limit: for r=1, Chi-square_1 CDF at 1.
    chi_one=math.erf(1/math.sqrt(2))
    assert abs(chi_one-0.682689492137086) < 1e-12
    # n*U approaches Chi-square_1; P(nU <= 1) approaches chi_one.
    n=300
    count=16000
    empirical=sum(n*sample_u1_squared(n,rng)<=1 for _ in range(count))/count
    assert abs(empirical-chi_one)<0.026,(empirical,chi_one)
    # Exactly computed critical-tail constants and a closed-form n=3,r=1 tail.
    assert abs(critical_tail_constant(2,1)-1/math.pi)<1e-14
    assert abs(critical_tail_constant(3,1)-1/3)<1e-14
    for threshold in (3.,10.,100.):
        # n=3, r=1: U has CDF sqrt(u), and K=(1+3U)/(9U)
        exact=1/(3*math.sqrt(threshold-1/3))
        rng2=random.Random(1521+int(threshold))
        observed=sum(critical_cond(3,sample_u1_squared(3,rng2))>threshold
                     for _ in range(45000))/45000
        assert abs(observed-exact)<0.014,(threshold,observed,exact)
    print('VERIFY_OK exact_spectral_cases=25 beta_cdf_cases=5 finite_probe_checks=4 high_dimension=1')


if __name__ == '__main__':
    check()
