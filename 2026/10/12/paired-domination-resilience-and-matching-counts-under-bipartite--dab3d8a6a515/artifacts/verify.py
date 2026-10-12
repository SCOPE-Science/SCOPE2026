"""Independent exhaustive paired-domination and matching-count checks.

Run: python artifacts/verify.py
"""
from itertools import combinations
from math import comb, factorial


def graph(m, n, t):
    # Deleted edges are (a_i, b_i) for 0 <= i < t.
    adj = [set() for _ in range(m + n)]
    for i in range(m):
        for j in range(n):
            if i == j and i < t:
                continue
            adj[i].add(m + j)
            adj[m + j].add(i)
    return adj


def dominates(adj, subset):
    selected = set(subset)
    return all(v in selected or any(u in selected for u in adj[v])
               for v in range(len(adj)))


def matching_number(adj, subset):
    selected = set(subset)
    if len(subset) % 2:
        return 0
    if not subset:
        return 1
    v = min(subset)
    count = 0
    for u in sorted(adj[v] & selected):
        rem = tuple(sorted(selected - {v, u}))
        count += matching_number(adj, rem)
    return count


def is_paired_direct(adj, subset):
    return bool(subset) and dominates(adj, subset) and matching_number(adj, subset) > 0


def is_paired_formula(m, n, t, subset):
    A = [v for v in subset if v < m]
    B = [v - m for v in subset if v >= m]
    if len(A) != len(B):
        return False
    s = len(A)
    if s >= 2:
        return True
    if s == 1:
        return A[0] >= t and B[0] >= t
    return False


def polynomial_formula(m, n, t):
    d = {2: (m - t) * (n - t)}
    for s in range(2, min(m, n) + 1):
        d[2*s] = comb(m, s) * comb(n, s)
    return d


def matching_formula(m, n, t, s):
    return sum((-1)**j * comb(t, j) * comb(m-j, s-j) *
               comb(n-j, s-j) * factorial(s-j)
               for j in range(min(t, s) + 1))


profiles = 0
subsets = 0
all_direct_matching_instances = 0
for m in range(2, 7):
    for n in range(2, 7):
        for t in range(min(m, n) + 1):
            profiles += 1
            adj = graph(m, n, t)
            observed = {2*s: 0 for s in range(1, min(m, n) + 1)}
            pairing_count = {2*s: 0 for s in range(1, min(m, n) + 1)}
            N = m + n
            for bitmask in range(1 << N):
                subsets += 1
                selected = tuple(i for i in range(N) if (bitmask >> i) & 1)
                direct = is_paired_direct(adj, selected)
                predicted = is_paired_formula(m, n, t, selected)
                assert direct == predicted, (m, n, t, selected, direct, predicted)
                if direct:
                    s = len(selected)
                    observed[s] += 1
                    q = matching_number(adj, selected)
                    assert q >= 1
                    pairing_count[s] += q
                    all_direct_matching_instances += q
            assert observed == polynomial_formula(m, n, t), (m, n, t, observed)
            for s in range(2, min(m, n) + 1):
                assert pairing_count[2*s] == matching_formula(m, n, t, s), (
                    m, n, t, s, pairing_count[2*s], matching_formula(m, n, t, s))
            assert pairing_count[2] == (m - t)*(n - t)

print(f"ALL CHECKS PASSED; profiles={profiles}; subsets_checked={subsets}; "
      f"paired_set_matching_pairs_checked={all_direct_matching_instances}; "
      "m,n=2..6; all matching deletions")
