#!/usr/bin/env python3
"""Standalone finite checks for binary neighbor-parity dynamics on sunlet graphs.

Python 3 standard library only; use `python3 verify.py`.
"""
from math import gcd


def adjacency_rows(n):
    """Bit-row representation, cycle vertices 0..n-1 and pendant vertices n..2n-1."""
    rows = [0] * (2 * n)
    for i in range(n):
        rows[i] = (1 << ((i - 1) % n)) | (1 << ((i + 1) % n)) | (1 << (n + i))
        rows[n + i] = 1 << i
    return rows


def compose_rows(left, right):
    """Matrix product over F2, row representation."""
    out = []
    for mask in left:
        r = 0
        while mask:
            bit = mask & -mask
            j = bit.bit_length() - 1
            r ^= right[j]
            mask ^= bit
        out.append(r)
    return out


def matrix_power(rows, exponent):
    dimension = len(rows)
    identity = [1 << j for j in range(dimension)]
    out = identity
    base = rows[:]
    while exponent:
        if exponent & 1:
            out = compose_rows(out, base)
        exponent >>= 1
        if exponent:
            base = compose_rows(base, base)
    return out


def matrix_rank(rows):
    pivots = {}
    for raw in rows:
        v = raw
        while v:
            leading = v.bit_length() - 1
            if leading in pivots:
                v ^= pivots[leading]
            else:
                pivots[leading] = v
                break
    return len(pivots)


def apply(rows, config):
    return sum(((config & r).bit_count() & 1) << j for j, r in enumerate(rows))


def fixed_dimension(n, t):
    return 2 * gcd(n, t) - int(n % 2 == 1 and t % 2 == 1)


def mobius(k):
    m = k
    parity = 0
    d = 2
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            parity ^= 1
        d += 1
    if m > 1:
        parity ^= 1
    return -1 if parity else 1


def divisors(k):
    return [d for d in range(1, k + 1) if k % d == 0]


def primitive_orbits(n, k):
    numerator = sum(mobius(k // d) * (1 << fixed_dimension(n, d)) for d in divisors(k))
    assert numerator % k == 0, (n, k, numerator)
    return numerator // k


def main():
    rank_cases = 0
    exhaustive_states = 0
    census_cases = 0
    for n in range(3, 33):
        F = adjacency_rows(n)
        period = n if n % 2 == 0 else 2 * n
        for t in range(1, 2 * n + 6):
            rows = matrix_power(F, t)
            identity_adjusted = [row ^ (1 << j) for j, row in enumerate(rows)]
            got = 2 * n - matrix_rank(identity_adjusted)
            expected = fixed_dimension(n, t)
            assert got == expected, ('rank', n, t, got, expected)
            rank_cases += 1
        assert matrix_power(F, period) == [1 << j for j in range(2 * n)]
        assert all(matrix_power(F, d) != [1 << j for j in range(2 * n)]
                   for d in divisors(period) if d < period)
        if n <= 7:
            seen = set()
            actual_cycles = {}
            for state in range(1 << (2 * n)):
                if state in seen:
                    continue
                orbit = []
                s = state
                while s not in seen:
                    seen.add(s)
                    orbit.append(s)
                    s = apply(F, s)
                assert s == state, ('nonperiodic', n, state, s)
                actual_cycles[len(orbit)] = actual_cycles.get(len(orbit), 0) + 1
                exhaustive_states += len(orbit)
            assert sum(k * v for k, v in actual_cycles.items()) == 1 << (2 * n)
            for k in divisors(period):
                predicted = primitive_orbits(n, k)
                assert actual_cycles.get(k, 0) == predicted, (
                    'orbit count', n, k, actual_cycles.get(k, 0), predicted)
                census_cases += 1
        for k in divisors(period):
            assert primitive_orbits(n, k) >= 0
    print('SUNLET_PARITY_CENSUS_VERIFIED')
    print('matrix_rank_cases:', rank_cases)
    print('individually_enumerated_states:', exhaustive_states)
    print('direct_orbit_census_cases:', census_cases)
    print('fixed_counts_n3:', [(k, 1 << fixed_dimension(3, k)) for k in [1,2,3,6]])
    print('fixed_counts_n4:', [(k, 1 << fixed_dimension(4, k)) for k in [1,2,4]])
    print('primitive_counts_n3:', [(k, primitive_orbits(3,k)) for k in [1,2,3,6]])
    print('primitive_counts_n4:', [(k, primitive_orbits(4,k)) for k in [1,2,4]])

if __name__ == '__main__':
    main()
