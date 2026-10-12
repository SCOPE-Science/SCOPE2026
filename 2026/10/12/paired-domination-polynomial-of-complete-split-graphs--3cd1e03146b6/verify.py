from itertools import combinations
from math import comb
from collections import Counter


def complete_split(r, n):
    N = r + n
    adj = [set() for _ in range(N)]
    for i in range(r):
        for j in range(i + 1, r):
            adj[i].add(j); adj[j].add(i)
    for i in range(r):
        for j in range(r, N):
            adj[i].add(j); adj[j].add(i)
    return adj


def dominates(S, adj):
    S = set(S)
    return all(v in S or bool(adj[v] & S) for v in range(len(adj)))


def has_perfect_matching(S, adj):
    S = tuple(sorted(S))
    if len(S) % 2:
        return False
    if not S:
        return True
    v = S[0]
    rest = set(S[1:])
    for w in tuple(rest):
        if w in adj[v] and has_perfect_matching(tuple(sorted(rest - {w})), adj):
            return True
    return False


def paired_dominating(S, adj):
    return dominates(S, adj) and has_perfect_matching(S, adj)


def criterion(S, r):
    a = sum(v < r for v in S)
    b = len(S) - a
    return a >= 1 and b <= a and (a + b) % 2 == 0


def predicted_coefficients(r, n):
    out = Counter()
    for a in range(1, r + 1):
        for b in range(0, min(a, n) + 1):
            if (a + b) % 2 == 0:
                out[a + b] += comb(r, a) * comb(n, b)
    return out

subset_checks = 0
criterion_checks = 0
coefficient_checks = 0
minimal_checks = 0
for r in range(1, 8):
    for n in range(1, 8):
        adj = complete_split(r, n)
        N = r + n
        actual = Counter()
        paired_sets = []
        for mask in range(1 << N):
            S = tuple(v for v in range(N) if (mask >> v) & 1)
            got = paired_dominating(S, adj)
            want = criterion(S, r)
            subset_checks += 1
            criterion_checks += 1
            assert got == want, (r, n, S, got, want)
            if got:
                actual[len(S)] += 1
                paired_sets.append(S)
        predicted = predicted_coefficients(r, n)
        assert actual == predicted, (r, n, actual, predicted)
        coefficient_checks += len(set(actual) | set(predicted))
        assert min(actual) == 2
        assert actual[2] == comb(r, 2) + r * n
        for S in paired_sets:
            if len(S) > 2:
                assert any(paired_dominating(T, adj) for T in combinations(S, 2)), (r, n, S)
            minimal_checks += 1
print(
    'VERIFY_OK '
    f'r_range=1..7 n_range=1..7 subset_checks={subset_checks} '
    f'criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} '
    f'paired_set_minimality_checks={minimal_checks} max_order=14'
)
