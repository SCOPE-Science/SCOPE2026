#!/usr/bin/env python3

def vertices(n):
    return list(range(1, 1 << n))

def adjacent(a, b):
    return (a & b) != 0

def dominates(block, W):
    return all(any(adjacent(v, u) for u in block) for v in W)

def complement_blocks(n):
    full = (1 << n) - 1
    seen = set()
    blocks = []
    for a in range(1 << n):
        if a in seen:
            continue
        b = full ^ a
        seen.add(a)
        seen.add(b)
        block = {x for x in (a, b) if x != 0}
        blocks.append(block)
    return blocks

# Exact lower construction through n=8.
for n in range(1, 9):
    W = set(vertices(n))
    blocks = complement_blocks(n)
    assert len(blocks) == 2 ** (n - 1)
    assert set().union(*blocks) == W
    assert sum(len(b) for b in blocks) == len(W)
    assert all(dominates(b, W) for b in blocks)

# Set partitions, used only for the small exhaustive replay.
def partitions(seq):
    seq = list(seq)
    if not seq:
        yield []
        return
    x = seq[0]
    for rest in partitions(seq[1:]):
        yield [{x}] + [set(b) for b in rest]
        for i in range(len(rest)):
            new = [set(b) for b in rest]
            new[i].add(x)
            yield new

def domatic_number(W):
    W = list(W)
    best = 0
    for p in partitions(W):
        if len(p) <= best:
            continue
        if all(dominates(b, W) for b in p):
            best = len(p)
    return best

# Exhaustive maximum over every nonempty induced subgraph for n<=3.
for n in range(1, 4):
    V = vertices(n)
    best = 0
    for mask in range(1, 1 << len(V)):
        W = [V[i] for i in range(len(V)) if (mask >> i) & 1]
        best = max(best, domatic_number(W))
    assert best == 2 ** (n - 1), (n, best)

# Coordinate coding: q_i is true at B iff i is absent from B.
for m in range(2, 8):
    full = (1 << m) - 1
    for A in range(1 << m):
        for B in range(1, 1 << m):
            theta = True
            for i in range(m):
                q_i = (B & (1 << i)) == 0
                needed = ((A >> i) & 1) == 0
                theta = theta and (q_i == needed)
            assert theta == (A == B)

# Construct quotient fibers at stage n+1 and verify the bounded-morphism back condition.
for n in range(1, 8):
    m = n + 1
    V = set(vertices(m))
    base = complement_blocks(m)
    r = 2 ** (n - 1) + 1
    assert r <= len(base)

    # Merge the surplus base blocks into the last retained fiber.
    fibers = [set(b) for b in base[:r]]
    for b in base[r:]:
        fibers[-1] |= b

    assert len(fibers) == r
    assert set().union(*fibers) == V
    assert all(fibers)

    # Back condition to a universal reflexive target:
    # every source vertex has a neighbor in every fiber.
    for x in V:
        for F in fibers:
            assert any(adjacent(x, y) for y in F)

print("VERIFY_OK")
