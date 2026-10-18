#!/usr/bin/env python3
"""Exact finite tests of uniform-facet covariance for path-suspension graphs.

No optional packages are required. This is verification of finite cases,
not a substitute for the general combinatorial argument.
"""
from fractions import Fraction
from itertools import product


def extension_counts(n):
    a = [1, 2, 4]
    for k in range(3, n+1):
        a.append(a[-1] + 2*a[-2] + 2*a[-3])
    return a[:n+1]


def connected_tight_edges(x):
    """Independent facet test via graph traversal, rather than word rules."""
    m = len(x)
    seen = {0}
    stack = [0]
    edges = [(0, k+1) for k, value in enumerate(x) if abs(value) == 1]
    edges.extend((k+1, k+2) for k in range(m-1)
                 if abs(x[k]-x[k+1]) == 1)
    adjacency = [[] for _ in range(m+1)]
    for a,b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    while stack:
        v = stack.pop()
        for u in adjacency[v]:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    return len(seen) == m + 1


def enumerate_facets(m):
    return [x for x in product((-1,0,1), repeat=m)
            if all(abs(x[k]-x[k+1])<=1 for k in range(m-1))
            and connected_tight_edges(x)]


def inverse_fraction(matrix):
    n = len(matrix)
    a = [[Fraction(matrix[i][j]) for j in range(n)] +
         [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        pivot = next(i for i in range(c,n) if a[i][c] != 0)
        a[c],a[pivot] = a[pivot],a[c]
        divisor = a[c][c]
        a[c] = [v/divisor for v in a[c]]
        for i in range(n):
            if i == c: continue
            factor = a[i][c]
            a[i] = [u-factor*v for u,v in zip(a[i],a[c])]
    return [row[n:] for row in a]


def predicted_covariance(m):
    b = extension_counts(m)
    denom = b[m-1]+b[m-2]
    return [[Fraction(b[min(i,j)]*b[m-1-max(i,j)],denom)
             for j in range(m)] for i in range(m)]


def verify_one(m):
    words=enumerate_facets(m)
    b=extension_counts(m)
    z=2*(b[m-1]+b[m-2])
    assert len(words)==z, (m,len(words),z)
    assert all(sum(x[i] for x in words)==0 for i in range(m))
    actual=[[Fraction(sum(x[i]*x[j] for x in words),z)
             for j in range(m)] for i in range(m)]
    predicted=predicted_covariance(m)
    assert actual==predicted,(m,actual,predicted)
    q=inverse_fraction(predicted)
    assert all(q[i][j]==0 for i in range(m) for j in range(m)
               if abs(i-j)>1)
    deltas=[]
    for i in range(m-1):
        delta=b[i+1]*b[m-i-1]-b[i]*b[m-i-2]
        assert delta>0
        assert q[i][i+1]==-Fraction(z//2,delta)
        deltas.append(delta)
    assert q[0][0]==Fraction(2*(z//2),deltas[0])
    assert q[m-1][m-1]==Fraction(2*(z//2),deltas[-1])
    for i in range(1,m-1):
        diagonal=Fraction(z//2,b[i])*(
            Fraction(b[i-1],deltas[i-1])+Fraction(b[i+1],deltas[i]))
        assert q[i][i]==diagonal
    return len(words)


def main():
    for m in range(2,10):
        print(f'm={m}: {verify_one(m)} facets; exact covariance and tridiagonal precision OK')
    print('ALL EXACT FINITE FAN-GRAPH CHECKS PASSED')

if __name__ == '__main__': main()
