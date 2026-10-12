"""Finite regression checks for two-by-d rectangular-edge arithmetic.
Only uses Python standard library. Mathematical proofs are in RESULT.md.
"""
from math import gcd


def remainder_t_power(d, a, b):
    """Return coeffs for t**d mod (t**2 + a*t + b) over integers."""
    u, v = 1, 0
    for _ in range(d):
        u, v = -b*v, u-a*v
    return u, v


def smallest_prime_factor(n):
    for p in range(2, n + 1):
        if n % p == 0:
            return p
    raise AssertionError(n)


def phi(n):
    return sum(gcd(j, n) == 1 for j in range(1, n+1))


count_construction = 0
for d in range(3, 301):
    if d % 2 == 0:
        # t^2-1, corresponding to y^2-x^2.
        u, v = remainder_t_power(d, 0, -1)
        assert (u, v) == (1, 0)
        count_construction += 1
    if d % 3 == 0:
        # t^2+t+1, corresponding to y^2+xy+x^2.
        u, v = remainder_t_power(d, 1, 1)
        assert (u, v) == (1, 0)
        count_construction += 1

count_degree = 0
for d in range(3, 2001):
    if d % 2 == 0:
        expect = 1
    else:
        expect = (smallest_prime_factor(d)-1)//2
    candidates = [1 if m==2 else phi(m)//2 for m in range(2,d+1) if d%m==0]
    assert min(candidates) == expect
    assert (expect == 1) == (d%2==0 or d%3==0)
    count_degree += 1

print('VERIFY_OK rational constructions', count_construction,
      'arithmetic degree cases', count_degree)
