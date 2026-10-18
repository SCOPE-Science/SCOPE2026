#!/usr/bin/env python3
"""Independent exhaustive recurrences for dyadic nontotient stopping times."""
from array import array
from math import isqrt

LIMIT = 1 << 19


def totients_by_prime_sieve(limit):
    phi = array('I', range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for n in range(p, limit + 1, p):
                phi[n] -= phi[n] // p
    return phi


def totients_by_smallest_factor(limit):
    spf = array('I', [0]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == 0:
            for n in range(p*p, limit + 1, p):
                if spf[n] == 0:
                    spf[n] = p
    phi = array('I', [0]) * (limit + 1)
    phi[1] = 1
    for n in range(2, limit + 1):
        p = spf[n] or n
        m = n // p
        phi[n] = phi[m] * p if m % p == 0 else phi[m] * (p - 1)
    return phi


def heights(phi, limit):
    h = bytearray(limit + 1)
    for n in range(2, limit + 1):
        successor = n - phi[n]
        assert 1 <= successor < n
        h[n] = h[successor] + 1
    return h


def maxima(h, limit):
    table = []
    for i in range(1, 20):
        lo = (1 << (i - 1)) + 1
        hi = 1 << i
        section = h[lo:hi + 1]
        height = max(section)
        winners = [lo + j for j, v in enumerate(section) if v == height]
        table.append((i, int(height), len(winners), winners[0]))
    return table


def main():
    phi_a = totients_by_prime_sieve(LIMIT)
    phi_b = totients_by_smallest_factor(LIMIT)
    assert phi_a == phi_b
    a = heights(phi_a, LIMIT)
    b = heights(phi_b, LIMIT)
    assert a == b
    t = maxima(a, LIMIT)
    assert t == [
        (1,1,1,2),(2,2,1,4),(3,3,2,6),(4,4,4,10),
        (5,6,1,30),(6,7,5,42),(7,9,2,114),(8,10,9,186),
        (9,12,4,390),(10,14,2,798),(11,16,2,1950),
        (12,18,1,4074),(13,20,2,7770),(14,22,3,15810),
        (15,24,6,30702),(16,26,15,53130),(17,28,18,105090),
        (18,30,44,206910),(19,33,1,462210)
    ], t
    jumps = [(t[j][0], t[j][1] - t[j - 1][1]) for j in range(1,len(t))]
    assert all(x <= 2 for k, x in jumps if k < 19)
    assert jumps[-1] == (19,3)
    assert [n for n in range((1<<18)+1, (1<<19)+1) if a[n] == 33] == [462210]
    orbit=[462210]
    while orbit[-1]!=1:
        orbit.append(orbit[-1]-phi_a[orbit[-1]])
    assert len(orbit)==34
    print('FULL_RANGE',LIMIT,'TWO_INDEPENDENT_SIEVES_PASS')
    print('TABLE k:M,count,first')
    for i, v, count, first in t:
        print(f'{i}:{v},{count},{first}')
    print('FIRST_JUMP_AT',jumps[-1], 'UNIQUE_WITNESS',462210)
    print('WITNESS_ORBIT',','.join(map(str,orbit)))
    print('VERIFIED')

if __name__ == '__main__':
    main()
