"""Finite spot checks for a primorial obstruction to primitive representations.

These computations do not prove the asymptotic theorem.
"""
from math import gcd, isqrt


def primes_leq(n):
    if n < 2:
        return []
    prime = bytearray(b'\x01') * (n + 1)
    prime[0:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if prime[p]:
            prime[p*p::p] = b'\x00' * (((n-p*p)//p)+1)
    return [p for p in range(n + 1) if prime[p]]


def witness(a, t):
    assert a >= 3 and t >= a
    q = 1
    for p in primes_leq(t):
        if (p <= isqrt(t) and a % p != 0) or (p > isqrt(t) and p % a == a-1):
            q *= p
    lower = (q + t - 1)//t
    b = lower + ((-q - lower) % a)
    return q, b


def verify(a, t):
    q, b = witness(a, t)
    assert gcd(a,b) == 1
    assert b*t >= q and b > 0
    for y in range(2, t + 1):
        if y % a == a - 1:
            assert gcd(q, y) > 1, (a,t,q,y)
    for p in primes_leq(t):
        if p % a == a - 1:
            assert q % p == 0, (a,t,q,p)
    all_reps = []
    for y in range(q // b + 1):
        if (q-b*y) % a == 0:
            x = (q-b*y)//a
            assert gcd(x,y)>1, (a,t,q,b,x,y)
            all_reps.append((x,y))
    return q,b,len(all_reps)


if __name__ == '__main__':
    count = 0
    for a in range(3,15):
        for t in range(max(a,8),61):
            verify(a,t)
            count += 1
    assert verify(3,20) == (1870,95,6),verify(3,20)
    print(f'VERIFY_OK cases={count} example_a3_t20_Q1870_b95')
