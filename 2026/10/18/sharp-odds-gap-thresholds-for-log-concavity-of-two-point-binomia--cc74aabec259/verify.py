"""Exact-rational consistency tests for two-point binomial curvature formulas.

Run: python verify.py
Finite tests are not a proof of universal claims; see RESULT.md.
"""
from fractions import Fraction as Q
from math import comb


def masses(n, p, q, w):
    return [Q(comb(n, k)) * ((1-w)*p**k*(1-p)**(n-k)
           + w*q**k*(1-q)**(n-k)) for k in range(n+1)]


def check(n, p, q, w):
    assert n >= 2 and Q(0) < p < q < Q(1) and Q(0) < w < Q(1)
    a = masses(n, p, q, w)
    assert sum(a) == 1
    r = (q/(1-q)) / (p/(1-p))
    delta = (r-1)**2 / r
    t = (w/(1-w))*((1-q)/(1-p))**n
    for k in range(1, n):
        z = t*r**k
        ratio = Q(k*(n-k), (k+1)*(n-k+1)) * (
            1+delta*z/(1+z)**2)
        assert a[k-1]*a[k+1]/a[k]**2 == ratio
        lc = a[k]**2 >= a[k-1]*a[k+1]
        ulc = k*a[k]**2 >= (k+1)*a[k-1]*a[k+1]
        assert lc == (delta*k*(n-k)*z <= (n+1)*(1+z)**2)
        assert ulc == (delta*(n-k)*z <= (1+z)**2)


n, p, q = 10, Q(1,3), Q(1,2)
w = Q(4**10, 4**10+2*3**10)
a = masses(n,p,q,w)
assert a[1]**2/(2*a[0]*a[2]) == Q(80,81)
assert Q(1,2) < Q(4*(n+1),n*n//4)
assert Q(1,2) > Q(4,n-1)
check(n,p,q,w)
settings = indices = 0
for n in range(2,15):
    for i in range(1,7):
        for j in range(i+1,9):
            p, q = Q(i,10), Q(j,10)
            for w in (Q(1,7), Q(1,3), Q(1,2), Q(2,3), Q(6,7)):
                check(n,p,q,w)
                settings += 1
                indices += n-1
assert settings == 1755 and indices == 12285
print('PASS: exact witness,',settings,'parameter settings,',indices,'interior indices')
