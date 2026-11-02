#!/usr/bin/env python3
"""Exact finite certificate for four-base reverse-complement 4-palindrome avoidance.

Uses only Python's standard library. Run: python3 verify.py
The claims and mathematical derivation are in RESULT.md.
"""
from collections import defaultdict, deque
from itertools import product


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return out


def power(a, n):
    out = [1]
    for _ in range(n):
        out = multiply(out, a)
    return out


def expected_determinant():
    terms = [power([1, -1], 3), power([1, 1], 3),
             power([1, 0, 1], 2),
             [1, -3, -2, -3],
             power([1, -1, 1, -4, 2, -3], 2),
             [1, 1, 1, 4, 2, 3]]
    p = [1]
    for t in terms:
        p = multiply(p, t)
    return p + [0] * (65 - len(p))


def graph(q):
    assert q % 2 == 0
    # Complementary letters have adjacent even/odd labels.
    states = list(product(range(q), repeat=3))
    index = {s: i for i, s in enumerate(states)}
    edges = [[] for _ in states]
    for i, (a, b, c) in enumerate(states):
        for d in range(q):
            if b == (c ^ 1) and a == (d ^ 1):
                continue
            edges[i].append(index[(b, c, d)])
    return edges


def traces_via_walks(edges, max_n):
    size = len(edges)
    traces = [size] + [0] * max_n
    # Count rooted n-step closed walks from each starting vertex separately.
    for root in range(size):
        v = [0] * size
        v[root] = 1
        for n in range(1, max_n + 1):
            nxt = [0] * size
            for state, count in enumerate(v):
                if count:
                    for dest in edges[state]:
                        nxt[dest] += count
            v = nxt
            traces[n] += v[root]
    return traces


def determinant_from_newton(traces):
    # Newton identities: det(I-zM) coefficients d_k satisfy
    # k d_k = -sum_{j=1}^k tr(M^j) d_{k-j}.
    n = len(traces) - 1
    d = [1]
    for k in range(1, n + 1):
        numerator = -sum(traces[j] * d[k-j] for j in range(1, k + 1))
        assert numerator % k == 0, (k, numerator)
        d.append(numerator // k)
    return d


def connected(edges):
    n = len(edges)
    for graph_edges in (edges, [[i for i in range(n) if v in edges[i]] for v in range(n)]):
        visited = {0}
        todo = [0]
        for v in todo:
            for w in graph_edges[v]:
                if w not in visited:
                    visited.add(w)
                    todo.append(w)
        if len(visited) != n:
            return False
    return True


def direct_count(n, q=4, cyclic=False):
    # Deliberately independent of transfer-graph construction.
    c = lambda a: a ^ 1
    ans = 0
    for word in product(range(q), repeat=n):
        if cyclic:
            windows = ((word[(i+j) % n] for j in range(4)) for i in range(n))
        else:
            windows = (iter(word[i:i+4]) for i in range(max(0, n-3)))
        allowed = True
        for window in windows:
            a, b, x, d = tuple(window)
            if a == c(d) and b == c(x):
                allowed = False
                break
        ans += allowed
    return ans


def line_counts(q, N):
    states = {(): 1}
    out = [1]
    for n in range(1, N+1):
        next_states = defaultdict(int)
        for tup, val in states.items():
            for a in range(q):
                if len(tup) == 3 and tup[0] == (a ^ 1) and tup[1] == (tup[2] ^ 1):
                    continue
                next_states[(tup + (a,))[-3:]] += val
        states = next_states
        out.append(sum(states.values()))
    return out


def recurrence(q, n):
    t = [1, q, q*q, q**3, q**4-q*q, q**5-2*q**3+q]
    for k in range(6, n+1):
        t.append((q-1)*t[k-1] + (q-2)*t[k-2] + (q-1)*t[k-3])
    return t[:n+1]


def main():
    for q in (2, 4, 6, 8):
        actual = line_counts(q, 16)
        predicted = recurrence(q, 16)
        assert actual == predicted, (q, actual, predicted)
    for n in range(1, 9):
        assert direct_count(n) == line_counts(4, n)[n]
    edges = graph(4)
    assert len(edges) == 64
    assert connected(edges)
    traces = traces_via_walks(edges, 64)
    poly = determinant_from_newton(traces)
    assert poly == expected_determinant(), (poly, expected_determinant())
    for n in range(1, 9):
        assert traces[n] == direct_count(n, cyclic=True), (n, traces[n])
    print('linear n=0..16, q=2,4,6,8: OK')
    print('independent brute linear n=1..8 and cyclic n=1..8: OK')
    print('64-state exact characteristic polynomial / zeta factorization: OK')
    print('strong connectivity of DNA constraint graph: OK')
    print('cyclic counts n=1..12:', traces[1:13])
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
