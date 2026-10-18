#!/usr/bin/env python3
"""Exact finite certificate for a least mu-Sondow witness family."""
from collections import Counter


def prime_factorization(n):
    factors = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def orbit_mod_prime(p):
    x = pow(2, 8, p)
    orbit = []
    while x not in orbit:
        orbit.append(x)
        x = pow(x, 8, p)
    # For odd prime p, 2 is invertible, so exponentiation by 8
    # may have a transient but the entire forward trajectory is covered.
    return orbit


def cert():
    table = {}
    max_orbit = 0
    ncandidates = 0
    for n in range(3, 145, 2):
        factorization = prime_factorization(n)
        if any(e != 1 for e in factorization.values()):
            continue
        ncandidates += 1
        blockers = []
        for p in factorization:
            orbit = orbit_mod_prime(p)
            max_orbit = max(max_orbit, len(orbit))
            target = (-(n // p)) % p
            if target not in orbit:
                blockers.append(p)
        assert blockers, ('missing prime obstruction', n)
        table[n] = min(blockers)
    assert ncandidates == 58 and len(table) == 58
    assert max_orbit == 52
    assert pow(2, 8, 145) == 111
    assert pow(111, 8, 145) == 111
    assert 111 + 29 + 5 == 145
    for j in range(3, 25, 3):
        for n in range(2, 145):
            factors = prime_factorization(n)
            if all((pow(2, 2**j, p**e) + n // p) % (p**e) == 0 for p, e in factors.items()):
                raise AssertionError((j, n))
        assert all((pow(2, 2**j, p) + 145 // p) % p == 0 for p in (5, 29))
    hist = Counter(table.values())
    assert len(hist) == 33
    return table, hist, ncandidates, max_orbit


if __name__ == '__main__':
    table, hist, ncases, max_orbit = cert()
    print('CERTIFICATE_PASS')
    print('squarefree_odd_candidates', ncases, 'blocking_primes', len(hist), 'max_prime_orbit', max_orbit)
    print('cases', ' '.join(str(n) + ':' + str(p) for n,p in sorted(table.items())))
