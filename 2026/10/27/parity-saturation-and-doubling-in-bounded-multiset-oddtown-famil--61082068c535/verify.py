#!/usr/bin/env python3
"""Reproducible elementary checks for the multiset Oddtown theorem.

No third-party dependencies. The finite search is exhaustive, not a Monte Carlo
experiment. The unbounded statements require the mathematical proof.
"""
from itertools import combinations, permutations, product

W3 = [
    (0, 2, 1), (1, 2, 0), (2, 1, 2), (3, 1, 1),
]
W4 = [
    (0, 1, 2, 2), (1, 0, 2, 2), (1, 2, 1, 3), (1, 3, 1, 2),
    (2, 1, 3, 1), (2, 2, 0, 1), (2, 2, 1, 0), (3, 1, 2, 1),
]

def compatible(x, y):
    return sum(min(a, b) for a, b in zip(x, y)) % 2 == 0

def valid(family):
    return (len(set(family)) == len(family)
            and all(sum(v) % 2 for v in family)
            and all(compatible(a, b) for a, b in combinations(family, 2)))

def parity_group(v):
    return tuple(x % 2 for x in v)

def exhaustive_parity_saturation(n, cap):
    """List ALL full-parity-pattern Oddtown families in a fixed finite box.

    Distinct parity patterns are compulsory (proved separately). An extremizer
    saturating the bound therefore chooses exactly one word per odd pattern.
    At every branch, choices incompatible with previous words are discarded;
    a branch is pruned only when it has no compatible extension.
    """
    patterns = [p for p in product((0, 1), repeat=n) if sum(p) % 2]
    domain = list(product(range(cap + 1), repeat=n))
    options = [[v for v in domain if parity_group(v) == p] for p in patterns]
    answers = []
    nodes = 0
    def visit(chosen, groups):
        nonlocal nodes
        nodes += 1
        if not groups:
            answers.append(tuple(sorted(chosen)))
            return
        candidates = []
        for i, group in enumerate(groups):
            available = [v for v in group if all(compatible(v, u) for u in chosen)]
            if not available:
                return
            candidates.append((len(available), i, available))
        _, pivot, possible = min(candidates, key=lambda x: x[0])
        for v in possible:
            visit(chosen + [v], groups[:pivot] + groups[pivot + 1:])
    visit([], options)
    return answers, nodes

def maximum_clique(n, cap):
    """Independent exhaustive graph-based check, not using parity-group DFS."""
    vectors = [v for v in product(range(cap + 1), repeat=n) if sum(v) % 2]
    N = len(vectors)
    edges = [0] * N
    for i in range(N):
        for j in range(i):
            if compatible(vectors[i], vectors[j]):
                edges[i] |= 1 << j
                edges[j] |= 1 << i
    best = 0
    def visit(size, cand, excluded):
        nonlocal best
        if not cand and not excluded:
            best = max(best, size)
            return
        if size + cand.bit_count() <= best:
            return
        pool = cand | excluded
        pivot = max((i for i in range(N) if pool & (1 << i)),
                    key=lambda i: (cand & edges[i]).bit_count(), default=0)
        branch = cand & ~edges[pivot]
        while branch:
            bit = branch & -branch
            v = bit.bit_length() - 1
            visit(size + 1, cand & edges[v], excluded & edges[v])
            cand ^= bit
            excluded |= bit
            branch ^= bit
            if size + cand.bit_count() <= best:
                return
    visit(0, (1 << N) - 1, 0)
    return best

def direct_sum(blocks):
    n = sum(len(block[0]) for block in blocks)
    result = []
    offset = 0
    for block in blocks:
        width = len(block[0])
        for v in block:
            result.append((0,) * offset + v + (0,) * (n - offset - width))
        offset += width
    return result

def test():
    assert valid(W3) and valid(W4)
    assert sorted(parity_group(v) for v in W3) == sorted(p for p in product((0, 1), repeat=3) if sum(p) % 2)
    assert sorted(parity_group(v) for v in W4) == sorted(p for p in product((0, 1), repeat=4) if sum(p) % 2)
    maxima = {}
    for n, cap, expected in [(3, 1, 3), (3, 2, 3), (3, 3, 4),
                              (4, 1, 4), (4, 2, 6), (4, 3, 8)]:
        got = maximum_clique(n, cap)
        assert got == expected, (n, cap, got, expected)
        maxima[(n, cap)] = got
    optimal, nodes = exhaustive_parity_saturation(4, 3)
    assert len(optimal) == 6 and len(set(optimal)) == 6
    assert tuple(sorted(W4)) in optimal
    orbit = {tuple(sorted(tuple(v[i] for i in perm) for v in W4))
             for perm in permutations(range(4))}
    assert len(orbit) == 6 and orbit == set(optimal)
    for n in range(4, 81):
        a, r = divmod(n, 4)
        parts = [W4] * a + ([[(1,)]] if r == 1 else
                             [[(1, 0), (0, 1)]] if r == 2 else
                             [W3] if r == 3 else [])
        family = direct_sum(parts)
        assert valid(family) and len(family) == 8 * a + (0, 1, 2, 4)[r]
        assert len(family) >= 2 * n - 2
    print('VERIFY_OK exact_graph_cases=6 optimal_four_coordinate_families=6 '
          f'group_dfs_nodes={nodes} direct_sum_orders=77 max={maxima}')

if __name__ == '__main__':
    test()
