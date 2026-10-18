#!/usr/bin/env python3
"""Exact finite verification of two sixteen-vertex dissociation polynomials.

No nonstandard libraries or external data are needed.  The two counting
methods below independently implement the defining condition and a vertex
recursion respectively.  All counts are exact integers.
"""

from collections import Counter
from functools import lru_cache
from itertools import product

VERTICES = list(product(range(4), repeat=2))
N = len(VERTICES)
FULL = (1 << N) - 1
EXPECTED_ROOK = (1, 16, 120, 384, 528, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
EXPECTED_SHRIKHANDE = (1, 16, 120, 384, 544, 240, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def graph(kind):
    neighbors = []
    generators = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    for i, (a, b) in enumerate(VERTICES):
        mask = 0
        for j, (c, d) in enumerate(VERTICES):
            if i == j:
                continue
            if kind == 'rook':
                adjacent = a == c or b == d
            elif kind == 'shrikhande':
                adjacent = ((c - a) % 4, (d - b) % 4) in generators
            elif kind == 'shrikhande_alternative':
                adjacent = a != c and b != d and (a-b-c+d) % 4 != 0
            else:
                raise ValueError(kind)
            if adjacent:
                mask |= 1 << j
        neighbors.append(mask)
    return tuple(neighbors)


def brute_force(neighbors):
    counts = [0] * (N+1)
    edge_classes = Counter()
    for subset in range(1 << N):
        bits = subset
        edges_twice = 0
        while bits:
            low = bits & -bits
            idx = low.bit_length() - 1
            degree = (neighbors[idx] & subset).bit_count()
            if degree > 1:
                break
            edges_twice += degree
            bits ^= low
        else:
            counts[subset.bit_count()] += 1
            if subset.bit_count() >= 5:
                edge_classes[(subset.bit_count(), edges_twice//2)] += 1
    return tuple(counts), edge_classes


def recurrence(neighbors):
    @lru_cache(maxsize=None)
    def count(mask):
        if mask == 0:
            return (1,)
        bit = mask & -mask
        v = bit.bit_length() - 1
        # Case I: vertex v is unselected.
        absent = count(mask ^ bit)
        out = list(absent) + [0]
        # Case II: selected v has zero selected neighbors.
        isolated = count(mask & ~(bit | neighbors[v]))
        for k, coefficient in enumerate(isolated):
            out[k+1] += coefficient
        # Case III: selected v has exactly one selected neighbor u.
        partners = mask & neighbors[v]
        while partners:
            u_bit = partners & -partners
            u = u_bit.bit_length()-1
            partners ^= u_bit
            remaining = mask & ~(bit | u_bit | neighbors[v] | neighbors[u])
            paired = count(remaining)
            if len(out) < len(paired)+2:
                out.extend([0] * (len(paired)+2-len(out)))
            for k, coefficient in enumerate(paired):
                out[k+2] += coefficient
        return tuple(out)

    coeffs = count(FULL)
    return tuple(coeffs) + (0,) * (N+1-len(coeffs)), count.cache_info()


def check_strong_regularity(adj):
    assert all(mask.bit_count()==6 for mask in adj)
    for i in range(N):
        assert adj[i] & (1 << i) == 0
        for j in range(i+1,N):
            assert bool((adj[i]>>j)&1) == bool((adj[j]>>i)&1)
            assert (adj[i] & adj[j]).bit_count() == (2 if (adj[i]>>j)&1 else 2)
    return sum(mask.bit_count() for mask in adj)//2


def main():
    rook, shr = graph('rook'), graph('shrikhande')
    alt = graph('shrikhande_alternative')
    assert check_strong_regularity(rook) == 48
    assert check_strong_regularity(shr) == 48
    assert check_strong_regularity(alt) == 48
    # An invertible Z_4-linear change of coordinates (determinant one)
    # maps the Cayley generators to the second standard presentation.
    change = [VERTICES.index(((a+b)%4, (2*a+3*b)%4)) for a,b in VERTICES]
    assert len(set(change)) == N
    for i in range(N):
        for j in range(N):
            assert bool(shr[i]>>j & 1) == bool(alt[change[i]]>>change[j] & 1)
    results = []
    for name, adj, expected in (('rook', rook, EXPECTED_ROOK),
                                ('shrikhande', shr, EXPECTED_SHRIKHANDE)):
        direct, by_edges = brute_force(adj)
        recursive, stats = recurrence(adj)
        assert direct == recursive == expected, (name, direct, recursive)
        results.append((name, sum(direct), sum(direct[1:]),
                        [(k,direct[k]) for k in range(N+1) if direct[k]],
                        sorted(by_edges.items()),stats.currsize))
    assert (EXPECTED_SHRIKHANDE[4] - EXPECTED_ROOK[4],
            EXPECTED_SHRIKHANDE[5] - EXPECTED_ROOK[5],
            EXPECTED_SHRIKHANDE[6] - EXPECTED_ROOK[6]) == (16, 96, 32)
    for name, total, nonempty, coefficients, maximal_patterns, dpstates in results:
        print(f'{name}: D(1)={total}, nonempty={nonempty}, nonzero={coefficients}')
        print(f'{name}: large-set edge-counts={maximal_patterns}, dp_states={dpstates}')
    print('VERIFICATION_OK masks_per_graph=65536 methods=brute_and_recurrence graphs=rook_shrikhande')


if __name__ == '__main__':
    main()
