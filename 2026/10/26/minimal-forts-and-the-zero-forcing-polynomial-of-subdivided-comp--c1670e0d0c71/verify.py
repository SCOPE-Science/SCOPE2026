#!/usr/bin/env python3
"""Independent finite checks for forts and zero forcing in subdivided cliques.

Run: python3 verify.py
Only standard-library modules are needed.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def graph(n):
    edges = list(combinations(range(n), 2))
    adj = [0] * (n + len(edges))
    for i, (u, v) in enumerate(edges):
        w = n + i
        adj[u] |= 1 << w
        adj[v] |= 1 << w
        adj[w] |= (1 << u) | (1 << v)
    return edges, adj


def all_forests_by_edges(n, edges):
    hist = Counter()
    for m in range(1 << len(edges)):
        parent = list(range(n))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        acyclic = True
        for i, (u, v) in enumerate(edges):
            if (m >> i) & 1:
                a, b = root(u), root(v)
                if a == b:
                    acyclic = False
                    break
                parent[a] = b
        if acyclic:
            hist[m.bit_count()] += 1
    return hist


def zero_forces(mask, adj):
    all_mask = (1 << len(adj)) - 1
    current = mask
    while True:
        nxt = current
        active = current
        while active:
            bit = active & -active
            v = bit.bit_length() - 1
            active ^= bit
            possible = adj[v] & (all_mask ^ current)
            if possible and not (possible & (possible - 1)):
                nxt |= possible
        if nxt == current:
            return current == all_mask
        current = nxt


def exhaustive(n):
    edges, adj = graph(n)
    N = len(adj)
    size = 1 << N
    full = size - 1
    is_fort = bytearray(size)
    has_fort_sub = bytearray(size)
    fort_min = Counter()
    actual_minimal = set()
    zero_force = Counter()
    actual_zero = set()
    for mask in range(1, size):
        outside = full ^ mask
        valid = True
        while outside:
            b = outside & -outside
            v = b.bit_length() - 1
            outside ^= b
            if (adj[v] & mask).bit_count() == 1:
                valid = False
                break
        is_fort[mask] = valid
        smaller = False
        selected = mask
        while selected:
            b = selected & -selected
            selected ^= b
            if has_fort_sub[mask ^ b]:
                smaller = True
                break
        if valid and not smaller:
            fort_min[mask.bit_count()] += 1
            actual_minimal.add(mask)
        has_fort_sub[mask] = valid or smaller
        if zero_forces(mask, adj):
            zero_force[mask.bit_count()] += 1
            actual_zero.add(mask)
    predicted_fort = Counter()
    for k in range(3, n+1):
        predicted_fort[k] += factorial(n) // (2*k*factorial(n-k))
    predicted_fort[n] += 1
    predicted_fort[2*n-2] += n
    assert fort_min == predicted_fort, (n,fort_min,predicted_fort)
    # Predict exact vertex families without using the fort test.
    m = len(edges)
    predicted_minimal = {(1 << n)-1}
    for v in range(n):
        mask = ((1 << n)-1) ^ (1 << v)
        for i, (u, w) in enumerate(edges):
            if v in (u, w):
                mask |= 1 << (n+i)
        predicted_minimal.add(mask)
    for es in range(1 << m):
        if es.bit_count() < 3:
            continue
        deg = [0]*n
        graph_e = [[] for _ in range(n)]
        for i, (u,v) in enumerate(edges):
            if (es>>i)&1:
                deg[u] += 1
                deg[v] += 1
                graph_e[u].append(v)
                graph_e[v].append(u)
        if any(d not in (0,2) for d in deg):
            continue
        active = {i for i,d in enumerate(deg) if d}
        if not active:
            continue
        seen = set()
        queue = [next(iter(active))]
        while queue:
            u=queue.pop()
            if u in seen: continue
            seen.add(u)
            queue.extend(graph_e[u])
        if seen == active:
            predicted_minimal.add(es << n)
    assert actual_minimal == predicted_minimal, (n,len(actual_minimal),len(predicted_minimal))
    # Independently compare every zero-forcing set with forest/vertex conditions.
    original_full = (1 << n)-1
    full_edge = (1 << m)-1
    expected_zero = set()
    for z in range(1,size):
        X = z & original_full
        if not X:
            continue
        missing_edges = full_edge ^ (z >> n)
        par = list(range(n))
        def find(x):
            while par[x] != x:
                x = par[x]
            return x
        forest = True
        for i,(u,v) in enumerate(edges):
            if missing_edges & (1<<i):
                a,b = find(u),find(v)
                if a == b:
                    forest = False
                    break
                par[a] = b
        if forest and X.bit_count() == 1:
            x = X.bit_length()-1
            # A forbidden forest is exactly the full star centered at x.
            if all(missing_edges & (1<<i) for i,(u,v) in enumerate(edges) if x in (u,v)):
                forest = False
        if forest:
            expected_zero.add(z)
    assert expected_zero == actual_zero, (n,len(expected_zero),len(actual_zero))
    forests = all_forests_by_edges(n, edges)
    m = len(edges)
    predicted_zero = Counter()
    for k in range(1,n+1):
        for num_edges, count in forests.items():
            predicted_zero[k+m-num_edges] += comb(n,k) * count
    predicted_zero[m-n+2] -= n
    assert all(v >= 0 for v in predicted_zero.values())
    predicted_zero += Counter()
    assert zero_force == predicted_zero, (n,zero_force,predicted_zero)
    target_min = m-n+2
    assert min(zero_force) == target_min
    assert zero_force[target_min] == n*(n**(n-2)-1)
    print(f'n={n} vertices={N} subsets={size-1} minimal_forts={sum(fort_min.values())} '+
          f'fort_size_counts={dict(sorted(fort_min.items()))} zero_forcing_sets={sum(zero_force.values())} '+
          f'min_zero_forcing_sets={zero_force[target_min]}')

if __name__ == '__main__':
    for n in range(3,6):
        exhaustive(n)
    print('PASS: exact minimal-fort families, all zero-forcing sets, coefficient distributions and minimum counts agree.')
