#!/usr/bin/env python3
from itertools import product
coords = list(product(range(4), range(3), range(3)))
idx = {c: i for i, c in enumerate(coords)}

def conditions(u_index, k_basis_indices):
    return {idx[(u_index, v, w)] for v in k_basis_indices for w in range(3)}

c1 = conditions(0, (0, 1))
c2 = conditions(1, (0, 1))
assert len(coords) == 36
assert len(c1) == 6
assert len(c2) == 6
assert c1.isdisjoint(c2)
assert len(c1 | c2) == 12
one_fiber = 36 - 6 - 1
double_fiber = 36 - 12 - 1
incidence_dim = 3 + 2 + one_fiber
double_incidence_dim = 2 * (3 + 2) + double_fiber
rank_zero_ambiguity_dim = 3 + (36 - 9 - 1) + 2
assert one_fiber == 29
assert incidence_dim == 34
assert double_fiber == 23
assert double_incidence_dim == 33
assert rank_zero_ambiguity_dim == 31
print(f"one_fiber={one_fiber}")
print(f"incidence_dim={incidence_dim}")
print(f"double_fiber={double_fiber}")
print(f"double_incidence_dim={double_incidence_dim}")
print(f"rank_zero_ambiguity_dim={rank_zero_ambiguity_dim}")
print("VERIFY_OK")
