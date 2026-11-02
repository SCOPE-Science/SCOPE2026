#!/usr/bin/env python3
"""Independent exact-arithmetic checks for a binary valuation law of Narayana numbers."""
from fractions import Fraction
from collections import Counter

C = ((0, 1, 0), (0, 0, 1), (1, 0, 1))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

def matmul(a, b, modulus=None):
    result = tuple(tuple(sum(a[i][h] * b[h][j] for h in range(3)) for j in range(3)) for i in range(3))
    if modulus is not None:
        return tuple(tuple(x % modulus for x in row) for row in result)
    return result

def matpow(a, exponent, modulus=None):
    ans = I
    while exponent:
        if exponent & 1:
            ans = matmul(ans, a, modulus)
        a = matmul(a, a, modulus)
        exponent >>= 1
    return ans

def value_mod(index, bits):
    modulus = 1 << bits
    p = matpow(C, index, modulus)
    return (p[0][1] + p[0][2]) % modulus

def ord2(x):
    assert x > 0
    return (x & -x).bit_length() - 1

def leading_h(m, bits):
    assert m & 1
    modulus = 1 << bits
    val = value_mod(28 * m, bits + 5)
    assert val % 32 == 0
    return ((val // 32) * pow(m, -1, modulus)) % modulus

B = matpow(C, 28)
E = tuple(tuple((B[i][j] - I[i][j]) // 8 for j in range(3)) for i in range(3))
assert B == ((8641, 5896, 12664), (12664, 8641, 18560), (18560, 12664, 27201))
assert E == ((1080, 737, 1583), (1583, 1080, 2320), (2320, 1583, 3400))
assert 18560 == value_mod(28, 64)
assert 825604416 == value_mod(56, 64)
assert (825604416 - 2 * 18560) // 64 == 12899489

# Lift the unique odd 2-adic root using independent binary matrix powers.
root = 1
for k in range(2, 23):
    root += ((leading_h(root, k) >> (k - 1)) & 1) << (k - 1)
    assert leading_h(root, k) == 0
assert root == 698045

r0 = {1, 2, 3, 5, 8, 9, 10, 12, 15, 16, 17, 19, 22, 23, 24, 26}
r1 = {4, 7, 18, 21}
r2 = {6, 11, 13}
rthree = {20, 25, 27}
assert len(r0 | r1 | r2 | rthree | {0, 14}) == 28
assert len(r0) + len(r1) + len(r2) + len(rthree) + 2 == 28

# Reconstruct coefficients via the original recurrence, independently of C^n.
limit = 200000
modulus = 1 << 32
seq = [0, 1, 1]
for n in range(3, limit + 1):
    seq.append((seq[n - 1] + seq[n - 3]) % modulus)

counts = Counter()
for n in range(1, limit + 1):
    m, r = divmod(n, 28)
    if r in r0:
        predicted = 0
    elif r in r1:
        predicted = 1
    elif r in r2:
        predicted = 2
    elif r == 14:
        predicted = 3
    elif r in rthree:
        predicted = 3 + ord2(m + 1)
    else:
        assert m >= 1
        diff = (m - root) % (1 << 22)
        assert diff != 0, "Increase root precision for a larger check range"
        predicted = 5 + ord2(m) + ord2(diff)
    actual = ord2(seq[n]) if seq[n] else 32
    assert actual == predicted, (n, actual, predicted)
    counts[actual] += 1


def density(t):
    if t == 0: return Fraction(4, 7)
    if t == 1: return Fraction(1, 7)
    if t == 2: return Fraction(3, 28)
    if t == 3: return Fraction(5, 56)
    if t in (4, 5): return Fraction(3, 28 * (1 << (t - 2)))
    return Fraction(11, 28 * (1 << (t - 2)))

# Every individual finite count differs from its limiting prediction by <=16.
for t in range(0, 28):
    assert abs(Fraction(counts[t], 1) - density(t) * limit) <= 16
assert sum(counts.values()) == limit
assert sum((density(t) for t in range(0, 64)), Fraction(0)) < 1
assert sum((density(t) for t in range(0, 64)), Fraction(0)) > Fraction(999, 1000)
print("VERIFY_OK", "terms=200000", "root_mod_2^22=698045", "residues=28", "density_levels=28")
