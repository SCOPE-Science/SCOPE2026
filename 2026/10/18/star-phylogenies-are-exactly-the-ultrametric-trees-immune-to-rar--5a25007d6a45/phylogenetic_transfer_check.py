"""Exact independent checks for a phylogenetic-rarefaction abundance-transfer theorem.

Requires Python 3 and the standard library only. All computations are rational.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def detected(N, mass, sample_size):
    """Probability that a size-sample contains a member of a given clade."""
    assert 0 <= mass <= N and 1 <= sample_size <= N
    absent = comb(N - mass, sample_size) if sample_size <= N-mass else 0
    return 1 - Q(absent, comb(N, sample_size))


def mean_pd_by_clades(counts, sample_size, edges):
    """Edges are pairs (set of descendants, rational branch length)."""
    N = sum(counts)
    return sum((length * detected(N, sum(counts[t] for t in descendants),
                                  sample_size) for descendants, length in edges), Q(0))


def mean_pd_direct(counts, sample_size, edges):
    """Enumerate labeled subsets, rather than reusing the detection formula."""
    organisms = tuple(t for t, abundance in enumerate(counts)
                      for _ in range(abundance))
    tot = Q(0)
    for chosen in combinations(range(len(organisms)), sample_size):
        observed = {organisms[z] for z in chosen}
        tot += sum((length for descendants, length in edges
                    if observed.intersection(descendants)), Q(0))
    return tot / comb(len(organisms), sample_size)


def all_partitions(items):
    """Generate partitions of a finite labeled species set."""
    if not items:
        yield ()
        return
    for blocks in all_partitions(items[:-1]):
        item = items[-1]
        yield blocks + (frozenset([item]),)
        for idx in range(len(blocks)):
            replacement = list(blocks)
            replacement[idx] = replacement[idx] | frozenset([item])
            yield tuple(replacement)


def cut_gain(original, improved, sample_size, partition):
    N = sum(original)
    assert sum(improved) == N
    return sum((detected(N, sum(improved[t] for t in block), sample_size)
                - detected(N, sum(original[t] for t in block), sample_size)
                for block in partition), Q(0))


def verify_minimality():
    """All feasible populations <=5, transfers, and possible ultrametric cuts."""
    checked = 0
    for N in range(2, 6):
        for s in range(2, N + 1):
            # Positive labeled profiles: exact finite compositions.
            def compositions(n, length):
                if length == 1:
                    if n >= 1:
                        yield (n,)
                    return
                for first in range(1, n - length + 2):
                    for rest in compositions(n - first, length - 1):
                        yield (first,) + rest
            for counts in compositions(N, s):
                for i in range(s):
                    for j in range(s):
                        if counts[i] < counts[j] + 2:
                            continue
                        improved = list(counts)
                        improved[i] -= 1
                        improved[j] += 1
                        for m in range(1, N + 1):
                            for partition in all_partitions(tuple(range(s))):
                                gain = cut_gain(counts, improved, m, partition)
                                assert gain >= 0, (counts, i, j, m, partition, gain)
                                checked += 1
    assert checked > 0
    return checked


def main():
    eps = Q(1, 3)
    edges = ((frozenset((0,)), Q(1)),
             (frozenset((1, 2)), Q(2, 3)),
             (frozenset((1,)), eps),
             (frozenset((2,)), eps))
    before, after = (3, 1, 2), (2, 2, 2)
    expected = (Q(0), -Q(1, 45), -Q(1, 60), Q(1, 45), Q(1, 18), Q(0))
    for m, target in enumerate(expected, start=1):
        e_before = mean_pd_by_clades(before, m, edges)
        e_after = mean_pd_by_clades(after, m, edges)
        assert e_before == mean_pd_direct(before, m, edges)
        assert e_after == mean_pd_direct(after, m, edges)
        assert e_after-e_before == target, (m, e_before, e_after, target)
    # Coefficients over the entire cherry-length interval 0 <= eps <= 1.
    variable_expected = ((Q(0), Q(0)), (-Q(1, 15), Q(2, 15)),
                         (-Q(1, 10), Q(1, 4)), (-Q(1, 15), Q(4, 15)),
                         (Q(0), Q(1, 6)), (Q(0), Q(0)))
    for e in (Q(0), Q(1, 7), Q(1, 3), Q(9, 10), Q(1)):
        edge_set = ((frozenset((0,)), Q(1)),
                    (frozenset((1, 2)), Q(1) - e),
                    (frozenset((1,)), e), (frozenset((2,)), e))
        for m, (intercept, slope) in enumerate(variable_expected, start=1):
            difference = (mean_pd_by_clades(after, m, edge_set)
                          - mean_pd_by_clades(before, m, edge_set))
            assert difference == intercept + slope*e
    # Weakly resolved nonstar with a much larger third-species population.
    e = Q(9, 10)
    edges_large = ((frozenset((0,)), Q(1)),
                   (frozenset((1, 2)), Q(1)-e),
                   (frozenset((1,)), e), (frozenset((2,)), e))
    a, b = (3, 1, 31), (2, 2, 31)
    assert mean_pd_by_clades(b, 2, edges_large) < mean_pd_by_clades(a, 2, edges_large)
    assert (mean_pd_by_clades(b, 34, edges_large)
            - mean_pd_by_clades(a, 34, edges_large)) == Q(9, 350)
    nchecked = verify_minimality()
    print('PASS: exact six-individual example at every sample depth')
    print('PASS: independent enumeration of all 6-individual subsets')
    print('PASS: exact parameter-dependent six-individual identities')
    print('PASS: arbitrarily weak three-tip phylogenetic clustering witness')
    print(f'PASS: {nchecked} exact small-population cut comparisons')


if __name__ == '__main__':
    main()
