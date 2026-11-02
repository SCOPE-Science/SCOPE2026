#!/usr/bin/env python3
"""Exact finite kernel for a domination reconfiguration theorem.

Stdlib only. The generator uses row/column multiplicities, not domination
simulation; a separate direct domination comparison is included below.
"""
from collections import defaultdict, Counter
from itertools import combinations
from math import comb


def kind(triple, ncols):
    rows = [v // ncols for v in triple]
    cols = [v % ncols for v in triple]
    rs = sorted(Counter(rows).values())
    cs = sorted(Counter(cols).values())
    if rs == [1, 1, 1] and cs == [1, 1, 1]:
        return 'matching'
    if rs == [1, 2] and cs == [1, 2]:
        return 'corner'
    return None


def families(m, n):
    return [a for a in combinations(range(m*n), 3) if kind(a, n)]


def direct_dom(m, n, triple):
    S = set(triple)
    for x in range(m*n):
        if x in S:
            continue
        if not any((x // n != y // n and x % n != y % n) for y in triple):
            return False
    return True


def adjacency(fams):
    by_pair = defaultdict(list)
    for i, triple in enumerate(fams):
        for pair in combinations(triple, 2):
            by_pair[pair].append(i)
    masks = [0] * len(fams)
    for ids in by_pair.values():
        mask = sum(1 << i for i in ids)
        for i in ids:
            masks[i] |= mask ^ (1 << i)
    return masks


def reachable_two(adj):
    out = []
    for i, bits in enumerate(adj):
        reach = bits | (1 << i)
        while bits:
            lo = bits & -bits
            bits -= lo
            reach |= adj[lo.bit_length()-1]
        out.append(reach)
    return out


def check_kernel(m, n):
    fam = families(m, n)
    N = len(fam)
    assert N > 0
    adj = adjacency(fam)
    reach2 = reachable_two(adj)
    all_mask = (1 << N) - 1
    for i, bits in enumerate(adj):
        reach = reach2[i]
        while bits:
            lo = bits & -bits
            bits -= lo
            reach |= reach2[lo.bit_length()-1]
            if reach == all_mask:
                break
        assert reach == all_mask, ('kernel diameter >3', m, n, i, N-reach.bit_count())
    return N


def main():
    cells_checked = 0
    # Verify the all-purpose 3-set characterization against the ORIGINAL
    # domination predicate on several complete-product boards.
    for m, n in [(4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]:
        for tri in combinations(range(m*n), 3):
            assert (kind(tri, n) is not None) == direct_dom(m, n, tri), (m, n, tri)
            cells_checked += 1
        fam = families(m, n)
        adj = adjacency(fam)
        degree_corner = m*n-1
        degree_matching = 3*((m-2)*(n-2)+1)
        assert len(fam) == m*n*(m-1)*(n-1)+6*comb(m,3)*comb(n,3)
        for tri, neighbors in zip(fam, adj):
            assert neighbors.bit_count() == (degree_corner if kind(tri,n)=='corner' else degree_matching)
    kernels=[]
    for m in range(2, 7):
        for n in range(2, 7):
            kernels.append((m, n, check_kernel(m, n)))
    print('DIRECT_PREDICATE_TRIPLES', cells_checked)
    print('FINITE_KERNEL_CASES', len(kernels))
    for m,n,N in kernels:
        print('KERNEL',m,n,N,'DIAMETER_LE_3')
    print('ALL_ASSERTIONS_PASSED')

if __name__ == '__main__':
    main()
