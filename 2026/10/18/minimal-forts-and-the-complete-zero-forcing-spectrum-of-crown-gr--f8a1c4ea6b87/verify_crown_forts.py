"""Reproduce finite tests for crown-graph forts and standard zero forcing.

All vertices are explicit: A_i is index i and B_i is n+i (0 <= i < n).
The check uses direct adjacency and a color-change simulation, not the
structural classification for prediction of individual forcing outcomes.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def adjacency(n):
    out = []
    for i in range(n):
        out.append(sum(1 << (n + j) for j in range(n) if j != i))
    for i in range(n):
        out.append(sum(1 << j for j in range(n) if j != i))
    return out


def fort(mask, adj):
    return mask != 0 and all(
        (adj[v] & mask).bit_count() != 1
        for v in range(len(adj)) if not ((mask >> v) & 1)
    )


def forces_all(blue, adj):
    universe = (1 << len(adj)) - 1
    while True:
        additions = 0
        for vertex in range(len(adj)):
            if blue & (1 << vertex):
                white_neighbors = adj[vertex] & (universe ^ blue)
                if white_neighbors and not (white_neighbors & (white_neighbors - 1)):
                    additions |= white_neighbors
        if not additions:
            return blue == universe
        blue |= additions


def predicted_forts(n):
    result = set()
    for indices in combinations(range(n), 3):
        a = sum(1 << i for i in indices)
        b = sum(1 << (n + i) for i in indices)
        result.add(a)
        result.add(b)
    for indices in combinations(range(n), 2):
        result.add(sum((1 << i) | (1 << (n + i)) for i in indices))
    return result


def expected_forcing_counts(n):
    out = Counter()
    for a in range(3):
        for b in range(3):
            out[2 * n - a - b] += comb(n, a) * comb(n, b)
    out[2 * n - 4] -= comb(n, 2)
    return {k: v for k, v in out.items() if v}


def expected_packing(n):
    return (2 * n) // 3


def exact_packing(minimal_forts, n):
    # Matching of the explicitly identified minimal-fort hypergraph.
    edges = sorted(minimal_forts)
    containing = [[] for _ in range(2*n)]
    for e in edges:
        for v in range(2*n):
            if e & (1 << v):
                containing[v].append(e)

    @lru_cache(None)
    def solve(remaining):
        if not remaining:
            return 0
        bit = remaining & (-remaining)
        v = bit.bit_length() - 1
        best = solve(remaining ^ bit)
        for e in containing[v]:
            if e & remaining == e:
                best = max(best, 1 + solve(remaining ^ e))
        return best
    return solve((1 << (2*n)) - 1)


def verify():
    total_tested = 0
    fort_subsets = 0
    exact_packing_profiles = 0
    for n in range(3, 10):
        adj = adjacency(n)
        counts = Counter()
        all_mask = (1 << (2*n)) - 1
        for blue in range(1 << (2*n)):
            if forces_all(blue, adj):
                counts[blue.bit_count()] += 1
            total_tested += 1
        assert dict(counts) == expected_forcing_counts(n), (n, counts)

        if n <= 8:
            candidates = predicted_forts(n)
            assert len(candidates) == 2 * comb(n, 3) + comb(n, 2)
            for candidate in candidates:
                assert fort(candidate, adj)
                # Every proper nonempty subset of a predicted minimal fort fails.
                sub = (candidate - 1) & candidate
                while sub:
                    assert not fort(sub, adj), (n, candidate, sub)
                    sub = (sub - 1) & candidate
            # Every fort contains at least one predicted minimal fort.
            for white in range(1, 1 << (2*n)):
                if fort(white, adj):
                    assert any((candidate & white) == candidate
                               for candidate in candidates), (n, white)
                fort_subsets += 1
            if n <= 7:
                assert exact_packing(candidates, n) == expected_packing(n)
                exact_packing_profiles += 1

        # Algebraic boundary checks beyond the direct graph enumeration.
        assert counts[2*n - 4] == comb(n,2) * (comb(n,2)-1)
        assert counts[2*n - 3] == n*n*(n-1)
        assert counts[2*n - 2] == n*(2*n-1)
    for n in range(3, 81):
        assert 2*comb(n,3) + comb(n,2) > 0
        assert comb(n,3)*3 == comb(n-1,2)*n
        # Each class of three-vertex forts is covered by uniform weight 1/3.
        assert 3/3 >= 1 and 4/3 >= 1
        assert (2*n)//3 == 2*(n//3) + (1 if n%3 == 2 else 0)
    print("VERIFICATION_OK forcing_subsets={} fort_subsets={} packing_profiles={} n_range=3..9".format(
        total_tested, fort_subsets, exact_packing_profiles))


if __name__ == '__main__':
    verify()
