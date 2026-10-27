"""Numerical witness for a rare-tail moment law in a stochastic search model.

Uses independent exponential underlying completion, where the exact survival
probability is an elementary expression. No external datasets are required.
"""
from math import exp, expm1, gamma, comb, factorial
from scipy.integrate import quad

KAPPA = 2.0
BETA = 1.7
DELTA = 0.9
MEAN_BARE = 1.0 / KAPPA


def survival(t, eps):
    d = DELTA * eps
    b = BETA * eps
    h = KAPPA + d
    lone = (d + KAPPA * exp(-h * t)) / h
    integral = KAPPA / h * (t + expm1(-h * t) / h)
    return lone * exp(-b * integral)


def scaled_moment(q, eps):
    # eps^(q-1) E[T_eps^q]; transformed variable u=eps*t.
    def weighted(u):
        if u == 0.0:
            return 0.0
        return q * (u ** (q - 1)) * survival(u / eps, eps) / eps
    cut = 10 * eps
    a = quad(weighted, 0.0, cut, epsabs=2e-10, epsrel=2e-9, limit=400)[0]
    b = quad(weighted, cut, 30, epsabs=2e-10, epsrel=2e-9, limit=400)[0]
    return a + b


def run():
    count = 0
    for eps in (0.002, 0.0003):
        for u in (0.5, 1.0, 2.0):
            predicted = DELTA * MEAN_BARE * exp(-BETA * u)
            ratio = survival(u / eps, eps) / eps
            assert abs(ratio - predicted) / predicted < 0.035, (eps, u, ratio, predicted)
            count += 1
        for q in (2., 3.):
            predicted = DELTA * MEAN_BARE * gamma(q + 1) / (BETA ** q)
            actual = scaled_moment(q, eps)
            assert abs(actual - predicted) / predicted < 0.035, (eps, q, actual, predicted)
            count += 1
        mean = scaled_moment(1.,eps)
        pred_mean = MEAN_BARE * (1 + DELTA / BETA)
        assert abs(mean - pred_mean)/pred_mean<0.01,(eps,mean,pred_mean)
        count += 1
    # Independent deterministic bare first-passage witness: the first searcher
    # succeeds exactly at t0, unless its mortality clock rings first.
    t0 = 0.7
    for eps in (0.002, 0.0003):
        b, d = BETA * eps, DELTA * eps
        probability_failure = -expm1(-d*t0)
        successful_arrival_rate = b*exp(-d*t0)
        for u in (0.5, 1.0, 2.0):
            assert u/eps > t0
            actual = (probability_failure / eps)*exp(-successful_arrival_rate*(u/eps-t0))
            expected = DELTA*t0*exp(-BETA*u)
            assert abs(actual-expected)/expected < 0.035
            count += 1
        for q in (2, 3):
            actual_raw = t0**q + probability_failure*sum(
                comb(q,k)*t0**(q-k)*factorial(k)/successful_arrival_rate**k
                for k in range(1,q+1))
            actual = eps**(q-1)*actual_raw
            expected = DELTA*t0*factorial(q)/(BETA**q)
            assert abs(actual-expected)/expected < 0.035
            count += 1
        mean = t0 + probability_failure / successful_arrival_rate
        expected = t0*(1+DELTA/BETA)
        assert abs(mean-expected)/expected < 0.01
        count += 1
    print(f"PASS: {count} independent finite-parameter witness comparisons; analytical proof remains essential")
    print(f"eps=0.0003, predicted eps*E[T^2]={DELTA * MEAN_BARE * 2 / (BETA**2):.12g}")

if __name__ == '__main__':
    run()
