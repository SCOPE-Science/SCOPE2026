#!/usr/bin/env python3
"""Independent finite diagnostics for cubic Walsh absolute kernel averages.
All calculations use the Python standard library. Infinite statements rest on proofs.
"""
import math
from fractions import Fraction


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def direct_exact(n):
    numerator = sum(choose(n, k) * abs((n - 2*k) * ((n - 2*k)**2 - (3*n - 2))) for k in range(n+1))
    return Fraction(numerator, 6 * 2**n)


def boundary_exact(n):
    # Integer comparison avoids root-rounding ambiguity at perfect squares.
    k = 0
    while k <= n and (n - 2*k) > 0 and (n - 2*k)**2 > 3*n - 2:
        k += 1
    K = k - 1
    H = (n - 1) // 2
    def P(L):
        return choose(n, 3) * (choose(n-3, L)-2*choose(n-3, L-1)+choose(n-3, L-2))
    return Fraction(2*P(K)-P(H), 2**(n-1))


def b2(t):
    t %= 1
    return t*t-t+1/6


p0 = 1 / math.sqrt(2 * math.pi)
pa = p0 * math.exp(-1.5)
c = (2*p0 + 8*pa) / 6


def scaled_phase(n):
    delta = 0.0 if n % 2 == 0 else 0.5
    theta = (math.sqrt(3*n) - n) / 2
    return (-2.5*p0 - 4*pa - 12*p0*b2(delta) - 48*pa*b2(theta))/6


def numeric_average(n):
    # Complete sum in log-binomial arithmetic, without loss at large dimensions.
    constant = math.lgamma(n + 1) - n * math.log(2)
    terms = []
    for k in range(n + 1):
        s = n - 2*k
        qabs = abs(s * (s*s - (3*n - 2))) / 6
        if qabs:
            terms.append(math.exp(constant - math.lgamma(k+1)-math.lgamma(n-k+1))*qabs)
    return math.fsum(terms)


def run():
    for n in range(3, 401):
        assert direct_exact(n) == boundary_exact(n), ('boundary mismatch', n)
    assert abs((2*p0 + 8*pa) / 6 - c) < 1e-14
    assert abs(((-2.5*p0 - 4*pa)) - (1.5*p0 - 12*pa + 8*pa - 4*p0)) < 1e-14
    for n in (2000, 2001, 5000, 5001, 10000, 10001, 20000, 20001):
        scaled_actual = (numeric_average(n) - c*n**1.5) / math.sqrt(n)
        scaled_predicted = scaled_phase(n)
        assert abs(scaled_actual-scaled_predicted) < 0.015, (n, scaled_actual, scaled_predicted)
        print('phase', n, round(scaled_actual, 8), round(scaled_predicted, 8))
    print('PASS: 398 exact rational identities, 8 large-dimension phase comparisons')


if __name__ == '__main__':
    run()
