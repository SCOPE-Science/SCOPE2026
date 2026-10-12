#!/usr/bin/env python3
from math import isqrt


def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factorization(n):
    x = n
    out = {}
    d = 2
    while d*d <= x:
        while x % d == 0:
            out[d] = out.get(d, 0) + 1
            x //= d
        d = 3 if d == 2 else d + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def j2(n):
    v = n*n
    for p in factorization(n):
        v = (v // (p*p)) * (p*p - 1)
    return v

pairs = [(1,1)]
P,Q = 1,1
for t in range(1,101):
    P,Q = 2*P + 3*Q, P + 2*Q
    pairs.append((P,Q))
    assert P*P - 3*Q*Q == -2
    if t % 3 == 1 and t > 1:
        assert P % 5 == 0
        assert Q % 3 == 0
        assert P > 5 and Q > 3
    if t <= 30 and isprime(P) and isprime(Q):
        assert j2(P) == j2(2*Q)

assert pairs[1] == (5,3)
assert pairs[2] == (19,11)
assert pairs[3] == (71,41)
assert j2(5) == j2(6) == 24
assert j2(19) == j2(22) == 360
assert j2(71) == j2(82) == 5040

pell_set = set()
for P,Q in pairs:
    if P <= 5000 and Q <= 5000:
        pell_set.add((P,Q))

primes = [n for n in range(2,5001) if isprime(n)]
hits = []
for p in primes:
    target = j2(p)
    for q in primes:
        if j2(2*q) == target:
            hits.append((p,q))
            assert (p,q) in pell_set

expected = [(P,Q) for P,Q in pairs if P <= 5000 and Q <= 5000 and isprime(P) and isprime(Q)]
assert sorted(hits) == sorted(expected)

print('VERIFY_OK', f'pell_indices=0..100', f'prime_window=5000', f'hits={hits}', f'first={pairs[1:4]}')
