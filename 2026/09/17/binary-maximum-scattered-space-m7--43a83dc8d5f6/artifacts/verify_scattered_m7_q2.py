#!/usr/bin/env python3
"""Verify a 10-dimensional scattered F_2-subspace of F_128^3.

Field convention: F_128 = F_2[a]/(a^7 + a + 1).
An integer c in [0,127] encodes sum_i bit_i(c) a^i.
"""

MOD = 0b10000011
BASIS = [
    (126, 2, 64),
    (38, 5, 32),
    (36, 12, 16),
    (111, 14, 8),
    (9, 8, 4),
    (46, 3, 2),
    (12, 8, 1),
    (22, 71, 0),
    (7, 36, 0),
    (32, 18, 0),
]

def gf_mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 0x80:
            a ^= MOD
    return r & 0x7f

def pack(t):
    x, y, z = t
    return x | (y << 7) | (z << 14)

def scalar_mul(lam, v):
    x = v & 127
    y = (v >> 7) & 127
    z = (v >> 14) & 127
    return pack((gf_mul(lam, x), gf_mul(lam, y), gf_mul(lam, z)))

def binary_rank(rows):
    piv = {}
    for x in rows:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in piv:
                y ^= piv[p]
            else:
                piv[p] = y
                break
    return len(piv)

seen = set()
x = 1
for _ in range(127):
    seen.add(x)
    x = gf_mul(x, 2)
assert x == 1
assert len(seen) == 127

B = [pack(t) for t in BASIS]
assert binary_rank(B) == 10

concat_ranks = {}
for lam in range(2, 128):
    lamB = [scalar_mul(lam, v) for v in B]
    r = binary_rank(B + lamB)
    concat_ranks[lam] = r
    assert r == 20

inv = [0] * 128
for a in range(1, 128):
    for b in range(1, 128):
        if gf_mul(a, b) == 1:
            inv[a] = b
            break

def normalized_projective(v):
    x = v & 127
    y = (v >> 7) & 127
    z = (v >> 14) & 127
    if x:
        s = inv[x]
        return (1, gf_mul(s, y), gf_mul(s, z))
    if y:
        s = inv[y]
        return (0, 1, gf_mul(s, z))
    return (0, 0, 1)

vectors = [0]
for b in B:
    vectors += [v ^ b for v in vectors]
nonzero = vectors[1:]
points = {normalized_projective(v) for v in nonzero}
assert len(nonzero) == 1023
assert len(points) == 1023

print("field_nonzero_elements=127")
print("basis_rank_F2=10")
print("lambda_tests=126")
print("min_concat_rank_F2=%d" % min(concat_ranks.values()))
print("nonzero_vectors=1023")
print("distinct_projective_points=1023")
print("scattered=True")
