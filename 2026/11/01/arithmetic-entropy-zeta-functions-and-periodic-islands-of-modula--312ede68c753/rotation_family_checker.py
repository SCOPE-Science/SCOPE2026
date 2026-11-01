"""Independent exact-arithmetic checks for modular connect-the-dots interval maps.

Usage: python rotation_family_checker.py
Requires Python >=3.9 and standard library only. Finite tests do not replace
proofs of statements quantified over all n, q, or all iteration times.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def model(n, q):
    assert n >= 3 and 1 <= q < n
    w = n - q - 1
    cells = list(range(n - 1))
    aff = {}
    adj = {}
    for i in cells:
        if i == w:
            aff[i] = (-(n - 1), (n - 1) * (w + 1))
            adj[i] = list(cells)
        else:
            delta = q if i < w else q - n
            aff[i] = (1, delta)
            adj[i] = [i + delta]
    return w, aff, adj


def periodic_graph_words(adj, length):
    for s in adj:
        stack = [(s, (s,))]
        while stack:
            v, seq = stack.pop()
            if len(seq) == length:
                if s in adj[v]:
                    yield seq
            else:
                for u in adj[v]:
                    stack.append((u, seq + (u,)))


def fixed_point_from_word(aff, word):
    a, b = 1, 0
    for i in word:
        u, v = aff[i]
        a, b = u * a, u * b + v
    assert a != 1, (aff, word)
    x = Fraction(-b, a - 1)
    y = x
    for i in word:
        assert i <= y <= i + 1, (word, i, y)
        u, v = aff[i]
        y = u * y + v
    assert y == x
    return x


def graph_matrix(adj):
    n = len(adj)
    return [[int(j in adj[i]) for j in range(n)] for i in range(n)]


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def det_integer(A):
    """Exact determinant by fraction-free Bareiss elimination."""
    M = [list(row) for row in A]
    n = len(M)
    if n == 0:
        return 1
    prev, sign = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            p = next((p for p in range(k + 1, n) if M[p][k]), None)
            if p is None:
                return 0
            M[k], M[p] = M[p], M[k]
            sign = -sign
        pivot = M[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                t = M[i][j] * pivot - M[i][k] * M[k][j]
                assert t % prev == 0
                M[i][j] = t // prev
        for i in range(k + 1, n):
            M[i][k] = 0
        prev = pivot
    return sign * M[-1][-1]


def check():
    scenarios = 0
    words = 0
    for n in range(3, 15):
        for q in range(1, n):
            scenarios += 1
            d = gcd(n, q)
            m = n // d
            w, aff, adj = model(n, q)
            N = n - 1
            # All slopes, images, graph transitions match exact knot interpolation.
            for i in range(N):
                u, v = aff[i]
                assert u * i + v == (i + q) % n
                assert u * (i + 1) + v == (i + 1 + q) % n
                low, high = sorted([u * i + v, u * (i + 1) + v])
                assert adj[i] == list(range(low, high))
            # Removing the hub leaves exactly d-1 cycles of length m,
            # and one directed string of length m-1 terminating at hub.
            hub_residue = w % d
            hub_class = [i for i in range(N) if i % d == hub_residue]
            assert len(hub_class) == m - 1
            assert w in hub_class
            for r in range(d):
                nodes = [i for i in range(N) if i % d == r]
                if r == hub_residue:
                    assert len(nodes) == m - 1
                    assert all(adj[i] == [(i + q) % n] for i in nodes if i != w)
                else:
                    assert len(nodes) == m
                    for i in nodes:
                        v = i
                        a, b = 1, 0
                        seen = set()
                        for _ in range(m):
                            assert v not in seen
                            seen.add(v)
                            u, c = aff[v]
                            a, b = u * a, u * b + c
                            v = adj[v][0]
                        assert seen == set(nodes)
                        assert v == i
                        assert a == 1 and b == 0
            # Nonzero-entropy component characteristic recurrence plus
            # (d-1) isometric m-cycles: characteristic polynomial.
            A = graph_matrix(adj)
            # Evaluate det(tI-A) at t=2 and t=3 (exact nontrivial checks).
            for t in (2, 3):
                actual = det_integer([[t * (i == j) - A[i][j]
                                      for j in range(N)] for i in range(N)])
                r = m - 1
                expected = (t ** r - sum(t ** j for j in range(r))) * (t ** m - 1) ** (d - 1)
                assert actual == expected, (n, q, actual, expected)
            if d == 1:
                # Wang characteristic lengths are the distances to hub plus one.
                lengths = []
                for i in range(N):
                    v = i
                    ell = 1
                    while v != w:
                        v = adj[v][0]
                        ell += 1
                        assert ell <= N
                    lengths.append(ell)
                assert sorted(lengths) == list(range(1, N + 1))
    for n in range(3, 9):
        for q in range(1, n):
            if gcd(n, q) != 1:
                continue
            w, aff, adj = model(n, q)
            for k in range(1, 10):
                symbolic = list(periodic_graph_words(adj, k))
                points = [fixed_point_from_word(aff, x) for x in symbolic]
                assert len(points) == len(set(points)), (n, q, k)
                words += len(symbolic)
                # Counts also equal trace of the explicitly constructed matrix.
                A = graph_matrix(adj)
                B = [[int(i == j) for j in range(n - 1)] for i in range(n - 1)]
                for _ in range(k):
                    B = matmul(B, A)
                assert len(points) == sum(B[i][i] for i in range(n - 1))
    print(f"PASS {scenarios} (n,q) structural cases; {words} exact periodic-address checks")


if __name__ == "__main__":
    check()
