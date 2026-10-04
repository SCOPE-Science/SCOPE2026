#!/usr/bin/env python3
"""Finite sanity checks for the two covering-radius-three BCH families."""
from collections import Counter, deque

MOD = 0x11D  # x^8+x^4+x^3+x^2+1

def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 0x100:
            a ^= MOD
    return out & 0xFF

def power(a, e):
    out = 1
    while e:
        if e & 1:
            out = mul(out, a)
        a = mul(a, a)
        e >>= 1
    return out

def order(a):
    x = 1
    for k in range(1, 256):
        x = mul(x, a)
        if x == 1:
            return k
    raise AssertionError("order not found")

def gf2_rank(vectors, bits=9):
    basis = [0] * bits
    rank = 0
    for v in vectors:
        x = v
        while x:
            b = x.bit_length() - 1
            if basis[b]:
                x ^= basis[b]
            else:
                basis[b] = x
                rank += 1
                break
    return rank

def syndrome_distribution(subgroup_order, exponent):
    alpha = 2
    beta = power(alpha, exponent)
    assert order(alpha) == 255
    assert order(beta) == subgroup_order
    field_columns = [power(beta, i) for i in range(subgroup_order)]
    assert len(set(field_columns)) == subgroup_order
    # A column is (field-coordinate vector, parity bit 1).
    cols = [(1 << 8) | x for x in field_columns] + [1 << 8]
    assert len(set(cols)) == subgroup_order + 1
    assert gf2_rank(cols) == 9
    dist = [-1] * 512
    dist[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        for c in cols:
            y = x ^ c
            if dist[y] < 0:
                dist[y] = dist[x] + 1
                q.append(y)
    assert -1 not in dist
    return Counter(dist)

def check_formulas():
    for s in range(2, 15):
        n = (2 ** (2 * s) + 1) * (2 ** s - 1)
        N = n + 1
        r = 4 * s
        assert N == 2 ** (3 * s) - 2 ** (2 * s) + 2 ** s
        assert N < 2 ** r
        counts = (1, N, 2 ** r - 1, 2 ** r - N)
        assert all(x > 0 for x in counts)
        assert sum(counts) == 2 ** (r + 1)
    for s in range(4, 15):
        n = (2 ** (2 * s) - 1) // 3
        N = n + 1
        r = 2 * s
        assert N == (2 ** (2 * s) + 2) // 3
        assert N < 2 ** r
        counts = (1, N, 2 ** r - 1, 2 ** r - N)
        assert all(x > 0 for x in counts)
        assert sum(counts) == 2 ** (r + 1)

def main():
    check_formulas()
    a = syndrome_distribution(51, 5)
    b = syndrome_distribution(85, 3)
    assert a == Counter({0: 1, 1: 52, 2: 255, 3: 204}), a
    assert b == Counter({0: 1, 1: 86, 2: 255, 3: 170}), b
    print("family_A_s2", dict(sorted(a.items())))
    print("family_B_s4", dict(sorted(b.items())))
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
