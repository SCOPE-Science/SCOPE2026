#!/usr/bin/env python3
"""Exact finite checks of sl2 character and nilpotent Kronecker sum identities."""
from collections import Counter
from fractions import Fraction
from math import pi, sqrt


def character(blocks):
    out = Counter()
    for m in blocks:
        for j in range(m):
            out[m - 1 - 2 * j] += 1
    return out


def multiply(a, b):
    out = Counter()
    for k, v in a.items():
        for j, w in b.items():
            out[k + j] += v * w
    return out


def character_tau(blocks, r):
    q = Counter({0: 1})
    p = character(blocks)
    for _ in range(r):
        q = multiply(q, p)
    return q[0] + q[1]


def direct_kernel_dimension(blocks, r):
    """Exact rational rank of diagonal Jordan raising map in a tensor basis."""
    mu = sum(blocks)
    predecessors = [None] * mu
    offset = 0
    for m in blocks:
        for a in range(1, m):
            predecessors[offset + a] = offset + a - 1
        offset += m
    size = mu ** r
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for col in range(size):
        coords = []
        x = col
        for _ in range(r):
            coords.append(x % mu)
            x //= mu
        for pos, coord in enumerate(coords):
            below = predecessors[coord]
            if below is not None:
                target = col + (below - coord) * mu ** pos
                matrix[target][col] += 1
    rank = 0
    for col in range(size):
        pivot = next((i for i in range(rank, size) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        v = matrix[rank][col]
        for k in range(col, size):
            matrix[rank][k] /= v
        for i in range(rank + 1, size):
            if matrix[i][col]:
                m = matrix[i][col]
                for k in range(col, size):
                    matrix[i][k] -= m * matrix[rank][k]
        rank += 1
        if rank == size:
            break
    return size - rank


def main():
    families = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    checks = 0
    for blocks in families:
        mu = sum(blocks)
        p = character(blocks)
        assert sum(p.values()) == mu
        assert sum(k * v for k, v in p.items()) == 0
        sig2_num = sum(k*k*v for k, v in p.items())
        assert sig2_num == sum(m * (m*m - 1) // 3 for m in blocks)
        for r in (1, 2, 3):
            if mu ** r > 64:
                continue
            assert direct_kernel_dimension(blocks, r) == character_tau(blocks, r), (blocks, r)
            checks += 1
    for blocks in ((2,), (3,), (1,2), (1,3), (2,3)):
        mu = sum(blocks)
        sig2 = Fraction(sum(m * (m*m - 1) // 3 for m in blocks), mu)
        r = 100
        ratio = (character_tau(blocks, r) / mu**r) / sqrt(2 / (pi * float(sig2) * r))
        assert 0.97 < ratio < 1.03, (blocks, ratio)
    assert checks >= 17
    print("VERIFY_OK", checks)

if __name__ == '__main__':
    main()
