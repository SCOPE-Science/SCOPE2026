#!/usr/bin/env python3
"""Direct finite checks for parity dynamics on cycle-corona graphs.

The general all-size result is proved mathematically in RESULT.md.
This program corroborates ranks, periods and orbit populations for stated ranges.
"""
from collections import Counter
from math import gcd
from itertools import product


def step_bits(n, state):
    mask = (1 << n) - 1
    x = state & mask
    y = state >> n
    left = ((x << 1) | (x >> (n - 1))) & mask
    right = (x >> 1) | ((x & 1) << (n - 1))
    return (left ^ right ^ y) | (x << n)


def adjacency_rows(n):
    rows = []
    for i in range(n):
        rows.append((1 << ((i - 1) % n)) ^ (1 << ((i + 1) % n)) ^ (1 << (n + i)))
    for i in range(n):
        rows.append(1 << i)
    return rows


def matrix_multiply_rows(A, B):
    out = []
    for row in A:
        accum = 0
        while row:
            low = row & -row
            row -= low
            accum ^= B[low.bit_length() - 1]
        out.append(accum)
    return out


def rank_binary(rows):
    basis = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in basis:
                row ^= basis[p]
            else:
                basis[p] = row
                break
    return len(basis)


def mu(z):
    p = 2
    sign = 1
    while p * p <= z:
        if z % p == 0:
            z //= p
            if z % p == 0:
                return 0
            sign = -sign
        p += 1
    return -sign if z > 1 else sign


def expected_dim(n, t):
    return 2 * gcd(n, t) - int(n % 2 == 1 and t % 2 == 1)


def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def expected_primitive(n, t):
    L = n if n % 2 == 0 else 2 * n
    if L % t:
        return 0
    return sum(mu(t // d) * (1 << expected_dim(n, d)) for d in divisors(t))


def polynomial_mod(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_mod(a, b)
    return a


def polynomial_quotient(a, b):
    q = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length() - b.bit_length()
        q ^= 1 << shift
        a ^= b << shift
    assert a == 0
    return q


def exact_cycle_count(n):
    states = 1 << (2 * n)
    seen = bytearray(states)
    counts = Counter()
    periods = bytearray(states)
    for start in range(states):
        if seen[start]:
            continue
        cur = start
        cycle = []
        length = 0
        while not seen[cur]:
            seen[cur] = 1
            cycle.append(cur)
            length += 1
            cur = step_bits(n, cur)
        assert cur == start, (n, start, cur)
        counts[length] += 1
        for z in cycle:
            periods[z] = length
    assert sum(length * count for length, count in counts.items()) == states
    return counts, periods


def main():
    rank_cases = 0
    symmetry_cases = 0
    for n in range(3, 49):
        A = adjacency_rows(n)
        size = 2 * n
        I = [1 << i for i in range(size)]
        power = I
        first_identity = None
        for t in range(1, 2 * n + 1):
            power = matrix_multiply_rows(power, A)
            if power == I and first_identity is None:
                first_identity = t
            rank = rank_binary([row ^ (1 << i) for i, row in enumerate(power)])
            assert size - rank == expected_dim(n, t), (n, t, size-rank, expected_dim(n, t))
            rank_cases += 1
        assert first_identity == (n if n % 2 == 0 else 2 * n), (n, first_identity)
        symmetry_cases += 1
    print('RANK_CASES', rank_cases, 'ORDER_CASES', symmetry_cases)

    poly_cases = 0
    for n in range(3, 41):
        modulus = (1 << n) | 1
        for t in range(1, 81):
            S_t = (1 << t) | 1
            if t % 2:
                a = polynomial_quotient(S_t, 3)
                b = polynomial_multiply(S_t, 3)
            else:
                a = b = S_t
            fixed = polynomial_gcd(modulus, a).bit_length() - 1
            fixed += polynomial_gcd(modulus, b).bit_length() - 1
            assert fixed == expected_dim(n, t), (n, t, fixed, expected_dim(n, t))
            poly_cases += 1
    print('POLYNOMIAL_GCD_CASES', poly_cases)

    orbit_cases = 0
    orbit_states = 0
    for n in range(3, 10):
        counts, periods = exact_cycle_count(n)
        if n % 2:
            bits = (1 << n) - 1
            both = bits | (bits << n)
            for state in range(1 << (2 * n)):
                parity = state.bit_count() % 2
                assert periods[state] % 2 == 1 - parity, (n, state)
                toggled = state ^ bits
                assert periods[toggled] == (2 * periods[state] if parity == 0 else periods[state] // 2), (n, state)
                if state % 97 == 0:
                    run = state
                    for _ in range(n):
                        run = step_bits(n, run)
                    assert run == (state ^ (both if parity else 0)), (n, state)
        l = n if n % 2 == 0 else 2 * n
        for t in divisors(l):
            actual = t * counts[t]
            expected = expected_primitive(n, t)
            assert actual == expected, (n, t, actual, expected)
            orbit_cases += 1
        assert all(l % t == 0 for t in counts)
        orbit_states += 1 << (2 * n)
        print('EXHAUSTIVE', n, 'states', 1 << (2*n), 'period_cycles', dict(sorted(counts.items())))
    print('EXHAUSTIVE_STATES', orbit_states, 'PERIOD_CLASS_CASES', orbit_cases)
    print('SUNLET_PARITY_VERIFY_OK')


def polynomial_multiply(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out

if __name__ == '__main__':
    main()
