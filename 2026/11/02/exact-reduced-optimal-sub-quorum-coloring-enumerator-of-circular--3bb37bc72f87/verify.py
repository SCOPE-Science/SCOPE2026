"""Exact checks for the optimal reduced sub-quorum colorings of prism graphs.

No external packages are needed.  The transfer matrix is reconstructed from
its local alphabet, and its characteristic polynomial is computed over Z.
"""
from itertools import product
from collections import defaultdict

ALPHABET = 'UTLRV'
COLUMNS = tuple(c for c in product(ALPHABET, repeat=2)
                if ('V' not in c or c == ('V', 'V')))


def compatible(a, b):
    return all((a[r] == 'R') == (b[r] == 'L') for r in (0, 1))


def weight(c):
    return c.count('T') + c.count('R') + (c == ('V', 'V'))


def triple_ok(a, b, c):
    return compatible(a, b) and compatible(b, c) and all(
        b[r] != 'T' or sum(d != 'U' for d in (a[r], b[1-r], c[r])) <= 1
        for r in (0, 1))


def graph():
    pairs = tuple((a, b) for a in COLUMNS for b in COLUMNS if compatible(a, b))
    indices = {p: i for i, p in enumerate(pairs)}
    adj = [[] for _ in pairs]
    for a, b in pairs:
        i = indices[(a, b)]
        for c in COLUMNS:
            if triple_ok(a, b, c) and (weight(b) != 0 or weight(a) == 2):
                adj[i].append(indices[(b, c)])
    return pairs, adj


def strongly_connected_components(adj):
    n = len(adj)
    seen = set()
    order = []
    def dfs(v):
        seen.add(v)
        for w in adj[v]:
            if w not in seen:
                dfs(w)
        order.append(v)
    for v in range(n):
        if v not in seen:
            dfs(v)
    rev = [[] for _ in adj]
    for v, children in enumerate(adj):
        for w in children:
            rev[w].append(v)
    seen = set()
    out = []
    def visit(v, block):
        seen.add(v)
        block.append(v)
        for w in rev[v]:
            if w not in seen:
                visit(w, block)
    for v in reversed(order):
        if v not in seen:
            block = []
            visit(v, block)
            if len(block) > 1 or v in adj[v]:
                out.append(sorted(block))
    return sorted(out, key=lambda a: (-len(a), a))


def matrix_for_component(adj, comp):
    ix = {v: j for j, v in enumerate(comp)}
    m = len(comp)
    A = [[0] * m for _ in range(m)]
    for v in comp:
        for w in adj[v]:
            if w in ix:
                A[ix[v]][ix[w]] += 1
    return A


def traces_and_charpoly(A, count):
    n = len(A)
    mult = [[(i == j) for j in range(n)] for i in range(n)]
    cols = [[j for j, a in enumerate(row) if a] for row in A]
    tr = []
    for k in range(1, count + 1):
        nxt = [[0] * n for _ in range(n)]
        for i in range(n):
            for j, c in enumerate(mult[i]):
                if c:
                    for h in cols[j]:
                        nxt[i][h] += c * A[j][h]
        mult = nxt
        tr.append(sum(mult[i][i] for i in range(n)))
    coeff = [1]
    if count >= n:
        for k in range(1, n + 1):
            s = sum(coeff[k-j] * tr[j-1] for j in range(1, k+1))
            assert s % k == 0
            coeff.append(-s // k)
    return tr, coeff


def poly_product_ascending(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def original_graph(n):
    N = 2*n
    neighbors = [set() for _ in range(N)]
    for i in range(n):
        for x, y in ((i, (i+1)%n), (n+i, n+(i+1)%n), (i, n+i)):
            neighbors[x].add(y)
            neighbors[y].add(x)
    return neighbors


def original_reduced_count(n):
    neighbors = original_graph(n)
    V = set(range(2*n))
    result = 0
    def rec(undecided, T, matching):
        nonlocal result
        if not undecided:
            if len(T)+len(matching) != n:
                return
            selected = set(T)
            for u, v in matching:
                selected.add(u)
                selected.add(v)
            if any(sum(w in selected for w in neighbors[t]) > 1 for t in T):
                return
            # Verify on the actual graph, not merely the transfer rules.
            classes = [(t,) for t in T] + list(matching)
            color = {v: j for j, C in enumerate(classes) for v in C}
            for v, j in color.items():
                colored = [u for u in ({v} | neighbors[v]) if u in color]
                own = sum(color[u] == j for u in colored)
                assert 2*own >= len(colored)
            result += 1
            return
        v = min(undecided)
        tail = undecided - {v}
        rec(tail, T, matching)
        rec(tail, T + (v,), matching)
        for u in neighbors[v] & tail:
            rec(tail - {u}, T, matching + ((v, u),))
    rec(V, (), ())
    return result


def main():
    pairs, adj = graph()
    assert len(COLUMNS) == 17 and len(pairs) == 119
    assert sum(map(len, adj)) == 343
    # Every weight-two column is followed by a weight-zero column.
    for a, b in pairs:
        if weight(b) == 2:
            for c in COLUMNS:
                if triple_ok(a, b, c):
                    assert weight(c) == 0
    comp = strongly_connected_components(adj)
    assert sorted(map(len, comp)) == [2, 2, 49]
    all_traces = [0] * 20
    p5 = [-1, 1, 0, -1, 1, 1]
    p7 = [-1, -2, 0, 2, 2, -3, -2, 1]
    expected49 = list(reversed(poly_product_ascending(p5, p7))) + [0] * 37
    for C in comp:
        A = matrix_for_component(adj, C)
        tr, charpoly = traces_and_charpoly(A, max(len(A), 20))
        if len(C) == 49:
            assert charpoly == expected49
        else:
            assert charpoly == [1, 0, -1]
        for i in range(20):
            all_traces[i] += tr[i]
    expected = {3:16, 4:65, 5:151, 6:434, 7:1177, 8:3225,
                9:8890, 10:24337, 11:66947, 12:183638}
    for n, val in expected.items():
        assert all_traces[n-1] == val, (n, all_traces[n-1], val)
    print('EXACT_119_STATE_TRANSFER_AND_CHARPOLY_OK',
          [len(x) for x in comp])
    for n in range(3, 7):
        direct = original_reduced_count(n)
        assert direct == all_traces[n-1]
        print('INDEPENDENT_ORIGINAL_GRAPH_COUNT_OK', n, direct)
    print('FORMAL_RATIONAL_GENERATING_FUNCTION_CHECK_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
