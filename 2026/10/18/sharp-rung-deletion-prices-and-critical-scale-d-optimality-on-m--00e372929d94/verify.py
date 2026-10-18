#!/usr/bin/env python3
"""Exact and numerical checks for weighted Möbius-ladder tree allocation.
Run with Python 3; no external dependencies.
"""
from fractions import Fraction as F
import math


def det_exact(rows):
    a = [[F(z) for z in row] for row in rows]
    n = len(a)
    ans = F(1)
    for k in range(n):
        i = next((i for i in range(k, n) if a[i][k]), None)
        if i is None:
            return F(0)
        if i != k:
            a[k], a[i] = a[i], a[k]
            ans = -ans
        pivot = a[k][k]
        ans *= pivot
        for j in range(k + 1, n):
            coeff = a[j][k] / pivot
            if coeff:
                for m in range(k + 1, n):
                    a[j][m] -= coeff * a[k][m]
            a[j][k] = F(0)
    return ans


def reduced_laplacian(n, a, b):
    nn = 2*n
    L = [[F(0) for j in range(nn)] for i in range(nn)]
    edges = [(i, (i+1) % nn, b) for i in range(nn)]
    edges += [(i, i+n, a) for i in range(n)]
    for i, j, w in edges:
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return [row[:-1] for row in L[:-1]]


def cheby(n, x):
    if n == 0:
        return F(1)
    a, b = F(1), F(x)
    for _ in range(2, n+1):
        a, b = b, 2*x*b-a
    return b


def grad(n, t, r):
    if r == 0:
        return (n*n-(2*n-1)*t)/2
    u = math.acosh(1+r)
    return n*math.tanh(n*u/2)/math.sqrt(r*(r+2))-(2*n-1)*t/(2+t*r)


def optimum_ratio(n, t):
    if t >= n*n/(2*n-1):
        return 0.0
    lo, hi = 0.0, 1.0
    while grad(n, t, hi) > 0:
        hi *= 2
    for _ in range(90):
        mid = (lo+hi)/2
        if grad(n, t, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def limiting_z(c):
    assert 0 < c < 0.5
    lo, hi = 0.0, 1.0
    while math.tanh(hi)/hi > 2*c:
        hi *= 2
    for _ in range(100):
        z = (lo+hi)/2
        if math.tanh(z)/z > 2*c:
            lo = z
        else:
            hi = z
    return (lo+hi)/2


def main():
    count=0
    for n in range(2,8):
        for a in (0,1,2,3):
            for b in (1,2,3):
                actual = det_exact(reduced_laplacian(n,F(a),F(b)))
                expected = n * F(b)**(2*n-1) * (cheby(n, F(a,b)+1)+1)
                assert actual == expected, (n,a,b,actual,expected)
                count+=1
    for n, expected in ((2,16),(3,81),(4,392),(5,1815)):
        assert det_exact(reduced_laplacian(n, F(1), F(1))) == expected
    threshold=0
    for n in range(2,50):
        tc=F(n*n,2*n-1)
        assert grad(n,float(tc),0) < 1.e-11
        assert grad(n,float(tc)*1.01,0)<0
        assert grad(n,float(tc)*0.99,0)>0
        threshold+=1
    fixed_t=0
    for t in (0.25,1.0,3.0):
        rad=math.sqrt((2*t-1)**2+3)
        rlim=2*(1-2*t+rad)/(3*t)
        r=optimum_ratio(500,t)
        assert abs(r-rlim)/rlim < 0.04, (t,r,rlim)
        fixed_t+=1
    critical=0
    for c in (0.2,0.3,0.4):
        z=limiting_z(c)
        n=500
        t=c*n
        r=optimum_ratio(n,t)
        assert abs(n*n*r-2*z*z)/(2*z*z)<0.03
        gain=(2*n-1)*math.log(2/(2+t*r)) + 2*math.log(math.cosh(n*math.acosh(1+r)/2))
        pred=2*math.log(math.cosh(z))-2*c*z*z
        assert abs(gain-pred)<0.03, (c,gain,pred)
        critical+=1
    for n in (8,50,200):
        assert optimum_ratio(n,n) == 0.0
    print(f'VERIFY_OK exact_cofactors={count} unweighted_counts=4 threshold_cases={threshold} fixed_price_limits={fixed_t} critical_price_limits={critical}')

if __name__ == '__main__':
    main()
