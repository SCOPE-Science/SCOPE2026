"""Exact finite-ring Rule 90 fixed-sensor observability checks.
Run: python verify.py (Python 3 standard library only)."""
from math import comb, gcd
from itertools import combinations
from random import Random


def gf2_rank(rows):
    pivot = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivot:
                row ^= pivot[p]
            else:
                pivot[p] = row
                break
    return len(pivot)


def rule90_rows(n, sensors, horizon):
    mask = (1 << n) - 1
    rows = []
    for j in sensors:
        state = 1 << j
        for _ in range(horizon):
            rows.append(state)
            left = ((state << 1) & mask) | (state >> (n - 1))
            right = (state >> 1) | ((state & 1) << (n - 1))
            state = left ^ right
    return rows


def predicted_nullity(n, sensors):
    g = n
    for s in sensors[1:]:
        g = gcd(g, s - sensors[0])
    if (n // g) % 2:
        return g // 2
    return g - 1


def mobius(n):
    x = n
    sign = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0:
                return 0
            sign = -sign
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        sign = -sign
    return sign


def expected_count(n, k):
    return sum(mobius(d) * d * comb(n // d, k)
               for d in range(1, n + 1) if n % d == 0 and k <= n // d)


def test():
    checks = 0
    counts = 0
    for n in range(3, 12):
        observed = [0] * (n + 1)
        for mask in range(1, 1 << n):
            sensors = [j for j in range(n) if mask >> j & 1]
            k = len(sensors)
            r = gf2_rank(rule90_rows(n, sensors, n))
            nu = n - r
            expected = predicted_nullity(n, sensors)
            assert nu == expected, ('rank', n, sensors, nu, expected)
            if expected == 0:
                observed[k] += 1
            checks += 1
        for k in range(1, n + 1):
            assert observed[k] == expected_count(n, k), ('count', n, k)
            counts += 1
        for d in range(1, n):
            rr = gf2_rank(rule90_rows(n, [0, d], (n + 1) // 2))
            assert (rr == n) == (gcd(d, n) == 1)
            if gcd(d, n) == 1:
                assert gf2_rank(rule90_rows(n, [0, d], (n + 1) // 2 - 1)) < n
            checks += 1
    rng = Random(20261020)
    random_checks = 0
    for n in [12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 30, 32, 37, 48, 64, 96, 127]:
        for _ in range(80):
            k = rng.randint(1, min(n, 7))
            sensors = sorted(rng.sample(range(n), k))
            nu = n - gf2_rank(rule90_rows(n, sensors, n))
            assert nu == predicted_nullity(n, sensors), ('random', n, sensors, nu)
            random_checks += 1
    assert expected_count(12, 2) == 12 * 4 // 2
    print('VERIFY_OK exhaustive_sensor_sets=%d census_checks=%d pair_horizon_checks=%d random_checks=%d'
          % (checks - sum(range(2, 11)), counts, sum(range(2, 11)), random_checks))

if __name__ == '__main__':
    test()
