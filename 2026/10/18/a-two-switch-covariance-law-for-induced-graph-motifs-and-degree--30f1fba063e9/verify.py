"""Exact finite checks for the induced-motif/degree-count covariance law.

Uses exhaustive labeled graphs and rational weights; no external dependencies.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def induced_masks(h, motif_edges):
    base = {frozenset(edge) for edge in motif_edges}
    local_edges = list(combinations(range(h), 2))
    found = set()
    for perm in permutations(range(h)):
        image = {frozenset((perm[i], perm[j])) for i, j in base}
        mask = sum(1 << t for t, e in enumerate(local_edges)
                   if frozenset(e) in image)
        found.add(mask)
    return found


def count_by_total_edges(n, motif_edges, k):
    h = 1 + max(max(edge) for edge in motif_edges)
    graph_edges = list(combinations(range(n), 2))
    positions = {edge: i for i, edge in enumerate(graph_edges)}
    patterns = induced_masks(h, motif_edges)
    subset_patterns = []
    for subset in combinations(range(n), h):
        local = list(combinations(range(h), 2))
        offsets = [positions[(subset[a], subset[b])] for a, b in local]
        graph_masks = {
            sum(1 << offsets[t] for t in range(len(local)) if mask >> t & 1)
            for mask in patterns
        }
        all_edges = sum(1 << off for off in offsets)
        subset_patterns.append((all_edges, graph_masks))

    size = len(graph_edges)
    count = [0] * (size + 1)
    sum_motif = [0] * (size + 1)
    sum_degree = [0] * (size + 1)
    sum_product = [0] * (size + 1)
    for bits in range(1 << size):
        edge_count = bits.bit_count()
        degrees = [0] * n
        for i, (a, b) in enumerate(graph_edges):
            if bits >> i & 1:
                degrees[a] += 1
                degrees[b] += 1
        y = sum(deg == k for deg in degrees)
        x = sum((bits & mask) in patterns_here
                for mask, patterns_here in subset_patterns)
        count[edge_count] += 1
        sum_motif[edge_count] += x
        sum_degree[edge_count] += y
        sum_product[edge_count] += x * y
    return count, sum_motif, sum_degree, sum_product


def weighted(seq, edge_total, p):
    return sum((v * p**m * (1-p)**(edge_total-m)
                for m, v in enumerate(seq)), Fraction(0))


def closed_cov(n, motif_edges, k, p):
    h = 1 + max(max(edge) for edge in motif_edges)
    degrees = [0] * h
    for a, b in motif_edges:
        degrees[a] += 1
        degrees[b] += 1
    types = len(induced_masks(h, motif_edges))
    ex = comb(n, h) * types * p**len(motif_edges) * (1-p)**(comb(h, 2)-len(motif_edges))
    def binmass(trials, successes):
        if not (0 <= successes <= trials):
            return Fraction(0)
        return comb(trials, successes)*p**successes*(1-p)**(trials-successes)
    return ex * (sum(binmass(n-h, k-d) for d in degrees)
                 - h*binmass(n-1, k))


def cycle_closed(n, p):
    return (12*comb(n, 4)*p**4*(1-p)**(n-2)
            * (1-comb(n-1, 2)*p**2*(1-p)))


def main():
    square = ((0, 1), (1, 2), (2, 3), (3, 0))
    path = ((0, 1), (1, 2), (2, 3))
    cases = [(square, 4), (square, 5), (square, 6),
             (path, 5), (path, 6)]
    tests = 0
    for motif, n in cases:
        counts = count_by_total_edges(n, motif, k=2)
        total_edges = comb(n, 2)
        assert sum(counts[0]) == 2**total_edges
        for p in [Fraction(1, 5), Fraction(1, 2), Fraction(9, 10)]:
            weight, x, degree, product = [weighted(arr, total_edges, p)
                                          for arr in counts]
            assert weight == 1
            direct = product - x*degree
            predicted = closed_cov(n, motif, 2, p)
            assert direct == predicted, (motif, n, p, direct, predicted)
            if motif == square:
                assert direct == cycle_closed(n, p)
            tests += 1
    for n in (4, 5):
        for p in (Fraction(1, 5), Fraction(1, 2), Fraction(9, 10)):
            assert cycle_closed(n, p) > 0
    assert cycle_closed(6, Fraction(1, 5)) > 0
    assert cycle_closed(6, Fraction(1, 2)) < 0
    assert cycle_closed(6, Fraction(9, 10)) > 0
    print(f"PASS: {tests} exact exhaustive motif-degree covariance comparisons; "
          "six-vertex three-phase sign example verified")


if __name__ == '__main__':
    main()
