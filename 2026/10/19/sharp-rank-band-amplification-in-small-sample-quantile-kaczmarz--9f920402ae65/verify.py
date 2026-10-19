#!/usr/bin/env python3
"""Exact finite checks and finite-population asymptotic diagnostics for
median-selected small-sample randomized Kaczmarz."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, erf, sqrt, exp, lgamma, fsum


def choose(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def weights(m, k):
    assert k % 2 == 0 and 2 <= k <= m
    p = k // 2
    den = comb(m, k)
    return [Q(choose(i - 1, p - 1) * choose(m - i, k - p), den)
            for i in range(1, m + 1)]


def exact_error(m, marked, w):
    marked = set(marked)
    answer = Q(0)
    for i, wi in enumerate(w, 1):
        r = Q(i, m + 1)
        answer += wi * ((1 + r)**2 if i in marked else 1 - r*r)
    return answer


def logchoose(n, j):
    if j < 0 or j > n:
        return float('-inf')
    return lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)


def order_cdf(m, k, t):
    """P(k/2-th sampled rank <= t), from a hypergeometric tail."""
    p = k // 2
    z = logchoose(m, k)
    return fsum(exp(logchoose(t, j) + logchoose(m-t, k-j) - z)
                for j in range(p, k + 1)
                if 0 <= j <= t and 0 <= k-j <= m-t)


def diagnostics():
    count = 0
    for m in range(6, 16):
        for k in range(2, min(8, m) + 1, 2):
            w = weights(m, k)
            assert sum(w) == 1
            p = k // 2
            brute = [0] * m
            for subset in combinations(range(1, m+1), k):
                brute[subset[p - 1]-1] += 1
            assert all(wi == Q(b, comb(m, k)) for wi, b in zip(w, brute))
            mu = Q(p * (m + 1), k + 1)
            var = Q(p * (k-p+1) * (m+1) * (m-k), (k+1)**2 * (k+2))
            assert sum(w[i-1] * i for i in range(1, m+1)) == mu
            assert sum(w[i-1] * (i - mu)**2 for i in range(1, m+1)) == var
            for c in range(1, min(4, m-2)+1):
                optimal = max(sum(w[j:j+c]) for j in range(m-c+1))
                brute_opt = max(sum(w[i-1] for i in indices)
                                for indices in combinations(range(1,m+1), c))
                assert optimal == brute_opt
                center = set(range((m-c)//2+1, (m-c)//2+c+1))
                error = exact_error(m, center, w)
                baseline = 1 - sum(w[i-1]*Q(i,m+1)**2 for i in range(1,m+1))
                premium = sum(w[i-1]*(2*Q(i,m+1)+2*Q(i,m+1)**2)
                              for i in center)
                assert error == baseline + premium
                count += 1
    print('Finite exact checks:', count)
    for k in (20, 40, 80, 120):
        m = k**3
        for theta in (0.5, 1.0, 2.0):
            h = max(1, round(theta*m/(2*sqrt(k))))
            left, right = m//2-h+1, m//2+h
            prob = order_cdf(m,k,right)-order_cdf(m,k,left-1)
            normal = erf(theta/sqrt(2))
            assert 0 <= prob <= 1
            print('sample, population, theta, exact P, Gaussian limit',
                  k, m, theta, f'{prob:.8f}', f'{normal:.8f}')

if __name__ == '__main__':
    diagnostics()
