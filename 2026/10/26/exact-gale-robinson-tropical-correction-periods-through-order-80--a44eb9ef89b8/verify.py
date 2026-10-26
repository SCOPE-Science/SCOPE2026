#!/usr/bin/env python3
"""Exact finite certificates for the primitive three-term Gale--Robinson tropical recurrence.

Run: python3 verify.py
Uses only Python's standard library and exact integer arithmetic.
Every period conclusion follows from the affine-translation lemma in RESULT.md.
"""
import hashlib
from itertools import combinations
from math import gcd

LIMIT = 80
EXPECTED_TRIPLES = 11052
EXPECTED_TOTAL_PERIOD = 84412414
EXPECTED_MAX_PERIOD = (13, 26, 41, 36556)


def candidate_period(p, q, r):
    return (gcd(p, q)*r*r + gcd(p, r)*q*q
            + gcd(q, r)*p*p + p*q*r)


def standard_parameter_list(limit):
    return [(p, q, r) for p, q, r in combinations(range(1, limit), 3)
            if p+q+r <= limit and gcd(gcd(p, q), r) == 1]


def independently_enumerated_list(limit):
    values = []
    for m in range(6, limit+1):
        for p in range(1, m+1):
            for q in range(p+1, m+1):
                r = m-p-q
                if r > q and gcd(gcd(p, q), r) == 1:
                    values.append((p, q, r))
    return sorted(values)


def check_one(p, q, r):
    m = p + q + r
    N = candidate_period(p, q, r)
    if N % 2:
        raise AssertionError(('odd period', p, q, r, N))
    k = [0] * (N+m+1)
    k[m] = 1
    # The recurrence is indexed starting at n=1; each referenced term
    # has an index between n and n+m-1.
    for n in range(1, N+1):
        k[n+m] = max(k[n+p]+k[n+m-p],
                     k[n+q]+k[n+m-q],
                     k[n+r]+k[n+m-r])-k[n]
    # Only m identities are required; the affine-translation lemma proves
    # every subsequent identity and consequently all future periodicity.
    for i in range(1, m+1):
        if k[N+i] != k[i] + i + N//2:
            raise AssertionError(('shift mismatch', p, q, r, i,
                                  k[N+i], k[i]+i+N//2))
    return N, (k[N+1], k[N+m], k[(N+1)//2])


def main():
    xs = standard_parameter_list(LIMIT)
    ys = independently_enumerated_list(LIMIT)
    if sorted(xs) != ys:
        raise AssertionError('two parameter enumerations disagree')
    if len(xs) != EXPECTED_TRIPLES:
        raise AssertionError(('triple count', len(xs)))
    checksum = hashlib.sha256()
    count_new = 0
    total_period = 0
    max_period = (0, 0, 0, 0)
    for p, q, r in xs:
        N, anchors = check_one(p, q, r)
        count_new += (p, q) != (1, 2)
        total_period += N
        if N > max_period[3]:
            max_period = (p, q, r, N)
        checksum.update(f'{p},{q},{r},{N},{anchors[0]},{anchors[1]},{anchors[2]}\n'.encode('ascii'))
    if total_period != EXPECTED_TOTAL_PERIOD:
        raise AssertionError(('total candidate periods', total_period))
    if max_period != EXPECTED_MAX_PERIOD:
        raise AssertionError(('largest candidate period', max_period))
    if count_new != 10977:
        raise AssertionError(('outside previously proved family', count_new))
    print('VERIFY_OK')
    print('triples', len(xs))
    print('triples_outside_p1_q2', count_new)
    print('total_candidate_periods', total_period)
    print('largest_candidate_period', max_period)
    print('certificate_digest_sha256', checksum.hexdigest())


if __name__ == '__main__':
    main()
