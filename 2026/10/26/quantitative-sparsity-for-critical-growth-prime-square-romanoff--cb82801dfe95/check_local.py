"""Exact finite checks of the local congruence frequencies and exponent identity.
This checks illustrative small moduli; it does not establish the infinite bound.
"""
from fractions import Fraction
from math import log


def primes_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * (((n-i*i)//i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def check_one(r):
    assert r % 4 == 1
    units = range(1, r)
    count = sum((u*u + v*v) % r == 0 for u in units for v in units)
    assert count == 2*(r-1), (r, count)
    assert Fraction(count, (r-1)**2) == Fraction(2, r-1)
    for t in range(1, r):
        # Exact count with quadratic character chi(t) = +/-1.
        chi = 1 if pow(t, (r-1)//2, r) == 1 else -1
        got = sum((u*u + v*v - t) % r == 0 for u in units for v in units)
        assert got == r - 3 - 2*chi, (r, t, got)


def main():
    ps = [r for r in primes_to(151) if r % 4 == 1]
    for r in ps:
        check_one(r)
    t = 1 / log(2)
    delta = 1 - t + t*log(t)
    rhs = 2 - t - t*log(2/t)
    assert abs(delta-rhs) < 1e-13
    assert 0.085 < delta < 0.087
    print('VERIFY_OK',len(ps),'moduli','delta',format(delta,'.15f'))


if __name__ == '__main__':
    main()
