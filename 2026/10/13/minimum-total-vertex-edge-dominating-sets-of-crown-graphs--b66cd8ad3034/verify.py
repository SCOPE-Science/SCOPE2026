from itertools import combinations

def crown(n):
    # A = 0..n-1, B = n..2n-1, missing edges a_i b_i
    N = 2*n
    adj = [set() for _ in range(N)]
    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                u, v = i, n+j
                adj[u].add(v)
                adj[v].add(u)
                edges.append((u,v))
    return adj, edges

def is_total_ve(adj, edges, S):
    S = set(S)
    # total condition: no selected isolated vertex in G[S]
    if not S or any(not (adj[v] & S) for v in S):
        return False
    # ve-domination: every edge has an endpoint in N[S]
    NS = set(S)
    for v in S:
        NS.update(adj[v])
    return all(u in NS or v in NS for u,v in edges)

def expected_minima(n):
    out = set()
    for i,j in combinations(range(n),2):
        for k in range(n):
            if k not in (i,j):
                out.add(frozenset((i,j,n+k)))
                out.add(frozenset((n+i,n+j,k)))
    return out

checked = 0
print("VERIFY_OK")
for n in range(3,9):
    adj, edges = crown(n)
    N = 2*n
    best = N+1
    mins = set()
    for mask in range(1<<N):
        checked += 1
        w = mask.bit_count()
        if w > best:
            continue
        S = frozenset(v for v in range(N) if (mask>>v)&1)
        if is_total_ve(adj, edges, S):
            if w < best:
                best = w
                mins = set()
            mins.add(S)
    expected = expected_minima(n)
    assert best == 3, (n,best)
    assert mins == expected, (n,len(mins),len(expected),mins^expected)
    assert len(mins) == n*(n-1)*(n-2)
    print(f"n={n}: gamma_tve=3, minimum_sets={len(mins)}")
print("subsets_checked =", checked)
print("all minimum sets matched the pairwise-distinct-index classification")
