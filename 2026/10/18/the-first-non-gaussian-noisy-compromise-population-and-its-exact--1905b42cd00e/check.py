#!/usr/bin/env python3
"""Exact rational checks for a neutral, always-interacting noisy compromise chain.

Run: python3 check.py
No external packages are required. The proof is in RESULT.md; these tests
check the finite-dimensional identities used in its derivation.
"""
from fractions import Fraction as Q
from itertools import combinations


def centered(n):
    return [[Q(int(i == j)) - Q(1, n) for j in range(n)] for i in range(n)]


def sq(v):
    return sum((z * z for z in v), Q(0))


def update(d, i, j, mu):
    y = d.copy()
    gap = y[i] - y[j]
    y[i] -= mu * gap
    y[j] += mu * gap
    return y


def pair_average(n, fn):
    pairs = list(combinations(range(n), 2))
    return sum((fn(i, j) for i, j in pairs), Q(0)) / len(pairs)


def test_all_n():
    for n in range(2, 10):
        d = [Q(k + 1) for k in range(n)]
        m = sum(d) / n
        d = [v - m for v in d]
        S = sq(d)
        for mu in [Q(1, 9), Q(1, 4), Q(1, 2), Q(3, 4), Q(8, 9)]:
            t = 2 * mu * (1 - mu)
            avg_pair_gap2 = pair_average(n, lambda i, j: (d[i] - d[j]) ** 2)
            assert avg_pair_gap2 == 2 * S / (n - 1)
            loss = pair_average(n, lambda i, j: sq(update(d, i, j, mu)))
            assert loss == (1 - 2 * t / (n - 1)) * S
            # Exact second-moment equilibrium from drift and noise trace.
            stationary_S = Q((n - 1) ** 2, n) / t
            lam = 1 - 2 * t / (n - 1)
            assert stationary_S == lam * stationary_S + 2 * Q(n - 1, n)
            # The covariance of selected-pair noise has rank >= 2 at n>=3.
            if n >= 3:
                P = centered(n)
                vi = [P[k][0] for k in range(n)]
                vj = [P[k][1] for k in range(n)]
                assert vi[0] * vj[1] - vi[1] * vj[0] != 0


def test_three():
    for d in [[Q(-1), Q(0), Q(1)], [Q(2), Q(-3), Q(1)],
              [Q(1, 2), Q(1, 4), Q(-3, 4)]]:
        S = sq(d)
        assert sum(d) == 0
        assert sum(z**4 for z in d) == S**2 / 2
        assert pair_average(3, lambda i,j: (d[i]-d[j])**2) == S
        assert pair_average(3, lambda i,j: (d[i]-d[j])**4) == Q(3,2)*S*S
        for mu in [Q(1, 7), Q(1, 4), Q(1, 2), Q(3, 4)]:
            t = 2 * mu * (1-mu)
            def mean_second(i,j):
                y = update(d,i,j,mu)
                return sq(y) + Q(4,3)
            def mean_fourth(i,j):
                y = update(d,i,j,mu)
                # Conditional Gaussian squared-norm moment,
                # selected noises each have variance 1.
                # Trace covariance 4/3 and trace covariance squared 10/9.
                return sq(y)**2 + 2*sq(y)*Q(4,3) + 4*(y[i]**2+y[j]**2) + 4
            m2 = pair_average(3,mean_second)
            m4 = pair_average(3,mean_fourth)
            assert m2 == (1-t)*S+Q(4,3)
            assert m4 == (1-2*t+Q(3,2)*t*t)*S*S + Q(16-20*t,3)*S + 4
            stationary_S = Q(4,3)/t
            stationary_S2 = 4*(16-11*t)/(9*t*t*(2-Q(3,2)*t))
            assert stationary_S2 == (1-2*t+Q(3,2)*t*t)*stationary_S2 + Q(16-20*t,3)*stationary_S+4
            variance = stationary_S/3
            fourth = stationary_S2/6
            K = fourth / (variance**2)
            assert K == 3*(16-11*t)/(16-12*t)
            assert K-3 == 3*t/(16-12*t) > 0
    assert 3*(16-11*Q(1,2))/(16-12*Q(1,2)) == Q(63,20)
    print('Exact rational checks passed: N=2..9, five learning rates,')
    print('three three-agent configurations, four learning rates;')
    print('minimal non-Gaussian boundary, stationary variance, fourth moment.')

if __name__ == '__main__':
    test_all_n()
    test_three()
