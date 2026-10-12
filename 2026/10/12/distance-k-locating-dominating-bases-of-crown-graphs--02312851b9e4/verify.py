from itertools import combinations
from collections import deque

def crown_graph(n):
    # A={0,...,n-1}, B={n,...,2n-1}; missing matching a_i b_i.
    N = 2*n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def all_distances(adj):
    D = []
    for s in range(len(adj)):
        d = [10**9]*len(adj)
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] == 10**9:
                    d[v] = d[u] + 1
                    q.append(v)
        D.append(d)
    return D

def resolves_k(D, S, k):
    seen = set()
    for v in range(len(D)):
        sig = tuple(min(D[v][s], k+1) for s in S)
        if sig in seen:
            return False
        seen.add(sig)
    return True

def dominates_k(D, S, k):
    S = set(S)
    for v in range(len(D)):
        if v in S:
            continue
        if min(D[v][s] for s in S) > k:
            return False
    return True

def predicted_basis(n, S, k):
    S = set(S)
    if len(S) != n-1:
        return False
    empty = []
    A = 0
    B = 0
    for i in range(n):
        c = (i in S) + (n+i in S)
        if c == 0:
            empty.append(i)
        elif c == 1:
            if i in S:
                A += 1
            else:
                B += 1
        else:
            return False
    if len(empty) != 1:
        return False
    if k >= 2:
        return True
    return A >= 2 and B >= 2

subset_trials = 0
basis_trials = 0

for n in range(5, 9):
    adj = crown_graph(n)
    D = all_distances(adj)
    for k in (1, 2, 3):
        target = n - 1

        for r in range(target):
            for S in combinations(range(2*n), r):
                subset_trials += 1
                assert not (resolves_k(D, S, k) and dominates_k(D, S, k)), (n, k, r, S)

        actual = set()
        for S in combinations(range(2*n), target):
            subset_trials += 1
            good = resolves_k(D, S, k) and dominates_k(D, S, k)
            pred = predicted_basis(n, S, k)
            assert good == pred, (n, k, S, good, pred)
            if good:
                actual.add(S)

        if k == 1:
            expected_count = n * (2**(n-1) - 2*n)
        else:
            expected_count = n * 2**(n-1)
        assert len(actual) == expected_count, (n, k, len(actual), expected_count)
        basis_trials += len(actual)

print("VERIFY_OK")
print("crown_parameters_checked =", 4)
print("parameters n = 5..8")
print("distance_ranges_checked = 1,2,3")
print("subset_trials =", subset_trials)
print("minimum_bases_checked =", basis_trials)
print("all smaller sets failed")
print("all minimum sets matched the structural classifications")
print("k=1 counts matched n(2^(n-1)-2n)")
print("k>=2 counts matched n*2^(n-1)")
