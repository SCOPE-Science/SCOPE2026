#!/usr/bin/env python3
"""Exhaustive, finite verification of one-variable unary bimodal orbits.

No nonstandard dependencies. Run: python3 checker.py
A relation's row bit masks encode its reflexive transitive edges.
The two ordered modal operations are the additive forward-image maps.
"""
from collections import Counter, deque
from itertools import permutations


def orders(n):
    """All labelled partial orders, including their reflexive edges."""
    off = [(a, b) for a in range(n) for b in range(n) if a != b]
    for code in range(1 << len(off)):
        rows = [1 << i for i in range(n)]
        for k, (a, b) in enumerate(off):
            if code & (1 << k):
                rows[a] |= 1 << b
        if any((rows[a] & (1 << b)) and (rows[b] & (1 << a))
               for a in range(n) for b in range(a + 1, n)):
            continue
        if any((rows[a] & (1 << b)) and (rows[b] & ~rows[a])
               for a in range(n) for b in range(n)):
            continue
        image = []
        for mask in range(1 << n):
            closure = 0
            for i, row in enumerate(rows):
                if mask & (1 << i):
                    closure |= row
            image.append(closure)
        yield tuple(rows), tuple(image)


def orbit(C, D, seed, n):
    seen = {seed}
    q = deque([seed])
    U = (1 << n) - 1
    while q:
        a = q.popleft()
        for b in (U ^ a, C[a], D[a]):
            if b not in seen:
                seen.add(b)
                q.append(b)
    return seen


def permute_mask(a, permutation):
    return sum(1 << permutation[i] for i in range(len(permutation))
               if a & (1 << i))


def permute_rows(rows, permutation):
    out = [0] * len(rows)
    for i, r in enumerate(rows):
        out[permutation[i]] = permute_mask(r, permutation)
    return tuple(out)


def census(n):
    posets = dict(orders(n))
    counts = Counter()
    commuting_pairs = 0
    full_triples = set()
    seed_hist = Counter()
    minimum_strict_edges = None
    for P, C in posets.items():
        for Q, D in posets.items():
            # Singleton tests suffice because both operations preserve unions;
            # check all subsets anyway to independently enforce the condition.
            if any(C[D[a]] != D[C[a]] for a in range(1 << n)):
                continue
            commuting_pairs += 1
            for seed in range(1 << n):
                reachable = orbit(C, D, seed, n)
                counts[len(reachable)] += 1
                if len(reachable) == (1 << n):
                    full_triples.add((P, Q, seed))
                    seed_hist[seed.bit_count()] += 1
                    edges = sum(row.bit_count() - 1 for row in P + Q)
                    minimum_strict_edges = (edges if minimum_strict_edges is None
                                            else min(minimum_strict_edges, edges))
                    # Every four-world maximal triple has incomparable orders.
                    if n == 4:
                        assert not (all((x & ~y) == 0 for x, y in zip(P, Q))
                                    or all((y & ~x) == 0 for x, y in zip(P, Q)))
    return len(posets), commuting_pairs, counts, full_triples, seed_hist, minimum_strict_edges


def main():
    expected = {
        1: (1, 1, 2, {2: 2}),
        2: (3, 9, 16, {2: 20, 4: 16}),
        3: (19, 271, 180, {2: 596, 4: 900, 6: 492, 8: 180}),
        4: (219, 22735, 960, {2: 48124, 4: 102252,
                                 6: 107568, 8: 59376, 10: 29280,
                                 12: 12144, 14: 4056, 16: 960})
    }
    for n in range(1, 5):
        p, comm, hist, full, seed_hist, min_edges = census(n)
        ep, ec, ef, eh = expected[n]
        assert (p, comm, len(full), dict(hist)) == (ep, ec, ef, eh), (
            n, p, comm, len(full), hist)
        print('n=%d posets=%d commuting_pairs=%d full_triples=%d' %
              (n, p, comm, len(full)))
        if n == 4:
            assert dict(seed_hist) == {1: 168, 2: 624, 3: 168}
            assert min_edges == 4
            # A successful triple has trivial stabilizer; verify orbit sizes.
            perms = list(permutations(range(n)))
            remaining = full.copy()
            orbit_count = 0
            while remaining:
                P, Q, A = next(iter(remaining))
                images = {
                    (permute_rows(P, perm), permute_rows(Q, perm),
                     permute_mask(A, perm)) for perm in perms
                }
                assert len(images) == 24
                assert images <= full
                remaining.difference_update(images)
                orbit_count += 1
            assert orbit_count == 40
            # Independent explicit 4-world example, using only edge rows.
            P, Q, A = (3, 2, 4, 8), (13, 6, 4, 8), 5
            table = dict(orders(n))
            assert P in table and Q in table
            C, D = table[P], table[Q]
            assert all(C[D[a]] == D[C[a]] for a in range(1 << n))
            assert orbit(C, D, A, n) == set(range(16))
            print('four-point-isomorphism-classes=40; witness=16/16')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
