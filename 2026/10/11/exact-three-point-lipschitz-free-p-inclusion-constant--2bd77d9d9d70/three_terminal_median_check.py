"""Finite independent checks for the three-terminal p-free median reduction.

This test enumerates all labelled spanning trees of small finite metric spaces.
Finite tests complement, but cannot replace, the universal proof.
"""
from itertools import product
from math import inf, isclose
from fractions import Fraction


def spanning_trees(n):
    if n == 2:
        yield [(0, 1)]
        return
    for seq in product(range(n), repeat=n - 2):
        degree = [1] * n
        for x in seq:
            degree[x] += 1
        out = []
        for x in seq:
            leaf = next(i for i in range(n) if degree[i] == 1)
            out.append((leaf, x))
            degree[leaf] -= 1
            degree[x] -= 1
        leaves = [i for i in range(n) if degree[i] == 1]
        out.append(tuple(leaves))
        yield out


def tree_cost(edges, rho, masses, p):
    n = len(masses)
    cost = 0.0
    for u, v in edges:
        seen = {u}
        todo = [u]
        while todo:
            x = todo.pop()
            for a, b in edges:
                if a == x and b not in seen and not (a == u and b == v or a == v and b == u):
                    seen.add(b)
                    todo.append(b)
                if b == x and a not in seen and not (a == u and b == v or a == v and b == u):
                    seen.add(a)
                    todo.append(a)
        flow = sum(masses[i] for i in seen)
        cost += abs(flow)**p * rho[u][v]
    return cost


def shortest_path_metric(n, seed):
    # Positive integral edge lengths, symmetric; Floyd--Warshall closure.
    d = [[0 if i == j else 1 + ((17*i + 23*j + 19*i*j + 13*seed) % 17)
          for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d[i][j] = d[j][i] = min(d[i][j], d[j][i])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def test_trees():
    for n in (3, 4, 5):
        ts = list(spanning_trees(n))
        assert len(ts) == n ** (n-2)
        for seed in range(12):
            rho = shortest_path_metric(n, seed)
            for v in (-2, -1, 1, 2):
                masses = [0] * n
                masses[0], masses[1], masses[2] = 1, v, -1-v
                for p in (0.25, 0.5, 0.75, 1.0):
                    med = min(sum(abs(masses[i])**p * rho[i][z]
                                  for i in range(3)) for z in range(n))
                    brute = min(tree_cost(t, rho, masses, p) for t in ts)
                    assert isclose(med, brute, rel_tol=1e-11, abs_tol=1e-11), (n, seed, v, p, med, brute)


def test_sharp_star():
    for p in (0.1, 0.25, 0.5, 0.75, 0.9):
        q = 2.0 ** p
        r, s = 1 / q, 1 / (2 - q)
        S = 2*r + q*s
        N = min(2*(r+s), (2+q)*r + q*s)
        result = N / S
        want = 4 / (4 - 2*q + q*q)
        assert isclose(result, want, rel_tol=1e-13, abs_tol=1e-13)
        for u in (0.01, 0.1, 0.25, 0.5, 0.8, 0.99):
            a,b,c=u**p,(1-u)**p,1
            B=(b+c-a, a+c-b, a+b-c)
            h=sum(w/v for w,v in zip((a,b,c),B))
            assert 1+1/h <= want+1e-12


def test_rational_special():
    # Pure rational identities at the formal variable q=3/2: the
    # sharp star formulas are rational functions of q=2^p.
    q=Fraction(3,2)
    r=1/q
    s=1/(2-q)
    S=2*r+q*s
    N=2*(r+s)
    assert N==S+1
    assert N/S == 4/(4-2*q+q*q)
    assert N == (2+q)*r+q*s

if __name__ == '__main__':
    test_trees()
    test_sharp_star()
    test_rational_special()
    print('THREE_TERMINAL_P_FREE_MEDIAN_AND_SHARP_CONSTANT_CHECK_OK')
