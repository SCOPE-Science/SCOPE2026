"""Independent finite checks for open-neighborhood sequences of rook graphs.

No external packages are required. The universal proof is separate from this test.
"""
from functools import lru_cache


def rook(p, q):
    cells = [(i, j) for i in range(p) for j in range(q)]
    neighbors = []
    for i, j in cells:
        mask = 0
        for k, l in cells:
            if (i == k and j != l) or (j == l and i != k):
                mask |= 1 << (k * q + l)
        neighbors.append(mask)
    return cells, neighbors


def longest_length(p, q):
    cells, neighborhoods = rook(p, q)

    @lru_cache(maxsize=None)
    def dp(covered):
        return max((1 + dp(covered | n) for n in neighborhoods
                    if n & ~covered), default=0)

    return dp(0), dp.cache_info().currsize


def is_forest(p, q, subset):
    parent = list(range(p + q))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for i in range(p):
        for j in range(q):
            if subset & (1 << (i*q+j)):
                a, b = find(i), find(p+j)
                if a == b:
                    return False
                parent[a] = b
    return True


def uncovered_formula(p, q, subset):
    cells, neighborhoods = rook(p, q)
    selected_rows = {i for k, (i, j) in enumerate(cells) if subset & (1<<k)}
    selected_cols = {j for k, (i, j) in enumerate(cells) if subset & (1<<k)}
    uncovered = 0
    for k, (i, j) in enumerate(cells):
        if i not in selected_rows and j not in selected_cols:
            uncovered |= 1<<k
        elif subset & (1<<k):
            if not any(subset & (1<<h) for h, (a, b) in enumerate(cells)
                       if h != k and (a == i or b == j)):
                uncovered |= 1<<k
    covered = 0
    for k, mask in enumerate(neighborhoods):
        if subset & (1<<k):
            covered |= mask
    full = (1<<(p*q))-1
    return uncovered == (full ^ covered)


def test_reachable(p, q):
    cells, neighborhoods = rook(p, q)
    seen = {0}
    stack = [0]
    while stack:
        subset = stack.pop()
        assert is_forest(p, q, subset), (p, q, subset, 'cycle')
        assert uncovered_formula(p, q, subset), (p, q, subset, 'uncovered')
        covered = 0
        for k, n in enumerate(neighborhoods):
            if subset & (1<<k):
                covered |= n
        for k, n in enumerate(neighborhoods):
            if not (subset & (1<<k)) and (n & ~covered):
                nxt = subset | (1<<k)
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
    return len(seen)


def main():
    for p in range(2, 6):
        for q in range(p, 9):
            value, states = longest_length(p, q)
            expected = p + q - 2 + (q == p + 1)
            assert value == expected, (p, q, value, expected)
            print(f'OPT {p}x{q}: {value}, DP states={states}')
    for p, q in [(2, 2), (2, 3), (2, 5), (3, 3), (3, 4), (4, 4)]:
        n = test_reachable(p, q)
        print(f'REACH {p}x{q}: {n} legal-prefix sets, forest/uncovered checks pass')
    print('PASS: all independent finite checks')


if __name__ == '__main__':
    main()
