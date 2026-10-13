"""Exhaustive small-case check of strong-domination deletion robustness.
No third-party dependencies. Runs as: python verify.py
"""
from itertools import combinations
from functools import lru_cache
from math import comb


def profiles(total, low=1):
    if total == 0:
        yield ()
    for x in range(low, total + 1):
        if x == total:
            yield (x,)
        else:
            for rest in profiles(total - x, x):
                yield (x,) + rest


@lru_cache(None)
def graph_gamma(part_sizes):
    """Compute the minimum directly from the vertex-level definition."""
    n = sum(part_sizes)
    if n == 0:
        return 0
    group = tuple(i for i, count in enumerate(part_sizes) for _ in range(count))
    degrees = tuple(n - part_sizes[i] for i in group)
    witness_mask = []
    for v in range(n):
        mask = 1 << v
        for u in range(n):
            if group[u] != group[v] and degrees[u] >= degrees[v]:
                mask |= 1 << u
        witness_mask.append(mask)
    for k in range(1, n + 1):
        for subset in combinations(range(n), k):
            chosen = sum(1 << v for v in subset)
            if all(chosen & mask for mask in witness_mask):
                return k
    assert False


def expected_gamma(a):
    if not a:
        return 0
    if len(a) == 1:
        return a[0]
    s = min(a)
    if s == 1:
        return 1
    return 2 if a.count(s) >= 2 else s


def expected_stability(a):
    s = min(a)
    t = a.count(s)
    if s == 1:
        return t
    if s == 3 and t >= 2:
        return 2
    return 1


def expected_min_witness_count(a):
    s = min(a)
    t = a.count(s)
    if s == 1:
        return 1
    if t >= 2:
        return 3 * t if s == 3 else s * t
    return s + ((s + 1) * a.count(s + 1) if s >= 3 else 0)


def actual_stability_and_count(a):
    n = sum(a)
    group = tuple(i for i, count in enumerate(a) for _ in range(count))
    base = graph_gamma(a)
    for k in range(1, n + 1):
        good = 0
        for picked in combinations(range(n), k):
            remaining = list(a)
            for v in picked:
                remaining[group[v]] -= 1
            surviving = tuple(sorted(c for c in remaining if c))
            if graph_gamma(surviving) != base:
                good += 1
        if good:
            return k, good
    raise AssertionError(a)


def main():
    cases = 0
    deletions = 0
    examples = {}
    for n in range(2, 12):
        for a in profiles(n):
            if len(a) < 2:
                continue
            cases += 1
            if graph_gamma(a) != expected_gamma(a):
                raise AssertionError(('gamma', a, graph_gamma(a), expected_gamma(a)))
            st, count = actual_stability_and_count(a)
            deletions += sum(comb(n, k) for k in range(1, st + 1))
            predicted = (expected_stability(a), expected_min_witness_count(a))
            if (st, count) != predicted:
                raise AssertionError(('stability/count', a, (st, count), predicted))
            if a in {(3,3), (3,3,3), (4,4,4), (1,1,2), (2,3,4), (3,4,4)}:
                examples[a] = (graph_gamma(a), st, count)
    assert graph_gamma((4, 4, 4)) == 2
    assert graph_gamma((3, 4, 4)) == 3
    assert graph_gamma((3, 3, 3)) == 2
    assert graph_gamma((1, 3, 3)) == 1
    print('ALL CHECKS PASSED; multipartite_profiles=%s; max_order=11;'
          ' inspected_deletion_subsets=%s; cached_remaining_profiles=%s;'
          ' critical_witness_counts=yes' % (cases, deletions, graph_gamma.cache_info().currsize))
    print('special: (4,4,4)->(3,4,4), gamma 2->3; (3,3,3)->(1,3,3), gamma 2->1')
    for a in sorted(examples):
        print('part_sizes=%s gamma/stability/witnesses=%s' % (a, examples[a]))


if __name__ == '__main__':
    main()
