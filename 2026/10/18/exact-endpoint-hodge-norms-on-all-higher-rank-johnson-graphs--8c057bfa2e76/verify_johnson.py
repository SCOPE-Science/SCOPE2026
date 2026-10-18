#!/usr/bin/env python3
"""Exact-rational checks for Johnson-graph cut/cycle projection norms.

Uses only the Python standard library. Running: python verify_johnson.py
The finite calculations are consistency tests, not a proof for all ranks.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def solve(A, b):
    """Gaussian elimination over the rational field."""
    N = len(b)
    M = [[F(x) for x in A[i]] + [F(b[i])] for i in range(N)]
    for c in range(N):
        p = next((i for i in range(c, N) if M[i][c]), None)
        assert p is not None, 'singular grounded Laplacian'
        M[c], M[p] = M[p], M[c]
        pc = M[c][c]
        for i in range(c+1, N):
            a = M[i][c]
            if not a:
                continue
            t = a / pc
            M[i][c] = F(0)
            for j in range(c+1, N+1):
                M[i][j] -= t * M[c][j]
    out = [F(0)] * N
    for i in range(N-1, -1, -1):
        out[i] = (M[i][N] - sum(M[i][j]*out[j] for j in range(i+1, N))) / M[i][i]
    return out


def johnson_graph(n, k):
    vertices = list(combinations(range(n), k))
    edges = []
    for i, a in enumerate(vertices):
        a = set(a)
        for j in range(i+1, len(vertices)):
            if len(a.intersection(vertices[j])) == k-1:
                edges.append((i, j))
    return vertices, edges


def exact_case(n, k):
    V, E = johnson_graph(n, k)
    size = len(V)
    assert len(E) == size*k*(n-k)//2
    L = [[0]*size for _ in range(size)]
    for a, b in E:
        L[a][a] += 1
        L[b][b] += 1
        L[a][b] -= 1
        L[b][a] -= 1
    idx = {x: i for i, x in enumerate(V)}
    u = idx[tuple(range(k))]
    v = idx[tuple(range(k-1)) + (k,)]
    b = [0]*size
    b[u], b[v] = 1, -1
    h = solve([row[:-1] for row in L[:-1]], b[:-1]) + [F(0)]
    assert all(sum(L[i][j]*h[j] for j in range(size)) == b[i]
               for i in range(size))

    q = sum(abs(h[x]-h[y]) for x, y in E)
    r = h[u]-h[v]
    c = 1+q-2*r
    predicted_q = F((k+1)*n*n - (k*k+3)*n + 2, n*(n-1))
    predicted_r = F(2*(comb(n, k)-1), comb(n, k)*k*(n-k))
    predicted_c = 1+predicted_q-2*predicted_r
    assert (q, r, c) == (predicted_q, predicted_r, predicted_c)

    # Independently check the potential orbit pattern and strict ordering.
    center = (h[u]+h[v])/2
    commons = set(range(k-1))
    a, z = k-1, k
    potentials = {}
    for label, vertex in enumerate(V):
        s = set(vertex)
        if (a in s) == (z in s):
            assert h[label] == center
        else:
            i = len(s.intersection(commons))
            signed_value = (h[label]-center) if a in s else (center-h[label])
            if i in potentials:
                assert potentials[i] == signed_value
            potentials[i] = signed_value
    p = [potentials[i] for i in range(k)]
    assert all(p[i] > (p[i-1] if i else 0) for i in range(k))
    w = [comb(k-1, i)*comb(n-k-1, k-1-i) for i in range(k)]
    assert sum(w[i]*p[i] for i in range(k)) == F(1,n)
    m1 = sum(i*w[i]*p[i] for i in range(k))
    assert m1 == F(n*(k-1)+(k-1)**2, 2*n*(n-1))
    reconstruction = 2*(F(n-1,n) +
                        sum(w[i]*i*(n-2*k+i)*(p[i]-p[i-1])
                            for i in range(1,k)))
    assert reconstruction == q
    print('PASS: n=%d k=%d vertices=%d edges=%d Q=%s C=%s R=%s' %
          (n, k, size, len(E), q, c, r))


def level_chain_case(n, k):
    """Exact independent arithmetic check of the symbolic orbit reduction."""
    assert n >= 2*k and k >= 2
    A = [[0]*k for _ in range(k)]
    for i in range(k):
        up = (k-1-i)**2
        down = i*(n-2*k+i)
        A[i][i] = n+up+down
        if i+1 < k:
            A[i][i+1] = -up
        if i > 0:
            A[i][i-1] = -down
    b = [0]*(k-1)+[1]
    p = solve(A, b)
    assert all(p[i] > (p[i-1] if i else 0) for i in range(k))
    w = [comb(k-1, i)*comb(n-k-1, k-1-i) for i in range(k)]
    s0 = sum(w[i]*p[i] for i in range(k))
    s1 = sum(i*w[i]*p[i] for i in range(k))
    assert s0 == F(1,n)
    assert s1 == F(n*(k-1)+(k-1)**2,2*n*(n-1))
    q = 2*((n-1)*s0+sum(w[i]*i*(n-2*k+i)*(p[i]-p[i-1])
                                for i in range(1,k)))
    assert q == F((k+1)*n*n-(k*k+3)*n+2, n*(n-1))
    print('PASS: orbit chain n=%d k=%d Q=%s' % (n, k, q))


if __name__ == '__main__':
    for pair in [(4,2), (5,2), (6,3), (7,3), (8,3), (8,4), (9,4)]:
        exact_case(*pair)
    for pair in [(10,5), (18,9), (40,20), (100,3), (100,50)]:
        level_chain_case(*pair)
    print('ALL JOHNSON CHECKS PASSED')
