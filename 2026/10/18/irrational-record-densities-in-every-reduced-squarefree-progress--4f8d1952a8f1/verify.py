#!/usr/bin/env python3
"""Exact checks for congruence-class densities in a recursive record set."""
from fractions import Fraction
from decimal import Decimal, localcontext


def primes_upto(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(limit**.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = b'\x00' * (((limit - p*p)//p) + 1)
    return [p for p in range(2, limit+1) if sieve[p]]

PRIMES = primes_upto(2000)
P = {0: 1}
for n in range(1, 7):
    P[n] = P[n - 1] * PRIMES[n - 1]


def records_below(bound):
    out = []
    x = 3
    while x <= bound:
        out.append(x)
        q = next(p for p in PRIMES if (x - 1) % p != 0)
        x += q - 1
    return out

R = records_below(P[6] + 1)
assert R[:9] == [3, 5, 7, 11, 13, 17, 19, 23, 25]
assert len(R) > 8000

def W(n, m, a):
    return sum(1 for r in R if PRIMES[n] <= r <= P[n] + 1 and r % m == a)

def S(n, m, a):
    return sum(1 for r in R if PRIMES[n-1] <= r < PRIMES[n] and r % m == a)

checks = 0
for m in [2,3,5,6,7,10,11,15]:
    n0 = min(n for n in range(2,6) if P[n] % m == 0)
    for a in range(m):
        if __import__('math').gcd(a,m) != 1:
            continue
        for n in range(n0,6):
            lhs = W(n+1,m,a)
            rhs = PRIMES[n] * W(n,m,a) - S(n+1,m,a)
            assert lhs == rhs, (m,a,n,lhs,rhs)
            checks += 1
assert W(3,3,1) == 5 and W(3,3,2) == 4
assert sum(W(4,3,a) for a in range(3)) == 62

# Numerically evaluate the exact convergent rational approximations to the densities.
# For m=3, n0=3 and the tail after n=40 is smaller than 1e-40.
with localcontext() as c:
    c.prec = 60
    densities = {}
    for a in (1,2):
        rho = Fraction(W(3,3,a),P[3])
        q = P[3]
        for n in range(4,41):
            q *= PRIMES[n-1]
            # All records in short prime gaps can be computed directly from R,
            # as p_41 < 200 and R covers every prime gap through that point.
            s = sum(1 for r in R if PRIMES[n-1] <= r < PRIMES[n] and r % 3 == a)
            rho -= Fraction(s,q)
        densities[a] = Decimal(rho.numerator)/Decimal(rho.denominator)
    bias = densities[1] - densities[2]
    assert bias > Decimal(1)/72
    assert Decimal('0.0289') < bias < Decimal('0.0291')
    print('delta_3_1=',densities[1])
    print('delta_3_2=',densities[2])
    print('bias_3=',bias)
print('records_through_30031=',len(R))
print('recurrence_checks=',checks)
print('VERIFY_OK')
