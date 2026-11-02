"""Exact tests for the rise/drop covariance in uniform integer compositions.

All calculations are over integers or rational numbers.  Run with Python 3.
"""
from fractions import Fraction as F
from math import comb


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def coefficients(num, den, cutoff):
    assert den[0] == 1
    out = []
    for i in range(cutoff + 1):
        value = (num[i] if i < len(num) else 0) - sum(
            den[j] * out[i - j] for j in range(1, min(i, len(den) - 1) + 1)
        )
        out.append(value)
    return out


def closed_a(n):
    return F(2**n * (3*n-5), 36) - F((-1)**n, 9)


def closed_ad(n):
    p = (13, -2, -11)[n % 3]
    return (2**n * (F((n+1)*(n+2), 72) - F(61*(n+1), 756) + F(155, 5292))
            + F((-1)**n*(2*n+1), 54) + F(1, 6) + F(p, 147))


def covariance(n):
    total = F(2**(n-1))
    return closed_ad(n)/total - (closed_a(n)/total)**2


def closed_cov(n):
    sign = (-1)**n
    p = (13, -2, -11)[n % 3]
    return (F(231*n-1975, 15876) + F(1, 2**n) *
            (F(4*sign*n, 27) - F(7*sign, 81) + F(1, 3) + F(2*p, 147))
            - F(4, 81*4**n))


def exhaustive(n):
    sa = sd = sad = 0
    for mask in range(1 << (n-1)):
        last = 0
        parts = []
        for i in range(1, n):
            if (mask >> (i-1)) & 1:
                parts.append(i-last)
                last = i
        parts.append(n-last)
        a = sum(u < v for u, v in zip(parts, parts[1:]))
        d = sum(u > v for u, v in zip(parts, parts[1:]))
        sa += a
        sd += d
        sad += a*d
    return sa, sd, sad


def run():
    tested = 0
    # Independently calculate power-series coefficients from rational identities.
    den_a = multiply([1, 1], multiply([1, -2], [1, -2]))
    num_a = [0, 0, 0, 1]
    den_ad = [1]
    for factor in ([1, -1], [1, 1], [1, 1], [1, -2], [1, -2], [1, -2], [1, 1, 1]):
        den_ad = multiply(den_ad, factor)
    num_ad = [0, 0, 0, 0, 1, 0, 1, -2, -2]
    arr_a = coefficients(num_a, den_a, 240)
    arr_ad = coefficients(num_ad, den_ad, 240)
    for n in range(1, 241):
        assert arr_a[n] == closed_a(n), ('A', n)
        assert arr_ad[n] == closed_ad(n), ('AD', n)
        assert closed_cov(n) == covariance(n), ('Cov', n)
        tested += 3
    for n in range(1, 14):
        a, d, ad = exhaustive(n)
        assert a == d == arr_a[n], ('exhaustive A D', n)
        assert ad == arr_ad[n], ('exhaustive AD', n)
        tested += 2
    assert covariance(1) == covariance(2) == 0
    tested += 1
    for n in range(3, 9):
        assert covariance(n) < 0, ('negative', n)
        tested += 1
    # For all n >= 9, a positive line dominates the absolute
    # exponentially decreasing remainder.  The bound is decreasing in n.
    baseline9 = F(231*9-1975, 15876)
    bound9 = F(1, 2**9) * (F(4*9,27) + F(7,81) + F(26,147) + F(1,3)) + F(4,81*4**9)
    assert baseline9 > bound9 > 0
    tested += 1
    for n in range(9, 241):
        bound = F(1, 2**n) * (F(4*n,27) + F(7,81) + F(26,147) + F(1,3)) + F(4,81*4**n)
        assert F(231*n-1975,15876) > bound
        assert covariance(n) > 0
        tested += 2
    print('PASS', tested, 'exact assertions', 'cov(n=8)=', covariance(8), 'cov(n=9)=', covariance(9))


if __name__ == '__main__':
    run()
