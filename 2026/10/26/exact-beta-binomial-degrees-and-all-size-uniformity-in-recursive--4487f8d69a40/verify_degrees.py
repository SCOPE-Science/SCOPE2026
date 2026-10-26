"""Exact finite-size checks for true/false-twin random graphs.
Standard-library only; all probabilities are fractions. No stochastic simulation.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial


def rising(x, m):
    r = Fraction(1)
    for j in range(m):
        r *= x + j
    return r


def betabin(m, k, a, b):
    if not 0 <= k <= m:
        return Fraction(0)
    return Fraction(comb(m, k)) * rising(a, k) * rising(b, m-k) / rising(a+b, m)


def grow(graph, parent, join):
    n = len(graph)
    rows = list(graph)
    original = rows[parent]
    new = original | ((1 << parent) if join else 0)
    for j in range(n):
        if new & (1 << j):
            rows[j] |= 1 << n
    rows.append(new)
    return tuple(rows)


def enumerate_graphs(nmax, q):
    graphs = {(0,): Fraction(1)}
    yield 1, graphs
    for n in range(1, nmax):
        nxt = defaultdict(Fraction)
        for g, weight in graphs.items():
            for j in range(n):
                nxt[grow(g, j, 0)] += weight * (1-q) / n
                nxt[grow(g, j, 1)] += weight * q / n
        graphs = dict(nxt)
        assert sum(graphs.values()) == 1
        yield n+1, graphs


def verify_graphs(n, gs, q):
    p = 1-q
    root = defaultdict(Fraction)
    sampled = defaultdict(Fraction)
    for g, prob in gs.items():
        assert len(g) == n
        assert all(((g[i] >> j) & 1) == ((g[j] >> i) & 1) for i in range(n) for j in range(n))
        d = [x.bit_count() for x in g]
        root[d[0]] += prob
        for k in d:
            sampled[k] += prob / n
    tests = 0
    for k in range(n):
        assert root[k] == betabin(n-1,k,q,p), (n,q,k,'root',root[k])
        assert sampled[k] == betabin(n-1,k,2*q,2*p), (n,q,k,'sampled',sampled[k])
        tests += 2
        if q == Fraction(1,2):
            assert sampled[k] == Fraction(1,n)
            tests += 1
    assert sum(root.values()) == sum(sampled.values()) == 1
    tests += 1
    return tests


def verify_recursions(q, nmax=45):
    p = 1-q
    root = [Fraction(1)]
    sampled = [Fraction(1)]
    total=0
    for n in range(1,nmax):
        nr = [Fraction(0)]*(n+1)
        ns = [Fraction(0)]*(n+1)
        for k in range(n+1):
            oldk = root[k] if k < n else Fraction(0)
            oldkm = root[k-1] if k>=1 else Fraction(0)
            oldsk = sampled[k] if k < n else Fraction(0)
            oldskm = sampled[k-1] if k>=1 else Fraction(0)
            nr[k]=oldk*(1-Fraction(k, n)-q/n)+oldkm*(k-1+q)/n
            ns[k]=oldsk*(n+1-k-2*q)/(n+1)+oldskm*(k-1+2*q)/(n+1)
            assert nr[k] == betabin(n,k,q,p)
            assert ns[k] == betabin(n,k,2*q,2*p)
            total+=2
        root, sampled=nr, ns
        assert sum(root)==sum(sampled)==1
        total+=1
    return total


def main():
    total=0
    for q in [Fraction(1,7),Fraction(1,3),Fraction(1,2),Fraction(3,5),Fraction(6,7)]:
        for n, graphs in enumerate_graphs(6, q):
            checked = verify_graphs(n,graphs,q)
            total += checked
            print('graph enumeration', 'q=',q,'n=',n,'models=',len(graphs),'checks=',checked)
        total += verify_recursions(q)
    print('PASS',total,'exact assertions on finite graph distributions and recurrences')

if __name__ == '__main__':
    main()
