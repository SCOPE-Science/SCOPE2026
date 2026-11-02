#!/usr/bin/env python3
"""Exact integer verification of the seven-carry-state Thue--Morse identity.

This is a finite certificate for the matrix identity used in the proof, plus
independent direct sample sums.  It is not a substitute for the derivation of
the carry transfer rule in the accompanying mathematical argument.
"""

from itertools import product

STATES = ((0, 0), (1, 2), (0, 1), (2, 3), (1, 3), (1, 1), (2, 4))
N = len(STATES)
INDEX = {pair: i for i, pair in enumerate(STATES)}


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(N)) for j in range(N)]
            for i in range(N)]


def eye():
    return [[int(i == j) for j in range(N)] for i in range(N)]


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(N)) for i in range(N)]


def bitparity(n):
    return -1 if n.bit_count() % 2 else 1


def build_transfer():
    m = [[0] * N for _ in range(N)]
    for i, (carry3, carry5) in enumerate(STATES):
        for bit in (0, 1):
            a, b = 3 * bit + carry3, 5 * bit + carry5
            destination = (a // 2, b // 2)
            assert destination in INDEX
            sign = -1 if ((bit + (a % 2) + (b % 2)) % 2) else 1
            m[i][INDEX[destination]] += sign
    return m


def main():
    m = build_transfer()
    wanted = [
        [1, -1, 0, 0, 0, 0, 0],
        [0, 0, -1, 1, 0, 0, 0],
        [-1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, -1, 1],
        [0, 0, 1, 0, 0, 0, -1],
        [1, 0, 0, -1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, -1],
    ]
    assert m == wanted
    m2 = matmul(m, m)
    delta = [[m2[i][j] - int(i == j) for j in range(N)] for i in range(N)]
    d3 = matmul(matmul(delta, delta), delta)
    annihilator = matmul(m, d3)
    assert all(x == 0 for row in annihilator for x in row)
    w = [bitparity(c3) * bitparity(c5) for c3, c5 in STATES]
    assert w == [1, 1, -1, -1, -1, 1, 1]
    u = w[:]
    initial = []
    for r in range(20):
        expected = 1 if r == 0 else -2 * ((r - 1) // 2)
        assert u[0] == expected, (r, u[0], expected)
        if r < 7:
            initial.append(u[0])
        u = matvec(m, u)
    assert initial == [1, 0, 0, -2, -2, -4, -4]

    entries_checked = 0
    for r in range(16):
        direct = sum(bitparity(n) * bitparity(3 * n) * bitparity(5 * n)
                     for n in range(1 << r))
        assert direct == (1 if r == 0 else -2 * ((r - 1) // 2))
        entries_checked += 1 << r
    # Explicitly checks all source states and both possible binary input bits.
    assert all(((3 * bit + c3) // 2, (5 * bit + c5) // 2) in INDEX
               for c3, c5 in STATES for bit in (0, 1))
    print("PASS: 7 states, 14 transition branches, 7x7 annihilator,"
          " 20 transfer evaluations,", entries_checked, "direct summands")


if __name__ == "__main__":
    main()
