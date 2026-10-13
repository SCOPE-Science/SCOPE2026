#!/usr/bin/env python3
from math import gcd

SRC = 9
TGT = 27

# Multiplicative generators for Z/9Z: 2 generates the six units, while 3
# supplies the nonunit layer and 3^2=0.  Each residue has the representation
# 3^u 2^k used below.
REPS = {
    0: (2, 0),
    1: (0, 0),
    2: (0, 1),
    4: (0, 2),
    8: (0, 3),
    7: (0, 4),
    5: (0, 5),
    3: (1, 0),
    6: (1, 1),
}


def map_from_images(a, b):
    """Candidate map with 2 -> a and 3 -> b."""
    return {
        x: (pow(b, u, TGT) * pow(a, k, TGT)) % TGT
        for x, (u, k) in REPS.items()
    }


def is_unital_monoid_hom(m):
    if m[1] != 1:
        return False
    return all(
        m[(x * y) % SRC] == (m[x] * m[y]) % TGT
        for x in range(SRC)
        for y in range(SRC)
    )


maps = []
image_pairs = []
for a in range(TGT):
    for b in range(TGT):
        m = map_from_images(a, b)
        if is_unital_monoid_hom(m):
            maps.append(tuple(m[x] for x in range(SRC)))
            image_pairs.append((a, b))

assert len(set(maps)) == 19
assert len(image_pairs) == 19

# The source's displayed stratum count in this case uses six unit-group
# homomorphisms.  Its printed lower bound v >= floor(3/2)=1 gives strata
# of sizes 6*|U_9|, 6*|U_3|, and 6*|U_1|, plus the constant-one map.
unit_homs = gcd(6, 18)
printed_count = 1 + unit_homs * (6 + 2 + 1)
corrected_count = 1 + unit_homs * (2 + 1)
assert unit_homs == 6
assert printed_count == 55
assert corrected_count == 19
assert corrected_count == len(set(maps))

# Explicit forbidden bottom-stratum witness: p=q=3, e=2, f=3, v=1,
# r=1 and the trivial unit homomorphism.  The zero class is represented by
# 3^2, but the formula sends it to 3^2=9 mod 27 instead of zero.
spurious_zero_image = pow(3, 2, 27)
assert spurious_zero_image == 9
assert spurious_zero_image != 0

print(f"actual_homomorphisms={len(set(maps))}")
print(f"printed_parameter_count={printed_count}")
print(f"corrected_parameter_count={corrected_count}")
print(f"spurious_v1_zero_image={spurious_zero_image}")
print("VERIFY_OK")
