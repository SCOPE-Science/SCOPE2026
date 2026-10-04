#!/usr/bin/env python3
from fractions import Fraction

def patterns(m):
    return [tuple((i >> j) & 1 for j in range(m)) for i in range(1 << m)]

def compatible(p, q):
    """p lives on D={0,...,m-1}; q lives on D-1."""
    m = len(p)
    a = {d: p[d] for d in range(m)}
    for d in range(m):
        c = d - 1
        if c in a and a[c] != q[d]:
            return False
        a[c] = q[d]
    return True

def maximum_family(m):
    ps = patterns(m)
    # A loop means a pattern conflicts with itself and can never be accepted.
    allowed = [i for i, p in enumerate(ps) if not compatible(p, p)]
    adj = {i: set() for i in allowed}
    for ai, i in enumerate(allowed):
        for j in allowed[ai + 1:]:
            # I intersect shift(I)=empty is symmetric after translating,
            # so either directed compatibility creates a conflict.
            if compatible(ps[i], ps[j]) or compatible(ps[j], ps[i]):
                adj[i].add(j)
                adj[j].add(i)

    best = []

    def search(cands, chosen):
        nonlocal best
        if len(chosen) + len(cands) <= len(best):
            return
        if not cands:
            if len(chosen) > len(best):
                best = chosen[:]
            return
        v = max(cands, key=lambda z: len(adj[z].intersection(cands)))
        search([u for u in cands if u != v and u not in adj[v]], chosen + [v])
        search([u for u in cands if u != v], chosen)

    search(allowed[:], [])
    witness = [ps[i] for i in best]

    # Directly recheck all ordered pairs, including equal pairs.
    for p in witness:
        for q in witness:
            assert not compatible(p, q)
    return len(witness), witness

expected = [0, 1, 2, 6, 12, 27]
densities = []
for m, exp in enumerate(expected, start=1):
    got, witness = maximum_family(m)
    assert got == exp, (m, got, exp)
    densities.append(Fraction(got, 1 << m))

for a, b in zip(densities, densities[1:]):
    assert a <= b, (a, b)

print("counts", expected)
print("densities", [str(x) for x in densities])
print("VERIFY_OK")
