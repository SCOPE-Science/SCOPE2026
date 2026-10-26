"""Finite exhaustive check of the annealed stable-extension size profile.

Run: python size_profile_checker.py
Only n <= 6 are exhaustively enumerated. The infinite theorem uses a proof.
"""
from itertools import product
from collections import Counter
from math import comb, lgamma, log, sqrt, exp, pi


def is_stable(mask, f):
    n = len(f)
    return all(bool((mask >> v) & 1) != bool((mask >> f[v]) & 1) for v in range(n))


def coeff(n, k):
    if not 0 < k < n:
        return 0
    return comb(n, k) * (n-k)**k * k**(n-k)

for n in range(1, 7):
    actual = Counter()
    for f in product(range(n), repeat=n):
        for mask in range(1 << n):
            if is_stable(mask, f):
                actual[mask.bit_count()] += 1
    expected = {k: coeff(n,k) for k in range(n+1)}
    assert all(actual[k] == expected[k] for k in range(n+1)), (n, actual, expected)
    positive = [expected[k] for k in range(1,n)]
    assert all(positive[i]**2 > positive[i-1]*positive[i+1] for i in range(1,len(positive)-1))
    print(n, 'maps', n**n, 'stable size histogram', [actual[k] for k in range(n+1)])

def log_annealed(n, k):
    return (lgamma(n+1) - lgamma(k+1) - lgamma(n-k+1)
            + k*log(n-k) + (n-k)*log(k) - n*log(n))

for n in (100, 1000, 10000):
    k=n//2
    scaled=sqrt(n)*exp(log_annealed(n,k))
    limit=sqrt(2/pi)
    print('center',n,scaled,'target',limit)
    assert abs(scaled-limit) < 3/n
print('PASS finite exhaustion and local saddle-point cross-check')
