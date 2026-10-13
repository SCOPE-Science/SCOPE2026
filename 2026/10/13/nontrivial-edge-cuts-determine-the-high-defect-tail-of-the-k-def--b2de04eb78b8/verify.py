from itertools import combinations


def crown_edges(n):
    return [(i, n+j) for i in range(n) for j in range(n) if i != j]


def cut_size(n, mask):
    return sum(((mask >> u) & 1) != ((mask >> v) & 1) for u, v in crown_edges(n))


def restricted_cut_min(n):
    N = 2*n
    best = None
    for mask in range(1, 1 << N):
        s = mask.bit_count()
        if 2 <= s <= N-2:
            c = cut_size(n, mask)
            best = c if best is None else min(best, c)
    return best


def rgs_partitions(N):
    a = [0]*N
    def rec(pos, mx):
        if pos == N:
            yield tuple(a)
            return
        for c in range(mx+2):
            a[pos] = c
            yield from rec(pos+1, max(mx, c))
    if N == 0:
        yield ()
    else:
        a[0] = 0
        yield from rec(1, 0)


def min_colors_by_defect(n):
    edges = crown_edges(n)
    best = {}
    for lab in rgs_partitions(2*n):
        q = 1 + max(lab)
        k = sum(lab[u] == lab[v] for u, v in edges)
        old = best.get(k)
        if old is None or q < old:
            best[k] = q
    return best


subset_checks = 0
for n in range(4, 10):
    got = restricted_cut_min(n)
    want = 2*n - 4
    assert got == want, (n, got, want)
    subset_checks += (1 << (2*n)) - 2 - 4*n

partition_counts = {8: 4140, 10: 115975}
partition_checks = 0
for n in (4, 5):
    best = min_colors_by_defect(n)
    m = n*(n-1)
    T = n*n - 3*n + 4
    special = (n-1)*(n-1)
    assert best[T] == 2
    for k in range(T+1, m+1):
        expected = 1 if k == m else (2 if k == special else 0)
        actual = best.get(k, 0)
        assert actual == expected, (n, k, actual, expected)
    partition_checks += partition_counts[2*n]

for n in range(4, 101):
    m = n*(n-1)
    T = n*n - 3*n + 4
    special = (n-1)*(n-1)
    assert m - T == 2*n - 4
    assert m - special == n - 1
    assert T < special < m

print(
    'ALL CHECKS PASSED; '
    f'restricted_cut_orders=4..9; subset_checks={subset_checks}; '
    f'partition_orders=4,5; set_partitions={partition_checks}; '
    'symbolic_orders=4..100'
)
