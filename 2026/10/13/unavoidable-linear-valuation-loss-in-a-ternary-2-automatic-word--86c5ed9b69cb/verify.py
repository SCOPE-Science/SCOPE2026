#!/usr/bin/env python3
"""Finite reproducibility checks for a ternary logarithmic-block word."""
from itertools import product
from math import gcd

MAX_LENGTH = 48
PREFIX_LENGTH = 1 << 13


def digit_word(n):
    return (n.bit_length() - 1) % 3 if n else 0


def four_state_automaton(n):
    state = -1
    for c in bin(n)[2:]:
        if state == -1:
            if c == '1':
                state = 0
        else:
            state = (state + 1) % 3
    return 0 if state == -1 else state


def stats(prefix, n):
    parikh = set()
    factors = set()
    count = [0, 0, 0]
    for z in prefix[:n]:
        count[z] += 1
    parikh.add(tuple(count))
    factors.add(bytes(prefix[:n]))
    for i in range(n, len(prefix)):
        count[prefix[i - n]] -= 1
        count[prefix[i]] += 1
        parikh.add(tuple(count))
        factors.add(bytes(prefix[i - n + 1:i + 1]))
    return parikh, len(factors)


def check():
    for n in range(1 << 16):
        assert digit_word(n) == four_state_automaton(n)
    prefix = [digit_word(i) for i in range(PREFIX_LENGTH)]
    tested_valuations = list(product(range(-3, 4), repeat=3))
    lengths = 0
    valuation_length_checks = 0
    for n in range(1, MAX_LENGTH + 1):
        ps, factor_count = stats(prefix, n)
        assert factor_count <= 5 * n + 2
        edges = set()
        for a, b in ((0, 1), (1, 2), (2, 0)):
            for t in range(n + 1):
                counts = [0, 0, 0]
                counts[a] = n - t
                counts[b] = t
                edges.add(tuple(counts))
        assert len(edges) == 3 * n
        assert edges <= ps
        identity_sums = {counts[1] + 2 * counts[2] for counts in ps}
        assert identity_sums == set(range(2 * n + 1))
        for v in tested_valuations:
            sums = {sum(v[a] * c[a] for a in range(3)) for c in ps}
            deficit = len(ps) - len(sums)
            if len(set(v)) == 3:
                a, b, c = sorted(range(3), key=lambda i: v[i])
                alpha = v[b] - v[a]
                beta = v[c] - v[a]
                g = gcd(alpha, beta)
                expected = n * g // beta
                assert deficit >= expected, (v, n, deficit, expected)
                if expected:
                    for t in range(1, expected + 1):
                        j = beta // g * t
                        i = alpha // g * t
                        pa = [0, 0, 0]
                        pc = [0, 0, 0]
                        pa[a], pa[b] = n - j, j
                        pc[a], pc[c] = n - i, i
                        assert tuple(pa) in ps and tuple(pc) in ps
                        assert sum(pa[z] * v[z] for z in range(3)) == sum(pc[z] * v[z] for z in range(3))
            elif n == 1:
                assert deficit >= 1
            valuation_length_checks += 1
        lengths += 1
    print('VERIFY_OK',
          'automaton_terms=65536',
          f'factor_lengths={lengths}',
          f'valuations={len(tested_valuations)}',
          f'valuation_length_checks={valuation_length_checks}',
          'all_three_triangle_edges=True',
          'exact_identity_sum_spectrum=True')


if __name__ == '__main__':
    check()
