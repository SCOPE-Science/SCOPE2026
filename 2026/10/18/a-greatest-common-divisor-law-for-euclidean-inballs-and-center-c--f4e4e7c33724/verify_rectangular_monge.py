#!/usr/bin/env python3
"""Exact rational checks for normalized rectangular Monge inball theorem.

Run: python3 verify_rectangular_monge.py
Uses Python standard library only; finite checks do not replace the proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd


def center_slack(p, q, delta):
    g = gcd(p, q)
    assert len(delta) == g - 1 and all(-1 <= x <= 1 for x in delta)
    u, v = [Q(0)], [Q(0)]
    for i in range(1, p):
        j, r = divmod(i*q, p)
        step = Q(2*j) if r else Q(2*j-1) + delta[i//(p//g)-1]
        u.append(u[-1] + step)
    for j in range(1, q):
        i, r = divmod(j*p, q)
        step = Q(2*i) if r else Q(2*i-1) - delta[j//(q//g)-1]
        v.append(v[-1] + step)
    return [[u[i]+v[j]-2*i*j for j in range(q)] for i in range(p)]


def verify(p, q, delta):
    g = gcd(p, q)
    z = center_slack(p, q, delta)
    assert all(a >= 0 for row in z for a in row)
    assert all(z[i][j+1]+z[i+1][j]-z[i][j]-z[i+1][j+1] == 2
               for i in range(p-1) for j in range(q-1))
    lam = {(a,b): min(q*a, p*b)-a*b
           for a in range(1, p) for b in range(1, q)}
    assert min(lam.values()) > 0
    L = lambda a,b: lam.get((a,b),0)
    for i in range(p):
        for j in range(q):
            left = 1 - (L(i+1,j)+L(i,j+1)-L(i+1,j+1)-L(i,j))
            overlap = max(Q(0),min(Q(i+1,p),Q(j+1,q))-
                          max(Q(i,p),Q(j,q)))
            assert left == p*q*overlap
    sum_lam = sum(lam.values())
    T = Q(p*p*q*q-p*p-q*q+g*g,6)
    assert T == 2*sum_lam == sum(map(sum,z))
    zeros = {(i,j) for i in range(p) for j in range(q) if z[i][j] == 0}
    base = {(i,j) for i in range(p) for j in range(q)
            if min(Q(i+1,p),Q(j+1,q)) > max(Q(i,p),Q(j,q))}
    extra = set()
    for k, value in enumerate(delta, start=1):
        i, j = k*p//g, k*q//g
        if value == 1:
            extra.add((i-1,j))
        if value == -1:
            extra.add((i,j-1))
    assert len(base) == p+q-g
    assert not extra.intersection(base)
    assert zeros == base.union(extra), (p,q,delta,zeros,base,extra)
    return True


def main():
    checked = 0
    for p in range(2, 13):
        for q in range(2, 13):
            g = gcd(p,q)
            for k in range(g-1):
                for d in [-1, 1]:
                    ds = [Q(0)]*(g-1)
                    ds[k] = Q(d)
                    verify(p,q,ds)
                    checked += 1
            verify(p,q,[Q(0)]*(g-1))
            checked += 1
            if g <= 6:
                for t in product([-1,0,1],repeat=g-1):
                    verify(p,q,[Q(x) for x in t])
                    checked += 1
    print('PASS: %d exact rational parameter profiles for 2 <= p,q <= 12' % checked)


if __name__ == '__main__':
    main()
