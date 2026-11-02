#!/usr/bin/env python3
"""Reproducibility checks for the Ewens derangement-time upper-tail theorem.
No third-party packages are required. All random tests use an explicit seed.
"""
from fractions import Fraction
from math import comb, exp, expm1, log, lgamma, factorial, isclose, sqrt
import random


def joint_path_exact(n, theta):
    """Enumerate the Markov path distribution of (singleton count, zero visits)."""
    theta = Fraction(theta)
    states = {(1, 0): Fraction(1)}
    for m in range(1, n):
        nxt = {}
        for (c, z), mass in states.items():
            transitions = ((c + 1, theta / (m + theta)),
                           (c - 1, Fraction(c, 1) / (m + theta)),
                           (c, Fraction(m - c, 1) / (m + theta)))
            for d, weight in transitions:
                if weight == 0:
                    continue
                key = (d, z + int(d == 0))
                nxt[key] = nxt.get(key, Fraction()) + mass * weight
        states = nxt
    assert sum(states.values()) == 1
    return [sum(p * Fraction(z**r, n**r) for (c, z), p in states.items())
            for r in range(4)]


def moment_dp(n, theta, cutoff=None):
    """An independent Markov recursion for zero-occupation power moments."""
    th = Fraction(theta) if cutoff is None else float(theta)
    zero = Fraction(0) if cutoff is None else 0.0
    one = Fraction(1) if cutoff is None else 1.0
    cap = n + 1 if cutoff is None else cutoff + 1
    state = [[zero] * cap for _ in range(4)]
    state[0][1] = one
    for m in range(1, n):
        nxt = [[zero] * cap for _ in range(4)]
        for c in range(min(m, cap - 1) + 1):
            if state[0][c] == 0:
                continue
            for d, weight in ((c+1, th/(m+th)), (c-1, c/(m+th)),
                              (c, (m-c)/(m+th))):
                if d < 0 or d >= cap or weight == 0:
                    continue
                if d != 0:
                    for r in range(4):
                        nxt[r][d] += weight * state[r][c]
                else:
                    for r in range(4):
                        nxt[r][0] += weight * sum(comb(r,j)*state[j][c]
                                                       for j in range(r+1))
        state = nxt
    return [sum(state[r])/n**r for r in range(4)]


def a_k(theta, k):
    """E[exp(-theta*(1-U))], U~Beta(k,1); stable power series."""
    term, s = 1.0, 1.0
    for j in range(1, 150):
        term *= -theta / (k + j)
        s += term
        if abs(term) <= 1e-17 * abs(s):
            break
    assert s > 0
    return s


def limit_moments(theta, max_r):
    out = [1.0, exp(-theta)]
    for r in range(2, max_r+1):
        out.append(out[-1]*a_k(theta, r-1))
    return out


def constant(theta, limit):
    logm = -theta
    for k in range(1, limit):
        logm += log(a_k(theta,k))
    return exp(logm + theta * log(limit))


def simulate_y(theta, paths, seed=38056):
    rng = random.Random(seed)
    samples = []
    for _ in range(paths):
        # Poisson(theta) by Knuth's method
        threshold, prod, count = exp(-theta), 1.0, -1
        while prod > threshold:
            prod *= rng.random()
            count += 1
        c, t, y = count, 0.0, 0.0
        while t < 19:
            rate = theta + c
            tn = t - log(rng.random())/rate
            if c == 0:
                y += exp(-t) - exp(-tn)
            t = tn
            if rng.random() < theta/rate:
                c += 1
            else:
                c -= 1
        samples.append(y)
    return [sum(y**r for y in samples)/paths for r in range(1,4)]


def main():
    assertions = 0
    for theta in (Fraction(1), Fraction(2), Fraction(1,2)):
        for n in range(2, 10):
            a = joint_path_exact(n,theta)
            b = moment_dp(n,theta)
            for r in range(4):
                assert a[r] == b[r], (theta,n,r,a[r],b[r])
                assertions += 1
    for theta in (0.5, 1.0, 2.0):
        ms = limit_moments(theta, 7)
        assert isclose(ms[1], exp(-theta), rel_tol=1e-14)
        assert all(ms[j] >= ms[j+1] > 0 for j in range(1,7))
        assert isclose(ms[2]-ms[1]**2, exp(-2*theta) *
                       (expm1(theta)-theta)/theta, rel_tol=1e-13)
        assertions += 3
    # Direct Markov recursion approaching the stated limiting variance.
    for n in (2000, 8000, 24000):
        m = moment_dp(n, 1.0, cutoff=32)
        v = m[2] - m[1]**2
        vt = exp(-2)*(exp(1)-2)
        assert abs(m[1]-exp(-1)) < 4/sqrt(n)
        assert abs(v-vt) < 4/sqrt(n)
        assertions += 2
    # Independent CTMC simulation: stationary M/M/infinity path integral.
    for theta in (0.5, 1.0, 2.0):
        empirical = simulate_y(theta, 14000)
        expected = limit_moments(theta,3)[1:]
        assert all(abs(a-b) < 0.014 for a,b in zip(empirical,expected)), (theta,empirical,expected)
        assertions += 3
    # Upper-tail exponent: r^theta E[Y^r] approaches a finite positive constant.
    for theta in (0.5,1.0,2.0):
        c1 = constant(theta,5000)
        c2 = constant(theta,10000)
        assert 0.00001 < c1 < 100
        assert abs(c1-c2) < 0.002, (theta,c1,c2)
        assertions += 2
        print('theta=',theta,'limit mean,variance=',exp(-theta),
              exp(-2*theta)*(expm1(theta)-theta)/theta,
              'tail_prefactor_at_10000=',c2/exp(lgamma(theta+1)))
    print('All', assertions, 'assertions passed.')

if __name__ == '__main__':
    main()
