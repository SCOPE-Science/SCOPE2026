from itertools import permutations

def direct_check(grid, q):
    m = len(grid)
    n = len(grid[0])
    # proper: each row and column has distinct colors
    for row in grid:
        if len(set(row)) != n:
            return False
    for j in range(n):
        col = [grid[i][j] for i in range(m)]
        if len(set(col)) != m:
            return False

    # ordinary odd coloring: each non-isolated vertex has a neighborhood
    # color whose multiplicity is odd.
    for i in range(m):
        for j in range(n):
            counts = [0] * q
            for jj in range(n):
                if jj != j:
                    counts[grid[i][jj]] += 1
            for ii in range(m):
                if ii != i:
                    counts[grid[ii][j]] += 1
            if not any(x % 2 == 1 for x in counts):
                return False
    return True

def unbalanced_grid(m, n):
    # m < n, colors Z_n
    return [[(i + j) % n for j in range(n)] for i in range(m)]

def balanced_grid(n):
    # q=n+2. Use F=Z_q \ {0,2} as column offsets.
    q = n + 2
    F = [x for x in range(q) if x not in (0, 2)]
    assert len(F) == n
    return [[(i + F[j]) % q for j in range(n)] for i in range(n)]

def proper_completions_balanced(n, q):
    # WLOG fix first row to 0,1,...,n-1.
    # Any q-coloring of K_n square K_n can be globally relabeled so a
    # specified row has these colors, provided q is n or n+1.
    grid = [[None] * n for _ in range(n)]
    grid[0] = list(range(n))
    row_used = [set() for _ in range(n)]
    col_used = [set() for _ in range(n)]
    row_used[0] = set(range(n))
    for j in range(n):
        col_used[j].add(j)

    leaves = 0
    odd_leaves = 0

    cells = [(i, j) for i in range(1, n) for j in range(n)]

    def rec(pos):
        nonlocal leaves, odd_leaves
        if pos == len(cells):
            leaves += 1
            if direct_check(grid, q):
                odd_leaves += 1
            return
        i, j = cells[pos]
        for c in range(q):
            if c in row_used[i] or c in col_used[j]:
                continue
            grid[i][j] = c
            row_used[i].add(c)
            col_used[j].add(c)
            rec(pos + 1)
            row_used[i].remove(c)
            col_used[j].remove(c)
            grid[i][j] = None

    rec(0)
    return leaves, odd_leaves

unbalanced = 0
for n in range(2, 21):
    for m in range(1, n):
        g = unbalanced_grid(m, n)
        if not direct_check(g, n):
            raise AssertionError(("unbalanced construction failed", m, n))
        unbalanced += 1

balanced = 0
for n in range(2, 51):
    g = balanced_grid(n)
    if not direct_check(g, n + 2):
        raise AssertionError(("balanced construction failed", n))
    balanced += 1

proper_leaves = 0
for n in range(2, 5):
    for q in (n, n + 1):
        leaves, odd = proper_completions_balanced(n, q)
        proper_leaves += leaves
        if odd != 0:
            raise AssertionError(("unexpected balanced odd coloring", n, q, odd))

print(
    "ALL CHECKS PASSED; "
    f"unbalanced_constructions={unbalanced}; "
    f"balanced_constructions={balanced}; "
    "balanced_exhaustive_n=2..4; "
    f"proper_completions_checked={proper_leaves}"
)
