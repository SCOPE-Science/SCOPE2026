#!/usr/bin/env python3
"""Finite checks for the Golden-Mean de Bruijn construction used in RESULT.md.

This script is verification support, not the proof of the infinite statement.
It uses only the Python standard library.
"""

from collections import defaultdict


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def lucas(n):
    return fib(n - 1) + fib(n + 1)


def cyclic_golden_words(n):
    words = []
    for x in range(1 << n):
        w = tuple((x >> (n - 1 - i)) & 1 for i in range(n))
        if all(not (w[i] == w[(i + 1) % n] == 1) for i in range(n)):
            words.append(w)
    return words


def golden_debruijn(n):
    """Eulerian construction for cyclic Golden-Mean words of length n."""
    edges = cyclic_golden_words(n)
    adj = defaultdict(list)
    for w in edges:
        u, v = w[:-1], w[1:]
        adj[u].append((v, w))
    for u in adj:
        adj[u].sort(reverse=True)

    start = (0,) * (n - 1)
    vertex_stack = [start]
    edge_stack = []
    circuit = []
    while vertex_stack:
        u = vertex_stack[-1]
        if adj[u]:
            v, w = adj[u].pop()
            vertex_stack.append(v)
            edge_stack.append(w)
        else:
            vertex_stack.pop()
            if edge_stack:
                circuit.append(edge_stack.pop())
    circuit.reverse()
    assert len(circuit) == len(edges)
    # The first symbol of each traversed edge gives the cyclic sequence.
    return [w[0] for w in circuit]


def parse_code_cyclic(bits):
    """Parse the cyclic code 0 -> 0 and 1 -> 10 at a genuine boundary."""
    m = len(bits)
    starts = [i for i in range(m) if bits[i] == 1 or (bits[i] == 0 and bits[(i - 1) % m] == 0)]
    assert starts
    start = starts[0]
    symbols = []
    i = start
    for _ in range(m + 1):
        if bits[i] == 1:
            assert bits[(i + 1) % m] == 0
            symbols.append(1)
            i = (i + 2) % m
        else:
            symbols.append(0)
            i = (i + 1) % m
        if i == start:
            return symbols
    raise AssertionError("cyclic parsing did not close")


def weighted_lcp(word, a, b):
    n = len(word)
    total = 0
    for k in range(n):
        x, y = word[(a + k) % n], word[(b + k) % n]
        if x != y:
            return total
        total += 1 if x == 0 else 2
    return total


def primitive(word):
    n = len(word)
    for d in range(1, n):
        if n % d == 0 and all(word[i] == word[i % d] for i in range(n)):
            return False
    return True


def main():
    for n in range(2, 11):
        bits = golden_debruijn(n)
        m = len(bits)
        factors = {
            tuple(bits[(i + j) % m] for j in range(n))
            for i in range(m)
        }
        target = set(cyclic_golden_words(n))
        assert factors == target
        assert m == lucas(n)

        word = parse_code_cyclic(bits)
        assert len(word) == fib(n + 1)
        assert primitive(word)

        max_weighted_lcp = max(
            weighted_lcp(word, a, b)
            for a in range(len(word))
            for b in range(a + 1, len(word))
        )
        assert max_weighted_lcp <= n - 1

        print(
            f"n={n:2d} bit_length={m:3d} orbit_length={len(word):3d} "
            f"max_weighted_lcp={max_weighted_lcp:2d}"
        )
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
