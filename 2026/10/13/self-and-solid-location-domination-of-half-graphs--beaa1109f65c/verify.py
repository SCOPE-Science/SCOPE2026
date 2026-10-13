from itertools import combinations


def half_graph(n):
    # A = 0,...,n-1; B = n,...,2n-1; a_i b_j iff i <= j (1-based).
    N = 2*n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for j in range(i, n):
            u, v = i, n+j
            adj[u].add(v)
            adj[v].add(u)
    return adj


def ident(adj, C, u):
    return (adj[u] | {u}) & C


def is_sld(adj, C):
    C = set(C)
    N = len(adj)
    for u in range(N):
        if u in C:
            continue
        I = ident(adj, C, u)
        if not I:
            return False
        inter = set(range(N))
        for c in I:
            inter &= (adj[c] | {c})
        if inter != {u}:
            return False
    return True


def is_dld(adj, C):
    C = set(C)
    outs = [u for u in range(len(adj)) if u not in C]
    ids = {u: ident(adj, C, u) for u in outs}
    if any(not ids[u] for u in outs):
        return False
    for u in outs:
        for v in outs:
            if u != v and ids[u] <= ids[v]:
                return False
    return True


def expected_dld_minima(n):
    V = set(range(2*n))
    out = set()
    for i in range(n):
        for j in range(n):
            # Omitted pair {a_i,b_j}; the two leaf-corner complements fail domination.
            if (i, j) in {(0, 0), (n-1, n-1)}:
                continue
            out.add(frozenset(V - {i, n+j}))
    return out


def expected_sld_minimum(n):
    V = set(range(2*n))
    return frozenset(V - {0, 2*n-1})


print('VERIFY_OK')
subsets_checked = 0
for n in range(2, 9):
    adj = half_graph(n)
    N = 2*n
    dld = []
    sld = []
    for mask in range(1 << N):
        subsets_checked += 1
        C = frozenset(v for v in range(N) if (mask >> v) & 1)
        if is_dld(adj, C):
            dld.append(C)
        if is_sld(adj, C):
            sld.append(C)

    dmin = min(map(len, dld))
    dmins = {C for C in dld if len(C) == dmin}
    expected_d = expected_dld_minima(n)
    assert dmin == 2*n - 2, (n, dmin)
    assert dmins == expected_d, (n, len(dmins), len(expected_d), dmins ^ expected_d)

    smin = min(map(len, sld))
    smins = {C for C in sld if len(C) == smin}
    if n == 2:
        assert smin == 3, (n, smin)
        assert len(smins) == 2, (n, len(smins))
        print(f'n={n}: gamma_DLD={dmin}, DLD_minima={len(dmins)}; boundary gamma_SLD={smin}, SLD_minima={len(smins)}')
    else:
        expected_s = {expected_sld_minimum(n)}
        assert smin == 2*n - 2, (n, smin)
        assert smins == expected_s, (n, len(smins), smins ^ expected_s)
        print(f'n={n}: gamma_DLD=gamma_SLD={2*n-2}, DLD_minima={len(dmins)}, SLD_minima=1')

print('subsets_checked =', subsets_checked)
print('all minimum-code classifications matched the theorem')
