"""Exact, dependency-free verification of the small-habitat diffusion/Moran theorem.
Run: python3 verify_moran.py
All polynomial arithmetic uses unbounded Python integers; no floating point.
"""
from itertools import combinations, permutations


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    return trim([((p[i] if i < len(p) else 0) +
                  (q[i] if i < len(q) else 0))
                 for i in range(max(len(p), len(q)))])


def neg(p):
    return tuple(-a for a in p)


def sub(p, q):
    return add(p, neg(q))


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def scale(p, n):
    return trim([n * a for a in p])


def deriv(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def evaluate(p, t):
    out = 0
    for a in reversed(p):
        out = out * t + a
    return out


def det(mat):
    n = len(mat)
    if not n:
        return (1,)
    ans = (0,)
    for order in permutations(range(n)):
        inv = sum(order[i] > order[j] for i in range(n)
                  for j in range(i + 1, n))
        term = (1,)
        for i, j in enumerate(order):
            term = mul(term, mat[i][j])
        ans = sub(ans, term) if inv & 1 else add(ans, term)
    return ans


def adjugate(mat):
    n = len(mat)
    result = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [[mat[r][c] for c in range(n) if c != i]
                     for r in range(n) if r != j]
            term = det(minor)
            result[i][j] = neg(term) if (i + j) & 1 else term
    return result


def connected(n, edges):
    seen = {0}
    frontier = [0]
    while frontier:
        u = frontier.pop()
        for a, b in edges:
            v = b if a == u else (a if b == u else None)
            if v is not None and v not in seen:
                seen.add(v)
                frontier.append(v)
    return len(seen) == n


def make_data(n, edges):
    A = [[0] * n for _ in range(n)]
    for u, v in edges:
        A[u][v] = A[v][u] = 1
    deg = [sum(row) for row in A]
    L = [[(deg[i] if i == j else 0) - A[i][j]
          for j in range(n)] for i in range(n)]
    matrix = [[trim([int(i == j), L[i][j]])
               for j in range(n)] for i in range(n)]
    return A, L, adjugate(matrix)


def exact_numerator_denominator(n, adj, A, source):
    k = sum(source)
    centered = [n * bit - k for bit in source]
    z = []
    for i in range(n):
        term = (0,)
        for j in range(n):
            term = add(term, scale(adj[i][j], centered[j]))
        z.append(term)
    numerator = (0,)
    denominator = (0,)
    for i in range(n):
        denominator = add(denominator, mul(z[i], z[i]))
        for j in range(n):
            if A[i][j]:
                numerator = add(numerator, mul(z[i], z[j]))
    return numerator, denominator, z


def special_four_path(n, edges, source):
    if n != 4 or len(edges) != 3 or sum(source) != 2:
        return False
    deg = [sum(i in e for e in edges) for i in range(n)]
    if sorted(deg) != [1, 1, 2, 2]:
        return False
    same_source = sum(source[u] and source[v] for u, v in edges)
    same_nonsource = sum(not source[u] and not source[v] for u, v in edges)
    return same_source == same_nonsource == 1


def verify():
    graphs_by_n = {}
    tests_by_n = {}
    exceptions = []
    for n in (2, 3, 4):
        possible_edges = list(combinations(range(n), 2))
        graphs = tests = 0
        for graph_mask in range(1 << len(possible_edges)):
            edges = [e for bit, e in enumerate(possible_edges)
                     if (graph_mask >> bit) & 1]
            if not connected(n, edges):
                continue
            graphs += 1
            A, _L, adj = make_data(n, edges)
            for mask in range(1, (1 << n) - 1):
                source = tuple((mask >> i) & 1 for i in range(n))
                num, den, _z = exact_numerator_denominator(n, adj, A, source)
                assert evaluate(den, 0) > 0
                W = sub(mul(deriv(num), den), mul(num, deriv(den)))
                exceptional = special_four_path(n, edges, source)
                assert (any(a < 0 for a in W)) == exceptional, (
                    'coefficient-certificate discrepancy', n, edges, source, W)
                if exceptional:
                    assert evaluate(W, 0) > 0 and evaluate(W, 1) < 0
                    exceptions.append((edges, source))
                tests += 1
        graphs_by_n[n] = graphs
        tests_by_n[n] = tests
    assert graphs_by_n == {2: 1, 3: 4, 4: 38}
    assert tests_by_n == {2: 2, 3: 24, 4: 532}
    assert len(exceptions) == 24

    # Check one canonical representative symbolically, not numerically.
    n = 4
    edges = [(0, 1), (1, 2), (2, 3)]
    A, L, adj = make_data(n, edges)
    num, den, z = exact_numerator_denominator(n, adj, A, (0, 0, 1, 1))
    # n/(2m) = 2/3; I = ((2t+1)(6t+1))/(3(10t^2+6t+1)).
    quad = (1, 6, 10)
    assert mul(scale(num, 2), quad) == mul(den, mul((1, 2), (1, 6)))
    # C = ((6t^2+4t+1))/(2(10t^2+6t+1)).
    lap_num = (0,)
    for u, v in edges:
        diff = sub(z[u], z[v])
        lap_num = add(lap_num, mul(diff, diff))
    assert mul(lap_num, quad) == mul(den, (1, 4, 6))

    print('VERIFY_OK graphs=1,4,38 profiles=2,24,532 '
          'exceptions=24 exactly_P4_end_blocks=1 '
          'Moran_exact_identity=1 Geary_exact_identity=1')


if __name__ == '__main__':
    verify()
