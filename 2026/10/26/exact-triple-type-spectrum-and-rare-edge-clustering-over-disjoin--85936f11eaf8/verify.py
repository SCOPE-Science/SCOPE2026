"""Independent finite checks for clique-free tuple-type spectra.

Run with Python 3.9 or later; uses only the standard library.
The tests check finite cases, not the general asymptotic proof.
"""
from itertools import combinations, product
from math import comb
import random


def graph_edges(k):
    pairs = list(combinations(range(k), 2))
    for bits in range(1 << len(pairs)):
        yield tuple(pair for j, pair in enumerate(pairs) if bits >> j & 1)


def has_clique(vertices, edges, clique_size):
    graph = set(edges)
    for subset in combinations(range(vertices), clique_size):
        if all((u, v) in graph for u, v in combinations(subset, 2)):
            return True
    return False


def block_graph_edges(r, k, edges, masks, blocks=1):
    result = set(edges)
    # The tuple vertices are numbered 0,...,k-1.
    for block_index in range(blocks):
        base = k + block_index * r
        for a, c in combinations(range(r), 2):
            result.add((base + a, base + c))
        for tuple_index in range(k):
            mask = masks[block_index * k + tuple_index]
            for j in range(r):
                if mask >> j & 1:
                    result.add((tuple_index, base + j))
    return result


def admissible_via_graph(r, k, H, masks):
    n = r + k
    E = block_graph_edges(r, k, H, masks)
    return not has_clique(n, E, r + 1)


def admissible_via_common_neighbors(r, k, H, masks):
    edges = set(H)
    for s in range(1, min(k, r) + 1):
        for subset in combinations(range(k), s):
            if any((u, v) not in edges for u, v in combinations(subset, 2)):
                continue
            common = (1 << r) - 1
            for i in subset:
                common &= masks[i]
            if common.bit_count() > r - s:
                return False
    return True


def local_count(r, k, H, method):
    return sum(method(r, k, H, masks) for masks in product(range(1 << r), repeat=k))


def closed_bases(r, k):
    a = (1 << r) - 1
    return (a ** k,
            a ** k - r * a ** (k - 2),
            a ** k - 2 * r * a ** (k - 2) + r * a ** (k - 3))


def triangle_base(r):
    a = (1 << r) - 1
    return a ** 3 - 3 * r * a + 2 * r - 13 * comb(r, 2)


def run():
    explicit_graph_cases = 0
    profile_cases = 0
    for r, k in ((3, 3), (3, 4), (4, 3)):
        candidates = []
        for H in graph_edges(k):
            if has_clique(k, H, r + 1):
                continue
            c0 = local_count(r, k, H, admissible_via_graph)
            c1 = local_count(r, k, H, admissible_via_common_neighbors)
            assert c0 == c1, (r, k, H, c0, c1)
            candidates.append((H, c0))
            profile_cases += 1
            explicit_graph_cases += (1 << (r * k))
        a0, a1, a2 = closed_bases(r, k)
        for H, count in candidates:
            if len(H) == 0:
                assert count == a0
            elif len(H) == 1:
                assert count == a1
            elif len(H) == 2 and len(set(u for e in H for u in e)) == 3:
                assert count == a2
            else:
                assert count <= a2 - 1, (r, k, H, count, a2)
    # Independent larger-r 3-tuple count via the common-neighbor rule.
    for r in (5, 6):
        v = local_count(r, 3, ((0, 1), (0, 2), (1, 2)), admissible_via_common_neighbors)
        assert v == triangle_base(r), (r, v)
    for r in (3, 4, 5):
        b0, b1, b2 = closed_bases(r, 3)
        b3 = triangle_base(r)
        assert b0 > b1 > b2 > b3 >= 0
        for blocks in (1, 2, 3):
            closed = b0 ** blocks + 3 * b1 ** blocks + 3 * b2 ** blocks + b3 ** blocks
            by_graphs = 0
            for H in graph_edges(3):
                c = local_count(r, 3, H, admissible_via_common_neighbors)
                by_graphs += c ** blocks
            assert closed == by_graphs
    # Direct graph checks on two independent parameter cliques.
    rng = random.Random(40157)
    for H in graph_edges(3):
        for trial in range(600):
            masks = tuple(rng.randrange(8) for _ in range(6))
            E = block_graph_edges(3, 3, H, masks, blocks=2)
            brute = not has_clique(9, E, 4)
            factored = (admissible_via_common_neighbors(3, 3, H, masks[:3])
                        and admissible_via_common_neighbors(3, 3, H, masks[3:]))
            assert brute == factored, (H, masks)
    print('EXPLICIT_LOCAL_ASSIGNMENTS', explicit_graph_cases)
    print('LOCAL_GRAPH_PROFILES', profile_cases)
    print('DIRECT_TWO_BLOCK_SAMPLES', 8 * 600)
    print('TRIPLE_EXACT_CHECKS', 3 * 3)
    print('EXACT_K4_FREE_TRIPLE_BASES', 343, 322, 304, 247)
    print('ALL_TESTS_PASS')

if __name__ == '__main__':
    run()
