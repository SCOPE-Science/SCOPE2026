#!/usr/bin/env python3
from collections import Counter
from math import comb

def poly_deg(p):
    return p.bit_length() - 1

def poly_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out

def poly_divmod(a, b):
    q = 0
    db = poly_deg(b)
    while a and poly_deg(a) >= db:
        shift = poly_deg(a) - db
        q ^= 1 << shift
        a ^= b << shift
    return q, a

def poly(exponents):
    out = 0
    for e in exponents:
        out ^= 1 << e
    return out

def reduce_cyclic_85(p):
    while poly_deg(p) >= 85:
        d = poly_deg(p)
        p ^= 1 << d
        p ^= 1 << (d - 85)
    return p

def cyclic_mul_85(a, b):
    return reduce_cyclic_85(poly_mul(a, b))

def gf2_rank(rows):
    pivots = {}
    rank = 0
    for row in rows:
        x = row
        while x:
            p = poly_deg(x)
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                rank += 1
                break
    return rank

m = 85
h_factors = [
    poly([1, 0]),
    poly([4, 3, 2, 1, 0]),
    poly([8, 6, 5, 4, 2, 1, 0]),
    poly([8, 7, 5, 4, 3, 2, 0]),
]
h = 1
for fac in h_factors:
    h = poly_mul(h, fac)
g, rem = poly_divmod((1 << m) | 1, h)
assert rem == 0
assert poly_deg(h) == 21
assert poly_deg(g) == 64

f2 = poly([13, 9, 8, 7, 6, 5, 3, 1, 0])
tail_patterns = [
    "11001", "01001", "00101", "11101", "11110", "00111", "11100",
    "01010", "10010", "10001", "11111", "01110", "10011", "00110",
]
base2 = cyclic_mul_85(g, f2)
rows = []
for j in range(21):
    block1 = reduce_cyclic_85(g << j)
    block2 = reduce_cyclic_85(base2 << j)
    tail = 0
    for t, pattern in enumerate(tail_patterns):
        if pattern[j % 5] == "1":
            tail |= 1 << t
    rows.append(block1 | (block2 << 85) | (tail << 170))

assert gf2_rank(rows) == 21

def encode(message):
    out = 0
    j = 0
    while message:
        if message & 1:
            out ^= rows[j]
        message >>= 1
        j += 1
    return out

weights = Counter()
minimum = 185
minimum_words = []
minimum_messages = []
word = 0
previous_gray = 0
for i in range(1 << 21):
    gray = i ^ (i >> 1)
    if i:
        changed = gray ^ previous_gray
        j = (changed & -changed).bit_length() - 1
        word ^= rows[j]
    previous_gray = gray
    w = word.bit_count()
    weights[w] += 1
    if i and w < minimum:
        minimum = w
        minimum_words = [word]
        minimum_messages = [gray]
    elif i and w == minimum:
        minimum_words.append(word)
        minimum_messages.append(gray)

assert minimum == 72
assert len(minimum_words) == 9826
minimum_set = set(minimum_words)

pair_count = 0
for i, x in enumerate(minimum_words):
    for j in range(i + 1, len(minimum_words)):
        if (x ^ minimum_words[j]) in minimum_set:
            pair_count += 1

assert pair_count == 1748433
assert pair_count % 3 == 0
minimizing_spaces = pair_count // 3
assert minimizing_spaces == 582811

witness_messages = (0x63, 0x318, 0x37b)
assert witness_messages[0] ^ witness_messages[1] == witness_messages[2]
witness_words = tuple(encode(x) for x in witness_messages)
assert [x.bit_count() for x in witness_words] == [72, 72, 72]
assert (witness_words[0] | witness_words[1] | witness_words[2]).bit_count() == 108

print("RANK 21")
print("MINIMUM 72 A72 9826")
print("PAIR_TESTS", comb(9826, 2))
print("MIN_SHELL_PAIRS", pair_count, "MINIMIZING_2SPACES", minimizing_spaces)
print("WITNESS_MESSAGES 0x63 0x318 0x37b SUPPORT 108")
print("VERIFY_OK")
