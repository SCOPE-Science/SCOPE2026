#!/usr/bin/env python3
from itertools import product

def exact_depth_values(table, n, max_depth=3):
    exact = [set(range(n))]
    for depth in range(1, max_depth + 1):
        prior = set().union(*exact[:depth])
        values = set()
        for x in prior:
            for y in prior:
                if x in exact[depth - 1] or y in exact[depth - 1]:
                    values.add(table[x][y])
        exact.append(values)
    return exact

def is_three_nilpotent(table, n):
    return exact_depth_values(table, n, 3)[3] <= {0}

def g2_square(table, n):
    universe = range(n)
    g2 = {table[x][y] for x in universe for y in universe}
    return g2, {table[x][y] for x in g2 for y in g2}

def separates(table, n):
    if not is_three_nilpotent(table, n):
        return False
    _, g2sq = g2_square(table, n)
    return any(x != 0 for x in g2sq)

separator_count = 0
nilpotent_count = 0
for entries in product(range(3), repeat=4):
    table = [[0] * 3 for _ in range(3)]
    k = 0
    for x in (1, 2):
        for y in (1, 2):
            table[x][y] = entries[k]
            k += 1
    nilpotent_count += int(is_three_nilpotent(table, 3))
    separator_count += int(separates(table, 3))
assert separator_count == 0

example = [[0] * 4 for _ in range(4)]
example[3][3] = 2
example[2][2] = 1
depth = exact_depth_values(example, 4, 3)
g2, g2sq = g2_square(example, 4)
assert depth[1] == {0, 1, 2}
assert depth[2] == {0, 1}
assert depth[3] == {0}
assert g2 == {0, 1, 2}
assert g2sq == {0, 1}
assert separates(example, 4)

print("ORDER3_TOTAL", 3 ** 4)
print("ORDER3_3NIL", nilpotent_count)
print("ORDER3_SEPARATORS", separator_count)
print("EXAMPLE_DEPTH1", sorted(depth[1]))
print("EXAMPLE_DEPTH2", sorted(depth[2]))
print("EXAMPLE_DEPTH3", sorted(depth[3]))
print("EXAMPLE_G2", sorted(g2))
print("EXAMPLE_G2SQ", sorted(g2sq))
print("CHECK_OK")
