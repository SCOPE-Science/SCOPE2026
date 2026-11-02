"""Direct finite tests for exact solid-metric dimension of directed tori.

Run: python verify.py
No third-party packages are needed. The all-parameter theorem is proved
mathematically; these tests check its construction against the original
ordered-pair distance definition on many finite instances.
"""


def landmarks(m, n):
    """Construct the claimed optimal set; here 3 <= m <= n."""
    assert 3 <= m <= n
    if n >= 2 * m:
        return {(j % m, j) for j in range(n)}
    t = n - m
    return (
        {(i, i) for i in range(m)}
        | {(i, i + m) for i in range(t)}
        | {(i, (i + 1) % m) for i in range(t, m)}
    )


def directed_distance(s, u, m, n):
    return (u[0] - s[0]) % m + (u[1] - s[1]) % n


def directly_solid(m, n, S):
    """Check the paper's original ordered-pair criterion, without expansion lemma."""
    V = [(i, j) for i in range(m) for j in range(n)]
    distances = {s: [directed_distance(s, u, m, n) for u in V] for s in S}
    for u in range(len(V)):
        for v in range(len(V)):
            if u == v:
                continue
            if not any(ds[u] < ds[v] for ds in distances.values()):
                return V[u], V[v]
    return None


def check_interval_expansion(m, n, S):
    """Separately check the sufficient combinatorial expansion property."""
    for length in range(1, m):
        for start in range(m):
            columns = {(start + j) % m for j in range(length)}
            occupied_rows = {y for x, y in S if x in columns}
            assert len(occupied_rows) >= length + 1


def main():
    total = 0
    for m in range(3, 10):
        for n in range(m, max(2 * m + 2, 16) + 1):
            S = landmarks(m, n)
            assert len(S) == max(n, 2 * m), (m, n, len(S))
            assert all(sum(x == i for x, y in S) >= 2 for i in range(m))
            assert all(any(y == j for x, y in S) for j in range(n))
            check_interval_expansion(m, n, S)
            failure = directly_solid(m, n, S)
            assert failure is None, (m, n, failure)
            total += 1
    print('DIRECT_ORDERED_PAIRS_OK', total, 'parameter_pairs')
    print('INTERVAL_EXPANSION_OK', total, 'parameter_pairs')
    print('EXACT_SIZES_OK', total, 'parameter_pairs')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
