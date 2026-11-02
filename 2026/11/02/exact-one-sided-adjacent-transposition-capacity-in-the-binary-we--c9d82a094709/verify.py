"""Reproduce finite instances of the directed adjacent-swap packing theorem.

Run: python3 verify.py
Only Python 3 standard library is required.
"""
from functools import lru_cache
from itertools import combinations

MOVES = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)}


def positions(n):
    return {(i, j) for j in range(1, n) for i in range(j)}


def error_ball(p):
    i, j = p
    out = {p}
    if i > 0:
        out.add((i - 1, j))
    if j > i + 1:
        out.add((i, j - 1))
    return out


def confusable(p, q):
    return bool(error_ball(p) & error_ball(q))


def graph_adjacent(p, q):
    return (q[0] - p[0], q[1] - p[1]) in MOVES


def strip_cliques(m):
    out = []
    for i in range(0, m - 1, 2):
        out.append(((i, m), (i + 1, m), (i, m + 1)))
    for i in range(1, m + 1, 2):
        out.append(((i, m + 1), (i - 1, m + 2), (i, m + 2)))
    if m % 2:
        out.append(((m - 1, m), (m - 1, m + 1)))
    else:
        out.append(((m, m + 1), (m, m + 2)))
    out.append(((m + 1, m + 2),))
    return out


def exact_independent_number(n):
    pp = sorted(positions(n))
    neighbors = [0] * len(pp)
    for i, p in enumerate(pp):
        for j in range(i + 1, len(pp)):
            if confusable(p, pp[j]):
                neighbors[i] |= 1 << j
                neighbors[j] |= 1 << i
    @lru_cache(None)
    def alpha(mask):
        if not mask:
            return 0
        # Branch on highest degree of remaining graph.
        avail = [v for v in range(len(pp)) if mask & (1 << v)]
        v = max(avail, key=lambda a: (neighbors[a] & mask).bit_count())
        without = mask & ~(1 << v)
        return max(alpha(without), 1 + alpha(without & ~neighbors[v]))
    return alpha((1 << len(pp)) - 1)


def main():
    for n in range(2, 51):
        pp = sorted(positions(n))
        observed = {(i, j) for i, j in pp if (i + 2 * j) % 3 == 2}
        assert len(observed) == n * (n + 1) // 6, (n, len(observed))
        seen = set()
        for p in observed:
            ball = error_ball(p)
            assert not (ball & seen), (n, p)
            seen.update(ball)
        if n <= 20:
            for p, q in combinations(pp, 2):
                assert confusable(p, q) == graph_adjacent(p, q), (n, p, q)
    tested_strips = 0
    for m in range(1, 151):
        expected = {(i, j) for j in (m, m + 1, m + 2) for i in range(j)}
        cliques = strip_cliques(m)
        assert len(cliques) == m + 2
        flat = [p for clique in cliques for p in clique]
        assert len(flat) == len(set(flat)) and set(flat) == expected, m
        for clique in cliques:
            for p, q in combinations(clique, 2):
                assert confusable(p, q), (m, clique)
        assert sum((i + 2 * j) % 3 == 2 for i, j in expected) == m + 2
        tested_strips += 1
    census = {n: exact_independent_number(n) for n in range(2, 10)}
    assert all(v == n * (n + 1) // 6 for n, v in census.items())
    print('VERIFY_OK', 'code_lengths=2..50', 'strips=1..150',
          'literal_max_independent_lengths=2..9',
          'optima=' + str(census))

if __name__ == '__main__':
    main()
