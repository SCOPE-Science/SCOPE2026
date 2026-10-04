#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

MAX_ORDER = 9

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for tail in partitions(n - a, a):
            yield (a,) + tail

def build_graph(profile):
    part_of = []
    for i, n in enumerate(profile):
        part_of.extend([i] * n)
    N = len(part_of)
    adj = [[False] * N for _ in range(N)]
    for u in range(N):
        for v in range(u + 1, N):
            if part_of[u] != part_of[v]:
                adj[u][v] = adj[v][u] = True
    return part_of, adj

def connected(vertices, adj):
    U = set(vertices)
    if len(U) <= 1:
        return True
    start = next(iter(U))
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for v in U:
            if v not in seen and adj[u][v]:
                seen.add(v)
                stack.append(v)
    return seen == U

def literal_steiner_interval(W, adj):
    N = len(adj)
    W = frozenset(W)
    rest = tuple(v for v in range(N) if v not in W)
    for total in range(len(W), N + 1):
        union = set()
        found = False
        for extra in combinations(rest, total - len(W)):
            U = W.union(extra)
            if connected(U, adj):
                found = True
                union.update(U)
        if found:
            return frozenset(union)
    raise AssertionError('connected graph must admit a Steiner tree')

def theorem_is_steiner(W, part_of, profile):
    N = len(part_of)
    W = frozenset(W)
    if len(W) == N:
        return True
    touched = {part_of[v] for v in W}
    if len(touched) != 1:
        return False
    i = next(iter(touched))
    return profile[i] >= 2 and len(W) == profile[i]

def theorem_coefficients(profile):
    N = sum(profile)
    c = Counter({N: 1})
    for n in profile:
        if n >= 2:
            c[n] += 1
    return c

def theorem_minmax(profile):
    N = sum(profile)
    nontrivial = [n for n in profile if n >= 2]
    if not nontrivial:
        return N, N
    return min(nontrivial), max(nontrivial)

def main():
    profiles = subset_checks = coefficient_checks = minmax_checks = 0
    steiner_sets_seen = 0
    for N in range(2, MAX_ORDER + 1):
        for profile in partitions(N):
            if len(profile) < 2:
                continue
            profiles += 1
            part_of, adj = build_graph(profile)
            literal_coeff = Counter()
            literal_sets = []
            V = frozenset(range(N))
            for mask in range(1, 1 << N):
                W = frozenset(v for v in range(N) if (mask >> v) & 1)
                literal = literal_steiner_interval(W, adj) == V
                predicted = theorem_is_steiner(W, part_of, profile)
                subset_checks += 1
                if literal != predicted:
                    raise AssertionError(('criterion', profile, sorted(W), literal, predicted))
                if literal:
                    literal_sets.append(W)
                    literal_coeff[len(W)] += 1
            steiner_sets_seen += len(literal_sets)
            predicted_coeff = theorem_coefficients(profile)
            for s in range(1, N + 1):
                coefficient_checks += 1
                if literal_coeff[s] != predicted_coeff[s]:
                    raise AssertionError(('coefficient', profile, s, literal_coeff[s], predicted_coeff[s]))
            # Inclusion-minimal Steiner sets, then lower/upper values.
            minimal = []
            for W in literal_sets:
                if not any(U < W for U in literal_sets):
                    minimal.append(W)
            literal_min = min(map(len, literal_sets))
            literal_upper = max(map(len, minimal))
            predicted_min, predicted_upper = theorem_minmax(profile)
            minmax_checks += 1
            if (literal_min, literal_upper) != (predicted_min, predicted_upper):
                raise AssertionError(('minmax', profile, literal_min, literal_upper, predicted_min, predicted_upper))
    print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} steiner_sets={steiner_sets_seen} coefficient_checks={coefficient_checks} minmax_checks={minmax_checks} max_order={MAX_ORDER}')

if __name__ == '__main__':
    main()
