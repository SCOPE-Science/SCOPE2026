from itertools import combinations
from math import comb


def adjacency(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def is_k_power_dominating(n, k, chosen):
    adj = adjacency(n)
    observed = set(chosen)
    for v in chosen:
        observed.update(adj[v])
    while True:
        add = set()
        for v in observed:
            unobserved = adj[v] - observed
            if 0 < len(unobserved) <= k:
                add.update(unobserved)
        if not add:
            break
        observed.update(add)
    return len(observed) == 2*n


def predicted(n, k, chosen):
    a = sum(v < n for v in chosen)
    b = len(chosen) - a
    h = max(1, n-k-1)
    return ((a >= 1 and b >= 1) or
            (b == 0 and a >= h) or
            (a == 0 and b >= h))


def polynomial_coefficients(n, k):
    h = max(1, n-k-1)
    coeff = [0]*(2*n+1)
    # mixed sets
    for a in range(1, n+1):
        for b in range(1, n+1):
            coeff[a+b] += comb(n, a)*comb(n, b)
    # one-sided sets
    for t in range(h, n+1):
        coeff[t] += 2*comb(n, t)
    return coeff

subset_checks = 0
minimum_checks = 0
parameter_pairs = 0
for n in range(3, 9):
    for k in range(1, n+1):
        parameter_pairs += 1
        actual_counts = [0]*(2*n+1)
        for mask in range(1 << (2*n)):
            chosen = {v for v in range(2*n) if (mask >> v) & 1}
            actual = is_k_power_dominating(n, k, chosen)
            want = predicted(n, k, chosen)
            subset_checks += 1
            if actual != want:
                raise AssertionError((n, k, sorted(chosen), actual, want))
            if actual:
                actual_counts[len(chosen)] += 1
        expected_counts = polynomial_coefficients(n, k)
        if actual_counts != expected_counts:
            raise AssertionError((n, k, actual_counts, expected_counts))
        h = max(1, n-k-1)
        gamma = next(i for i, c in enumerate(actual_counts) if c)
        expected_gamma = 1 if k >= n-2 else 2
        if gamma != expected_gamma:
            raise AssertionError((n, k, gamma, expected_gamma))
        expected_min = (2*n if k >= n-2 else
                        comb(2*n, 2) if k == n-3 else
                        n*n)
        if actual_counts[gamma] != expected_min:
            raise AssertionError((n, k, actual_counts[gamma], expected_min))
        minimum_checks += 1

# Explicitly verify a small counterexample to the n-k lower bound reported in 2019.
if not is_k_power_dominating(5, 1, {0, 5+1}):
    raise AssertionError('counterexample failed')

print(
    'VERIFY_OK '
    f'n_range=3..8 parameter_pairs={parameter_pairs} '
    f'subset_checks={subset_checks} minimum_checks={minimum_checks} '
    'counterexample=n5_k1_mixed_pair'
)
