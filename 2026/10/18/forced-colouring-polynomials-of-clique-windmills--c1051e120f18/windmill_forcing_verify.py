"""Independent exhaustive checks for the forcing-colouring polynomial on clique windmills.

Usage: python windmill_forcing_verify.py
Uses exact integers throughout; no third-party dependencies.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def clique_windmill(k, m):
    """Hub 0; k disjoint m-cliques on consecutive vertex labels."""
    n = 1 + k * m
    neighbors = [set() for _ in range(n)]
    for i in range(k):
        block = range(1 + i*m, 1 + (i+1)*m)
        for a in block:
            neighbors[0].add(a)
            neighbors[a].add(0)
            for b in block:
                if a != b:
                    neighbors[a].add(b)
    return tuple(tuple(sorted(v)) for v in neighbors)


def forces(assignment, neighbors, q):
    vals = list(assignment)
    for i, v in enumerate(vals):
        if v < 0:
            continue
        if any(vals[j] == v for j in neighbors[i]):
            return False
    changed = True
    while changed:
        changed = False
        for i, v in enumerate(vals):
            if v >= 0:
                continue
            seen = {vals[j] for j in neighbors[i] if vals[j] >= 0}
            if len(seen) == q - 1:
                vals[i] = next(c for c in range(q) if c not in seen)
                changed = True
    return all(v >= 0 for v in vals) and all(
        vals[i] != vals[j] for i, adj in enumerate(neighbors) for j in adj)


def predicted(k, m):
    q = m + 1
    lo = k*(m-1)
    count = Counter()
    for r in range(k+2):
        coeff = comb(k, r)*m**(k-r) if r <= k else 0
        if r >= 1:
            coeff += comb(k, r-1)*m**(k-r+1)
        if r == 0:
            coeff -= m
        if coeff:
            count[lo+r] = q*factorial(m)**k*coeff
    return count


def exhaustive(k, m):
    adj = clique_windmill(k, m)
    q = m+1
    counts = Counter()
    for encoded in product(range(-1, q), repeat=len(adj)):
        if forces(encoded, adj, q):
            counts[sum(c >= 0 for c in encoded)] += 1
    expected = predicted(k, m)
    assert counts == expected, (k, m, counts, expected)
    print(f'PASS k={k}, m={m}, vertices={len(adj)}, assignments={(q+1)**len(adj)}, coefficients={dict(sorted(counts.items()))}')
    return (q+1)**len(adj)


def construction_check(k, m):
    # Minimal source: in each blade omit one colour, use at least two different omissions.
    # Explicitly choose alternate missing colours 0 and 1 in first two blades.
    q = m+1
    for hub_col in range(q):
        outer = [c for c in range(q) if c != hub_col]
        vals = [-1] + [outer[c] for _ in range(k) for c in range(m)]
        for i in range(k):
            missing_index = 0 if i != 1 else 1
            vals[1+i*m+missing_index] = -1
        assert forces(vals, clique_windmill(k, m), q)
        assert sum(c >= 0 for c in vals) == k*(m-1)
    print(f'PASS minimal construction k={k}, m={m}: {q} hub colours')


def main():
    total=0
    for k,m in [(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(1,4)]:
        total+=exhaustive(k,m)
    for k in range(2,8):
        for m in range(2,8):
            construction_check(k,m)
    print('ALL CHECKS PASS',total,'exhaustively classified partial assignments')

if __name__=='__main__':
    main()
