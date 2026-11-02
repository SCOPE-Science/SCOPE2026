"""Exact checks for payoff-neutrality thresholds in regular network public-goods dynamics.

Requires only the Python standard library. Run: python verify.py
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict


def graph_matrix(adjacency):
    n = len(adjacency)
    degree = len(adjacency[0])
    assert all(len(a) == degree for a in adjacency)
    assert all(i not in adjacency[i] for i in range(n))
    assert all(j in adjacency[i] for i in range(n) for j in adjacency[i])
    M = [[int(i == j) + 2 * int(j in adjacency[i]) + len(adjacency[i] & adjacency[j]) for j in range(n)] for i in range(n)]
    assert all(sum(M[i]) == (degree + 1) ** 2 for i in range(n))
    return M


def kernel_threshold(M, adjacency, r):
    n = len(M)
    d = len(adjacency[0])
    best = Fraction(0)
    for x in range(n):
        for y in adjacency[x]:
            h = [M[x][z] - M[y][z] for z in range(n)]
            assert sum(h) == 0
            a = h[x]
            assert a >= 0 and h[y] == -a
            H = sum(max(v, 0) for v in h)
            lo, hi = 2 * a - H, H
            E = max(abs(Fraction(r, d + 1) * lo - (d + 1)), abs(Fraction(r, d + 1) * hi - (d + 1)))
            best = max(best, E)
    return best


def brute_threshold(M, adjacency, r):
    n, d = len(M), len(adjacency[0])
    best = Fraction(0)
    for s in product((0, 1), repeat=n):
        pi = [Fraction(r, d+1) * sum(M[i][z] * s[z] for z in range(n)) - (d+1) * s[i] for i in range(n)]
        for x in range(n):
            for y in adjacency[x]:
                if s[x] != s[y]:
                    best = max(best, abs(pi[x]-pi[y]))
    return best


def cycle(n):
    return [{(i-1)%n, (i+1)%n} for i in range(n)]


def complete(n):
    return [set(range(n))-{i} for i in range(n)]


def cubic_bipartite():
    return [set(range(3,6)) for _ in range(3)] + [set(range(3)) for _ in range(3)]


def triangular_prism():
    return [{(i+1)%3, (i+2)%3, i+3} for i in range(3)] + [{3+(i+1)%3, 3+(i+2)%3, i} for i in range(3)]


def torus(L):
    return [{((x+1)%L)*L+y, ((x-1)%L)*L+y, x*L+(y+1)%L, x*L+(y-1)%L} for x in range(L) for y in range(L)]


def exact_torus_extrema(L):
    adj = torus(L)
    M = graph_matrix(adj)
    n=L*L
    x,y=0,L
    h=[M[x][z]-M[y][z] for z in range(n)]
    assert h[x] == 3 and h[y] == -3
    assert sum(max(0,z) for z in h) == 11
    assert sum(min(0,z) for z in h) == -11
    positives=[z for z in range(n) if h[z]>0]
    negatives=[z for z in range(n) if h[z]<0]
    assert len(positives) == len(negatives) == 7
    # All 12 unconstrained nonzero-stencil choices are checked.
    independent=[z for z in range(n) if h[z] and z not in (x,y)]
    seen=set()
    for v in product((0,1),repeat=len(independent)):
        profile={x:1,y:0}
        profile.update(zip(independent,v))
        j=sum(h[z]*profile.get(z,0) for z in range(n))
        seen.add(j)
        assert -5<=j<=11
    assert min(seen)==-5 and max(seen)==11
    return len(independent),len(seen)


def main():
    r_values=[Fraction(1),Fraction(2),Fraction(5),Fraction(25,3),Fraction(10),Fraction(30)]
    cases=0
    for graph in [cycle(n) for n in range(3,10)] + [complete(n) for n in range(2,9)] + [cubic_bipartite(),triangular_prism()]:
        M=graph_matrix(graph)
        for r in r_values:
            got=kernel_threshold(M,graph,r)
            expected=brute_threshold(M,graph,r)
            assert got==expected,(got,expected,len(graph),r)
            cases+=1
    for L in [6,7,10]:
        free,distinct=exact_torus_extrema(L)
        M=graph_matrix(torus(L))
        for r in r_values:
            got=kernel_threshold(M,torus(L),r)
            expected=max(5+r,abs(Fraction(11,5)*r-5))
            assert got==expected,(L,r,got,expected)
            cases+=1
        print(f'Torus L={L}: {free} free nonzero-stencil spins, {2**free} configurations, {distinct} attainable integer contrasts')
    print(f'PASS: {cases} exact graph/rate formula comparisons, including exhaustive profiles for graphs of 2 to 9 vertices.')
    print('PASS: sharp torus formula for L=6,7,10 and all local nonzero-stencil configurations.')


if __name__=='__main__':
    main()
