"""Independent maximum-clique check for short multiset deletion codes."""
from itertools import combinations


def compositions(n, q):
    if q == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for t in compositions(n - a, q - 1):
                yield (a,) + t


def max_clique(q, n):
    vs = list(compositions(n, q))
    N = len(vs)
    neighborhoods = [0] * N
    for i in range(N):
        for j in range(i):
            if sum(min(a, b) for a, b in zip(vs[i], vs[j])) <= 2:
                neighborhoods[i] |= 1 << j
                neighborhoods[j] |= 1 << i

    def coloring_bound(bits):
        # Proper greedy coloring of the compatibility graph: clique <= colors.
        # Return ordered vertices and color upper bounds for branch-and-bound.
        verts, colors = [], []
        rest = bits
        color = 0
        while rest:
            color += 1
            free = rest
            while free:
                low = free & -free
                v = low.bit_length() - 1
                verts.append(v)
                colors.append(color)
                rest ^= low
                free &= ~(low | neighborhoods[v])
        return verts, colors

    best = 0

    def dfs(bits, depth):
        nonlocal best
        if not bits:
            if depth > best:
                best = depth
            return
        vs, col = coloring_bound(bits)
        for i in range(len(vs) - 1, -1, -1):
            if depth + col[i] <= best:
                return
            v = vs[i]
            dfs(bits & neighborhoods[v], depth + 1)
            bits ^= 1 << v

    dfs((1 << N) - 1, 0)
    return best, N


def target(q, n):
    return q + 1 if q + 2 <= n <= 2 * q else q


if __name__ == '__main__':
    rows = []
    for q in range(2, 6):
        for n in range(q + 2, 2 * q + 2):
            val, count = max_clique(q, n)
            expected = target(q, n)
            assert val == expected, (q, n, val, expected)
            rows.append((q, n, count, val))
    # A separate diagnostic checks sharpness at the lower boundary, not exact size.
    for q in range(2, 6):
        val, count = max_clique(q, q + 1)
        assert val >= q + 2, (q, val)
        rows.append((q, q + 1, count, val))
    for q, n, v, m in sorted(rows):
        print('q=%d n=%d vectors=%d maximum=%d' % (q, n, v, m))
    print('VERIFY_SMALL_OK', len(rows))
