"""Independent finite checks for NAE triangle coloring reconfiguration.

Run: python verify.py
All computations are exact integer/finite-state tests. Infinite results require the proof.
"""
from collections import deque
from itertools import combinations
from math import comb


def triangles(n, edges):
    es = {tuple(sorted(e)) for e in edges}
    return tuple(sum(1 << x for x in t)
                 for t in combinations(range(n), 3)
                 if all(tuple(sorted(e)) in es for e in combinations(t, 2)))


def acceptable(n, triangles_masks):
    return {c for c in range(1 << n)
            if all(0 < (c & t) < t for t in triangles_masks)}


def degrees_and_degeneracy(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    alive = set(range(n))
    while alive:
        candidates = [v for v in alive if len(adj[v] & alive) <= 2]
        if not candidates:
            return False
        alive.remove(candidates[0])
    return True


def bfs_graph(n, states, start):
    distances = {start: 0}
    q = deque([start])
    while q:
        x = q.popleft()
        for i in range(n):
            y = x ^ (1 << i)
            if y in states and y not in distances:
                distances[y] = distances[x] + 1
                q.append(y)
    return distances


def exhaustive_small_graphs():
    graph_cases = 0
    degenerate_cases = 0
    for n in range(0, 7):
        pairs = list(combinations(range(n), 2))
        for code in range(1 << len(pairs)):
            graph_cases += 1
            edges = [pairs[j] for j in range(len(pairs)) if (code >> j) & 1]
            if not degrees_and_degeneracy(n, edges):
                continue
            degenerate_cases += 1
            T = triangles(n, edges)
            states = acceptable(n, T)
            assert states, (n, edges, 'no valid states')
            assert any(abs(2 * s.bit_count() - n) == n % 2 for s in states), (n, edges, 'not balanced')
            reached = bfs_graph(n, states, min(states))
            assert len(reached) == len(states), (n, edges, 'disconnected')
    return graph_cases, degenerate_cases


def book(m):
    n = m + 2
    edges = [(0, 1)]
    edges += [(u, v) for u in (0, 1) for v in range(2, n)]
    return n, edges


def rigid_apex(m):
    n = m + 3
    edges = list(combinations(range(3), 2))
    edges += [(u, v) for u in range(3) for v in range(3, n)]
    return n, edges


def exact_families():
    book_cases = 0
    book_state_checks = 0
    for m in range(1, 9):
        n, edges = book(m)
        T = triangles(n, edges)
        states = acceptable(n, T)
        assert len(states) == 2 ** (m + 1) + 2
        coeff = [sum(s.bit_count() == k for s in states) for k in range(n + 1)]
        expected = [0] * (n + 1)
        for k in range(m + 1):
            expected[k + 1] += 2 * comb(m, k)
        expected[m] += 1
        expected[2] += 1
        assert coeff == expected, (m, coeff, expected)
        diameter = max(max(bfs_graph(n, states, s).values()) for s in states)
        assert diameter == m + 2, (m, diameter)
        book_cases += 1
        book_state_checks += len(states)
    rigid_cases = 0
    for m in range(1, 10):
        n, edges = rigid_apex(m)
        assert not degrees_and_degeneracy(n, edges)
        states = acceptable(n, triangles(n, edges))
        assert len(states) == 6, (m, len(states))
        assert all(len(bfs_graph(n, states, s)) == 1 for s in states)
        assert {abs(2 * s.bit_count() - n) for s in states} == {m - 1}
        rigid_cases += 1
    return book_cases, book_state_checks, rigid_cases


def main():
    all_graphs, degenerate = exhaustive_small_graphs()
    books, book_states, rigid = exact_families()
    print(f'VERIFY_OK labelled_graphs={all_graphs} 2_degenerate_graphs={degenerate} '
          f'books={books} book_states={book_states} rigid_examples={rigid}')


if __name__ == '__main__':
    main()
