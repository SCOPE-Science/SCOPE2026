#!/usr/bin/env python3
"""Standalone bounded checks of a base-b digit-sum complement theorem."""
from collections import Counter

def digit_sum(n, b):
    s = 0
    while n:
        n, d = divmod(n, b)
        s += d
    return s

def valuation_b(n, b):
    t = 0
    while n > 0 and n % b == 0:
        n //= b
        t += 1
    return t

def prime_factor(n):
    for p in range(2, n+1):
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            return p, a, n
    raise AssertionError(n)

checked = 0
for b in range(2, 16):
    p, a, rest = prime_factor(b)
    for k in range(1, b):
        for L in range(1, 5):
            Q = b**L
            if Q > 42000:
                continue
            f = lambda n: digit_sum(k*n, b) - digit_sum(n, b)
            groups = [Counter(), Counter()]
            for n in range(1, Q):
                delta = min(L, valuation_b(k*n, b)) - valuation_b(n, b)
                lhs = f(n) + f(Q-n)
                assert lhs == k-1-(b-1)*delta, (b,k,L,n)
                if rest == 1:
                    assert delta in (0, 1)
                    groups[delta][f(n)] += 1
                checked += 1
            if rest == 1:
                c = 0
                w = k
                while w % p == 0:
                    w //= p
                    c += 1
                exceptional = (p**c-1)*(Q-1)//(b-1)
                assert sum(groups[1].values()) == exceptional
                for j, group in enumerate(groups):
                    center_twice = k-1 if j==0 else k-b
                    for exponent, count in group.items():
                        assert group[center_twice-exponent] == count
                assert 2*sum(f(n) for n in range(Q)) == (k-p**c)*(Q-1)
for b in range(4, 81):
    p, a, m = prime_factor(b)
    if m == 1:
        continue
    k = p**(a+1)
    Q = b*b
    assert k < b
    observed = [min(2, valuation_b(k*n, b))-valuation_b(n, b)
                for n in (1, m, Q//k)]
    assert observed == [0,1,2], (b, observed)
print('VERIFY_OK: reflection identities and reciprocal sectors:',checked,
      'direct cases; composite-base witnesses to 80')
