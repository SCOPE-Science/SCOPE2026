#!/usr/bin/env python3
"""Exact-integer checks for ranks of cyclic rectangular-window Gabor POVMs.

No floating point and no external packages. The complete all-N proof is in RESULT.md.
"""
from functools import lru_cache
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def poly_quotient_monic(a, b):
    v = a[:]
    out = [0] * max(1, (len(a) - len(b) + 1))
    while len(v) >= len(b):
        offset = len(v) - len(b)
        c = v[-1]
        out[offset] += c
        for j in range(len(b)):
            v[offset + j] -= c * b[j]
        while v and v[-1] == 0:
            v.pop()
    assert not v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


@lru_cache(None)
def cyclotomic(t):
    p = [-1] + [0] * (t - 1) + [1]
    for d in divisors(t):
        if d != t:
            p = poly_quotient_monic(p, cyclotomic(d))
    assert p[-1] == 1
    return p


def zero_at_primitive_root(coeffs, t):
    # With integer coefficients, f(zeta_t)=0 iff Phi_t divides f.
    p = cyclotomic(t)
    v = coeffs[:]
    while v and v[-1] == 0:
        v.pop()
    while len(v) >= len(p):
        c = v[-1]
        off = len(v) - len(p)
        for j, pj in enumerate(p):
            v[off + j] -= c * pj
        while v and v[-1] == 0:
            v.pop()
    return not v


def beta(m, a):
    q = gcd(m, a)
    return q if (m // q) % 2 == 0 else 0


def predicted_per_lag(N, k, a):
    r = k - a if a < k else 0
    s = a + k - N if a > N - k else 0
    if r + s == 0:
        return 0
    if not (r and s):
        return N - gcd(N, r + s) + 1
    d = gcd(N, k)
    return N - (d - 1) - beta(N, a) + beta(d, a)


def check(N):
    for k in range(1, N):
        g = set(range(k))
        actual_rank = 0
        predicted_rank = 0
        for a in range(N):
            overlap = [x for x in range(N) if x in g and ((x - a) % N) in g]
            actual = 0
            for b in range(N):
                t = N // gcd(N, b)
                cs = [0] * t
                for x in overlap:
                    cs[x % t] += 1
                if not zero_at_primitive_root(cs, t):
                    actual += 1
            expect = predicted_per_lag(N, k, a)
            assert actual == expect, (N, k, a, actual, expect)
            actual_rank += actual
            predicted_rank += expect
        assert actual_rank == predicted_rank
        if N % 2:
            p = next(i for i in range(3, N + 1, 2) if N % i == 0)
            assert (actual_rank == N * N) == (k >= N - (p - 1) // 2)
        else:
            assert actual_rank < N * N
    if N & (N - 1) == 0:
        ranks = [sum(predicted_per_lag(N, k, a) for a in range(N))
                 for k in range(1, N)]
        best = N * N - (N // 2) * (N.bit_length() - 1)
        winners = {k for k in range(1, N) if k % 2 and k > N // 2}
        assert max(ranks) == best
        assert {k for k, r in enumerate(ranks, 1) if r == best} == winners


if __name__ == '__main__':
    for n in range(3, 25):
        check(n)
    print('EXACT cyclotomic checks pass for all lengths and lags, 3 <= N <= 24')
    for n in (8, 9, 15, 16, 25):
        r = [sum(predicted_per_lag(n, k, a) for a in range(n))
             for k in range(1, n)]
        print(n, r)
