#!/usr/bin/env python3
from collections import Counter

def partitions(n, minimum=1):
    if n == 0:
        yield []
        return
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield [first] + rest

def graph(parts):
    part_of = []
    for i, size in enumerate(parts):
        part_of.extend([i] * size)
    n = len(part_of)
    adj = [0] * n
    for u in range(n):
        for v in range(n):
            if u != v and part_of[u] != part_of[v]:
                adj[u] |= 1 << v
    return adj

def is_ltd(adj, mask):
    n = len(adj)
    for v in range(n):
        if (adj[v] & mask) == 0:
            return False
    signatures = set()
    for v in range(n):
        if not ((mask >> v) & 1):
            sig = adj[v] & mask
            if sig in signatures:
                return False
            signatures.add(sig)
    return True

def actual(parts):
    adj = graph(parts)
    out = Counter()
    for mask in range(1 << len(adj)):
        if is_ltd(adj, mask):
            out[mask.bit_count()] += 1
    return out

def predicted(parts):
    N = sum(parts)
    non = [size for size in parts if size >= 2]
    s = sum(size == 1 for size in parts)
    out = Counter()

    # Directly enumerate the choices encoded by the theorem:
    # in each non-singleton part omit zero or one vertex;
    # among singleton parts omit zero or one vertex;
    # then enforce that the selected set meets at least two parts.
    for profile in range(1 << len(non)):
        omitted = 0
        ways = 1
        for j, size in enumerate(non):
            if (profile >> j) & 1:
                omitted += 1
                ways *= size

        support_parts = len(non) + s
        if support_parts >= 2:
            out[N - omitted] += ways

        if s:
            support_parts_after_singleton_omission = len(non) + s - 1
            if support_parts_after_singleton_omission >= 2:
                out[N - omitted - 1] += ways * s
    return out

checked = 0
for N in range(2, 10):
    for parts in partitions(N):
        if len(parts) < 2:
            continue
        a = actual(parts)
        b = predicted(parts)
        if a != b:
            raise SystemExit(f"MISMATCH parts={parts} actual={dict(a)} predicted={dict(b)}")
        checked += 1

print(f"VERIFY_OK multipartite_types={checked} max_order=9")
