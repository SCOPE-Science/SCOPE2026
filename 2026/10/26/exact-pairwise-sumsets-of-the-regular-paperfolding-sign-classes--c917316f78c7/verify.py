#!/usr/bin/env python3
"""Reproducible integer checks for paperfolding sign-class sumsets.

The universal assertion is proved in RESULT.md by induction; these calculations
are independent bounded checks of the digit recurrence, proposed exceptions,
and constructive representation formulas.
"""

def in_a(n):
    assert n >= 0
    v = n + 1
    return ((v // (v & -v)) % 4) == 1


def in_b(n):
    return not in_a(n)


def exceptional_bb(n):
    return n in (1, 3, 5, 9) or ((n + 2) & (n + 1)) == 0


def witness_aa(n):
    r = n % 4
    if r == 0:
        return n, 0
    if r == 1:
        return n - 1, 1
    if r == 3:
        return n - 3, 3
    a, b = witness_aa((n - 2) // 2)
    return 2 * a + 1, 2 * b + 1


def witness_ab(n):
    if n in (0, 1, 4):
        raise ValueError('exception')
    r = n % 4
    if r == 2:
        return n - 2, 2
    if r == 3:
        return 1, n - 1
    if r == 1:
        return n - 5, 5
    a, b = witness_ab((n - 2) // 2)
    return 2 * a + 1, 2 * b + 1


def witness_bb(n):
    if exceptional_bb(n):
        raise ValueError('exception')
    r = n % 4
    if r == 0:
        return n - 2, 2
    if r == 3:
        return n - 5, 5
    if r == 1:
        return n - 11, 11
    a, b = witness_bb((n - 2) // 2)
    return 2 * a + 1, 2 * b + 1


def finite_sumset(s1, s2, limit):
    # A direct Boolean convolution using Python arbitrary-precision bitsets.
    mask = (1 << limit) - 1
    base = sum(1 << k for k in s2)
    result = 0
    for a in s1:
        result |= base << a
    return result & mask


def run():
    N = 100000
    for n in range(N):
        if n % 4 == 0:
            assert in_a(n)
        if n % 4 == 2:
            assert in_b(n)
        if n % 2:
            assert in_a(n) == in_a(n // 2)
        aa = witness_aa(n)
        assert aa[0] + aa[1] == n and all(in_a(x) for x in aa)
        if n not in (0, 1, 4):
            ab = witness_ab(n)
            assert ab[0] + ab[1] == n and in_a(ab[0]) and in_b(ab[1])
        if not exceptional_bb(n):
            bb = witness_bb(n)
            assert bb[0] + bb[1] == n and all(in_b(x) for x in bb)
    print('PASS: membership recurrences and constructive witnesses for n < 100000')

    limit = 8192
    a = [x for x in range(limit) if in_a(x)]
    b = [x for x in range(limit) if in_b(x)]
    for s1, s2, predicate, label in (
        (a, a, lambda n: True, 'A+A'),
        (a, b, lambda n: n not in (0, 1, 4), 'A+B'),
        (b, b, lambda n: not exceptional_bb(n), 'B+B'),
    ):
        sums = finite_sumset(s1, s2, limit)
        assert all(bool((sums >> n) & 1) == predicate(n) for n in range(limit))
        print(f'PASS: direct Boolean sumset enumeration for {label}, 0 <= n < {limit}')

    exceptions = [n for n in range(100) if exceptional_bb(n)]
    assert exceptions == [0, 1, 2, 3, 5, 6, 9, 14, 30, 62]
    print('PASS: initial exceptional set and dyadic family')


if __name__ == '__main__':
    run()
