"""Standalone small-case tests for maximal subgroups of multipermutation monoids.

Run: python verify.py
Uses only the Python standard library. Brute force is restricted to n<=3.
"""
from itertools import permutations, product


def product_bool(A, B, n):
    """Boolean relational composition, rows encoded as integer bit masks."""
    out = []
    for a in A:
        r = 0
        for j in range(n):
            if (a >> j) & 1:
                r |= B[j]
        out.append(r)
    return tuple(out)


def full_support(A, n):
    if not all(A):
        return False
    support = 0
    for row in A:
        support |= row
    return support == (1 << n) - 1


def row_semilattice(E):
    rows = {0}
    for r in E:
        rows |= {u | r for u in list(rows)}
    return rows


def automorphism_count(L):
    """Join-semilattice automorphism count by finite exhaustive bijections."""
    items = sorted(L)
    zero_idx = items.index(0)
    count = 0
    for targets in permutations(items):
        if targets[zero_idx] != 0:
            continue
        p = dict(zip(items, targets))
        if all(p[a | b] == (p[a] | p[b]) for a in items for b in items):
            count += 1
    return count


def maximal_group_count(E, full, n):
    """Count g such that gh=hg=E for some h in the multipermutation monoid."""
    rows = [g for g in full if product_bool(E, g, n) == g and product_bool(g, E, n) == g]
    total = 0
    for g in rows:
        if any(product_bool(g, h, n) == E and product_bool(h, g, n) == E for h in rows):
            total += 1
    return total


def test_small_monoids():
    summary = []
    for n in (1, 2, 3):
        mats = [tuple(t) for t in product(range(1, 1 << n), repeat=n)]
        mono = [m for m in mats if full_support(m, n)]
        idempotents = [e for e in mono if product_bool(e, e, n) == e]
        # Exhaust all idempotents, not just order relations.
        for e in idempotents:
            lattice_aut = automorphism_count(row_semilattice(e))
            group_size = maximal_group_count(e, mono, n)
            assert lattice_aut == group_size, (n, e, lattice_aut, group_size)
        summary.append((n, len(mono), len(idempotents)))
    print('n, multipermutations, idempotents:', summary)


def test_cyclic_two_poset():
    # Four rank types: vertices, source nodes, edge nodes, one marker per edge.
    m = 2
    vertices = [(t, g) for t in ('v', 'a', 'b', 'c') for g in range(m)]
    where = {v: i for i, v in enumerate(vertices)}
    covers = set()
    for g in range(m):
        covers.add((where['v', g], where['a', g]))
        covers.add((where['a', g], where['b', g]))
        covers.add((where['v', (g + 1) % m], where['b', g]))
        covers.add((where['b', g], where['c', g]))
    automorphisms = 0
    for perm in permutations(range(len(vertices))):
        if all((perm[u], perm[v]) in covers for (u, v) in covers):
            automorphisms += 1
    assert automorphisms == 2
    # Reflexive transitive closure gives a full-support Boolean idempotent.
    R = [1 << i for i in range(len(vertices))]
    changed = True
    while changed:
        changed = False
        for u, v in covers:
            new = R[u] | R[v]
            if new != R[u]:
                R[u] = new
                changed = True
    E = tuple(R)
    assert full_support(E, len(vertices))
    assert product_bool(E, E, len(vertices)) == E
    print('C2 explicit poset:', len(vertices), 'points;', automorphisms, 'automorphisms')


if __name__ == '__main__':
    test_small_monoids()
    test_cyclic_two_poset()
    print('All finite checks passed.')
