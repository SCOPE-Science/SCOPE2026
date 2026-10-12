from itertools import combinations
from collections import deque

def book_graph(r):
    n = 2 + 2*r
    adj = [set() for _ in range(n)]
    adj[0].add(1); adj[1].add(0)
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        for u,v in ((0,a),(a,b),(b,1)):
            adj[u].add(v); adj[v].add(u)
    return adj

def all_distances(adj):
    n = len(adj)
    D = []
    for s in range(n):
        d = [10**9]*n
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

def is_outer_multiset_resolving(D, S):
    S = set(S)
    seen = set()
    for v in range(len(D)):
        if v in S:
            continue
        sig = tuple(sorted(D[v][s] for s in S))
        if sig in seen:
            return False
        seen.add(sig)
    return True

def predicted_basis_complement(r, U):
    U = set(U)
    x, y = 0, 1
    spine = [v for v in (x,y) if v in U]

    full = []
    a_only = []
    b_only = []
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        ina, inb = a in U, b in U
        if ina and inb:
            full.append(i)
        elif ina:
            a_only.append(i)
        elif inb:
            b_only.append(i)

    if len(spine) == 2:
        return len(full) == 1 and (
            (len(a_only) == 1 and len(b_only) == 0) or
            (len(a_only) == 0 and len(b_only) == 1)
        )

    if len(spine) == 1 and r >= 4:
        return len(full) == 1 and len(a_only) == 1 and len(b_only) == 1

    return False

graphs = 0
subsets_checked = 0
bases_checked = 0

for r in range(3, 10):
    adj = book_graph(r)
    D = all_distances(adj)
    n = len(adj)
    target = 2*r - 3

    # No smaller set resolves.
    for k in range(target):
        for S in combinations(range(n), k):
            subsets_checked += 1
            assert not is_outer_multiset_resolving(D, S), (r, k, S)

    actual = set()
    for S in combinations(range(n), target):
        subsets_checked += 1
        if is_outer_multiset_resolving(D, S):
            actual.add(frozenset(S))

    predicted = set()
    for U in combinations(range(n), 5):
        if predicted_basis_complement(r, U):
            S = frozenset(set(range(n)) - set(U))
            predicted.add(S)

    assert actual == predicted, (r, len(actual), len(predicted))

    expected_count = 12 if r == 3 else 2*r*(r-1)**2
    assert len(actual) == expected_count, (r, len(actual), expected_count)

    bases_checked += len(actual)
    graphs += 1

print("VERIFY_OK")
print("book_parameters_checked =", graphs)
print("vertex_subsets_checked =", subsets_checked)
print("minimum_outer_multiset_bases_checked =", bases_checked)
print("parameters r = 3..9")
print("all smaller landmark sets failed directly")
print("all bases matched the complement classification")
print("all basis counts matched the closed formula")
