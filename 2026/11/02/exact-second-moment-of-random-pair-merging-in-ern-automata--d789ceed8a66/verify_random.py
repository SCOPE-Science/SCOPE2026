"""Exact checks for fair-input pair merging in cyclic automata.

No external dependencies.  Finite checks support the separate all-n proof.
"""
from fractions import Fraction
from itertools import combinations


def canon_pairs(n):
    return {
        (r, s): frozenset(((-s) % n, (r - s) % n))
        for r in range(1, n // 2 + 1)
        for s in range(n // 2 if n % 2 == 0 and r == n // 2 else n)
    }


def predicted(n, r, s):
    k = n // 2
    base = 2 * (n - 1) ** 2 + (r - 1) * (4 * n * n - 12 * n + 4) - (r - 1) * (r - 2) * (4 * n - 2)
    if r < k:
        jump = (4 * n * n - 12 * n + 4 - (r - 1) * (8 * n - 4)) // 2
    elif n % 2:
        jump = n - 1
    else:
        jump = 0
    return base + 2 * s + jump * (s >= r)


def move(n, pair, letter):
    if letter == 'b':
        return frozenset(((x + 1) % n) for x in pair)
    return frozenset((1 if x == 0 else x) for x in pair)


def independent_linear(n, pairs):
    """Solve absorption equations using exact Fraction elimination, separately from formula."""
    nodes = list(pairs.values())
    pos = {p: i for i, p in enumerate(nodes)}
    N = len(nodes)
    A = [[Fraction(0) for _ in range(N + 1)] for _ in range(N)]
    for i, p in enumerate(nodes):
        A[i][i] = Fraction(2)
        A[i][-1] = Fraction(2)
        for letter in 'ab':
            nxt = move(n, p, letter)
            if len(nxt) == 2:
                A[i][pos[nxt]] -= Fraction(1)
    for col in range(N):
        pivot = next(i for i in range(col, N) if A[i][col])
        A[col], A[pivot] = A[pivot], A[col]
        denom = A[col][col]
        A[col] = [v / denom for v in A[col]]
        for row in range(col + 1, N):
            factor = A[row][col]
            if factor:
                A[row] = [x - factor * y for x, y in zip(A[row], A[col])]
    sol = [Fraction(0)] * N
    for i in range(N - 1, -1, -1):
        sol[i] = A[i][-1] - sum(A[i][j] * sol[j] for j in range(i + 1, N))
    return dict(zip(nodes, sol))


def run():
    num_bellman = 0
    num_independent = 0
    for n in range(2, 81):
        pairs = canon_pairs(n)
        allpairs = set(map(frozenset, combinations(range(n), 2)))
        assert len(pairs) == n * (n - 1) // 2
        assert len(set(pairs.values())) == len(pairs)
        assert set(pairs.values()) == allpairs
        preds = {p: predicted(n, r, s) for (r, s), p in pairs.items()}
        assert min(preds.values()) > 0
        for p, t in preds.items():
            rhs = 2
            for letter in 'ab':
                p1 = move(n, p, letter)
                rhs += preds.get(p1, 0) if len(p1) == 2 else 0
            assert 2 * t == rhs, (n, p, t, rhs)
            num_bellman += 1
        assert Fraction(sum(preds.values()), len(preds)) == Fraction((n - 1) * (2 * n * n + n - 4), 3), n
        if n <= 11:
            exact = independent_linear(n, pairs)
            for p, v in exact.items():
                assert preds[p] == v, (n, p, preds[p], v)
                num_independent += 1
    print('VERIFY_OK', 'n=2..80', 'Bellman_states=' + str(num_bellman), 'linear_states=' + str(num_independent))


if __name__ == '__main__':
    run()
