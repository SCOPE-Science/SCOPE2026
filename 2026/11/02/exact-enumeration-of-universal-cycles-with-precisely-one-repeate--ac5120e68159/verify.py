"""Exact verification of restricted triple universal-cycle enumeration.

Usage: python3 verify.py. Uses Python standard library only.
"""
from collections import Counter, defaultdict
from math import factorial


def targets(q):
    return [(a, b, c) for a in range(q) for b in range(q)
            for c in range(q) if len({a, b, c}) == 2]


def count_formula(q):
    assert q >= 2
    return (2 ** (q - 1) *
            3 ** ((q - 1) * (q - 2) // 2) *
            q ** (q - 2) * factorial(q - 2) ** q)


def euler_word(q):
    # Hierholzer traversal of the edge-distinct two-letter-overlap digraph.
    edges = targets(q)
    out = defaultdict(list)
    for a, b, c in edges:
        out[(a, b)].append((b, c))
    stack = [(0, 0)]
    tour = []
    while stack:
        v = stack[-1]
        if out[v]:
            stack.append(out[v].pop())
        else:
            tour.append(stack.pop())
    tour.reverse()
    assert len(tour) == len(edges) + 1
    assert tour[0] == tour[-1]
    # First components of consecutive overlapping pair vertices.
    return tuple(v[0] for v in tour[:-1])


def determinant_bareiss(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    prev = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((i for i in range(k + 1, n) if a[i][k]), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[n - 1][n - 1]


def tree_count(q):
    v = [(a, b) for a in range(q) for b in range(q)]
    idx = {p: i for i, p in enumerate(v)}
    n = len(v)
    L = [[0] * n for _ in range(n)]
    for a, b, c in targets(q):
        u = idx[(a, b)]
        w = idx[(b, c)]
        L[u][u] += 1
        L[u][w] -= 1
    # Remove diagonal vertex (0,0) as directed matrix-tree root.
    return determinant_bareiss([row[1:] for row in L[1:]])


def exhaustive_cycles(q):
    E = targets(q)
    out = defaultdict(list)
    for i, e in enumerate(E):
        out[e[:2]].append((1 << i, e[1:]))
    # Each rotational orbit has one edge (0,0,1); anchor that edge.
    first = E.index((0, 0, 1))
    full = (1 << len(E)) - 1
    count = 0

    def dfs(pair, used):
        nonlocal count
        if used == full:
            if pair == (0, 0):
                count += 1
            return
        for bit, nxt in out[pair]:
            if not (used & bit):
                dfs(nxt, used | bit)

    dfs((0, 1), 1 << first)
    return count


def check():
    for q in range(2, 9):
        t = tree_count(q)
        expected_t = (2 ** (q - 1) *
                      3 ** ((q - 1) * (q - 2) // 2) * q ** (q - 2))
        assert t == expected_t, (q, t, expected_t)
        assert count_formula(q) == t * factorial(q - 2) ** q
    for q in range(2, 26):
        w = euler_word(q)
        E = targets(q)
        assert len(w) == 3 * q * (q - 1)
        seen = Counter(tuple(w[i:i + 3]) if i + 3 <= len(w)
                       else tuple(w[(i + j) % len(w)] for j in range(3))
                       for i in range(len(w)))
        assert set(seen) == set(E) and all(c == 1 for c in seen.values())
        assert Counter(w) == Counter({a: 3 * (q - 1) for a in range(q)})
    for q in (2, 3, 4):
        exact = exhaustive_cycles(q)
        assert exact == count_formula(q), (q, exact, count_formula(q))
        print('q=', q, 'number=', exact)
    print('VERIFY_OK: matrices q=2..8; witnesses q=2..25; exhaustive q=2..4')


if __name__ == '__main__':
    check()
