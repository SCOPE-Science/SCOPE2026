#!/usr/bin/env python3
"""Exact rational checks for the two-leader windmill theorem (stdlib only)."""
from fractions import Fraction as Q
from itertools import combinations


def laplacian(r, m):
    n = 1 + r*m
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    edges = [(0, i) for i in range(1, n)]
    for j in range(r):
        nodes = range(1 + j*m, 1 + (j+1)*m)
        edges += list(combinations(nodes, 2))
    for i, j in edges:
        L[i][i] += 1
        L[j][j] += 1
        L[i][j] -= 1
        L[j][i] -= 1
    return L


def trace_inverse_pinned(L, pair, k):
    n = len(L)
    a = [row.copy() + [Q(int(i == j)) for j in range(n)] for i, row in enumerate(L)]
    for p in pair:
        a[p][p] += k
    for col in range(n):
        pivot = next(i for i in range(col,n) if a[i][col] != 0)
        a[col],a[pivot] = a[pivot],a[col]
        q = a[col][col]
        a[col] = [v/q for v in a[col]]
        for i in range(n):
            if i == col or a[i][col] == 0:
                continue
            q = a[i][col]
            a[i] = [x - q*y for x,y in zip(a[i],a[col])]
    return sum((a[i][n+i] for i in range(n)),Q(0))


def predicted(r,m,k,kind):
    H = (m+1)**2*(m*r+1)
    if kind == 'hub':
        numerator = k*k*(4*m*r-m-3)+2*k*m*(m+1)*(3*r-1)+H
        denominator = 2*k*(m+1)*(k+m+1)
    elif kind == 'same':
        numerator = k*k*(7*m*r-4*m-3)+4*k*m*(m+1)*(2*r-1)+H
        denominator = 2*k*(m+1)*(k+m+1)
    elif kind == 'different':
        numerator = k*k*(12*m*r-10*m-10)+4*k*m*(m+1)*(2*r-1)+H
        denominator = 2*k*(m+1)*(2*k+m+1)
    else:
        raise ValueError(kind)
    return numerator/denominator


def main():
    checks = 0
    for r in (2,3,4,5):
        for m in (2,3,4):
            L=laplacian(r,m)
            for k in (Q(1,7),Q(1,2),Q(1),Q(4),Q(19)):
                types = {'hub':(0,1), 'same':(1,2), 'different':(1,m+1)}
                values={}
                for kind, pair in types.items():
                    value = trace_inverse_pinned(L, pair, k)
                    assert value == predicted(r,m,k,kind), (r,m,k,kind,value)
                    values[kind] = value
                    checks += 1
                assert values['same'] > values['hub']
                assert (values['different'] < values['hub']) == (r == 2)
                checks += 2
    # Independently enumerate all two-element subsets rather than only orbit representatives.
    for r in (2,3):
        for m in (2,3,4):
            L=laplacian(r,m)
            for k in (Q(1,3),Q(3)):
                goal = min(predicted(r,m,k,t) for t in ('hub','same','different'))
                for pair in combinations(range(len(L)),2):
                    value = trace_inverse_pinned(L,pair,k)
                    assert value >= goal
                    kind = ('hub' if 0 in pair else
                            'same' if (pair[0]-1)//m == (pair[1]-1)//m else 'different')
                    assert value == predicted(r,m,k,kind)
                    if r == 2:
                        assert (value == goal) == (kind == 'different')
                    else:
                        assert (value == goal) == (kind == 'hub')
                    checks += 3
    print(f'VERIFY_OK: {checks} exact rational formula/order/orbit checks')

if __name__ == '__main__':
    main()
