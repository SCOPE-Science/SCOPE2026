#!/usr/bin/env python3
"""Exact rational verification for the voter-star stationary law."""
from fractions import Fraction as F
from math import comb
import json


def rising(a, n):
    ans = F(1)
    for j in range(n):
        ans *= a + j
    return ans


def candidate(m):
    a = F(1, m + 3)
    denom = rising(1 + 2 * a, m)
    result = []
    for h in (0, 1):
        for k in range(m + 1):
            left = a if h == 0 else 1 + a
            right = 1 + a if h == 0 else a
            result.append(F(comb(m, k), 2) * rising(left, k) * rising(right, m-k) / denom)
    return result


def generator(m):
    n = 2*(m+1)
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    index = lambda h,k: h*(m+1)+k
    for h in (0, 1):
        for k in range(m+1):
            i = index(h,k)
            edges = []
            if h == 0:
                if k > 0:
                    edges.append((index(h,k-1),F(k)))
                edges.append((index(1,k),F(k+1,m+2)))
            else:
                if k < m:
                    edges.append((index(h,k+1),F(m-k)))
                edges.append((index(0,k),F(m-k+1,m+2)))
            for j,v in edges:
                Q[i][j] += v
                Q[i][i] -= v
    return Q


def solve(A, b):
    n = len(b)
    B = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        pivot = next(i for i in range(c,n) if B[i][c] != 0)
        B[c],B[pivot] = B[pivot],B[c]
        q = B[c][c]
        B[c] = [x/q for x in B[c]]
        for i in range(n):
            if i != c:
                q = B[i][c]
                if q:
                    B[i] = [x-q*y for x,y in zip(B[i],B[c])]
    return [row[-1] for row in B]


def fraction(f):
    return str(f.numerator) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'


def check(m):
    P = candidate(m)
    Q = generator(m)
    n = len(P)
    assert sum(P) == 1 and min(P)>0
    assert all(sum(Q[i])==0 for i in range(n))
    assert all(sum(P[i]*Q[i][j] for i in range(n))==0 for j in range(n))
    equations = [[Q[j][i] for j in range(n)] for i in range(n)]
    equations[-1]=[F(1)]*n
    right = [F(0)]*(n-1)+[F(1)]
    assert solve(equations, right)==P
    dissent = [sum(P[h*(m+1)+(k if h==0 else m-k)] for h in (0,1)) for k in range(m+1)]
    a = F(1,m+3)
    beta = [F(comb(m,k))*rising(a,k)*rising(1+a,m-k)/rising(1+2*a,m) for k in range(m+1)]
    assert dissent==beta
    mean = sum(k*p for k,p in enumerate(dissent))
    fact2 = sum(k*(k-1)*p for k,p in enumerate(dissent))
    assert mean == F(m,m+5)
    assert fact2 == F(m*(m-1),2*(m+5))
    return {'m':m, 'stationary_mean_discord':fraction(mean),
            'second_factorial_moment':fraction(fact2),
            'probability_zero_discord':fraction(dissent[0]),
            'probability_all_dissent':fraction(dissent[-1]),
            'exact_solve_and_balance':True}


def main():
    report = {'verification':'exact independent rational linear solve and generator balance',
              'cases':[check(m) for m in range(1,8)],
              'asymptotic_basis':'algebraic product bounds, not inferred from finite enumeration'}
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
