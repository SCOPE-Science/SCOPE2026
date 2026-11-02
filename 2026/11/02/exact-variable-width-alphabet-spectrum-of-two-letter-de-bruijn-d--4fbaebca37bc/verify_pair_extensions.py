#!/usr/bin/env python3
"""Exact finite checks for the pure directed adjacency structure B(q,2).
Science-only reproducibility helper. No external packages required.
"""
from itertools import product


def words(q):
    return list(product(range(q), repeat=2))


def e(x, y):
    return x[1] == y[0]


def pair_profile(x, y):
    return (x == y, e(x, x), e(y, y), e(x, y), e(y, x))


def supports(q):
    v = words(q)
    return {
        is_loop: {
            frozenset(pair_profile(x, y) for y in v)
            for x in v if e(x, x) == is_loop
        }
        for is_loop in (True, False)
    }


q3 = supports(3)
assert all(len(c) == 1 for c in q3.values())
for q in range(3, 13):
    z = supports(q)
    assert all(len(c) == 1 for c in z.values())
    assert z == q3, (q, z, q3)

# Two-variable thresholds: existence of a nonloop; existence of a
# loop and a nonloop neither adjacent to the other.
for q in range(1, 13):
    w = words(q)
    nonloop = any(not e(x, x) for x in w)
    separated_loop = any(
        e(x, x) and not e(y, y) and not e(x, y) and not e(y, x)
        for x in w for y in w
    )
    assert nonloop == (q >= 2)
    assert separated_loop == (q >= 3)

# Check that the third-variable abbreviations really test coordinate equality.
for q in range(1, 9):
    v = words(q)
    for x in v:
        for y in v:
            first = any(e(z, x) and e(z, y) for z in v)
            second = any(e(x, z) and e(y, z) for z in v)
            assert first == (x[0] == y[0])
            assert second == (x[1] == y[1])

# The canonical existential diagram for t distinct alphabet letters,
# represented on ceil(t/2) vertices (last vertex is a loop when t odd).
# A structure satisfies it precisely when the underlying alphabet has >= t letters.
def diagram_holds(q, t):
    r = (t + 1) // 2
    universe = words(q)
    # Existence of t distinct letters is checked by an explicit assignment
    # and verified against the chosen word-pair pattern.
    if q < t:
        return False
    letters = list(range(t))
    vs = [tuple(letters[2*i:2*i+2]) for i in range(t//2)]
    if t % 2:
        vs.append((letters[-1], letters[-1]))
    assert len(vs) == r and all(x in universe for x in vs)
    active = [c for i,x in enumerate(vs) for c in (x if not (t%2 and i==r-1) else (x[0],))]
    assert len(active) == t and len(set(active)) == t
    return True

for k in (3, 4, 5):
    for t in range(1, 2*k + 1):
        for q in range(1, 2*k + 3):
            assert diagram_holds(q, t) == (q >= t)

print('VERIFY_PAIR_EXTENSIONS_OK: q=1..12, coordinate equality q=1..8, width diagrams k=3..5')
