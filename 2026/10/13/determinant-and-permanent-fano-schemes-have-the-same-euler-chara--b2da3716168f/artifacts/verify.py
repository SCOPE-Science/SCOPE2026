from itertools import combinations, permutations
from math import comb


def max_matching(m, n, edges):
    adj = [[] for _ in range(m)]
    for i, j in edges:
        adj[i].append(j)
    best = 0
    def rec(i, used, count):
        nonlocal best
        if i == m:
            best = max(best, count)
            return
        if count + (m - i) <= best:
            return
        rec(i + 1, used, count)
        for j in adj[i]:
            if not (used >> j) & 1:
                rec(i + 1, used | (1 << j), count + 1)
    rec(0, 0, 0)
    return best


def has_permutation_support(m, n, r, edges):
    E = set(edges)
    for rows in combinations(range(m), r):
        for cols in combinations(range(n), r):
            for p in permutations(cols):
                if all((rows[a], p[a]) in E for a in range(r)):
                    return True
    return False


def count_by_q(m, n, r, max_q=None):
    all_edges = [(i, j) for i in range(m) for j in range(n)]
    if max_q is None:
        max_q = len(all_edges)
    counts = {}
    checked = 0
    for q in range(0, min(max_q, len(all_edges)) + 1):
        c = 0
        for subset in combinations(all_edges, q):
            nu = max_matching(m, n, subset)
            alt = has_permutation_support(m, n, r, subset)
            assert (nu >= r) == alt
            if nu < r:
                c += 1
            checked += 1
        counts[q] = c
    return counts, checked

checked_subsets = 0
checked_parameter_slices = 0

for m, n in [(2,2), (2,3), (2,4), (3,3), (3,4), (3,5), (4,4)]:
    for r in range(2, m + 1):
        # Enough q-values to cross the first meaningful Fano levels while
        # keeping the explicit subset census small.
        max_q = min(m*n, 6)
        counts, c = count_by_q(m, n, r, max_q)
        checked_subsets += c
        checked_parameter_slices += 1

        # Extremal threshold: once q exceeds (r-1)n, no admissible subset exists.
        for q, val in counts.items():
            if q > (r - 1) * n:
                assert val == 0

        if r == 2:
            for q in range(2, max_q + 1):
                star = m * comb(n, q) + n * comb(m, q)
                assert counts[q] == star, (m, n, q, counts[q], star)

# Independently check the extremal threshold on all subsets for modest boards.
threshold_checks = 0
for m, n, r in [(2,5,2), (3,4,2), (3,4,3), (3,5,3)]:
    edges = [(i,j) for i in range(m) for j in range(n)]
    q = (r - 1) * n + 1
    if q <= len(edges):
        for subset in combinations(edges, q):
            assert max_matching(m, n, subset) >= r
            threshold_checks += 1

assert checked_parameter_slices >= 10
assert checked_subsets > 10000
assert threshold_checks > 0
print('VERIFY_OK', checked_parameter_slices, checked_subsets, threshold_checks)
