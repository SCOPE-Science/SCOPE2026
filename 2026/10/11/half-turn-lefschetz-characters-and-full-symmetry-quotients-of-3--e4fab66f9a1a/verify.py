#!/usr/bin/env python3
"""Exact signed matching-orbit and transfer checks for rectangular grid half-turns.
Uses Python's standard library only.  No finite check replaces the general proof.
"""
from functools import lru_cache

D = (1, 2, 0, 2, 4, -2, 1)
P_ODD = (1, 1, 0, 3, -1)
P_EVEN = (1, 0, -1, 3, 0, 1)
U_ODD = (1, 1, 0, 0, 1, 0, 0, 0)
U_EVEN = (1, 0, 1, 0, 0, -1, 0, -1)


def transfer():
    t = [[0] * 8 for _ in range(8)]
    for a in range(8):
        for b in range(8):
            if a & b:
                continue
            free = 7 ^ (a | b)
            t[a][b] = (-1 if b.bit_count() % 2 else 1) * (
                1 - int((free & 3) == 3) - int((free & 6) == 6)
            )
    return t


def times(row, matrix):
    return tuple(sum(row[i] * matrix[i][j] for i in range(8)) for j in range(8))


def dot(row, column):
    return sum(x * y for x, y in zip(row, column))


def transfer_sequence(column, limit=40):
    row = (1, 0, 0, 0, 0, 0, 0, 0)
    t = transfer()
    result = []
    for _ in range(limit):
        result.append(dot(row, column))
        row = times(row, t)
    return result


def check_rational_identity(column, numerator):
    """The 8-dimensional Cayley-Hamilton step establishes all coefficients."""
    sequence = transfer_sequence(column, 22)
    for index in range(14):
        value = sum(D[k] * sequence[index - k]
                    for k in range(min(index, 6) + 1))
        target = numerator[index] if index < len(numerator) else 0
        assert value == target, (index, value, target)
    # The zero coefficients 6 through 13 ensure all later ones vanish:
    # the coefficient sequence follows an order-at-most-eight recurrence,
    # because it is obtained by applying a polynomial in T to T^m.
    return sequence


def orbit_signed_matching_sum(n):
    """Independent exhaustive signed-orbit enumerator for 180-degree rotation."""
    edges = set()
    for col in range(n):
        for row in range(3):
            v = 3 * col + row
            if row < 2:
                edges.add((v, v + 1))
            if col < n - 1:
                edges.add((v, v + 3))
    def transform(v):
        return 3 * (n - 1 - v // 3) + (2 - v % 3)
    supports = []
    while edges:
        edge = edges.pop()
        reflected = tuple(sorted((transform(edge[0]), transform(edge[1]))))
        edges.discard(reflected)
        orbit = {edge, reflected}
        vertices = [v for pair in orbit for v in pair]
        if len(set(vertices)) != len(vertices):
            continue  # Orbit contains adjacent edges, so cannot be selected.
        support = sum(1 << v for v in vertices)
        supports.append(support)

    @lru_cache(maxsize=None)
    def count(index, used):
        if index == len(supports):
            return 1
        answer = count(index + 1, used)
        if not (supports[index] & used):
            answer -= count(index + 1, used | supports[index])
        return answer
    return count(0, 0), len(supports)


def identity_sum(n):
    return transfer_sequence((1, 0, 0, 0, 0, 0, 0, 0), n + 1)[-1]


def run():
    odd = check_rational_identity(U_ODD, P_ODD)
    even = check_rational_identity(U_EVEN, P_EVEN)
    assert odd[8] == -22, odd[8]
    assert even[8] == 53, even[8]
    checked = 0
    for n in range(2, 18):
        expected = (odd[(n - 1) // 2] if n % 2 else even[n // 2])
        direct, orbit_count = orbit_signed_matching_sum(n)
        assert expected == direct, (n, expected, direct, orbit_count)
        checked += 1
    assert identity_sum(17) == 320
    # The previous reflection characters are obtained independently by
    # one-axis fixed-edge-orbit reductions (not assumed by the orbit test).
    a = [1, 1]
    for _ in range(2, 18):
        a.append(a[-1] - a[-2])
    # n=17: identity = -320, row-reflection = 0,
    # column-reflection = +94, half-turn = +22.
    reduced_quotient_euler = (-identity_sum(17) - a[17]**2
                              + identity_sum(8) - odd[8]) // 4
    assert reduced_quotient_euler == -51
    print('VERIFY_OK', checked, 'independent half-turn orbit counts,')
    print('GF identities via 8-dimensional recurrence, quotient Euler n=17 = -51')


if __name__ == '__main__':
    run()
