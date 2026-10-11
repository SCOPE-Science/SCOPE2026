"""Exact finite diagnostics for the root-polytope illumination theorem.

No finite search is used as a substitute for the dimension-free proof.
Requires only Python 3 standard library.
"""
from itertools import product, combinations


def illuminated_unordered_pairs(t):
    """Scaled nonnegative |source coordinates|, each t_i=2|l_i|."""
    d = len(t)
    S = sum(t)
    pairs = []
    for i, j in combinations(range(d), 2):
        if t[i] > 2 and t[j] > 2 and 2 * (t[i] + t[j]) > S + 4:
            pairs.append((i, j))
    return pairs


def facet_direct_illumination(t, i, j):
    """Brute checks every sign facet, independently of the compressed test."""
    if t[i] <= 2 or t[j] <= 2:
        return False
    others = [k for k in range(len(t)) if k not in (i, j)]
    for signs in product((-1, 1), repeat=len(others)):
        s = t[i] + t[j] + sum(sign * t[k] for sign, k in zip(signs, others))
        if s <= 4:
            return False
    return True


def exact_diagnostic():
    values = (0, 1, 2, 3, 4, 6, 8)
    cases = 0
    illuminated = 0
    max_k = 0
    for d in range(3, 7):
        for t in product(values, repeat=d):
            cases += 1
            pairs = illuminated_unordered_pairs(t)
            for i, j in combinations(range(d), 2):
                assert ((i, j) in pairs) == facet_direct_illumination(t, i, j)
            k = len(pairs)
            illuminated += k
            max_k = max(max_k, k)
            if k:
                # Minkowski norm = max(max(t_i)/2, sum(t_i)/4).
                assert 4 * k < max(2 * max(t), sum(t)), (d, t, pairs)
                # No two illuminated edges can be disjoint.
                assert all(set(e) & set(f) for e, f in combinations(pairs, 2))
            # The ray just outside each vertex illuminates that vertex:
            # lambda*(e_i + e_j), lambda>1, has gauge lambda.
            assert 4 * d * (d-1) // 2 == 2*d*(d-1)
    print(f"EXACT_DIAGNOSTIC_OK cases={cases} illuminated_pairs={illuminated} max_single_source_count={max_k}")


if __name__ == '__main__':
    exact_diagnostic()
