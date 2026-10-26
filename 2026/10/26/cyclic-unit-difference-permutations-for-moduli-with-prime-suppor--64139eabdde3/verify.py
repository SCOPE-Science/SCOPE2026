#!/usr/bin/env python3
"""Construct and verify cyclic unit-difference orderings for 3^a p^b.
All arithmetic is exact; these finite checks supplement the general proof.
"""
from math import gcd


def primes_upto(B):
    return [p for p in range(2, B + 1) if all(p % q for q in range(2, int(p**0.5) + 1))]


def primitive_root(p):
    h = p - 1
    fs = [q for q in primes_upto(h) if h % q == 0]
    return next(g for g in range(2, p) if all(pow(g, h // q, p) != 1 for q in fs))


def crt_3_p(a, b, p):
    return (b + p * ((a - b) * pow(p, -1, 3) % 3)) % (3*p)


def base(p):
    assert p >= 5 and all(p % q for q in range(2, int(p**0.5)+1))
    g = primitive_root(p)
    c = next(c for c in range(2, p) if c != g)
    L = p - 1
    seq = []
    for t in range(L):
        gt = pow(g, t, p)
        seq.append(crt_3_p(1, gt, p))
        seq.append(crt_3_p(2, c * gt % p, p))
    return seq


def lift(seq, n, p):
    assert n % p == 0 and p % 2 == 1 and len(seq) % 2 == 0
    return [(x + n * ((1 if i % 2 == 0 else 2) * r)) % (n*p)
            for r in range(p) for i, x in enumerate(seq)]


def construction(p, a, b):
    assert a >= 1 and b >= 1
    seq, n = base(p), 3*p
    for _ in range(a-1):
        seq = lift(seq, n, 3)
        n *= 3
    for _ in range(b-1):
        seq = lift(seq, n, p)
        n *= p
    return n, seq


def verify(n, seq):
    unitset = {x for x in range(n) if gcd(x, n) == 1}
    assert len(seq) == len(unitset)
    assert set(seq) == unitset
    diffs = {(seq[i] - seq[(i+1) % len(seq)]) % n for i in range(len(seq))}
    assert len(diffs) == len(seq) and diffs == unitset


def main():
    cases, largest, units_checked = 0, 0, 0
    for p in primes_upto(53):
        if p < 5:
            continue
        for a in range(1, 5):
            for b in range(1, 5):
                n = 3**a * p**b
                if n > 100000:
                    continue
                n, seq = construction(p, a, b)
                verify(n, seq)
                cases += 1
                largest = max(largest, n)
                units_checked += len(seq)
    # Distinct source-independent edge analysis for a small mixed modulus.
    for n, vals in ((15, base(5)), (21, base(7))):
        assert [gcd((vals[i]-vals[(i+1) % len(vals)]) % n, n)
                for i in range(len(vals))] == [1]*len(vals)
    print('VERIFY_OK', 'moduli',cases,'largest_n',largest,
          'total_units_and_edges',units_checked)

if __name__ == '__main__':
    main()
