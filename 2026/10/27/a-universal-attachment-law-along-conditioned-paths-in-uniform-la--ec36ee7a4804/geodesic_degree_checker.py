"""Exact independent Prüfer enumeration of a conditional geodesic-degree law.

Run: python3 geodesic_degree_checker.py
Uses only the Python standard library. No empirical data are required.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial


def prufer_tree(code, n):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        u = next(i for i in range(n) if degree[i] == 1)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
    a, b = (i for i in range(n) if degree[i] == 1)
    edges.append((a, b))
    return edges


def path_from_zero_to_one(edges, n):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    parent = {0: -1}
    todo = [0]
    for u in todo:
        if u == 1:
            break
        for v in graph[u]:
            if v not in parent:
                parent[v] = u
                todo.append(v)
    path = [1]
    while path[-1] != 0:
        path.append(parent[path[-1]])
    return list(reversed(path))


def predicted(n, k, vector):
    q = k + 1
    m = n - q
    if not m:
        return Fraction(int(all(v == 0 for v in vector)))
    t = m - 1
    r = sum(vector)
    if r < 1 or r > m:
        return Fraction(0)
    out = Fraction(0)
    for i in range(q):
        if vector[i] == 0:
            continue
        rest = list(vector)
        rest[i] -= 1
        other = t - sum(rest)
        if other < 0:
            continue
        c = factorial(t) // (factorial(other) * __import__('math').prod(factorial(x) for x in rest))
        out += Fraction(c * m**other, q * n**t)
    return out


def run():
    tests = 0
    for n in range(2, 9):
        counts = Counter()
        cases = Counter()
        for code in product(range(n), repeat=n-2):
            edges = prufer_tree(code, n)
            path = path_from_zero_to_one(edges, n)
            k = len(path) - 1
            counts[k] += 1
            deg = Counter(u for e in edges for u in e)
            vector = tuple(deg[v] - (1 if i in (0, k) else 2) for i, v in enumerate(path))
            assert min(vector) >= 0
            cases[k, vector] += 1
        assert sum(counts.values()) == n**(n-2)
        for k in range(1, n):
            q = k + 1
            m = n - q
            if m:
                expected_num = factorial(n-2) // factorial(n-k-1) * q * n**(n-k-2)
            else:
                expected_num = factorial(n-2)
            assert counts[k] == expected_num
            tests += 1
            # All possible vectors, including forbidden vectors, not just observed ones.
            for vector in product(range(m+1), repeat=q):
                if sum(vector) > m:
                    continue
                observed = Fraction(cases[k, vector], counts[k])
                truth = predicted(n, k, vector)
                assert observed == truth, (n,k,vector,observed,truth)
                tests += 1
            assert sum(Fraction(v, counts[k]) for (kk,vec),v in cases.items() if kk==k)==1
            tests += 1
            if m:
                # The exact pairwise covariance, computed independently from the table.
                for i in range(q):
                    for j in range(i+1,q):
                        mu_i=sum(Fraction(v*vec[i],counts[k]) for (kk,vec),v in cases.items() if kk==k)
                        mu_j=sum(Fraction(v*vec[j],counts[k]) for (kk,vec),v in cases.items() if kk==k)
                        eij=sum(Fraction(v*vec[i]*vec[j],counts[k]) for (kk,vec),v in cases.items() if kk==k)
                        assert eij - mu_i*mu_j == -Fraction(m-1,n*n)-Fraction(1,q*q)
                        tests += 1
    print('PASS', tests, 'exact rational Prüfer/path/joint-law checks for n=2..8')


if __name__ == '__main__':
    run()
