"""Finite checks supporting the proof, not an exhaustive proof of the theorem.

Run: python3 output/artifacts/verify_pendant_fans.py (standard library only).
Compare a neighbourhood-matching predicate with a generic injective edge-
preserving map search, which does not use the matching characterization.
"""

from functools import lru_cache
from itertools import combinations
from random import Random


def graph(n, edges=()):
    g = [set() for _ in range(n)]
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)
    return g


def contains(g, t, q):
    @lru_cache(None)
    def matching(vertices):
        if len(vertices) < 2:
            return 0
        u, *rest = vertices
        best = matching(tuple(rest))
        for v in rest:
            if v in g[u]:
                best = max(best, 1 + matching(tuple(w for w in rest if w != v)))
        return best

    return any(len(nb) >= 2 * t + q and matching(tuple(sorted(nb))) >= t for nb in g)


def forbidden(t, q):
    return graph(1 + 2 * t + q, [(0, v) for v in range(1, 1 + 2 * t + q)]
                 + [(2 * i + 1, 2 * i + 2) for i in range(t)])


def construction(t, n):
    edges = [(0, v) for v in range(1, n)]
    for i in range(t - 1):
        edges.extend(combinations(range(3 * i + 1, 3 * i + 4), 2))
    return graph(n, edges)


def embeds(g, h):
    """Generic non-induced subgraph search; no fan-specific mathematical test."""
    if len(g) < len(h):
        return False
    order = sorted(range(len(h)), key=lambda x: -len(h[x]))
    image, used = {}, set()

    def visit(i):
        if i == len(h):
            return True
        u = order[i]
        for v in range(len(g)):
            if v in used or len(g[v]) < len(h[u]):
                continue
            if any(image[w] not in g[v] for w in h[u] if w in image):
                continue
            image[u] = v
            used.add(v)
            if visit(i + 1):
                return True
            used.remove(v)
            del image[u]
        return False

    return visit(0)


def additions(g):
    return [(u, v) for u, v in combinations(range(len(g)), 2) if v not in g[u]]


def main():
    rng = Random(76123)
    comparisons = 0
    for n in range(4, 8):
        pairs = list(combinations(range(n), 2))
        masks = range(1 << len(pairs)) if n <= 5 else [rng.getrandbits(len(pairs)) for _ in range(500)]
        for mask in masks:
            g = graph(n, [e for i, e in enumerate(pairs) if (mask >> i) & 1])
            for t, q in [(1, 1), (1, 2), (2, 1), (2, 2), (3, 0)]:
                assert contains(g, t, q) == embeds(g, forbidden(t, q))
                comparisons += 1
    print(f"Matching predicate vs generic embedding: {comparisons} agreements", flush=True)

    # Direct exhaustive comparison with Hua-Peng Theorem 1.4 at n=6,q=1.
    pairs = list(combinations(range(6), 2))
    best, winners = 16, []
    for mask in range(1 << len(pairs)):
        m = mask.bit_count()
        if m > best:
            continue
        g = graph(6, [e for i, e in enumerate(pairs) if (mask >> i) & 1])
        if contains(g, 2, 1):
            continue
        saturated = True
        for u, v in additions(g):
            g[u].add(v)
            g[v].add(u)
            found = contains(g, 2, 1)
            g[u].remove(v)
            g[v].remove(u)
            if not found:
                saturated = False
                break
        if saturated:
            if m < best:
                best, winners = m, []
            winners.append(g)
    assert best == 6 + 2
    assert all(embeds(g, construction(2, 6)) for g in winners)
    print(f"All 32768 labeled graphs, t=2 q=1 n=6: min={best}, formula=8; {len(winners)} labeled winners, one isomorphism type", flush=True)

    checked = independent = 0
    for t in range(3, 7):
        for q in [4 * t, 4 * t + 1]:
            for n in [q + 2 * t + 1, q + 2 * t + 3]:
                g = construction(t, n)
                assert sum(map(len, g)) // 2 == n + 3 * t - 4
                assert not contains(g, t, q)
                if t == 3:
                    h = forbidden(t, q)
                    assert not embeds(g, h)
                for u, v in additions(g):
                    g[u].add(v)
                    g[v].add(u)
                    assert contains(g, t, q)
                    if t == 3:
                        assert embeds(g, h)
                        independent += 1
                    g[u].remove(v)
                    g[v].remove(u)
                    checked += 1
    print(f"16 constructions: edge formulas and freeness passed; {checked} additions passed, {independent} independently checked", flush=True)
    assert not contains(graph(7, combinations(range(7), 2)), 3, 1)
    assert contains(graph(8, combinations(range(8), 2)), 3, 1)
    print("Small positive and negative controls passed")


if __name__ == '__main__':
    main()
