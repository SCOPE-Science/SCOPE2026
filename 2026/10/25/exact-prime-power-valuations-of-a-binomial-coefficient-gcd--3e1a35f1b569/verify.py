"""Exact finite checks of a binomial-coefficient gcd valuation theorem."""
from math import comb, gcd


def components(n):
    r = n
    p = 2
    while p * p <= r:
        if r % p == 0:
            a = 0
            while r % p == 0:
                r //= p
                a += 1
            yield p, a
        p += 1
    if r > 1:
        yield r, 1


def prediction(k):
    n = k + 1
    z = 1
    for p, a in components(n):
        b = n // (p ** a)
        if b == 1:
            exponent = a
        else:
            t, c = b - 1, 0
            while t >= p:
                t //= p
                c += 1
            exponent = max(0, a - c)
        z *= p ** exponent
    return z


def vp_fact(n, p):
    s = 0
    while n:
        n //= p
        s += n
    return s


def vp_choose(n, k, p):
    return vp_fact(n, p) - vp_fact(k, p) - vp_fact(n - k, p)


def verify():
    direct_cases = 0
    for k in range(2, 141):
        g = 0
        for q in range(2, k + 2):
            g = gcd(g, comb(q * k, k))
        assert g == prediction(k), (k, g, prediction(k))
        direct_cases += 1
    valuation_cases = 0
    for n in range(3, 2001):
        k = n - 1
        expected = prediction(k)
        for p, a in components(n):
            exponent = 0
            y = expected
            while y % p == 0:
                exponent += 1
                y //= p
            got = min(vp_choose(q * k, k, p) for q in range(2, n + 1))
            assert got == exponent, (n, p, exponent, got)
            valuation_cases += 1
    print('VERIFY_OK: %d direct exact gcd cases and %d prime-power valuation cases' % (direct_cases, valuation_cases))


if __name__ == '__main__':
    verify()
