"""Independent finite checks for the multinomial histogram roughness variance law.

Python >=3.9; standard library only. Run: python verify.py
"""
from itertools import product
from math import exp, factorial, sqrt, pi, log
from fractions import Fraction
import random


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for rest in compositions(total - a, length - 1):
                yield (a,) + rest


def multinomial_moments(n, N):
    q = Fraction(1, n ** N)
    m1 = Fraction(0)
    m2 = Fraction(0)
    factorial_N = factorial(N)
    for counts in compositions(N, n):
        d = sum(abs(counts[i + 1] - counts[i]) for i in range(n - 1))
        p = q * factorial_N
        for a in counts:
            p /= factorial(a)
        m1 += p * d
        m2 += p * d * d
    return m1, m2 - m1 * m1


def poisson_coeff(lam):
    maxval = int(lam + 15 * sqrt(lam + 1) + 20)
    masses = [exp(-lam)]
    for j in range(1, maxval + 1):
        masses.append(masses[-1] * lam / j)
    m = sum(abs(i - j) * masses[i] * masses[j]
            for i in range(maxval + 1) for j in range(maxval + 1))
    c = sum(abs(i - j) * (i + j - 2 * lam) * masses[i] * masses[j]
            for i in range(maxval + 1) for j in range(maxval + 1))
    mean_abs_at = [sum(abs(i - j) * masses[j] for j in range(maxval + 1))
                   for i in range(maxval + 1)]
    h = sum(masses[j] * mean_abs_at[j] ** 2 for j in range(maxval + 1))
    V = 2 * lam + 2 * h - 3 * m * m - c * c / lam
    return V, m, c



def disjoint_covariance(n, N, cutoff=11):
    # Compute separate first and mixed moments of edges (1,2) and (3,4).
    from math import lgamma
    p2 = 0.0
    p4 = 0.0
    for a in range(cutoff):
        for b in range(cutoff):
            s = a + b
            if s <= N:
                probability = exp(lgamma(N+1)-lgamma(N-s+1)-lgamma(a+1)-lgamma(b+1)
                                  -s*log(n)+(N-s)*log(1-2/n))
                p2 += abs(a-b)*probability
    for a in range(cutoff):
        for b in range(cutoff):
            if a == b: continue
            for c in range(cutoff):
                for d in range(cutoff):
                    s = a+b+c+d
                    if c==d or s>N: continue
                    probability = exp(lgamma(N+1)-lgamma(N-s+1)
                                      -lgamma(a+1)-lgamma(b+1)-lgamma(c+1)-lgamma(d+1)
                                      -s*log(n)+(N-s)*log(1-4/n))
                    p4 += abs(a-b)*abs(c-d)*probability
    return p4-p2*p2

def run():
    checks = 0
    for n in range(2, 7):
        for N in range(0, 10):
            m, v = multinomial_moments(n, N)
            assert 0 <= m <= 2 * N
            assert v >= 0
            assert m.denominator > 0 and v.denominator > 0
            checks += 3
    small = poisson_coeff(0.002)[0]
    assert abs(small / (4 * 0.002 ** 2) - 1) < 0.01
    checks += 1
    for lam in (0.1, 0.5, 1.0, 2.0, 5.0):
        V, m, c = poisson_coeff(lam)
        assert V > 0 and m > 0 and c > 0
        checks += 3
        n = 90
        N = round(n * lam)
        rng = random.Random(20000 + int(100 * lam))
        K = 14000
        mean = 0.0
        mean2 = 0.0
        for rep in range(K):
            counts = [0] * n
            for _ in range(N):
                counts[rng.randrange(n)] += 1
            d = sum(abs(counts[i + 1] - counts[i]) for i in range(n - 1))
            mean += d
            mean2 += d * d
        sample_v = (mean2 / K - (mean / K) ** 2) / n
        assert abs(sample_v - V) < 0.16 + 0.07 * V, (lam, sample_v, V)
        checks += 1
    # Verify that a distant pair's covariance is order -1/n, not zero.
    c_at_one = poisson_coeff(1.0)[2]
    for n in (80, 160, 320):
        scaled = n * disjoint_covariance(n, n)
        assert abs(scaled + c_at_one*c_at_one) < 0.07, (n, scaled, c_at_one)
        checks += 1
    high = poisson_coeff(30.0)[0] / 30.0
    limit = 8 / 3 + (4 * sqrt(3) - 12) / pi
    assert abs(high - limit) < 0.04, (high, limit)
    checks += 1
    print('PASS:', checks, 'exact/arithmetic/Monte Carlo checks')
    print('large-load theoretical constant:', limit)


if __name__ == '__main__':
    run()
