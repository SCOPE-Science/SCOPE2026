#!/usr/bin/env python3
"""Exact independent checks for non-contingency-positive-introspection on out-trees."""
from itertools import product
from math import comb
from heapq import heapify, heappush, heappop


def edges_from_prufer(n, word):
    if n == 1:
        return []
    degree = [1] * n
    for v in word:
        degree[v] += 1
    leaves = [u for u in range(n) if degree[u] == 1]
    heapify(leaves)
    edges = []
    for v in word:
        u = heappop(leaves)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heappush(leaves, v)
    a = heappop(leaves)
    b = heappop(leaves)
    edges.append((a, b))
    return edges


def children_from_tree(n, edges, root):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    ch = [[] for _ in range(n)]
    parent = [-1] * n
    parent[root] = root
    stack = [root]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if parent[u] == -1:
                parent[u] = v
                ch[v].append(u)
                stack.append(u)
    assert all(p >= 0 for p in parent)
    return ch


def structural(ch):
    return all(len(ch[v]) <= 1 or all(len(ch[u]) <= 1 for u in ch[v]) for v in range(len(ch)))


def semantic(ch):
    n = len(ch)
    for mask in range(1 << n):
        truth = [(mask >> i) & 1 for i in range(n)]
        d = [len(ch[v]) < 2 or all(truth[u] == truth[ch[v][0]] for u in ch[v]) for v in range(n)]
        for v in range(n):
            dd = len(ch[v]) < 2 or all(d[u] == d[ch[v][0]] for u in ch[v])
            if d[v] and not dd:
                return False
    return True


def recurrence(N):
    t = [0] * (N + 1)
    a = [0] * (N + 1)
    f = [0] * (N + 1)
    f[0] = 1
    for n in range(1, N + 1):
        a[n] = 1 if n == 1 else n * t[n - 1]
        f[n] = sum(comb(n - 1, k - 1) * a[k] * f[n-k] for k in range(1, n+1))
        t[n] = a[n] + n*(f[n-1] - (n == 1) - a[n-1])
    return t


def main():
    nums = recurrence(12)
    assert nums[1:9] == [1, 2, 9, 64, 565, 6036, 77749, 1176736]
    for n in range(1, 8):
        valid = 0
        total = 0
        for prufer in product(range(n), repeat=max(0, n-2)) if n > 1 else [()]:
            edges = edges_from_prufer(n, prufer)
            for root in range(n):
                ch = children_from_tree(n, edges, root)
                s = structural(ch)
                if n <= 6:
                    assert s == semantic(ch), ('semantics discrepancy', n, prufer, root)
                valid += s
                total += 1
        assert total == n**(n-1), (n, total)
        assert valid == nums[n], (n, valid, nums[n])
        print(f'n={n} all={total} valid={valid} invalid={total-valid}')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
