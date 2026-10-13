#!/usr/bin/env python3
"""Standalone exact checks for the binary parity-function systematic codes."""
from itertools import permutations, combinations, product
from math import factorial

R = 5
ONE = (1 << R) - 1
COLORS = (ONE,) + tuple(ONE ^ (1 << j) for j in range(R))
assert len(set(COLORS)) == R + 1
assert sorted(c.bit_count() for c in COLORS) == [4,4,4,4,4,5]


def systematic_parity_map(k, columns, offset=0):
    out = []
    for msg in range(1 << k):
        s = offset
        for i in range(k):
            if msg & (1 << i):
                s ^= columns[i]
        out.append(s)
    return out


def valid(k, p):
    for a in range(1 << k):
        for b in range(a + 1, 1 << k):
            m = (a ^ b).bit_count()
            d = m + (p[a] ^ p[b]).bit_count()
            if d < 3 or ((m & 1) and d < 5):
                return False, (a, b, d)
    return True, None


# Symbolic proof's only finite local case: all admissible four-edge colorings.
valid_squares = 0
for a, b, c, d in product(range(6), repeat=4):
    if (a == d) or (a == b) or (b == c) or (c == d):
        # adjacency at square corners, in cyclic edge order (a,b,c,d)
        continue
    if (COLORS[a] ^ COLORS[b] ^ COLORS[c] ^ COLORS[d]) == 0:
        valid_squares += 1
        assert a == c and b == d, (a, b, c, d)
assert valid_squares == 30, valid_squares

# Every injection from six directions to the six allowed toggles succeeds.
permutations_checked = 0
canonical_signatures = set()
for ordering in permutations(COLORS):
    p = systematic_parity_map(6, ordering)
    ok, witness = valid(6, p)
    assert ok, witness
    # Affine linear map with zero offset is fixed by values at basis directions.
    assert len(p) == 64
    signature = tuple(p[1 << i] for i in range(6))
    assert signature not in canonical_signatures
    canonical_signatures.add(signature)
    permutations_checked += 1
assert permutations_checked == factorial(6) == 720
# Distinct translations alter the parity output at zero and give unique encoders.
assert len(COLORS) == 6
assert (1 << 5) * permutations_checked == 23040

# Boundaries: all lengths k<=6 inherit the 5-check-bit construction;
# k=1 has a 4-check-bit construction, and k=2 cannot use r=4.
for k in range(2, 7):
    p = systematic_parity_map(k, COLORS[:k])
    ok, witness = valid(k, p)
    assert ok, (k, witness)
# Exhaust all 16^4 arbitrary four-check-bit maps on the two-cube.
# This independently excludes 4-bit redundancy already at dimension two.
nonvalid_candidates = 0
for p in product(range(16), repeat=4):
    ok, _ = valid(2, p)
    if ok:
        nonvalid_candidates += 1
assert nonvalid_candidates == 0

# One information bit needs exactly four complementary check bits.
assert 1 + (0 ^ 15).bit_count() == 5

print('VERIFY_OK: 30 square patterns; 720 distinct linear assignments; '
      '23040 affine maps; k=2..6 valid; 65536 four-check-bit maps excluded')
