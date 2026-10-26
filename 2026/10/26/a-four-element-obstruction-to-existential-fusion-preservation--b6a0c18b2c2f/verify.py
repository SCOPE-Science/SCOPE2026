"""Dependency-free checks for the four-element residuated-chain example."""

# Carrier indices encode the order bottom < a < e < b.
BOTTOM, A, E, B = range(4)
CARRIER = range(4)
FILTER = {E, B}

# Rows and columns are ordered BOTTOM, A, E, B.
MUL = (
    (BOTTOM, BOTTOM, BOTTOM, BOTTOM),
    (BOTTOM, A, A, B),
    (BOTTOM, A, E, B),
    (BOTTOM, B, B, B),
)


def mul(x, y):
    return MUL[x][y]


# Monoid, order, and designated-filter checks.
assert FILTER == {x for x in CARRIER if x >= E}
assert all(not (x in FILTER and x <= y) or y in FILTER for x in CARRIER for y in CARRIER)
assert all((min(x, y) in FILTER) == (x in FILTER and y in FILTER) for x in CARRIER for y in CARRIER)
assert all((max(x, y) in FILTER) == (x in FILTER or y in FILTER) for x in CARRIER for y in CARRIER)
assert all(mul(x, y) in FILTER for x in FILTER for y in FILTER)
assert all(mul(x, y) == mul(y, x) for x in CARRIER for y in CARRIER)
assert all(mul(E, x) == x == mul(x, E) for x in CARRIER)
assert all(mul(BOTTOM, x) == BOTTOM == mul(x, BOTTOM) for x in CARRIER)
assert all(
    mul(mul(x, y), z) == mul(x, mul(y, z))
    for x in CARRIER for y in CARRIER for z in CARRIER
)
assert all(
    mul(x, y) <= mul(x, z)
    for x in CARRIER for y in CARRIER for z in CARRIER if y <= z
)

# Right residual x -> z is the greatest y satisfying x * y <= z.
RESIDUAL = tuple(
    tuple(max(y for y in CARRIER if mul(x, y) <= z) for z in CARRIER)
    for x in CARRIER
)
assert all(
    (mul(x, y) <= z) == (y <= RESIDUAL[x][z])
    for x in CARRIER for y in CARRIER for z in CARRIER
)

# One-point source and target structures, using the identity domain/algebra maps.
source_R, source_P = A, B
target_R, target_P = A, E
assert (source_R not in FILTER) or (target_R in FILTER)
assert (source_P not in FILTER) or (target_P in FILTER)
assert mul(source_R, source_P) in FILTER
assert mul(target_R, target_P) not in FILTER
assert mul(source_R, source_P) == B
assert mul(target_R, target_P) == A

print("VERIFIED: commutative monoid, associativity, monotonicity, residuation (64 triples), and preservation counterexample")
