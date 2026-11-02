#!/usr/bin/env python3
"""Construct and check shortest cyclic covers of binary words avoiding 001.

All computations use Python's standard library; the theorem is proved independently
by the graph arguments in RESULT.md. Finite tests do not replace that proof.
"""

from collections import Counter, deque


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def formula(n):
    return fibonacci(n + 3) - 1 + (n - 2) * fibonacci(n - 1)


def admissible(x, n):
    return '001' not in format(x, '0%db' % n)


def build(n):
    if n < 3:
        raise ValueError('n must be at least three')
    length = n - 1
    mask = (1 << length) - 1
    word = lambda x: format(x, '0%db' % length)
    required = [x for x in range(1 << n) if admissible(x, n)]
    sources, sinks = [], []
    out = Counter()
    incoming = Counter()
    for x in required:
        u, v = x >> 1, x & mask
        out[u] += 1
        incoming[v] += 1
    active = {x >> 1 for x in required} | {x & mask for x in required}
    for v in sorted(active):
        b = out[v] - incoming[v]
        if b == -1:
            sources.append(v)
            assert word(v).endswith('00') and not word(v).startswith('01')
        elif b == 1:
            sinks.append(v)
            assert word(v).startswith('01') and '00' not in word(v)
        else:
            assert b == 0
    assert len(required) == fibonacci(n + 3) - 1
    assert len(sources) == len(sinks) == fibonacci(n - 1)
    # Edge identities keep duplicates distinct. An edge is (tail, head, label).
    edges = []
    adj = [[] for _ in range(1 << length)]
    def add(u, v, bit):
        edge_id = len(edges)
        edges.append((u, v, bit))
        adj[u].append(edge_id)
    for x in required:
        add(x >> 1, x & mask, x & 1)
    for source, sink in zip(sources, sinks):
        u = source
        target = word(sink)
        assert target[0] == '0' and (u & 1) == 0
        for ch in target[1:]:
            bit = int(ch)
            v = ((u << 1) | bit) & mask
            add(u, v, bit)
            u = v
        assert u == sink
    assert len(edges) == formula(n)
    delta = Counter()
    for u, v, _ in edges:
        delta[u] += 1
        delta[v] -= 1
    assert not any(delta.values())
    # Hierholzer: an Euler circuit exists because the augmented graph is connected.
    counters = [len(x) for x in adj]
    start = min(active)
    vertices = [start]
    stack_edges = []
    order = []
    while vertices:
        v = vertices[-1]
        if counters[v]:
            counters[v] -= 1
            e = adj[v][counters[v]]
            u, dest, _ = edges[e]
            assert u == v
            stack_edges.append(e)
            vertices.append(dest)
        else:
            vertices.pop()
            if stack_edges:
                order.append(stack_edges.pop())
    order.reverse()
    assert len(order) == len(edges)
    assert all(c == 0 for c in counters)
    assert edges[order[-1]][1] == edges[order[0]][0]
    seq = ''.join(str(edges[i][2]) for i in order)
    assert len(seq) == formula(n)
    cyclic = seq + seq[:n-1]
    observed = {int(cyclic[i:i+n], 2) for i in range(len(seq))}
    assert all(x in observed for x in required)
    return seq, len(required), len(sources)


def check_small_brute():
    # Independent brute coverage test for all shorter lengths at n=3 and n=4.
    for n in (3, 4):
        targets = {x for x in range(1 << n) if admissible(x, n)}
        L = formula(n)
        for k in range(n, L):
            for x in range(1 << k):
                w = format(x, '0%db' % k)
                ww = w + w[:n-1]
                have = {int(ww[j:j+n], 2) for j in range(k)}
                assert not targets <= have, (n, k, w)


def main():
    check_small_brute()
    for n in range(3, 19):
        seq, nreq, nim = build(n)
        print('n=%d required=%d imbalance=%d optimum=%d sample=%s' %
              (n, nreq, nim, len(seq), seq[:min(36, len(seq))]))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
