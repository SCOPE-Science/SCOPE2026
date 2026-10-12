from collections import Counter, deque
from math import comb


def windmill(k, m):
    n = 1 + k*m
    adj = [set() for _ in range(n)]
    for i in range(k):
        blade = list(range(1+i*m, 1+(i+1)*m))
        for u in blade:
            adj[0].add(u); adj[u].add(0)
        for a in range(m):
            for b in range(a+1, m):
                u, v = blade[a], blade[b]
                adj[u].add(v); adj[v].add(u)
    return adj


def distances(adj):
    n = len(adj)
    D = [[n+1]*n for _ in range(n)]
    for s in range(n):
        D[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if D[s][v] == n+1:
                    D[s][v] = D[s][u] + 1
                    q.append(v)
    return D


def is_doubly_resolving(mask, D):
    n = len(D)
    S = [v for v in range(n) if (mask >> v) & 1]
    if len(S) < 2:
        return False
    for u in range(n):
        for v in range(u+1, n):
            vals = {D[u][s] - D[v][s] for s in S}
            if len(vals) < 2:
                return False
    return True


def predicted(mask, k, m):
    for i in range(k):
        blade = range(1+i*m, 1+(i+1)*m)
        omitted = sum(1 for v in blade if not ((mask >> v) & 1))
        if omitted > 1:
            return False
    return True


def expected_coefficients(k, m):
    c = Counter()
    base = k*(m-1)
    for full in range(k+1):
        ways = comb(k, full) * (m ** (k-full))
        c[base+full] += ways
        c[base+full+1] += ways
    return c


subset_checks = 0
basis_checks = 0
for k in range(2, 5):
    for m in range(2, 5):
        if 1 + k*m > 13:
            continue
        adj = windmill(k, m)
        D = distances(adj)
        actual = Counter()
        for mask in range(1 << len(adj)):
            subset_checks += 1
            a = is_doubly_resolving(mask, D)
            p = predicted(mask, k, m)
            assert a == p, (k, m, mask, a, p)
            if a:
                actual[mask.bit_count()] += 1
        expected = expected_coefficients(k, m)
        assert actual == expected, (k, m, actual, expected)
        minimum = min(actual)
        assert minimum == k*(m-1)
        assert actual[minimum] == m**k
        basis_checks += actual[minimum]

# Boundary checks show why k>=2 and m>=2 are explicit hypotheses.
# With one blade, meeting the blade in all but one vertex need not distinguish the center
# from the omitted peripheral vertex; with m=1 the per-blade omission rule is vacuous.
for k, m in [(1, 2), (2, 1)]:
    adj = windmill(k, m)
    D = distances(adj)
    assert any(predicted(mask, k, m) != is_doubly_resolving(mask, D)
               for mask in range(1 << len(adj)))

print(f"VERIFY_OK parameter_pairs=8 subset_checks={subset_checks} basis_checks={basis_checks} max_order=13 boundary_checks=2")
