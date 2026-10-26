"""Exact-rational checks for endpoint cut/cycle projection norms on strongly regular graphs.

Uses only Python's standard library. Run: python check_srg.py
All floating-point arithmetic is avoided.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product


def graph(nodes, predicate):
    nodes = list(nodes)
    return nodes, [(i, j) for i in range(len(nodes)) for j in range(i + 1, len(nodes))
                   if predicate(nodes[i], nodes[j])]


def rook(k):
    return graph(product(range(k), repeat=2), lambda x, y: x[0] == y[0] or x[1] == y[1])


def shrikhande():
    differences = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    return graph(product(range(4), repeat=2), lambda x, y:
                 ((x[0] - y[0]) % 4, (x[1] - y[1]) % 4) in differences)


def cycle(n):
    return graph(range(n), lambda x, y: (x - y) % n in (1, n - 1))


def petersen():
    return graph(range(10), lambda x, y:
                 (x < 5 and y < 5 and (x-y) % 5 in (1, 4)) or
                 (x >= 5 and y >= 5 and (x-y) % 5 in (2, 3)) or
                 (abs(x-y) == 5))


def paley(q):
    sq = {j*j % q for j in range(1, q)}
    return graph(range(q), lambda x, y: (x-y) % q in sq)


def triangular(n):
    return graph(combinations(range(n), 2), lambda x, y: len(set(x) & set(y)) == 1)


def inverse(M):
    n = len(M)
    a = [[F(M[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[pivot], a[col] = a[col], a[pivot]
        d = a[col][col]
        a[col] = [t / d for t in a[col]]
        for i in range(n):
            if i == col: continue
            t = a[i][col]
            if t:
                a[i] = [a[i][j] - t*a[col][j] for j in range(2*n)]
    return [row[n:] for row in a]


def verify(name, data):
    nodes, edges = data
    n = len(nodes)
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    degrees = {len(N) for N in neighbors}
    assert len(degrees) == 1
    d = degrees.pop()
    adjacent = {tuple(sorted(e)) for e in edges}
    lam_set = set(); mu_set = set()
    for u in range(n):
        for v in range(u+1, n):
            target = lam_set if (u,v) in adjacent else mu_set
            target.add(len(neighbors[u] & neighbors[v]))
    assert len(lam_set) == 1 and len(mu_set) == 1
    lam = lam_set.pop(); mu = mu_set.pop()
    assert mu > 0
    m = d-lam-1
    assert m >= 0
    assert (n-d-1)*mu == d*m
    # Independently calculate the full cut projector via the inverse grounded Laplacian.
    lap = [[0]*n for _ in range(n)]
    for u, v in edges:
        lap[u][u] += 1; lap[v][v] += 1
        lap[u][v] -= 1; lap[v][u] -= 1
    inv = inverse([row[:n-1] for row in lap[:n-1]])
    qb = []; pb = []; ts = []
    assert len(edges) > 0
    for i, (u, v) in enumerate(edges):
        U = neighbors[u] - neighbors[v] - {v}
        V = neighbors[v] - neighbors[u] - {u}
        assert len(U) == len(V) == m
        T = sum(1 for a, b in edges if a in U and b in U or a in V and b in V)
        predicted_q = F(2*(d*(2*m+mu)-2*m-T), mu*n)
        predicted_p = predicted_q+1-F(4*(m+mu),mu*n)
        rhs = [F((j == u)-(j == v)) for j in range(n-1)]
        potential = [sum(inv[j][k]*rhs[k] for k in range(n-1)) for j in range(n-1)]+[F(0)]
        column = [potential[a]-potential[b] for a, b in edges]
        qactual = sum(map(abs, column), F(0))
        pactual = sum((abs((1 if j == i else 0)-x) for j,x in enumerate(column)), F(0))
        assert qactual == predicted_q, (name,i,qactual,predicted_q)
        assert pactual == predicted_p, (name,i,pactual,predicted_p)
        qb.append(qactual); pb.append(pactual); ts.append(T)
    assert max(qb) == F(2*(d*(2*m+mu)-2*m-min(ts)), mu*n)
    assert max(pb) == max(qb)+1-F(4*(m+mu),mu*n)
    print(f'{name}: srg=({n},{d},{lam},{mu}) edges={len(edges)} '
          f'T={dict(sorted(Counter(ts).items()))} ||Q||={max(qb)} ||P||={max(pb)}')
    return n, len(edges), max(qb), max(pb)


def main():
    tests = [('five-cycle',cycle(5)), ('Petersen',petersen()),
             ('rook-3x3',rook(3)), ('Paley-13',paley(13)),
             ('rook-4x4',rook(4)), ('Shrikhande',shrikhande()),
             ('triangular-6',triangular(6)),('rook-5x5',rook(5))]
    results = [verify(name, g) for name,g in tests]
    assert results[4][2:] == (F(9,4),F(21,8))
    assert results[5][2:] == (F(19,8),F(11,4))
    print('SRG_HODGE_EXACT_OK cases=%d columns=%d' % (len(results),sum(x[1] for x in results)))

if __name__ == '__main__': main()
