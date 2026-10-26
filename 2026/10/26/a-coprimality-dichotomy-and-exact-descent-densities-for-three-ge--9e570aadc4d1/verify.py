#!/usr/bin/env python3
"""Exact, finite checks of the denumerant first-difference slope formula."""
from math import gcd, lcm
from itertools import product
from fractions import Fraction


def denumerants(a, b, c, limit):
    arr = [0] * (limit + 1)
    arr[0] = 1
    for v in (a, b, c):
        for n in range(v, limit + 1):
            arr[n] += arr[n-v]
    return arr


def predicted_slope(a, b, c, r):
    total = 1
    for v, w, t in ((a, b, c), (a, c, b), (b, c, a)):
        d = gcd(v, w)
        if d == 1:
            continue
        u = pow(t, -1, d)
        k = (r*u) % d
        total += t * (-u + d * (k >= d-u))
    return Fraction(total, a*b*c)


def check(a, b, c):
    L = lcm(a, b, c)
    P = denumerants(a, b, c, 6*L + 1)
    for r in range(L):
        delta4 = P[r+4*L+1] - P[r+4*L]
        delta5 = P[r+5*L+1] - P[r+5*L]
        assert Fraction(delta5 - delta4, L) == predicted_slope(a, b, c, r), (a,b,c,r)


def run():
    checked = 0
    for a,b,c in product(range(2, 12), repeat=3):
        if gcd(gcd(a,b),c) != 1:
            continue
        check(a,b,c)
        checked += 1
    for a,b,c in ((1,2,3),(1,6,9),(1,4,4),(1,7,11),(1,1,1),(1,5,10)):
        check(a,b,c)
        P = denumerants(a,b,c,1000)
        d = gcd(b,c)
        for n in range(200, 999):
            step = P[n+1] - P[n]
            assert step >= 0
            assert (step > 0) == ((n+1) % d == 0)
    for a,b,c in ((6,9,5),(6,9,7),(4,6,5),(8,12,5),(6,10,7)):
        assert gcd(gcd(a,b),c)==1
        assert gcd(a,b)>1 and gcd(a,c)==gcd(b,c)==1
        d=gcd(a,b);u=pow(c,-1,d)
        L=lcm(a,b,c)
        P=denumerants(a,b,c,6*L+1)
        neg=0
        for r in range(L):
            delta=P[r+5*L+1]-P[r+5*L]
            assert delta != 0
            assert (delta < 0) == (((r*u)%d)<d-u)
            neg += delta<0
        assert Fraction(neg,L)==Fraction(d-u,d)
    print('VERIFY_OK', 'primitive_triples=',checked)

if __name__=='__main__':run()
