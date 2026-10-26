"""Finite exact checks for all-power left-right signatures of ordered cycles."""
from itertools import product, permutations
from collections import Counter


def constructed(m, r, shifts):
    assert len(shifts) == m and sum(shifts) % r == 1 % r
    f = [0] * (m * r)
    for j in range(m):
        for u in range(r):
            f[j * r + u] = ((j + 1) % m) * r + (u + shifts[j]) % r
    return tuple(f)


def signature(f):
    n = len(f)
    record = bytearray()
    for i in range(n):
        cur = i
        for t in range(1, n):
            cur = f[cur]
            record.append(int(cur > i))  # Equality only at n, not within 1..n-1.
    return bytes(record)


def enumerate_cycles(n):
    for tail in permutations(range(1, n)):
        orbit = (0,) + tail
        f = [0] * n
        for u, v in zip(orbit, orbit[1:] + orbit[:1]):
            f[u] = v
        yield tuple(f)


counts = []
for n, pairs in [(4, [(2, 2)]), (6, [(2, 3), (3, 2)]),
                 (8, [(2, 4), (4, 2)]), (9, [(3, 3)]),
                 (10, [(2, 5), (5, 2)])]:
    keys = {}
    for m, r in pairs:
        shifts = (0,) * (m - 1) + (1,)
        keys[(m, r)] = signature(constructed(m, r, shifts))
    found = Counter()
    for f in enumerate_cycles(n):
        sig = signature(f)
        for mr, key in keys.items():
            if sig == key:
                found[mr] += 1
    for m, r in pairs:
        expected = r ** (m - 1)
        assert found[(m, r)] == expected, (n, m, r, found[(m, r)], expected)
        counts.append((n, m, r, expected))
print('EXHAUSTIVE_ALL_N_CYCLES_EXACT_FIBERS_PASS', len(counts), counts)

for m in range(2, 6):
    for r in range(2, 6):
        base = signature(constructed(m, r, (0,) * (m - 1) + (1,)))
        seen = set()
        for shifts_head in product(range(r), repeat=m-1):
            last = (1 - sum(shifts_head)) % r
            f = constructed(m, r, shifts_head + (last,))
            assert f not in seen
            seen.add(f)
            assert signature(f) == base
            orbit = [0]
            for _ in range(m * r - 1):
                orbit.append(f[orbit[-1]])
            assert len(set(orbit)) == m * r and f[orbit[-1]] == 0
        assert len(seen) == r ** (m - 1)
print('ALL_FACTOR_PAIRS_THROUGH_FIVE_CONSTRUCTIONS_PASS', 16)
print('UNBOUNDED_CONVERSE_AND_CARDINALITY_REQUIRE_ANALYTICAL_PROOF')
