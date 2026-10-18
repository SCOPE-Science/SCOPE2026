"""Independent neighborhood-union enumeration of five-row ternary obstructions."""
from itertools import combinations, product

points = list(product(range(3), repeat=3))
assert len(points) == 27
full = (1 << 27) - 1
# A selector c is missed by a row x when all three coordinates differ.
missed = [
    sum(1 << i for i, c in enumerate(points) if all(x[j] != c[j] for j in range(3)))
    for x in points
]

def union_of(rows):
    result = 0
    for row in rows:
        result |= missed[row]
    return result

min5 = []
for rows in combinations(range(27), 5):
    if union_of(rows) != full:
        continue
    if all(union_of(rows[:j] + rows[j + 1:]) != full for j in range(5)):
        min5.append(rows)

assert len(min5) == 54, len(min5)
print("INDEPENDENT_SIZE5_OK", len(min5))
print("first_example", [points[j] for j in min5[0]])
