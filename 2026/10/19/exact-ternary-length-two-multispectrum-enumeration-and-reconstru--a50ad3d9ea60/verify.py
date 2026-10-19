#!/usr/bin/env python3
"""Independent exhaustive verification of a rational three-letter bigram profile count."""
from itertools import product
from math import comb

NUM = (1, 5, -8, 8, 13, -4, -10, -8, 11, 2, -5, 2)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return c


def generating_coefficients(length):
    den = [1]
    for _ in range(7):
        den = mul(den, [1, -1])
    for _ in range(2):
        den = mul(den, [1, 1])
    den = mul(den, [1, 1, 1])
    values = []
    for m in range(length):
        value = (NUM[m] if m < len(NUM) else 0)
        value -= sum(den[j] * values[m - j]
                     for j in range(1, min(m, len(den) - 1) + 1))
        assert value > 0
        values.append(value)
    return values


def word_profiles(n):
    unique = set()
    for w in product((0, 1, 2), repeat=n):
        b = [0] * 9
        for i in range(n - 1):
            b[w[i] * 3 + w[i + 1]] += 1
        unique.add(tuple(b))
    return len(unique)


def compositions(k, r):
    if r == 1:
        yield (k,)
        return
    for v in range(k + 1):
        for tail in compositions(k - v, r - 1):
            yield (v,) + tail


def feasible_matrix(b):
    if not any(b):
        return True
    outgoing = [sum(b[3*i:3*i+3]) for i in range(3)]
    incoming = [sum(b[3*j+i] for j in range(3)) for i in range(3)]
    delta = sorted(outgoing[i] - incoming[i] for i in range(3))
    if delta not in ([0, 0, 0], [-1, 0, 1]):
        return False
    support = {i for i in range(3) if outgoing[i] + incoming[i]}
    seen = {next(iter(support))}
    stack = list(seen)
    while stack:
        v = stack.pop()
        for u in range(3):
            if u not in seen and b[3*v+u] + b[3*u+v]:
                seen.add(u)
                stack.append(u)
    return seen == support


def matrix_profiles(m):
    return sum(feasible_matrix(mat) for mat in compositions(m, 9))


def main():
    coeff = generating_coefficients(18)
    assert coeff[:11] == [1, 9, 24, 65, 156, 342, 683, 1272, 2226, 3708, 5919]
    for n in range(1, 12):
        observed = word_profiles(n)
        assert observed == coeff[n - 1], (n, observed, coeff[n - 1])
    for m in range(13):
        observed = matrix_profiles(m)
        assert observed == coeff[m], (m, observed, coeff[m])
    print("TERNARY_BIGRAM_EXHAUSTIVE_PASS word_lengths=1..11 matrix_edge_totals=0..12 next_coefficients", coeff[13:17])


if __name__ == '__main__':
    main()
