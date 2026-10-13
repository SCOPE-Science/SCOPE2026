#!/usr/bin/env python3
from itertools import product, permutations

def upper_states(x, n):
    return [y for y in range(1 << n) if (x & ~y) == 0]

def extendable(alpha, n, v=4):
    labels = set(range(v))
    if set(alpha) != labels:
        return False
    for m in range(v):
        if not any(alpha[x] == m and {alpha[y] for y in upper_states(x, n)} == labels
                   for x in range(1 << n)):
            return False
    return True

def all_valid(n, v=4):
    return [a for a in product(range(v), repeat=1 << n) if extendable(a, n, v)]

v2 = all_valid(2)
assert len(v2) == 0
v3 = all_valid(3)
assert len(v3) == 24

canonical = (0, 1, 2, 3, 3, 2, 1, 0)
expected = {tuple(p[c] for c in canonical) for p in permutations(range(4))}
assert set(v3) == expected
for alpha in v3:
    assert all(alpha[x] == alpha[x ^ 7] for x in range(8))
    assert len({alpha[0], alpha[1], alpha[2], alpha[4]}) == 4

def parity_decoder(x):
    a = (x >> 0) & 1
    b = (x >> 1) & 1
    c = (x >> 2) & 1
    return (b ^ c) + 2 * (a ^ c)

pd = tuple(parity_decoder(x) for x in range(8))
assert all((pd[x] == pd[y]) == (x == y or x == (y ^ 7))
           for x in range(8) for y in range(8))

print("VERIFY_OK n2_valid=0 n3_valid=24 all_antipodal=true one_output_relabeling_class=true")
