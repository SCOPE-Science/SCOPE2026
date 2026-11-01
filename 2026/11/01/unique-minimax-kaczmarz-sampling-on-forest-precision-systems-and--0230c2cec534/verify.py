"""Exact rational checks for the tree-precision Kaczmarz sampling law.

Uses only the Python standard library.  The proof in RESULT.md is for all
finite trees; these finite checks are independent regression tests, not a
substitute for the proof.
"""
from fractions import Fraction as F
from random import Random

COUNT = 0

def confirm(v, msg='assertion failed'):
    global COUNT
    COUNT += 1
    if not v:
        raise AssertionError(msg)


def covariance(n, edges):
    adj = [[] for _ in range(n)]
    for a, b, r in edges:
        adj[a].append((b, r))
        adj[b].append((a, r))
    g = [[F(0) for _ in range(n)] for _ in range(n)]
    for source in range(n):
        seen = {source}
        stack = [(source, F(1))]
        while stack:
            a, product = stack.pop()
            g[source][a] = product
            for b, r in adj[a]:
                if b not in seen:
                    seen.add(b)
                    stack.append((b, product * r))
        confirm(len(seen) == n, 'input must be a tree')
    return g


def precision(n, edges):
    k = [[F(int(a == b)) for b in range(n)] for a in range(n)]
    for a, b, r in edges:
        inc = r * r / (1 - r * r)
        off = -r / (1 - r * r)
        k[a][a] += inc
        k[b][b] += inc
        k[a][b] += off
        k[b][a] += off
    return k


def product(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def fixture(n, edges):
    confirm(len(edges) == n - 1)
    g = covariance(n, edges)
    k = precision(n, edges)
    identity = product(g, k)
    for i in range(n):
        for j in range(n):
            confirm(identity[i][j] == int(i == j), 'precision inversion')
            confirm(g[i][j] == g[j][i], 'Gram symmetry')
            confirm(k[i][j] == k[j][i], 'precision symmetry')
    d = [F(1) for _ in range(n)]
    for a, b, r in edges:
        w = abs(r) / (1 - abs(r))
        d[a] += w
        d[b] += w
    total = sum(d)
    confirm(total == F(n) + 2 * sum((abs(r) / (1 - abs(r)) for _, _, r in edges), F(0)))
    p = [v / total for v in d]
    confirm(sum(p) == 1)
    confirm(all(v > 0 for v in p))
    lap = [[(d[i] if i == j else F(0)) - k[i][j]
            for j in range(n)] for i in range(n)]
    # Independent signed-edge sum-of-squares reconstruction.
    sos = [[F(0) for _ in range(n)] for _ in range(n)]
    signs_adj = [[] for _ in range(n)]
    for a, b, r in edges:
        off = k[a][b]
        if off:
            sign = 1 if off > 0 else -1
            w = abs(off)
            sos[a][a] += w
            sos[b][b] += w
            sos[a][b] -= sign * w
            sos[b][a] -= sign * w
            signs_adj[a].append((b, sign))
            signs_adj[b].append((a, sign))
    for i in range(n):
        for j in range(n):
            confirm(lap[i][j] == sos[i][j], 'PSD edge factorization')
    # A sign vector with sigma_i sigma_j = sign(K_ij).
    sig = [None] * n
    for root in range(n):
        if sig[root] is None:
            sig[root] = 1
            stack = [root]
            while stack:
                u = stack.pop()
                for v, sign in signs_adj[u]:
                    if sig[v] is None:
                        sig[v] = sign * sig[u]
                        stack.append(v)
                    else:
                        confirm(sig[v] == sign * sig[u])
    confirm(sum(sig[i] * k[i][j] * sig[j]
                for i in range(n) for j in range(n)) == total)
    for i in range(n):
        confirm(sum(lap[i][j] * sig[j] for j in range(n)) == 0)
        confirm(d[i] * sig[i] == sum(k[i][j] * sig[j] for j in range(n)))
        confirm(p[i] == d[i] / total)
    return p, F(1) / total


def run():
    # Exact heterogeneous example including a negative edge correlation.
    p, gamma = fixture(5, [(0, 1, F(1, 2)), (1, 2, -F(1, 3)),
                           (1, 3, F(1, 4)), (3, 4, F(2, 5))])
    confirm(p == [F(1, 5), F(17, 60), F(3, 20), F(1, 5), F(1, 6)])
    confirm(gamma == F(1, 10))

    # Topology invariance at identical edge magnitude, with signed edges.
    for n in range(2, 11):
        path = [(j - 1, j, F(1, 2)) for j in range(1, n)]
        star = [(0, j, F(1, 2)) for j in range(1, n)]
        ppath, gpath = fixture(n, path)
        pstar, gstar = fixture(n, star)
        want = F(1, 2) / (F(n) + F(n - 2, 2))
        confirm(gpath == want)
        confirm(gstar == want)
        confirm(sum(ppath) == sum(pstar) == 1)

    # Random edge signs, zero edges and varying magnitudes.
    rng = Random(20261028)
    choices = [F(0), F(1, 2), -F(1, 3), F(2, 5),
               -F(3, 7), F(1, 4), -F(2, 3)]
    for n in range(2, 11):
        for _ in range(26):
            edges = [(rng.randrange(v), v, rng.choice(choices))
                     for v in range(1, n)]
            fixture(n, edges)
    print(f'PASS: {COUNT} exact rational assertions; n=2..10; varied tree topologies and edge signs.')

if __name__ == '__main__':
    run()
