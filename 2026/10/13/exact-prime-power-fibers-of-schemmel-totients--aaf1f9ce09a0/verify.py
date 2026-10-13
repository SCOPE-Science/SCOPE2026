#!/usr/bin/env python3
from math import isqrt

LIMIT = 50000

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p*p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def schemmel(r, n):
    if n == 1:
        return 1
    z = 1
    for p, a in factor(n).items():
        if p <= r:
            return 0
        z *= p**(a-1) * (p-r)
    return z

def predicted(r, ell, t):
    E = [j for j in range(1, t+1) if is_prime(r + ell**j)]
    out = []
    for mask in range(1 << len(E)):
        chosen = [E[i] for i in range(len(E)) if (mask >> i) & 1]
        s = sum(chosen)
        base = 1
        for j in chosen:
            base *= r + ell**j
        if ell == r + 1 and is_prime(ell):
            if s > t:
                continue
            rem = t - s
            if rem == 0:
                out.extend([base, base*ell])
            else:
                out.append(base * ell**(rem+1))
        elif s == t:
            out.append(base)
            if is_prime(r+1):
                out.append(base*(r+1))
    return sorted(set(out))

primes = [p for p in range(2, 20) if is_prime(p)]
targets = {(ell, t): ell**t for ell in primes for t in range(1, 4)}
checks = 0
for r in range(1, 9):
    observed = {key: [] for key in targets}
    inverse = {value: key for key, value in targets.items()}
    for n in range(1, LIMIT+1):
        value = schemmel(r, n)
        if value in inverse:
            observed[inverse[value]].append(n)
    for key, value in targets.items():
        ell, t = key
        want = [n for n in predicted(r, ell, t) if n <= LIMIT]
        assert observed[key] == want, (r, ell, t, observed[key], want)
        checks += 1

assert predicted(1, 2, 1) == [3, 4, 6]
assert predicted(1, 2, 2) == [5, 8, 10, 12]
assert predicted(2, 3, 1) == [5, 9, 15]
assert predicted(2, 3, 2) == [11, 27, 33, 45]

print('VERIFY_OK', f'checks={checks}', f'window=1..{LIMIT}', 'r=1..8', 'ell<=19', 't=1..3')
