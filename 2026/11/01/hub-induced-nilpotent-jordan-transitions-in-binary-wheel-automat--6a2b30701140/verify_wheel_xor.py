"""Standalone finite checks for neighbor-XOR dynamics on wheel graphs.

Run: python verify_wheel_xor.py
Only finite instances are checked; the all-size theorem uses algebraic proof.
"""
from collections import Counter


def wheel_step(x, n):
    """Microscopic synchronous XOR update, n rim sites plus hub n."""
    rim = x & ((1 << n) - 1)
    hub = (x >> n) & 1
    nxt = sum(
        (((rim >> ((i - 1) % n)) ^ (rim >> ((i + 1) % n)) ^ hub) & 1) << i
        for i in range(n)
    )
    return nxt | ((rim.bit_count() & 1) << n)


def wheel_rows(n):
    # Independently construct row masks from undirected graph edges.
    edges = {(i, (i + 1) % n) for i in range(n)}
    edges |= {(i, n) for i in range(n)}
    rows = [0] * (n + 1)
    for a, b in edges:
        assert a != b
        rows[a] ^= 1 << b
        rows[b] ^= 1 << a
    return rows


def mat_apply(rows, x):
    return sum(((r & x).bit_count() & 1) << i for i, r in enumerate(rows))


def matmul(a, b):
    out = []
    for row in a:
        x = 0
        while row:
            low = row & -row
            x ^= b[low.bit_length() - 1]
            row -= low
        out.append(x)
    return out


def matrank(a):
    pivots = {}
    for original in a:
        r = original
        while r:
            k = r.bit_length() - 1
            if k in pivots:
                r ^= pivots[k]
            else:
                pivots[k] = r
                break
    return len(pivots)


def block_lengths(n):
    if n % 2:
        return []
    e = n & -n
    if e == 2:
        return [3]
    if e == 4:
        return [3, 1, 1]
    return [e // 2, e // 2, 1]


def expected_rank(n, t):
    blocks = block_lengths(n)
    if not blocks:
        return n + 1
    e = n & -n
    return n - e + sum(max(length - t, 0) for length in blocks)


def expected_shell(n):
    if n % 2:
        return {0: 1 << (n + 1)}
    e = n & -n
    blocks = block_lengths(n)
    periodic = 1 << (n - e)
    counts = {0: periodic}
    prev = periodic
    for t in range(1, max(blocks) + 1):
        current = periodic * (1 << sum(min(t, length) for length in blocks))
        counts[t] = current - prev
        prev = current
    assert prev == 1 << (n + 1)
    return counts


def functional_graph_shell(n):
    N = 1 << (n + 1)
    # -1: unresolved, 0: periodic, positive: first periodic entry time.
    entry = [-1] * N
    edges = [wheel_step(x, n) for x in range(N)]
    for start in range(N):
        if entry[start] != -1:
            continue
        path = []
        local_pos = {}
        x = start
        while entry[x] < 0 and x not in local_pos:
            local_pos[x] = len(path)
            path.append(x)
            x = edges[x]
        if entry[x] == -1:
            first = local_pos[x]
            for v in path[first:]:
                entry[v] = 0
            path = path[:first]
        for v in reversed(path):
            entry[v] = entry[edges[v]] + 1
    return dict(Counter(entry))


def run():
    matrix_cases = 0
    for n in range(3, 129):
        rows = wheel_rows(n)
        for i in range(n + 1):
            assert mat_apply(rows, 1 << i) == wheel_step(1 << i, n)
        matrix = [1 << i for i in range(n + 1)]
        final_t = max(block_lengths(n) or [0])
        for t in range(final_t + 2):
            assert matrank(matrix) == expected_rank(n, t), (n, t, matrank(matrix), expected_rank(n, t))
            matrix = matmul(matrix, rows)
            matrix_cases += 1
    brute_cases = 0
    for n in range(3, 17):
        actual = functional_graph_shell(n)
        assert actual == expected_shell(n), (n, actual, expected_shell(n))
        brute_cases += 1 << (n + 1)
    print('WHEEL_XOR_VERIFY_OK')
    print('matrix_size_range=3..128')
    print('matrix_power_rank_checks=' + str(matrix_cases))
    print('functional_graph_sizes=3..16')
    print('microscopic_states=' + str(brute_cases))
    print('example_n4=' + str(expected_shell(4)))
    print('example_n6=' + str(expected_shell(6)))
    print('example_n8=' + str(expected_shell(8)))
    print('example_n12=' + str(expected_shell(12)))

if __name__ == '__main__':
    run()
