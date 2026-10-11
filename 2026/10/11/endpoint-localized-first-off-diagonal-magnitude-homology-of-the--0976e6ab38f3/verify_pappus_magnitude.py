#!/usr/bin/env python3
"""Exact verification of endpoint-localized magnitude homology for the Pappus graph.

The graph is constructed from the LCF notation [5,7,-7,7,-7,-5]^3.
All chain groups and boundary ranks are computed over F_2 from the graph metric.
No third-party packages are used.
"""
from collections import deque, defaultdict
from itertools import product

N = 18
LCF = [5, 7, -7, 7, -7, -5] * 3


def build_graph():
    adj = [set() for _ in range(N)]
    for i in range(N):
        j = (i + 1) % N
        adj[i].add(j); adj[j].add(i)
    for i, s in enumerate(LCF):
        j = (i + s) % N
        adj[i].add(j); adj[j].add(i)
    return [tuple(sorted(a)) for a in adj]


def all_distances(adj):
    D = []
    for s in range(N):
        dist = [-1] * N
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    q.append(v)
        assert all(d >= 0 for d in dist)
        D.append(dist)
    return D


def girth(adj):
    best = 10**9
    for root in range(N):
        dist = [-1] * N
        parent = [-1] * N
        dist[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif parent[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


def chains(k, ell, D, start=None, end=None):
    """Tuples (x0,...,xk), consecutive entries distinct, total length ell."""
    out = []
    starts = range(N) if start is None else (start,)
    def rec(tup, total):
        if len(tup) == k + 1:
            if total == ell and (end is None or tup[-1] == end):
                out.append(tup)
            return
        last = tup[-1]
        for v in range(N):
            if v == last:
                continue
            nt = total + D[last][v]
            if nt <= ell:
                rec(tup + (v,), nt)
    for s in starts:
        rec((s,), 0)
    return out


def boundary_columns(domain, codomain_index, D):
    """Boundary columns as Python-int bitsets over F_2."""
    cols = []
    for tup in domain:
        bits = 0
        # delete interior point i when smooth: length preserved
        for i in range(1, len(tup) - 1):
            a, b, c = tup[i-1], tup[i], tup[i+1]
            if D[a][b] + D[b][c] == D[a][c]:
                face = tup[:i] + tup[i+1:]
                bits ^= 1 << codomain_index[face]
        cols.append(bits)
    return cols


def rank_bitcols(cols):
    basis = {}
    for x in cols:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in basis:
                y ^= basis[p]
            else:
                basis[p] = y
                break
    return len(basis)


def apply_boundary_column(col_bits, lower_cols):
    out = 0
    x = col_bits
    j = 0
    while x:
        if x & 1:
            out ^= lower_cols[j]
        x >>= 1
        j += 1
    return out


def local_data(x, y, D):
    C2 = chains(2, 4, D, x, y)
    C3 = chains(3, 4, D, x, y)
    C4 = chains(4, 4, D, x, y)
    i2 = {c:i for i,c in enumerate(C2)}
    i3 = {c:i for i,c in enumerate(C3)}
    d3 = boundary_columns(C3, i2, D)
    d4 = boundary_columns(C4, i3, D)
    # chain condition d3 d4 = 0
    for c in d4:
        assert apply_boundary_column(c, d3) == 0
    r3 = rank_bitcols(d3)
    r4 = rank_bitcols(d4)
    h3 = len(C3) - r3 - r4
    assert h3 >= 0
    return (len(C2), len(C3), len(C4), r3, r4, h3)


def main():
    adj = build_graph()
    assert sum(len(a) for a in adj) // 2 == 27
    assert all(len(a) == 3 for a in adj)
    D = all_distances(adj)
    assert max(map(max, D)) == 4
    assert girth(adj) == 6
    expected_shell = (1, 3, 6, 6, 2)
    for x in range(N):
        shell = tuple(sum(1 for y in range(N) if D[x][y] == d) for d in range(5))
        assert shell == expected_shell

    by_distance = defaultdict(list)
    global_C2 = global_C3 = global_C4 = 0
    global_r3 = global_r4 = global_h = 0
    pair_counts = defaultdict(int)
    for x in range(N):
        for y in range(N):
            dat = local_data(x, y, D)
            d = D[x][y]
            by_distance[d].append(dat)
            pair_counts[d] += 1
            global_C2 += dat[0]; global_C3 += dat[1]; global_C4 += dat[2]
            global_r3 += dat[3]; global_r4 += dat[4]; global_h += dat[5]

    expected_pairs = {0:18, 1:54, 2:108, 3:108, 4:36}
    assert dict(pair_counts) == expected_pairs
    expected_local = {
        0:(6,18,15,6,12,0),
        1:(0,0,0,0,0,0),
        2:(7,18,9,7,9,2),
        3:(0,0,0,0,0,0),
        4:(12,18,6,11,6,1),
    }
    expected_h = {d: expected_local[d][5] for d in expected_local}
    for d in range(5):
        patterns = set(by_distance[d])
        assert patterns == {expected_local[d]}, (d, patterns)

    # Global chain counts and ranks are direct sums over endpoint blocks.
    assert (global_C2, global_C3, global_C4) == (1296, 2916, 1458)
    assert (global_r3, global_r4, global_h) == (1260, 1404, 252)

    # Representative endpoint blocks, useful for independent spot checking.
    reps = {}
    for d in range(5):
        found = None
        for y in range(N):
            if D[0][y] == d:
                found = y; break
        reps[d] = (0, found, local_data(0, found, D))

    print("VERIFY_OK")
    print("vertices=18 edges=27 degree=3 girth=6 diameter=4")
    print("distance_shell_per_vertex=1,3,6,6,2")
    print("endpoint_pair_counts=" + ",".join(f"d{d}:{pair_counts[d]}" for d in range(5)))
    print("localized_H34_F2=" + ",".join(f"d{d}:{expected_h[d]}" for d in range(5)))
    print(f"global_chain_counts_C2_C3_C4={global_C2},{global_C3},{global_C4}")
    print(f"global_boundary_ranks_d3_d4={global_r3},{global_r4}")
    print(f"global_dim_MH_3_4_F2={global_h}")
    for d in range(5):
        x,y,dat = reps[d]
        print(f"rep_d{d}=({x},{y}) C2,C3,C4,r3,r4,h3={','.join(map(str,dat))}")

if __name__ == "__main__":
    main()
