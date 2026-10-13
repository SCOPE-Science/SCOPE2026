"""Independent finite checks for a classification of 2-imperfect integers.
Pure Python 3; exact integer arithmetic; NOT a proof of unbounded claims.
"""
from math import isqrt


def prime_factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            result.append((d, a))
        d = 3 if d == 2 else d + 2
    if n > 1:
        result.append((n, 1))
    return result


def beta_power(p, a):
    assert a >= 1 and p >= 2
    return (p ** (a + 1) + (-1) ** a) // (p + 1)


def beta(n):
    result = 1
    for p, a in prime_factors(n):
        result *= beta_power(p, a)
    return result


def check(limit=300_000):
    # Independent sieve for beta and distinct-prime-support counts.
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for k in range(p * p, limit + 1, p):
                if spf[k] == k:
                    spf[k] = p
    all_hits, two_support_hits = [], []
    support_count = [0, 0, 0, 0]
    for n in range(1, limit + 1):
        t, b, omega = n, 1, 0
        while t > 1:
            p = spf[t]
            a = 0
            while t % p == 0:
                t //= p
                a += 1
            b *= beta_power(p, a)
            omega += 1
        if omega <= 2:
            support_count[min(omega, 3)] += 1
        if 2*b == n:
            all_hits.append(n)
            if omega <= 2:
                two_support_hits.append(n)
        if n <= 5000:
            assert b == beta(n), (n,b,beta(n))
    assert two_support_hits == [2,12,40], two_support_hits
    assert 252 in all_hits
    assert beta(2) == 1 and beta(12) == 6 and beta(40) == 20
    assert beta(252) == 126
    # Direct test of the solved exponential equation over a generous finite box.
    for a in range(2, 120, 2):
        for b in range(1, 100, 2):
            if 3 ** (b+1) == 2 ** (a+1) + 1:
                assert (a,b) == (2,1)
    print(f'VERIFY_OK limit={limit} support_le2_count={sum(support_count)} all_hits={all_hits} two_support_hits={two_support_hits} sharp_boundary=252 checked_power_box=a2..118_even_b1..99_odd')

if __name__ == '__main__':
    check()
