#!/usr/bin/env python3
"""Finite arithmetic checks for translated even-power Fibonacci congruences.

The infinite theorem is proved in RESULT.md; these assertions only test examples.
"""
from math import comb

Q = ((1, 1), (1, 0))
I = ((1, 0), (0, 1))

def mul(a, b, p):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % p
                       for j in range(2)) for i in range(2))

def mpow(a, exponent, p):
    out = I
    while exponent:
        if exponent & 1:
            out = mul(out, a, p)
        a = mul(a, a, p)
        exponent >>= 1
    return out

def fibmod(n, p):
    def pair(m):
        if not m:
            return 0, 1
        a, b = pair(m >> 1)
        c = a * (2 * b - a) % p
        d = (a * a + b * b) % p
        return (d, (c + d) % p) if m & 1 else (c, d)
    return pair(n)[0]

def fibexact(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def primes_under(limit):
    return [n for n in range(3, limit) if all(n % d for d in range(2, int(n**0.5) + 1))]

def main():
    for k in range(1, 12):
        assert all(comb(2 * k, j) % 2 == 0 for j in range(1, 2*k, 2))
    primes = [p for p in primes_under(250) if p % 5 in (2, 3)]
    translations = range(1, 21)
    degrees = range(1, 7)
    total = 0
    for p in primes:
        assert mpow(Q, p, p) == ((0, (-1) % p), ((-1) % p, 1))
        assert mpow(Q, p * p, p) == tuple(tuple(e % p for e in row) for row in Q)
        for h in translations:
            for k in degrees:
                exponent = (p + h)**(2*k)
                target = (h - 1)**(2*k)
                lhs = mpow(Q, exponent, p)[0][1]
                rhs = fibmod(target, p)
                assert lhs == rhs
                assert lhs == fibmod(exponent, p)
                total += 1
    diffs = 0
    for h in range(1, 7):
        for k in range(1, 4):
            delta = fibexact((h+1)**(2*k)) - fibexact((h-1)**(2*k))
            assert delta > 0
            diffs += 1
    unshifted = 0
    for k in range(1, 7):
        assert fibmod(5**(2*k), 5) == 0
        assert (fibmod(5**(2*k), 5) - fibmod(1, 5)) % 5 == 4
        unshifted += 1
    print(f'VERIFY_OK inert_primes={len(primes)} translated_congruences={total} parity_degrees=11 positive_deltas={diffs} unshifted_obstructions={unshifted}')

if __name__ == '__main__':
    main()
