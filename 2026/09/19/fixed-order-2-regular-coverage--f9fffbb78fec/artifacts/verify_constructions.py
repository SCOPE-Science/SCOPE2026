#!/usr/bin/env python3
"""Verify the explicit sharpness constructions for the fixed-order 2-regular coverage theorem."""

from collections import deque


def add_edge(adj, u, v):
    if u == v or v in adj[u]:
        raise AssertionError("construction is not simple")
    adj[u].add(v)
    adj[v].add(u)


def walecki_cycles(N):
    assert N >= 3 and N % 2 == 1
    m = (N - 1) // 2
    infinity = 2 * m
    base = [infinity, 0]
    for j in range(1, m + 1):
        base.append(2 * m - j)
        if j < m:
            base.append(j)
    assert len(base) == N
    cycles = []
    for shift in range(m):
        cyc = [infinity]
        cyc += [((x + shift) % (2 * m)) for x in base[1:]]
        cycles.append(cyc)
    # Verify that these cycles partition E(K_N).
    seen = set()
    for cyc in cycles:
        for i in range(N):
            e = tuple(sorted((cyc[i], cyc[(i + 1) % N])))
            if e in seen:
                raise AssertionError("Walecki cycles are not edge-disjoint")
            seen.add(e)
    if len(seen) != N * (N - 1) // 2:
        raise AssertionError("Walecki cycles do not cover K_N")
    return cycles


def deficient_block(r, N):
    """Return an r-near-regular block and a spanning Hamilton cycle.

    The distinguished vertex has degree r-1; every other vertex has degree r.
    """
    assert r >= 3 and r % 2 == 1
    assert N >= r + 2 and N % 2 == 1
    cycles = walecki_cycles(N)
    d = (r - 1) // 2
    Hcycles = cycles[:d]
    C = cycles[d]
    distinguished = N - 1  # the Walecki infinity vertex

    adj = [set() for _ in range(N)]
    for cyc in Hcycles:
        for i in range(N):
            add_edge(adj, cyc[i], cyc[(i + 1) % N])

    # Delete distinguished from the next Hamilton cycle and take alternate path edges.
    path = C[1:]
    assert len(path) % 2 == 0
    for i in range(0, len(path), 2):
        add_edge(adj, path[i], path[i + 1])

    degs = [len(a) for a in adj]
    assert degs[distinguished] == r - 1
    assert all(degs[v] == r for v in range(N) if v != distinguished)

    factor = set()
    cyc = Hcycles[0]
    for i in range(N):
        factor.add(tuple(sorted((cyc[i], cyc[(i + 1) % N]))))
    return adj, distinguished, factor


def target_omission(r, n):
    assert r >= 3 and r % 2 == 1 and n % 2 == 0 and n >= r + 1
    a = r * r - 3
    C = 2 * (r + 2)
    return max(0, (n - C) // a)


def construct_extremal(r, n):
    """Construct a connected simple r-regular graph with f_2 = n-t at the theorem's t.

    Returns adjacency, an explicit 2-regular factor on n-t vertices, and t.
    """
    assert r >= 3 and r % 2 == 1 and n % 2 == 0 and n >= r + 1
    t = target_omission(r, n)
    adj = [set() for _ in range(n)]
    factor = set()

    if t == 0:
        d = (r - 1) // 2
        for i in range(n):
            for step in range(1, d + 1):
                j = (i + step) % n
                if j not in adj[i]:
                    add_edge(adj, i, j)
            j = (i + n // 2) % n
            if j not in adj[i]:
                add_edge(adj, i, j)
        for i in range(n):
            factor.add(tuple(sorted((i, (i + 1) % n))))
        return adj, factor, t

    a = r * r - 3
    C = 2 * (r + 2)
    baseline = a * t + C
    extra = n - baseline
    assert 0 <= extra < a and extra % 2 == 0

    # Core is a path on t vertices. Attach enough blocks at each core vertex
    # to raise its total degree to r.
    for i in range(t - 1):
        add_edge(adj, i, i + 1)

    attachment_cores = []
    for i in range(t):
        internal_degree = (1 if i > 0 else 0) + (1 if i + 1 < t else 0)
        attachment_cores.extend([i] * (r - internal_degree))
    expected_blocks = (r - 2) * t + 2
    assert len(attachment_cores) == expected_blocks

    next_v = t
    for b, core in enumerate(attachment_cores):
        N = r + 2 + (extra if b == 0 else 0)
        badj, special, bfactor = deficient_block(r, N)
        offset = next_v
        for u in range(N):
            for v in badj[u]:
                if u < v:
                    add_edge(adj, offset + u, offset + v)
        add_edge(adj, core, offset + special)
        for u, v in bfactor:
            factor.add((offset + u, offset + v))
        next_v += N
    assert next_v == n
    return adj, factor, t


def connected(adj):
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == len(adj)


def bridges(adj):
    n = len(adj)
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    out = []

    def dfs(u, parent):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v in adj[u]:
            if v == parent:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    out.append(tuple(sorted((u, v))))

    dfs(0, -1)
    assert all(x != -1 for x in tin)
    return set(out)


def verify_case(r, n):
    adj, factor, t = construct_extremal(r, n)
    assert len(adj) == n
    assert connected(adj)
    assert all(len(a) == r for a in adj)

    fdeg = [0] * n
    for u, v in factor:
        assert v in adj[u]
        fdeg[u] += 1
        fdeg[v] += 1
    covered = [v for v, d in enumerate(fdeg) if d]
    assert len(covered) == n - t
    assert all(d in (0, 2) for d in fdeg)

    B = bridges(adj)
    if t == 0:
        # The circulant construction is visibly Hamiltonian; bridge count is not needed.
        assert len(covered) == n
    else:
        assert len(B) == (r - 1) * t + 1
        # The t core vertices lie only in the bridge tree, hence no 2-regular
        # subgraph can contain them. This certifies optimality of the explicit factor.
        assert all(fdeg[v] == 0 for v in range(t))
        for v in range(t):
            assert all(tuple(sorted((v, w))) in B for w in adj[v])
    return t


def main():
    cases = 0
    max_t = 0
    for r in (3, 5, 7, 9, 11):
        a = r * r - 3
        C = 2 * (r + 2)
        upper = C + 4 * a - 2
        for n in range(r + 1, upper + 1, 2):
            t = verify_case(r, n)
            cases += 1
            max_t = max(max_t, t)

    # The r=3 specialization agrees arithmetically with the known cubic formula
    # min(n, ceil(5(n+2)/6)) on all tested admissible orders.
    for n in range(4, 500, 2):
        t = target_omission(3, n)
        lhs = n - t
        rhs = min(n, (5 * (n + 2) + 5) // 6)
        assert lhs == rhs

    print("construction verification: PASS")
    print(f"parameter cases checked: {cases}")
    print(f"largest certified omission in the sweep: {max_t}")
    print("degrees/connectivity/bridge counts/explicit 2-regular coverage: PASS")
    print("cubic specialization against the known exact formula through n=498: PASS")


if __name__ == "__main__":
    main()
