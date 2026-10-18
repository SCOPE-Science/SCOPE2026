#!/usr/bin/env python3
"""Exact finite-prime-divisor census for the sixth-cyclotomic 3-cycle."""
import csv
from math import isqrt
from pathlib import Path


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def prime_factors(n):
    """All distinct positive prime divisors; complete trial division."""
    assert n >= 1
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors.append(n)
    return factors


def f(a):
    return a * a - a + 1


def candidates(bound):
    """All directed p->q->r with prime p=min(p,q,r)<=bound."""
    for p in range(2, bound + 1):
        if not is_prime(p):
            continue
        for q in prime_factors(f(p)):
            if q <= p:
                continue
            for r in prime_factors(f(q)):
                if r <= p or r == q:
                    continue
                yield p, q, r, int(f(r) % p == 0)


def main():
    records = list(candidates(349))
    assert len(records) == 70, len(records)
    assert sum(p < 349 for p, q, r, closure in records) == 69
    cycles = [row for row in records if row[3] == 1]
    assert cycles == [(349, 121453, 9710803, 1)], cycles

    path = Path(__file__).resolve().with_name('paths.csv')
    with path.open(newline='', encoding='utf-8') as stream:
        rows = csv.DictReader(stream)
        assert rows.fieldnames == ['p', 'q', 'r', 'closes']
        on_disk = [tuple(int(row[k]) for k in rows.fieldnames) for row in rows]
    assert on_disk == records, 'Exact CSV data differs from complete recomputation.'

    p, q, r = cycles[0][:3]
    assert all(is_prime(t) for t in (p, q, r))
    assert f(p) == q
    assert f(q) == 49 * 31 * r
    assert f(r) % p == 0
    n = p * q * r
    h = f(p) * f(q) * f(r)
    assert n == 411612748708891
    assert h % n == 0
    assert h // n == 410433300314317
    print('VERIFICATION_OK; vertices_le_349=70; candidate_paths=70; cycles=1; '
          'least_vertex=349; n=411612748708891; H(n)=410433300314317')


if __name__ == '__main__':
    main()
