#!/usr/bin/env python3
"""Independent finite checks for defect-one transformation idempotent commuting graphs.
No third-party libraries are required. Does not substitute for the all-n proof.
"""
from itertools import combinations
from math import comb, factorial
from collections import Counter


def compose(f, g):
    # Standard functional composition f after g.
    return tuple(f[g[x]] for x in range(len(f)))


def graph(n):
    vertices = [(a,b) for a in range(n) for b in range(n) if a != b]
    maps = []
    for a, b in vertices:
        f = list(range(n)); f[a] = b; maps.append(tuple(f))
    adj = [set() for _ in vertices]
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            equal = compose(maps[i], maps[j]) == compose(maps[j], maps[i])
            a,b = vertices[i]; c,d = vertices[j]
            expected = (a != c and b != c and d != a)
            assert equal == expected, (n, vertices[i], vertices[j])
            if equal:
                adj[i].add(j); adj[j].add(i)
    return vertices, adj


def stirling(n, k):
    if k == 0: return int(n == 0)
    s = [[0]*(k+1) for _ in range(n+1)]
    s[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,k+1): s[i][j] = s[i-1][j-1] + j*s[i-1][j]
    return s[n][k]


def enumerate_cliques(adj):
    # Independent graph-based recursion, no function assignments or closed formula.
    cliques = []
    def rec(chosen, candidates):
        if chosen:
            cliques.append((tuple(chosen), not bool(candidates))) # placeholder maximal recomputed below
        while candidates:
            v = candidates.pop()
            rec(chosen+[v], candidates & adj[v])
    rec([], set(range(len(adj))))
    counts = Counter(); max_counts=Counter()
    for clique,_ in cliques:
        counts[len(clique)] +=1
        C=set(clique)
        if not any(u not in C and all(u in adj[v] for v in C) for u in range(len(adj))):
            max_counts[len(clique)] += 1
    return counts, max_counts


def matrix_product(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def characteristic_polynomial(A):
    # Direct trace/Newton-identity computation, independent of the proof's invariant-space argument.
    m = len(A)
    I = [[int(i==j) for j in range(m)] for i in range(m)]
    P = I
    traces = []
    for _ in range(m):
        P = matrix_product(P,A)
        traces.append(sum(P[i][i] for i in range(m)))
    c = [1]
    for k in range(1,m+1):
        numerator = sum(c[k-j]*traces[j-1] for j in range(1,k+1))
        assert numerator % k == 0
        c.append(-numerator//k)
    return c


def polmul(f,g):
    h=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g): h[i+j]+=a*b
    return h


def polpow(f,k):
    ans=[1]
    for _ in range(k):ans=polmul(ans,f)
    return ans


def spectral_prediction(n):
    if n==2:return [1,0,0]
    # Ascending coefficients then reverse for the monic characteristic polynomial.
    F = polmul([-(n-2)**2,1],polpow([-(n-2)**2,n-3,1],n-1))
    F = polmul(F,polpow([-1,1],n*(n-3)//2))
    F = polmul(F,polpow([1,1],(n-1)*(n-2)//2))
    return list(reversed(F))


def check(n, charpoly=True):
    v,adj = graph(n)
    assert len(v)==n*(n-1)
    assert all(len(x)==(n-2)**2 for x in adj)
    c,m = enumerate_cliques(adj)
    expected_c = {r:comb(n,r)*(n-r)**r for r in range(1,n)}
    expected_m = {r:comb(n,r)*factorial(n-r)*stirling(r,n-r)
                  for r in range(1,n)}
    expected_m={r:v for r,v in expected_m.items() if v}
    assert c == expected_c,(n,c,expected_c)
    assert m == expected_m,(n,m,expected_m)
    assert sum(c.values())+1 == 1+sum(expected_c.values())
    if charpoly:
        A = [[int(j in adj[i]) for j in range(len(adj))] for i in range(len(adj))]
        actual = characteristic_polynomial(A)
        expected = spectral_prediction(n)
        assert actual == expected,(n,actual,expected)
    print('n=%d vertices=%d cliques=%s maximal=%s spectrum=%s' %
          (n,len(v),dict(sorted(c.items())),dict(sorted(m.items())),charpoly))

if __name__=='__main__':
    for n in range(2,8):check(n,charpoly=(n<=6))
    print('VERIFY_OK_DEFECT_ONE_COMMUTING_SPECTRUM')
