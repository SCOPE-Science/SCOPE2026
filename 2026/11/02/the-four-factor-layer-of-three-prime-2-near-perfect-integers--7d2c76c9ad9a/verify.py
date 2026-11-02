#!/usr/bin/env python3
"""Reproducible exact finite checks for the four-factor 2-near-perfect theorem.

The infinite exclusions are proved in RESULT.md.  This checker verifies
all finite prime pairs surviving those exclusions and every omitted pair.
Standard-library Python 3 only.
"""
from math import isqrt

EXPECTED = {
    84: (14, 42),
    90: (9, 45),
    126: (18, 42),
    132: (6, 66),
    156: (2, 78),
    198: (6, 66),
    220: (20, 44),
    364: (4, 52),
    380: (4, 76),
    550: (5, 11),
}


def primes_through(limit):
    return [n for n in range(2, limit + 1) if n > 1 and all(n % d for d in range(2, isqrt(n) + 1))]


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def pairs(n):
    div = divisors(n)
    delta = sum(div) - 2 * n
    return tuple((a, b) for i, a in enumerate(div) for b in div[i + 1:] if a + b == delta)


def p3_candidates():
    # The only nonconstant q branch for n=2*3^2*q is 3q+39.
    base = divisors(18)
    possible = set()
    for a in base:
        for b in base:
            den = a - 3
            num = 39 - b
            if den > 0 and num % den == 0:
                q = num // den
                if q > 3 and q in primes_through(q):
                    possible.add(q)
    for i, a in enumerate(base):
        for b in base[i + 1:]:
            den = a + b - 3
            if den > 0 and 39 % den == 0:
                q = 39 // den
                if q > 3 and q in primes_through(q):
                    possible.add(q)
    return tuple(sorted(possible))


def main():
    ps = primes_through(60)
    assert p3_candidates() == (5, 7, 11)
    # n=4*p*q: p>=13 excluded; p=11 needs q<21;
    # for p in {3,5,7}, the algebraic proof forces q<=7*(p+1).
    ranges = {3: 28, 5: 42, 7: 56, 11: 20}
    class_4pq = {}
    checked_4pq = 0
    for p, qmax in ranges.items():
        for q in ps:
            if p < q <= qmax:
                checked_4pq += 1
                n = 4 * p * q
                if pairs(n):
                    class_4pq[n] = pairs(n)
    assert sorted(class_4pq) == [84, 132, 156, 220, 364, 380]

    # n=2*p^2*q: the remaining p are 3 and 5;
    # p=3 has exactly the algebraically permitted prime q values above.
    class_2p2q = {}
    checked_2p2q = 0
    for p, qs in ((3, p3_candidates()), (5, (7, 11, 13))):
        for q in qs:
            checked_2p2q += 1
            n = 2 * p * p * q
            if pairs(n):
                class_2p2q[n] = pairs(n)
    assert sorted(class_2p2q) == [90, 126, 198, 550]

    # n=2*p*q^2: only (p,q)=(3,5),(3,7),(3,11),(5,7)
    # survive the infinite inequalities, and none has an omitted pair.
    checked_2pq2 = 0
    for p, q in ((3, 5), (3, 7), (3, 11), (5, 7)):
        checked_2pq2 += 1
        assert not pairs(2 * p * q * q), (p, q)

    actual = {**class_4pq, **class_2p2q}
    assert set(actual) == set(EXPECTED)
    for n, pair in EXPECTED.items():
        assert actual[n] == (pair,), (n, actual[n], pair)
        assert sum(divisors(n)) - 2 * n == sum(pair)
        assert all(n % d == 0 for d in pair)
        assert pair[0] < pair[1] < n
    # The maximizing odd three-prime-support factorisation has 3^2,5,7.
    assert 13 * 6 * 8 < 2 * 9 * 5 * 7
    print(
        'VERIFY_OK unique_examples=%d finite_4pq=%d finite_2p2q=%d '
        'finite_2pq2=%d p3_candidate_q=%s sum_odd_bound=624/315'
        % (len(EXPECTED), checked_4pq, checked_2p2q,
           checked_2pq2, p3_candidates())
    )


if __name__ == '__main__':
    main()
