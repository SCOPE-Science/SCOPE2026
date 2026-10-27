#!/usr/bin/env python3
"""Exact finite cross-checks for the Moser–de Bruijn dilation-three theorem.

The infinite claims are proved by the digit-state induction in RESULT.md.
"""
from collections import Counter


def moser_at(i):
    out = 0
    place = 1
    while i:
        out += (i & 1) * place
        i >>= 1
        place *= 4
    return out


def multiplicity(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    q, r = divmod(n, 4)
    if r == 0:
        return multiplicity(q) + multiplicity(q - 1)
    if r == 2:
        return 0
    return multiplicity(q)


def digit_transition(pair, digit):
    a, b = pair
    return ((a, a + b), (a + b, b), (b, 0), (a, 0))[digit]


def expected_size(k):
    u, v = 1, 3
    if k == 0:
        return u
    if k == 1:
        return v
    for _ in range(2, k + 1):
        u, v = v, 4 * v - 2 * u
    return v


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def check():
    # Digit-by-digit carry transitions are enumerated from the four pairs.
    for carry in (0, 1):
        for digit in range(4):
            counts = Counter()
            for x in (0, 1):
                for y in (0, 1):
                    raw = x + 3*y + carry
                    if raw % 4 == digit:
                        counts[raw // 4] += 1
            observed = (counts[0], counts[1])
            basis = (1, 0) if carry == 0 else (0, 1)
            assert digit_transition(basis, digit) == observed, (carry, digit)
    # Direct pair enumeration, independent of the valuation recurrence.
    for k in range(8):
        bound = 4 ** k
        digit_set = [moser_at(i) for i in range(2 ** k)]
        direct = [0] * bound
        for a in digit_set:
            for b in digit_set:
                total = a + 3*b
                if total < bound:
                    direct[total] += 1
        assert all(direct[n] == multiplicity(n) for n in range(bound)), k
        support = sum(v > 0 for v in direct)
        unique = sum(v == 1 for v in direct)
        peak = max(direct)
        assert support == expected_size(k), (k, support)
        assert unique == 3 ** k, (k, unique)
        assert peak == fib(k + 1), (k, peak)
        print(f'k={k}: support={support}, unique={unique}, max={peak}: OK')
    # Independent state-vector propagation beyond the direct-pair range.
    states = Counter({(1, 0): 1})
    for k in range(1, 15):
        next_states = Counter()
        for pair, count in states.items():
            for digit in range(4):
                next_states[digit_transition(pair, digit)] += count
        states = next_states
        size = sum(c for (a, b), c in states.items() if a > 0)
        unique = sum(c for (a, b), c in states.items() if a == 1)
        peak = max(a for (a, b) in states)
        assert size == expected_size(k)
        assert unique == 3 ** k
        assert peak == fib(k + 1)
    print('PASS: direct pair enumerations k=0..7 and state-vector checks k=1..14')


if __name__ == '__main__':
    check()
