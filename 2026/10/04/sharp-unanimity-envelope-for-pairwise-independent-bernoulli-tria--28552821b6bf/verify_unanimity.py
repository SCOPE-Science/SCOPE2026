#!/usr/bin/env python3
"""Exact rational checks for the sharp pairwise-independent Bernoulli unanimity formula."""
from fractions import Fraction as F
from itertools import combinations
from math import ceil


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def solve3(a, b):
    d = det3(a)
    if d == 0:
        return None
    out = []
    for j in range(3):
        aj = [row[:] for row in a]
        for i in range(3):
            aj[i][j] = b[i]
        out.append(det3(aj) / d)
    return out


def bound(n, p):
    q = min(p, 1-p)
    if q == 0:
        return F(1)
    if n % 2 == 0 and q >= F(n-2, 2*(n-1)):
        return F(1, n) + 4*F(n-1, n)*(p-F(1,2))**2
    r = ceil((n-1)*q)
    return (n*(n-1)*q*q - 2*n*r*q + r*(r+1)) / (r*(r+1))


def vertex_max(n, p):
    target = [F(1), n*p, n*(n-1)*p*p]
    best = F(-1)
    for support in combinations(range(n+1), 3):
        a = [
            [F(1), F(1), F(1)],
            [F(k) for k in support],
            [F(k*(k-1)) for k in support],
        ]
        w = solve3(a, target)
        if w is None or min(w) < 0:
            continue
        objective = sum(w[i] for i,k in enumerate(support) if k in (0,n))
        if objective > best:
            best = objective
    return best


def construction(n, p):
    q = min(p, 1-p)
    if q == 0:
        return [(0 if p == 0 else n, F(1))]
    if n % 2 == 0 and q >= F(n-2, 2*(n-1)):
        m = n//2
        w0 = (1-p)*(m-(2*m-1)*p)/m
        wm = 2*(2*m-1)*p*(1-p)/m
        wn = p*((2*m-1)*p-m+1)/m
        return [(0,w0),(m,wm),(n,wn)]
    r = ceil((n-1)*q)
    w0 = (n*(n-1)*q*q - 2*n*r*q + r*(r+1))/(r*(r+1))
    wr = n*q*(r-(n-1)*q)/r
    wr1 = n*q*((n-1)*q-r+1)/(r+1)
    if p <= F(1,2):
        return [(0,w0),(r,wr),(r+1,wr1)]
    return [(n,w0),(n-r,wr),(n-r-1,wr1)]


def moments(support):
    return [
        sum(w for _,w in support),
        sum(F(k)*w for k,w in support),
        sum(F(k*(k-1))*w for k,w in support),
    ]

cases = 0
for n in range(2, 13):
    for den in range(2, 11):
        for num in range(den+1):
            p = F(num, den)
            b = bound(n,p)
            vm = vertex_max(n,p)
            assert vm == b, (n,p,vm,b)
            s = construction(n,p)
            assert min(w for _,w in s) >= 0, (n,p,s)
            assert moments(s) == [F(1),n*p,n*(n-1)*p*p], (n,p,s,moments(s))
            obj = sum(w for k,w in s if k in (0,n))
            assert obj == b, (n,p,obj,b,s)
            cases += 1
print(f"EXACT_VERTEX_CASES={cases}")
print("CHECK_OK")
