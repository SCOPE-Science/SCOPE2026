#!/usr/bin/env python3
"""Independent, reproducible checks for cyclic Rule 184 image and enumeration.

Standard library only. Run: python3 verify.py
This finite test supplements, and does not replace, the all-length proof.
"""
from itertools import product
from math import comb


def local184(a, b, c):
    return (b & c) | (a & (1 - b))


def local226(a, b, c):
    return (a & b) | (c & (1 - b))


def evolve(word, local):
    n = len(word)
    bits = tuple(int(bit) for bit in word)
    return ''.join(str(local(bits[(i - 1) % n], bits[i], bits[(i + 1) % n]))
                   for i in range(n))


def forbidden(word):
    n = len(word)
    return any(''.join(word[(i + j) % n] for j in range(4)) == '1100'
               for i in range(n))


def inclusion_exclusion(n, k):
    total = 0
    for j in range(n // 4 + 1):
        circular_selections = n * comb(n - 3 * j, j) // (n - 3 * j)
        remaining_weight = k - 2 * j
        if 0 <= remaining_weight <= n - 4 * j:
            total += (-1) ** j * circular_selections * comb(n - 4 * j, remaining_weight)
    return total


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def trace_weighted_automaton(n):
    # Coefficient arrays represent polynomial entries in the variable u.
    size = n + 1
    zero = lambda: [0] * size
    one = zero(); one[0] = 1
    u = zero(); u[1] = 1
    e = [[zero() for _ in range(4)] for _ in range(4)]
    e[0][0] = one[:]; e[0][1] = u[:]
    e[1][0] = one[:]; e[1][2] = u[:]
    e[2][2] = u[:]; e[2][3] = one[:]
    e[3][1] = u[:]
    cur = [[zero() for _ in range(4)] for _ in range(4)]
    for i in range(4):
        cur[i][i] = one[:]
    for _ in range(n):
        nxt = [[zero() for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for k in range(4):
                for j in range(4):
                    a, b = cur[i][k], e[k][j]
                    for x in range(n + 1):
                        if not a[x]:
                            continue
                        for y in range(n + 1 - x):
                            if b[y]:
                                nxt[i][j][x + y] += a[x] * b[y]
        cur = nxt
    return [sum(cur[i][i][k] for i in range(4)) for k in range(n + 1)]


def check():
    # The two decisive local truth tables, checked without global enumeration.
    image_blocks = set()
    for s in product((0, 1), repeat=6):
        image_blocks.add(''.join(str(local184(*s[i:i + 3])) for i in range(4)))
    assert image_blocks == ({''.join(map(str, s))
                             for s in product((0, 1), repeat=4)} - {'1100'})

    errors = []
    for a, b, c, d, e in product((0, 1), repeat=5):
        observed = local184(local226(a, b, c), local226(b, c, d),
                            local226(c, d, e))
        if observed != c:
            errors.append(f'{a}{b}{c}{d}{e}')
    assert errors == ['01100', '11000', '11001', '11100'], errors

    # Exhaustive global images, right-inverse tests, and composition counts.
    for n in range(1, 14):
        words = [''.join(w) for w in product('01', repeat=n)]
        images = {evolve(w, local184) for w in words}
        allowed = {w for w in words if not forbidden(w)}
        assert images == allowed, ('image', n)
        for w in words:
            assert (evolve(evolve(w, local226), local184) == w) == (w in allowed), ('inverse', n, w)
        counts = [sum(w.count('1') == k for w in allowed) for k in range(n + 1)]
        predicted = [inclusion_exclusion(n, k) for k in range(n + 1)]
        assert counts == predicted, ('inclusion-exclusion', n)

    # Two independent all-n enumerators agree for additional n beyond brute force.
    totals = []
    for n in range(1, 19):
        weights = [inclusion_exclusion(n, k) for k in range(n + 1)]
        matrix = trace_weighted_automaton(n)
        assert weights == matrix, ('matrix', n, weights, matrix)
        totals.append(sum(weights))
    for i in range(4, len(totals)):
        assert totals[i] == 2 * totals[i - 1] - totals[i - 4]
    assert totals[:16] == [2, 4, 8, 12, 22, 40, 72, 132,
                           242, 444, 816, 1500, 2758, 5072, 9328, 17156]
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
