"""Independent finite checks for the exact Cerny pair-synchronization metric.

Execute with Python 3: python verify.py. The general theorem requires the
symbolic proof in RESULT.md; finite tests are supplementary only.
"""
from collections import deque


def rank(n, pair):
    if not pair:
        return 0
    i, j = pair
    d = j - i
    return n * d - i if 2 * d < n else (n + 1) * (n - d) - n - i


def step(n, pair, c):
    if not pair:
        return ()
    if c == 'a':
        result = sorted({(x + 1) % n for x in pair})
    elif c == 'b':
        result = sorted({0 if x == n - 1 else x for x in pair})
    else:
        raise ValueError('Only a or b permitted')
    return tuple(result) if len(result) == 2 else ()


def master(n):
    m = n // 2
    head = n - 1 if n % 2 else m - 1
    return 'a' * head + 'b' + ('a' * (n - 1) + 'b') * (m - 1)


def independent_reverse_bfs(n, pairs):
    pred = {pair: [] for pair in pairs}
    d = {}
    queue = deque()
    for pair in pairs:
        for c in 'ab':
            nxt = step(n, pair, c)
            if not nxt:
                if pair not in d:
                    d[pair] = 1
                    queue.append(pair)
            else:
                pred[nxt].append(pair)
    while queue:
        v = queue.popleft()
        for u in pred[v]:
            if u not in d:
                d[u] = d[v] + 1
                queue.append(u)
    return d


checks = 0
for n in range(2, 81):
    all_pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    N = n * (n - 1) // 2
    ranks = [rank(n, pair) for pair in all_pairs]
    assert sorted(ranks) == list(range(1, N + 1)), n
    checks += len(all_pairs)
    for pair in all_pairs:
        h = rank(n, pair)
        delta = {c: rank(n, step(n, pair, c)) - h for c in 'ab'}
        assert list(delta.values()).count(-1) == 1, (n, pair, delta)
        assert all(x >= -1 for x in delta.values()), (n, pair, delta)
        checks += 2
    word = master(n)
    assert len(word) == N
    assert (0, n // 2) in all_pairs
    assert rank(n, (0, n // 2)) == N
    current = (0, n // 2)
    seen = {current}
    for p, c in enumerate(word):
        nxt = step(n, current, c)
        assert rank(n, nxt) == N - p - 1
        if nxt:
            assert nxt not in seen
            seen.add(nxt)
        current = nxt
    assert not current and len(seen) == N
    checks += N
    if n <= 35:
        distances = independent_reverse_bfs(n, all_pairs)
        assert len(distances) == N
        assert all(distances[pair] == rank(n, pair) for pair in all_pairs)
        checks += N
    # The complete suffix of length h must be the unique optimal word for
    # whichever pair has rank h, not just for the maximal pair.
    inv = {rank(n, pair): pair for pair in all_pairs}
    for h in range(1, N + 1):
        p = inv[h]
        for c in word[-h:]:
            p = step(n, p, c)
        assert not p
    checks += N
print('VERIFY_OK: n=2..80 all ranks, transitions, unique decreasing edges,')
print('          explicit master paths and their every suffix;')
print('          independent reverse BFS n=2..35.')
print('finite assertions:', checks)
print('examples:', [(n, master(n)) for n in (3,4,5,6,7,8)])
