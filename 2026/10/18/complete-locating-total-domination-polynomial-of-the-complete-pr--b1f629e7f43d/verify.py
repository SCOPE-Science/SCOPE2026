#!/usr/bin/env python3
"""Independent finite verification of the locating-total polynomial on complete prisms.

Run with Python 3: python verify.py
All graph checks use the adjacency definition rather than the proof's counting argument.
The exhaustive graphs have n=2,...,9 and thus at most 18 vertices.
"""
from collections import Counter
from itertools import product
from math import comb


def multiply(p, q):
    out = Counter()
    for i, a in p.items():
        for j, b in q.items():
            out[i+j] += a*b
    return out


def power(p, n):
    out = {0: 1}
    for _ in range(n):
        out = multiply(out, p)
    return Counter(out)


def formula(n):
    if n == 2:
        return Counter({2:4, 3:4, 4:1})
    if n == 3:
        return Counter({3:14, 4:15, 5:6, 6:1})
    z = Counter({1:2, 2:1})
    p = power(z, n)
    q = power(z, n-1)
    for k, v in q.items():
        p[k] += n*v
    p[n-1] -= 2*n*n
    p[n] -= 2*n
    return Counter({k:v for k,v in p.items() if v})


def predicts_membership(n, mask):
    X = {j for j in range(n) if mask & (1 << j)}
    Y = {j for j in range(n) if mask & (1 << (n+j))}
    p, q = len(X), len(Y)
    if n - len(X|Y) > 1:
        return False
    if p == 0 and q != n:
        return False
    if q == 0 and p != n:
        return False
    if p == 1 and not X <= Y:
        return False
    if q == 1 and not Y <= X:
        return False
    return True


def directly_valid(n, mask, adj):
    signatures=[]
    for v, neighbors in enumerate(adj):
        signature=mask & neighbors
        if not signature:
            return False
        if not (mask & (1 << v)):
            signatures.append(signature)
    return len(set(signatures))==len(signatures)


def brute(n):
    adj=[]
    for a in (0,1):
        for j in range(n):
            bits=0
            for b in (0,1):
                for k in range(n):
                    if (a == b and j != k) or (a != b and j == k):
                        bits |= 1 << (b*n+k)
            adj.append(bits)
    counts=Counter()
    for mask in range(1 << (2*n)):
        actual=directly_valid(n,mask,adj)
        structure=predicts_membership(n,mask)
        assert actual==structure, (n,mask,actual,structure)
        if actual:
            counts[mask.bit_count()] += 1
    return counts


def main():
    all_masks=0
    for n in range(2,10):
        actual=brute(n)
        expected=formula(n)
        assert actual==expected, (n,actual,expected)
        all_masks += (1 << (2*n))
        print(f'n={n}: subsets={1 << (2*n)}; polynomial_coefficients={dict(sorted(actual.items()))}')
    for n in range(4,201):
        f=formula(n)
        expected_min=4 if n==4 else n-1
        expected_count=56 if n==4 else n*(2**(n-1)-2*n)
        assert min(f)==expected_min
        assert f[expected_min]==expected_count
        assert sum(f.values())>0
        assert f[2*n]==1
    print(f'PASS exhaustive graph subsets: {all_masks}; formula minimum checks n=4..200')

if __name__=='__main__':
    main()
