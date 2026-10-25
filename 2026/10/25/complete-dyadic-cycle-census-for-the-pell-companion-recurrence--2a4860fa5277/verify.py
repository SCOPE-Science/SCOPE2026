#!/usr/bin/env python3
"""Reproduce exact finite Pell recurrence period and cycle checks, Python stdlib."""
from collections import Counter


def nu2(n):
    if n == 0:
        return 10**9
    n = abs(n)
    return (n & -n).bit_length() - 1


def theorem_period(a, b, k):
    norm = (a + b)**2 - 2*b*b
    h = 2*k - min(2*k, nu2(norm))
    if h <= 1:
        return 1
    if h == 2:
        return 2
    if h <= 5:
        return 4
    return 1 << (h // 2)


def predicted_cycle_counts(k):
    c = Counter({1:2, 2:1})
    if k == 2:
        c[4] = 3
    if k >= 3:
        c[4] = 7
    for t in range(3, k + 1):
        c[1 << t] = (1 << (t-1)) * (1 if k == t else 3)
    return c


def check_one_modulus(k):
    modulus = 1 << k
    seen = bytearray(modulus * modulus)
    cycles = Counter()
    for a in range(modulus):
        for b in range(modulus):
            if seen[a * modulus + b]:
                continue
            x, y = a, b
            orbit = []
            while not seen[x * modulus + y]:
                seen[x * modulus + y] = 1
                orbit.append((x, y))
                x, y = y, (x + 2*y) % modulus
            assert (x, y) == (a, b), (k, a, b)
            period = len(orbit)
            cycles[period] += 1
            for u, v in orbit:
                assert theorem_period(u, v, k) == period, (k, u, v)
    assert cycles == predicted_cycle_counts(k), (k, cycles)
    assert sum(t * count for t, count in cycles.items()) == modulus**2
    if k == 1:
        assert sum(cycles.values()) == 3
    else:
        assert sum(cycles.values()) == (1 << (k+1)) - 2


def main():
    for k in range(1, 9):
        check_one_modulus(k)
    print('VERIFY_OK: 87380 independent orbit traces; all eight exact cycle spectra and norm-valuation periods')


if __name__ == '__main__':
    main()
