#!/usr/bin/env python3
"""Standalone exact verifier for the circular-ladder two-packing census.
Uses only Python 3 standard library. Its finite tests do not substitute
for the all-order combinatorial proof.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb


def formula(n):
    out = [1] + [0] * (n // 2)
    for k in range(1, n // 2 + 1):
        t = n - 2 * k
        if t == 0:
            out[k] = 4 if k % 2 == 0 else 0
        else:
            total = sum((2 ** r) * comb(k, r) * comb(t - 1, r - 1)
                        for r in range(1, min(k, t) + 1))
            assert (n * total) % k == 0
            out[k] = n * total // k
    return out


def matmul(A, B):
    d = len(A)
    return [[sum(A[i][h] * B[h][j] for h in range(d)) for j in range(d)]
             for i in range(d)]


def transfer_poly(n):
    # Polynomial ring Z[u] truncated at floor(n/2).
    cap = n // 2
    zero = tuple(0 for _ in range(cap + 1))
    one = (1,) + zero[1:]
    u = (0, 1) + tuple(0 for _ in range(cap - 1))

    def multiply(x, y):
        return tuple(sum(x[i] * y[k - i] for i in range(k + 1))
                     for k in range(cap + 1))

    def multiply_matrices(A, B):
        d = len(A)
        return [[tuple(sum(multiply(A[i][h], B[h][j])[k]
                           for h in range(d)) for k in range(cap + 1))
                 for j in range(d)] for i in range(d)]

    M = [[zero for j in range(5)] for i in range(5)]
    transitions = {(0,0):one,(0,1):u,(0,2):u,
                   (1,3):one,(2,4):one,(3,0):one,(3,2):u,
                   (4,0):one,(4,1):u}
    for (i,j), weight in transitions.items():
        M[i][j] = weight
    A = [[one if i == j else zero for j in range(5)] for i in range(5)]
    for _ in range(n):
        A = multiply_matrices(A, M)
    return [sum(A[i][i][k] for i in range(5)) for k in range(cap + 1)]


def graph(n):
    # Actual prism edges: cyclic horizontal steps and each vertical rung.
    N = 2 * n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for layer in range(2):
            a = i + n * layer
            for j in ((i - 1) % n, (i + 1) % n):
                b = j + n * layer
                adj[a].add(b); adj[b].add(a)
            b = i + n * (1 - layer)
            adj[a].add(b); adj[b].add(a)
    return adj


def forbidden_pairs(adj):
    N = len(adj)
    banned = [0] * N
    for a in range(N):
        q = {a} | adj[a]
        for b in adj[a]:
            q.update(adj[b])
        banned[a] = sum(1 << b for b in q)
    return banned


def brute_packings(n):
    adj = graph(n)
    ban = forbidden_pairs(adj)
    counts = [0] * (n // 2 + 1)
    for k in range(n // 2 + 1):
        for S in combinations(range(2*n), k):
            seen = 0
            for v in S:
                if (seen >> v) & 1:
                    break
                seen |= ban[v]
            else:
                counts[k] += 1
    return counts


def brute_roman(n):
    adj = graph(n)
    out = Counter()
    for f in product(range(3), repeat=2*n):
        twos = [v for v,x in enumerate(f) if x == 2]
        ok = True
        for v,x in enumerate(f):
            num = sum(f[w] == 2 for w in adj[v])
            if (x == 0 and num != 1) or (x != 0 and num != 0):
                ok = False; break
        if ok:
            out[len(twos)] += 1
            assert sum(f) == 2*n - 2*len(twos)
    return [out[k] for k in range(n//2 + 1)]


def recurrence_polys(N):
    P = {n: formula(n) for n in range(3,N+1)}
    def get(poly, degree):
        return poly[degree] if degree < len(poly) else 0
    for n in range(8,N+1):
        a,b,c,d = P[n-1],P[n-3],P[n-4],P[n-5]
        expected = [get(a,k)+2*get(b,k-1) if k>=1 else get(a,k)
                    for k in range(n//2+1)]
        for k in range(2,n//2+1):
            expected[k] += get(c,k-2)+get(d,k-2)
        assert expected == P[n], (n,expected,P[n])


def polynomial_determinant_check():
    # Exact Leibniz expansion of det(I-x M) in Z[x,u], independent
    # of the symbolic factorizations in the proof.
    def add(A,B):
        R = dict(A)
        for e,c in B.items():
            R[e] = R.get(e,0) + c
        return {e:c for e,c in R.items() if c}
    def mul(A,B):
        R = {}
        for (a,b),x in A.items():
            for (c,d),y in B.items():
                e=(a+c,b+d)
                R[e]=R.get(e,0)+x*y
        return {e:c for e,c in R.items() if c}
    M = [[{} for j in range(5)] for i in range(5)]
    T = {(0,0):{(0,0):1},(0,1):{(0,1):1},(0,2):{(0,1):1},
         (1,3):{(0,0):1},(2,4):{(0,0):1},
         (3,0):{(0,0):1},(3,2):{(0,1):1},
         (4,0):{(0,0):1},(4,1):{(0,1):1}}
    for (i,j),poly in T.items(): M[i][j]=poly
    B=[[add({(0,0):1} if i==j else {},
            {(a+1,b):-c for (a,b),c in M[i][j].items()})
        for j in range(5)] for i in range(5)]
    det={}
    for perm in permutations(range(5)):
        parity=sum(perm[i]>perm[j] for i in range(5) for j in range(i+1,5))%2
        term={(0,0):(-1)**parity}
        for i,j in enumerate(perm): term=mul(term,B[i][j])
        det=add(det,term)
    assert det=={(0,0):1,(1,0):-1,(3,1):-2,(4,2):-1,(5,2):-1}, det


def extreme(n):
    vals=formula(n)
    rho=max(k for k,a in enumerate(vals) if a)
    if n%2:
        want=(n-1)//2
        ways=2*n
        weight=n+1
    elif n%4==0:
        want=n//2
        ways=4
        weight=n
    else:
        want=n//2-1
        ways=n*(n-2)
        weight=n+2
    assert rho==want and vals[rho]==ways and 2*n-2*rho==weight


if __name__=='__main__':
    polynomial_determinant_check()
    print('DETERMINANT_OK')
    for n in range(3,13):
        direct = brute_packings(n)
        f = formula(n)
        t = transfer_poly(n)
        assert direct==f==t, (n,direct,f,t)
        extreme(n)
    print('BRUTE_GRAPH_PACKINGS_AND_TRANSFER_OK n=3..12')
    for n in range(3,7):
        assert brute_roman(n)==formula(n), n
    print('FULL_TERNARY_ROMAN_CONDITIONS_OK n=3..6')
    recurrence_polys(60)
    for n in range(3,101): extreme(n)
    print('RECURRENCE_TO_60_AND_EXTREMA_TO_100_OK')
    for n in range(3,11): print(n,formula(n))
    print('VERIFY_OK')
