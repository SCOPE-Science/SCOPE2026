"""Exact arithmetic checks for the monomial Hilbert--Schmidt identity."""
from fractions import Fraction
from math import factorial, comb


def rising(a, k):
    p = 1
    for i in range(k):
        p *= a + i
    return p


def compositions(k, n):
    if n == 1:
        yield (k,)
        return
    for u in range(k + 1):
        for tail in compositions(k - u, n - 1):
            yield (u,) + tail


def direct(n, alpha, beta, m):
    nu = n + alpha + 1
    ans = Fraction(0)
    for j in range(m + 1):
        k = m - j
        b = comb(beta + j - 1, j)
        for u in compositions(k, n):
            ans += (Fraction(rising(nu, k), rising(nu, m))
                    * Fraction(factorial(u[0]+j), factorial(u[0])) * b*b)
    return ans


def collapsed(n, alpha, beta, m):
    nu = n + alpha + 1
    ans = Fraction(0)
    for j in range(m + 1):
        k = m - j
        b = comb(beta + j - 1, j)
        ans += (Fraction(factorial(m+n-1)*factorial(k+nu-1)*factorial(j),
                         factorial(m+nu-1)*factorial(k)*factorial(j+n-1))*b*b)
    return ans


def special(n, m):
    assert n == 2
    harmonic = sum((Fraction(1, k) for k in range(1, m + 2)), Fraction(0))
    return ((m+3)*harmonic - Fraction((m+1)*(2*m+5), m+2)
            + Fraction(m+1, 2))


def main():
    for n, alpha, beta in ((2,0,1), (2,2,3), (3,0,1), (3,1,2), (4,0,1), (4,1,3)):
        for m in range(8):
            assert direct(n, alpha, beta, m) == collapsed(n, alpha, beta, m), (n,alpha,beta,m)
    for m in range(22):
        assert collapsed(2,0,1,m) == special(2,m), m
    assert collapsed(2,0,1,0) == 1
    assert collapsed(2,0,1,1) == Fraction(7,3)
    print('BALL_CESARO_HS_IDENTITY_EXACT_OK')


if __name__ == '__main__':
    main()
