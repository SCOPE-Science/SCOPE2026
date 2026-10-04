#!/usr/bin/env python3

def cyclic_cover(m):
    # Worlds are (row, col); symbol is col-row mod m.
    pts = [(r, c) for r in range(m) for c in range(m)]
    f = {(r, c): (c - r) % m for r, c in pts}
    R1 = lambda x, y: x[0] == y[0]
    R2 = lambda x, y: x[1] == y[1]
    return pts, f, R1, R2

for m in range(1, 13):
    pts, f, R1, R2 = cyclic_cover(m)
    assert len(pts) == m * m
    assert set(f.values()) == set(range(m))

    for R in (R1, R2):
        # Equivalence relation.
        for x in pts:
            assert R(x, x)
        for x in pts:
            for y in pts:
                assert R(x, y) == R(y, x)
                for z in pts:
                    if R(x, y) and R(y, z):
                        assert R(x, z)

        # Bounded morphism to the universal target: forth is automatic,
        # and back says every class contains every target label.
        for x in pts:
            labels = {f[y] for y in pts if R(x, y)}
            assert labels == set(range(m))

    # Properness.
    for x in pts:
        for y in pts:
            if x != y:
                assert not (R1(x, y) and R2(x, y))

def set_partitions(n):
    # Return partitions as tuples of frozenset blocks.
    if n == 0:
        yield ()
        return
    blocks = []
    def rec(x):
        if x == n:
            yield tuple(frozenset(b) for b in blocks)
            return
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(x + 1)
            blocks[i].pop()
        blocks.append([x])
        yield from rec(x + 1)
        blocks.pop()
    yield from rec(0)

def admissible_partition(p, m):
    return all(len(b) >= m for b in p)

def cross_intersections_at_most_one(p, q):
    return all(len(a & b) <= 1 for a in p for b in q)

# Exhaustively corroborate the lower bound for m=2,3.
for m in (2, 3):
    for n in range(1, m * m):
        ps = [p for p in set_partitions(n) if admissible_partition(p, m)]
        for p in ps:
            for q in ps:
                assert not cross_intersections_at_most_one(p, q), (m, n, p, q)

# Exhaustively corroborate equality rigidity for m=2,3.
for m in (2, 3):
    n = m * m
    ps = [p for p in set_partitions(n) if admissible_partition(p, m)]
    found = 0
    for p in ps:
        for q in ps:
            if not cross_intersections_at_most_one(p, q):
                continue
            found += 1
            assert len(p) == m and len(q) == m
            assert all(len(b) == m for b in p)
            assert all(len(b) == m for b in q)
            assert all(len(a & b) == 1 for a in p for b in q)
    assert found > 0

print("VERIFY_OK")
