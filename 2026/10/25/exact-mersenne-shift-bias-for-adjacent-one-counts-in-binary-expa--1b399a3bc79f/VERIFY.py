#!/usr/bin/env python3
"""Exact arithmetic checks for the Mersenne-shift adjacent-one comparison."""
from fractions import Fraction as F


def r(n):
    assert n >= 0
    return (n & (n >> 1)).bit_count()


def ge(x):
    if x >= 0:
        return F(1)
    if x == -1:
        return F(1, 2)
    return F(0)


def go(x):
    if x <= -2:
        return F(0)
    return F(1) - F(3, 2**(x + 3))


def exact_density(k):
    n = 1 << k
    total = F(2)  # a=0, both parities always favorable
    for a in range(1, n):
        d = r(a-1) - r(a)
        high_a = (a >> (k-1)) & 1
        high_predecessor = ((a-1) >> (k-1)) & 1
        total += ge(d + high_predecessor) + go(d - high_a)
    return total / (2*n)


def check():
    for q in range(1, 1 << 16):
        delta = r(q+1)-r(q)
        if q % 2 == 0:
            assert delta == ((q >> 1) & 1)
        else:
            j = 0
            z = q
            while z & 1:
                j += 1
                z >>= 1
            assert delta == ((q >> (j+1)) & 1) - (j-1)
    expected = [F(13, 16), F(47, 64), F(87, 128)]
    for k in range(1, 14):
        target = expected[k-1] if k <= 3 else F(83,128)
        result = exact_density(k)
        assert result == target, (k, result, target)
    for j in range(0, 20):
        w = F(0)
        for b in (0, 1):
            for h in (0, 1):
                d = -b if j == 0 else j-1-b
                w += ge(d+h) + go(d-h)
        target = F(37,8) if j <= 1 else F(8) - F(27,2**(j+2))
        assert w == target, (j, w, target)
    for k in range(4, 20):
        j = k-2
        u = sum((ge(j-1-h+h)+go(j-1-h-h) for h in (0,1)), F(0))
        v = ge(k-2) + go(k-3)
        assert u == 4 - F(15,2**k), (k, u)
        assert v == 2 - F(3,2**k), (k, v)
        whole = F(8) - F(18,2**k) + sum(
            (2**(k-jj-3) * (F(37,8) if jj<=1 else 8-F(27,2**(jj+2)))
             for jj in range(k-2)),F(0))
        assert whole == F(83*2**k,64), (k, whole)
    # Independent direct integer walk, using a finite but long high-bit sample.
    # A residual long carry contributes at most the fraction 2**(-12).
    for k in range(1, 7):
        t = (1 << k) - 1
        favorable = 0
        count = 1 << (k + 12)
        for n in range(count):
            favorable += (r(n+t) >= r(n))
        frequency = F(favorable,count)
        assert abs(frequency-exact_density(k)) <= F(1,2**11), (k,frequency)
    print('PASS: exact conditional change laws; 13 all-ones shifts; 20 bulk weights; 16 boundary identities; direct integer checks')

if __name__ == '__main__':
    check()
