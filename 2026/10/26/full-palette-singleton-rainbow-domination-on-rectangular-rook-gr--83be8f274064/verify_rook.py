"""Standalone exact checks for degree-palette singleton rainbow domination on rook graphs."""
from math import comb, factorial
from itertools import permutations, combinations


def predicted(m, n, k):
    assert 2 <= m <= n and 0 <= k <= m
    d = m + n - 2
    return k < 2 or k % 2 == 0 or d >= 2 * k


def construct(m, n, k):
    """Place uncolored cells on the first k diagonal squares; return full labeling."""
    if not predicted(m, n, k):
        raise ValueError('mathematically impossible support')
    d = m + n - 2
    a = [[None] * n for _ in range(m)]
    for i in range(k):
        a[i][i] = -1
    if k >= 2 and k % 2 == 0:
        q = k - 1
        edge_round = {}
        for t in range(q):
            edge_round[tuple(sorted((q, t)))] = t
            for s in range(1, (q - 1) // 2 + 1):
                x, y = (t + s) % q, (t - s) % q
                edge_round[tuple(sorted((x, y)))] = t
        assert len(edge_round) == k * (k - 1) // 2
        for (i, j), t in edge_round.items():
            assert i < j
            a[i][j], a[j][i] = 2 * t, 2 * t + 1
    elif k >= 3:
        inverse2 = pow(2, -1, k)
        for i in range(k):
            for j in range(i + 1, k):
                t = (i + j) * inverse2 % k
                a[i][j], a[j][i] = t, k + t
    for i in range(k):
        neighbors = [(i, j) for j in range(n) if j != i]
        neighbors += [(h, i) for h in range(m) if h != i]
        used = {a[x][y] for x, y in neighbors if a[x][y] is not None}
        assert -1 not in used and len(used) == sum(a[x][y] is not None for x, y in neighbors)
        missing = [z for z in range(d) if z not in used]
        open_squares = [(x, y) for x, y in neighbors if a[x][y] is None]
        assert len(open_squares) == len(missing)
        for (x, y), z in zip(open_squares, missing):
            a[x][y] = z
    for i in range(m):
        for j in range(n):
            if a[i][j] is None:
                a[i][j] = 0
    return a


def validate(m, n, a):
    d = m + n - 2
    assert len(a) == m and all(len(row) == n for row in a)
    zeros = [(i, j) for i in range(m) for j in range(n) if a[i][j] == -1]
    assert all(-1 <= a[i][j] < d for i in range(m) for j in range(n))
    for i, j in zeros:
        nei = [a[i][h] for h in range(n) if h != j]
        nei += [a[h][j] for h in range(m) if h != i]
        assert sorted(nei) == list(range(d)), (m, n, i, j, nei)
    return len(zeros)


def direct_internal_feasibility(k, palette):
    """Independent backtracking for the true local inequality constraints.

    There is one variable for every oriented pair of distinct absent rows,
    and any two variables incident with one absent row must differ.
    """
    cells = [(i, j) for i in range(k) for j in range(k) if i != j]
    if not cells:
        return True
    incidence = [{t for t, (i, j) in enumerate(cells) if h in (i, j)} for h in range(k)]
    adjacent = [set().union(incidence[i], incidence[j]) - {t}
                for t, (i, j) in enumerate(cells)]
    assigned = {}
    def walk(max_color):
        if len(assigned) == len(cells):
            return True
        unassigned = [t for t in range(len(cells)) if t not in assigned]
        t = max(unassigned, key=lambda x:(len({assigned[y] for y in adjacent[x] if y in assigned}),len(adjacent[x])))
        forbidden = {assigned[y] for y in adjacent[t] if y in assigned}
        for col in range(min(palette - 1, max_color + 1) + 1):
            if col in forbidden:
                continue
            assigned[t] = col
            if walk(max(max_color, col)):
                return True
            del assigned[t]
        return False
    return walk(-1)


def run():
    construction_cases = 0
    for m in range(2, 16):
        for n in range(m, m + 7):
            for k in range(m + 1):
                if predicted(m, n, k):
                    a = construct(m, n, k)
                    assert validate(m, n, a) == k
                    construction_cases += 1
    print('CONSTRUCTION_CASES', construction_cases)
    direct_cases = 0
    for m in range(2, 6):
        for n in range(m, min(m + 3, 8)):
            for k in range(min(m, 4) + 1):
                actual = direct_internal_feasibility(k, m + n - 2)
                assert actual == predicted(m, n, k), (m, n, k, actual)
                direct_cases += 1
    print('INDEPENDENT_BACKTRACK_CASES', direct_cases)
    examples = [(2, 2), (3, 3), (3, 4), (3, 5), (4, 4), (5, 5), (5, 6), (5, 7), (6, 6)]
    for m, n in examples:
        maximum_k = max(k for k in range(m + 1) if predicted(m, n, k))
        support_count = comb(m, maximum_k) * comb(n, maximum_k) * factorial(maximum_k)
        value = m * n - maximum_k
        print('CASE', m, n, 'VALUE', value, 'MINIMUM_SUPPORT_COUNT', support_count)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
