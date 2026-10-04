#!/usr/bin/env python3
from math import lcm

def factor(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            out.append((d, a))
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append((n, 1))
    return out

def phi(n):
    if n == 1:
        return 1
    ans = n
    for p, _ in factor(n):
        ans = ans // p * (p - 1)
    return ans

def lambda_prime_power(p, a):
    if p == 2:
        if a == 1:
            return 1
        if a == 2:
            return 2
        return 2 ** (a - 2)
    return (p - 1) * p ** (a - 1)

def carmichael_lambda(n):
    if n == 1:
        return 1
    ans = 1
    for p, a in factor(n):
        ans = lcm(ans, lambda_prime_power(p, a))
    return ans

def printed_rhs(n):
    return phi(n) if n % 8 else phi(n) // 2

# First branch: 8 does not divide n.
for n in range(1, 12):
    if n % 8 != 0:
        assert carmichael_lambda(n) == phi(n)
assert 12 % 8 != 0
assert carmichael_lambda(12) == 2
assert phi(12) == 4
assert carmichael_lambda(12) != printed_rhs(12)

# Second branch: 8 divides n.
for n in range(1, 24):
    if n % 8 == 0:
        assert carmichael_lambda(n) == phi(n) // 2
assert 24 % 8 == 0
assert carmichael_lambda(24) == 2
assert phi(24) // 2 == 4
assert carmichael_lambda(24) != printed_rhs(24)

print("VERIFY_OK")
