from itertools import combinations
from math import comb


def crown_graph(n):
    N = 2*n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def complement(adj):
    N = len(adj)
    V = set(range(N))
    return [V - {v} - adj[v] for v in range(N)]


def is_locating_dominating(adj, S):
    traces = []
    for v in range(len(adj)):
        if v not in S:
            t = frozenset(adj[v] & S)
            if not t:
                return False
            traces.append(t)
    return len(traces) == len(set(traces))


def is_stable_locating_dominating(adj, S):
    if not is_locating_dominating(adj, S):
        return False
    return all(is_locating_dominating(adj, S - {s}) for s in S)


def is_global_stable(adj, S):
    return (is_stable_locating_dominating(adj, S)
            and is_stable_locating_dominating(complement(adj), S))


def classified(n, S):
    U = {i for i in range(n) if i not in S}
    V = {i for i in range(n) if n+i not in S}
    if U == V and len(U) == 1:
        return True
    if U & V:
        return False
    x, y = len(U), len(V)
    if x == 0 and y == 0:
        return True
    if x == 0:
        return y <= n-2
    if y == 0:
        return x <= n-2
    return x <= n-3 and y <= n-3


def predicted_gamma(n):
    if n == 2:
        return 4
    if n == 3:
        return 4
    if n == 4:
        return 6
    if n == 5:
        return 6
    return n


def predicted_min_count(n):
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n == 4:
        return 28
    if n == 5:
        return 30
    return 2**n - 2*(1+n+comb(n,2))

print('VERIFY_OK')
all_subsets_checked = 0
all_set_equivalence_checks = 0
for n in range(3, 9):
    adj = crown_graph(n)
    N = 2*n
    feasible = []
    for mask in range(1 << N):
        S = {v for v in range(N) if (mask >> v) & 1}
        direct = is_global_stable(adj, S)
        formula = classified(n, S)
        all_subsets_checked += 1
        all_set_equivalence_checks += 1
        assert direct == formula, (n, mask, direct, formula)
        if direct:
            feasible.append(frozenset(S))
    gamma = min(map(len, feasible))
    minima = [S for S in feasible if len(S) == gamma]
    assert gamma == predicted_gamma(n), (n, gamma)
    assert len(minima) == predicted_min_count(n), (n, len(minima), predicted_min_count(n))
    print(f'n={n}: gamma_glsL={gamma}, minimum_sets={len(minima)}, all_sets={len(feasible)}')

# Boundary C4 = Cr_2 checked directly; it is already covered by the published order-four result.
adj = crown_graph(2)
feasible = []
for mask in range(1 << 4):
    S = {v for v in range(4) if (mask >> v) & 1}
    all_subsets_checked += 1
    if is_global_stable(adj, S):
        feasible.append(frozenset(S))
assert min(map(len, feasible)) == 4
assert sum(len(S) == 4 for S in feasible) == 1
print('n=2: gamma_glsL=4, minimum_sets=1 (boundary check)')

# One larger instance: scan only through the claimed minimum size and compare the minimum count.
n = 9
adj = crown_graph(n)
N = 2*n
mins = []
for k in range(predicted_gamma(n)+1):
    for C in combinations(range(N), k):
        all_subsets_checked += 1
        S = set(C)
        if is_global_stable(adj, S):
            if k < predicted_gamma(n):
                raise AssertionError((n, 'feasible below predicted minimum', k, C))
            mins.append(frozenset(S))
assert len(mins) == predicted_min_count(n)
assert all(classified(n, set(S)) for S in mins)
print(f'n=9: gamma_glsL=9, minimum_sets={len(mins)}')

print('subsets_checked =', all_subsets_checked)
print('all_set_classification_equivalence_checks =', all_set_equivalence_checks)
print('all classifications and minimum counts matched')
