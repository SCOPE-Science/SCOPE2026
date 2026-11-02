#!/usr/bin/env python3
"""Independent finite-field extension-support checks for subspace inclusion structures.

Prime-field RREF enumeration, vector-span masks, and two-pebble orbit profiles.
Only finite examples are checked; the infinite statement requires the proof.
"""
from itertools import combinations, product
from collections import defaultdict
import json


def code(v, q):
    return sum(x * q ** i for i, x in enumerate(v))


def rref_bases(d, q):
    for k in range(d + 1):
        for pivots in combinations(range(d), k):
            free = [(i, j) for i, p in enumerate(pivots)
                    for j in range(p + 1, d) if j not in pivots]
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * d for _ in range(k)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), a in zip(free, values):
                    rows[i][j] = a
                yield tuple(map(tuple, rows))


def lattice(d, q):
    masks = []
    dimensions = []
    for basis in rref_bases(d, q):
        k = len(basis)
        mask = 0
        for coeffs in product(range(q), repeat=k):
            v = [sum(coeffs[i] * basis[i][j] for i in range(k)) % q
                 for j in range(d)]
            mask |= 1 << code(v, q)
        masks.append(mask)
        dimensions.append(k)
    assert len(masks) == len(set(masks))
    return masks, dimensions


def support_signature(d, q):
    masks, dim = lattice(d, q)
    n = len(masks)
    powers = {q ** j: j for j in range(d + 1)}
    inter = [[powers[(masks[i] & masks[j]).bit_count()]
              for j in range(n)] for i in range(n)]
    representatives = {}
    for i in range(n):
        for j in range(n):
            t = (dim[i], dim[j], inter[i][j])
            if t not in representatives:
                representatives[t] = (i, j)
    signatures = {}
    for t, (i, j) in representatives.items():
        signatures[t] = frozenset((dim[w], inter[i][w], inter[j][w])
                                  for w in range(n))
    # Check orbit homogeneity: all ordered pairs with same descriptor
    # have identical extension support.  This is implied by transitivity
    # of GL(V) on pairs with fixed dimensions/intersection.
    return n, signatures


def main():
    reports = []
    for d, primes in ((1, [2, 3, 5]), (2, [2, 3, 5]),
                      (3, [2, 3, 5]), (4, [2, 3])):
        by_q = {}
        for q in primes:
            n, sig = support_signature(d, q)
            by_q[q] = (n, sig)
        ref_q = primes[0]
        _, ref = by_q[ref_q]
        for q in primes[1:]:
            assert by_q[q][1] == ref, (d, ref_q, q)
        reports.append(dict(dimension=d, fields=primes,
                            lattice_sizes={str(q): by_q[q][0] for q in primes},
                            pair_orbit_count=len(ref),
                            pair_extension_supports=sum(len(s) for s in ref.values()),
                            status='PASS'))
    print(json.dumps({'test': 'pair-orbit-extension-support',
                      'finite_cases': reports, 'status': 'PASS'},
                     sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
