#!/usr/bin/env python3
"""Exact integer tests for maximum nondivisibility runs in Pascal rows.

Only standard-library integer arithmetic is used. This is finite corroboration,
not a proof of the universal statement.
"""
from math import comb
from random import Random


def expected(n, p, alpha):
    r = 0
    m = n + 1
    while m % p == 0:
        m //= p
        r += 1
    return (p ** r) * (m % (p ** alpha))


def brute(n, p, alpha):
    mod = p ** alpha
    best = cur = 0
    row = []
    coeff = 1
    for k in range(n + 1):
        if k:
            coeff = (coeff * (n - k + 1)) // k
        good = coeff % mod != 0
        row.append(good)
        cur = cur + 1 if good else 0
        best = max(best, cur)
    return best, row


def separating_index(k, p, alpha, r):
    q = p ** alpha
    digits = 0
    power = 1
    a, b = k % q, r
    for _ in range(alpha):
        x, y = a % p, b % p
        digits += max(x, y) * power
        power *= p
        a //= p
        b //= p
    return (k // q) * q + digits


def borrow_count(n, k, p):
    c = 0
    debt = 0
    while n or k:
        n_digit = n % p
        k_digit = k % p
        debt = int(k_digit + debt > n_digit)
        c += debt
        n //= p
        k //= p
    assert debt == 0
    return c


def run():
    rows = 0
    windows = 0
    digit_certificates = 0
    rng = Random(712065)
    testcases = [(n, p, a) for p in (2, 3, 5, 7) for a in range(1, 6) for n in range(401)]
    testcases += [(rng.randrange(0, 2000), rng.choice((2, 3, 5, 7)), rng.randrange(1, 6)) for _ in range(300)]
    for n, p, a in testcases:
        bound = expected(n, p, a)
        got, row = brute(n, p, a)
        assert bound == got, (n, p, a, bound, got)
        assert all(row[:bound]) and all(row[-bound:]), (n, p, a)
        # Directly test that no window of one greater length survives.
        if bound < n + 1:
            for k in range(n - bound + 1):
                assert not all(row[k:k + bound + 1]), (n, p, a, k)
                windows += 1
        rows += 1
    for p in (2, 3, 5, 7):
        for a in (1, 2, 3, 4):
            q = p ** a
            for m in range(1, 401):
                if m % p == 0:
                    continue
                r = m % q
                for k in range(max(0, m-r)):
                    z = separating_index(k, p, a, r)
                    assert k <= z <= k+r <= m-1, (m, p, a, k, z)
                    assert borrow_count(m-1, z, p) >= a, (m, p, a, k, z)
                    digit_certificates += 1
    print('VERIFY_OK exact_rows=%d forbidden_windows=%d digit_cover_certificates=%d' % (rows, windows, digit_certificates))


if __name__ == '__main__':
    run()
