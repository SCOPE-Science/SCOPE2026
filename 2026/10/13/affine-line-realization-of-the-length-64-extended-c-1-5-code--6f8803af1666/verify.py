"""Exact finite-field verification of the degree-six C_(1,5) affine-line identification.
Run: python3 verify.py (Python 3 stdlib only).
"""
from collections import defaultdict
from itertools import combinations
from functools import reduce

MOD = 0x43  # X^6+X+1, primitive irreducible over GF(2)

def mul(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= MOD
    return z

def power(a, n):
    z = 1
    while n:
        if n & 1:
            z = mul(z, a)
        a = mul(a, a)
        n >>= 1
    return z

def rank_gf2(rows):
    piv = {}
    for v in rows:
        while v:
            p = v.bit_length() - 1
            if p in piv:
                v ^= piv[p]
            else:
                piv[p] = v
                break
    return len(piv)

assert power(2, 63) == 1
assert all(power(2, k) != 1 for k in range(1, 63))
assert all(mul(x, power(x, 62)) == 1 for x in range(1, 64))
w = power(2, 21)
assert power(w, 3) == 1 and w != 1
F4 = (0, 1, w, w ^ 1)
assert len(set(F4)) == 4
assert all(mul(a, b) in F4 for a in F4 for b in F4)

lines = sorted({tuple(sorted(a ^ mul(t, v) for t in F4))
                for a in range(64) for v in range(1, 64)})
assert len(lines) == 336
assert all(len(set(L)) == 4 for L in lines)
assert sum(0 in L for L in lines) == 21
pairs = defaultdict(int)
for L in lines:
    for p in combinations(L, 2):
        pairs[p] += 1
assert len(pairs) == 2016 and set(pairs.values()) == {1}

col = [1 | (x << 1) | (power(x, 5) << 7) for x in range(64)]
assert rank_gf2([sum(((col[x] >> i) & 1) << x for x in range(64))
                 for i in range(13)]) == 13
for L in lines:
    assert reduce(int.__xor__, (col[x] for x in L), 0) == 0
line_vectors = [sum(1 << x for x in L) for L in lines]
assert rank_gf2(line_vectors) == 51

# Independent, exhaustive four-point zero-syndrome census by equal pair syndromes.
by_pair_syndrome = defaultdict(list)
for i, j in combinations(range(64), 2):
    by_pair_syndrome[col[i] ^ col[j]].append((i, j))
all_weight_four = set()
for group in by_pair_syndrome.values():
    for (a, b), (c, d) in combinations(group, 2):
        if len({a, b, c, d}) == 4:
            all_weight_four.add(tuple(sorted((a, b, c, d))))
assert len(all_weight_four) == 336
assert all_weight_four == set(lines)
# Parity excludes weight 1/3; distinct singleton syndromes exclude weight 2.
assert len(set(col)) == 64

assert len(lines) == 336 and rank_gf2(line_vectors) == 64-13
print('FIELD 64 SUBFIELD 4')
print('PARITY_CHECK_RANK 13')
print('AFFINE_LINES 336')
print('WEIGHT_FOUR_SUPPORTS 336')
print('LINE_SPAN_RANK 51')
print('CODE_PARAMETERS [64,51,4]')
print('AUT_GROUP_ORDER',64*63*60*48*2)
print('VERIFY_OK')
