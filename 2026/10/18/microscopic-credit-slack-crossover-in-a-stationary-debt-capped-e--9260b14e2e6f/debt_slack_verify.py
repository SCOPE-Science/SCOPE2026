"""Finite exact and asymptotic checks for capped-debt stationary distributions.

Run: python3 debt_slack_verify.py. Python standard library only.
These computations do not certify the limiting theorem, proved analytically.
"""
from math import comb, exp, lgamma, log, sqrt
from itertools import product


def count(n, k, b):
    if b == 0:
        return comb(k + n - 1, n - 1)
    return sum(comb(n, j) * comb(b - 1, j - 1) *
               comb(k + b + n - j - 1, n - j - 1)
               for j in range(1, min(n - 1, b) + 1))


def exhaustive(n, k, b):
    vals = range(-b, k + b + 1)
    return sum(sum(row) == k and sum(max(-v, 0) for v in row) == b
               for row in product(vals, repeat=n))


def logsumexp(items):
    top = max(items)
    return top + log(sum(exp(x - top) for x in items))


def log_count(n, k, b):
    if b == 0:
        return lgamma(k+n) - lgamma(n) - lgamma(k+1)
    terms = []
    for j in range(1, min(n-1,b)+1):
        terms.append(lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)
                     +lgamma(b)-lgamma(j)-lgamma(b-j+1)
                     +lgamma(k+b+n-j)-lgamma(n-j)-lgamma(k+b+1))
    return logsumexp(terms)


def run():
    assertions = 0
    for n in (2, 3, 4):
        for k in (0, 1, 2):
            for b in (0, 1, 2):
                assert count(n, k, b) == exhaustive(n, k, b)
                assertions += 1
    for n in (3, 4, 6):
        for k in (1, 3, 6):
            for b in range(2, 10):
                assert count(n, k, b) > count(n, k, b-1)
                assertions += 1
    for n, a, kap, r in ((100, 20, 1, 1), (250, 50, 1, 1),
                           (300, 35, 2, 0.5), (200, 50, 1, 2)):
        k = round(kap * a * n)
        l = round(r * k)
        c = 1 / (kap * sqrt(r * (r+1)))
        estimate = -a * (log_count(n, k, l-1) - log_count(n, k, l))
        assert abs(estimate - c) < 0.075
        assertions += 1
        log_ratio = log_count(n, k, l - round(a)) - log_count(n, k, l)
        assert abs(log_ratio + c) < 0.11
        assertions += 1
        for s in (0, 1, 2, 3, 5, 11):
            ratio = exp(log_count(n,k,l-s) - log_count(n,k,l))
            bound = exp(-max(s-1,0) * (n-2)/(k+l+n))
            assert ratio <= bound * (1+1e-8)
            assertions += 1
    print(f"PASS: {assertions} independent exact and numerical assertions")


if __name__ == '__main__':
    run()
