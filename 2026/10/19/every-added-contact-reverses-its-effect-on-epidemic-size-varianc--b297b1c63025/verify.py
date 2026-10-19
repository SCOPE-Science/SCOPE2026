#!/usr/bin/env python3
"""Exact independent finite checks for the edge-insertion outbreak-variance identity.

Only Python standard library is required. This checks finite examples and algebraic
identities at rational probabilities; it does not replace the universal proof.
"""
from fractions import Fraction
from itertools import combinations
from functools import lru_cache

def edge_list(n):
    return list(combinations(range(n), 2))

def components(n, edges):
    parent = list(range(n))
    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for i, j in edges:
        a, b = find(i), find(j)
        parent[a] = b
    labels = [find(i) for i in range(n)]
    sizes = {r: labels.count(r) for r in set(labels)}
    return labels, sizes

def connected(n, edge_mask):
    e = edge_list(n)
    labels, _ = components(n, [e[i] for i in range(len(e)) if (edge_mask >> i) & 1])
    return len(set(labels)) == 1

@lru_cache(None)
def moment_coeffs(n, edge_mask):
    e = edge_list(n)
    retained = [e[i] for i in range(len(e)) if (edge_mask >> i) & 1]
    m = len(retained)
    weights = [[0, 0] for _ in range(m + 1)]
    for sub in range(1 << m):
        opened = [retained[i] for i in range(m) if (sub >> i) & 1]
        _, sizes = components(n, opened)
        k = sub.bit_count()
        weights[k][0] += sum(a*a for a in sizes.values())
        weights[k][1] += sum(a*a*a for a in sizes.values())
    return m, weights

def moments(n, edge_mask, p):
    m, weights = moment_coeffs(n, edge_mask)
    mu = sum(Fraction(c[0], n)*p**k*(1-p)**(m-k)
             for k,c in enumerate(weights))
    second = sum(Fraction(c[1], n)*p**k*(1-p)**(m-k)
                 for k,c in enumerate(weights))
    return mu, second, second - mu*mu

def increments(n, edge_mask, missing_bit, p):
    e = edge_list(n)
    retained = [e[i] for i in range(len(e)) if (edge_mask >> i) & 1]
    u, v = e[missing_bit]
    m = len(retained)
    A = B = Fraction(0)
    for sub in range(1 << m):
        opened = [retained[i] for i in range(m) if (sub >> i) & 1]
        labels, sizes = components(n, opened)
        if labels[u] == labels[v]:
            continue
        a, b = sizes[labels[u]], sizes[labels[v]]
        w = p**sub.bit_count()*(1-p)**(m-sub.bit_count())
        A += w*Fraction(2*a*b, n)
        B += w*Fraction(3*a*b*(a+b), n)
    return A, B

def test_all():
    count = 0
    saturated = 0
    for n in range(2, 6):
        m = n*(n-1)//2
        for mask in range(1 << m):
            if not connected(n, mask) or mask == (1 << m)-1:
                continue
            for bit in range(m):
                if mask & (1 << bit):
                    continue
                for p in (Fraction(1,4), Fraction(1,2),
                          Fraction(3,4), Fraction(9,10)):
                    mu, s2, var = moments(n, mask, p)
                    mu1, s21, var1 = moments(n, mask | 1 << bit, p)
                    A, B = increments(n, mask, bit, p)
                    assert mu1 - mu == p*A
                    assert s21 - s2 == p*B
                    assert var1 - var == p*(B - 2*mu*A) - p*p*A*A
                    assert mu1 > mu
                    if mu >= Fraction(3*n, 4):
                        assert var1 < var
                        saturated += 1
                    count += 1
    return count, saturated

def example():
    n = 3
    edges = edge_list(n)
    path = (1 << edges.index((0,1))) | (1 << edges.index((1,2)))
    closing = 1 << edges.index((0,2))
    p = Fraction(1,2)
    dm = moments(n,path | closing,p)[0]-moments(n,path,p)[0]
    dv = moments(n,path | closing,p)[2]-moments(n,path,p)[2]
    assert dm == Fraction(5,12)
    assert dv == Fraction(7,144)
    p = Fraction(4,5)
    dm_hi = moments(n,path | closing,p)[0]-moments(n,path,p)[0]
    dv_hi = moments(n,path | closing,p)[2]-moments(n,path,p)[2]
    assert dm_hi > 0 and dv_hi < 0
    return dm,dv,dm_hi,dv_hi

if __name__ == "__main__":
    count,saturated = test_all()
    print("Exact tests n=2..5:",count,"edge/probability comparisons")
    print("High-mean check instances:",saturated)
    print("P3 triangle differences",example())
    print("All exact tests passed.")
