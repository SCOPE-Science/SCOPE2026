#!/usr/bin/env python3
"""Exact finite-graph resistance identities and numerical checks of scaling laws."""
from fractions import Fraction as F
from math import sqrt, pi, asin, sin, cos


def invert(a):
    n = len(a)
    m = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if m[k][j] != 0)
        m[j], m[k] = m[k], m[j]
        c = m[j][j]
        m[j] = [v / c for v in m[j]]
        for i in range(n):
            if i != j:
                f = m[i][j]
                m[i] = [u - f*v for u, v in zip(m[i], m[j])]
    return [row[n:] for row in m]


def kirchhoff_index(n, weights, p=None, q=None, chord=F(0)):
    assert len(weights) == n-1
    a = [[F(1,n) for _ in range(n)] for _ in range(n)]
    for i, w in enumerate(weights):
        assert w > 0
        a[i][i] += w
        a[i+1][i+1] += w
        a[i][i+1] -= w
        a[i+1][i] -= w
    if chord:
        a[p][p] += chord
        a[q][q] += chord
        a[p][q] -= chord
        a[q][p] -= chord
    inv = invert(a)
    return n*sum(inv[i][i] for i in range(n))-n


def shortcut_sensitivity(n, weights, p, q):
    total = F(0)
    for s in range(n):
        for t in range(s+1,n):
            voltage = sum((1/weights[i-1] for i in range(max(p+1,s+1), min(q,t)+1)),F(0))
            total += voltage**2
    return total


def theta(n,p,q):
    ix = list(range(p+1,q+1))
    return sum((min(i,j)*(n-max(i,j))/sqrt(i*(n-i)*j*(n-j))
                for i in ix for j in ix))


def continuum(a,b):
    ua, ub = asin(sqrt(a)), asin(sqrt(b))
    A = lambda u: u-sin(2*u)/2
    B = lambda u: u+sin(2*u)/2
    H = lambda u: u*u/2+u*sin(2*u)/2+cos(2*u)/2+cos(4*u)/16
    return 2*(H(ub)-H(ua)-A(ua)*(B(ub)-B(ua)))


def boundary_profile(k):
    if k == 0: return 2/3
    return (4/3)*(k+0.5-2*k**1.5*(sqrt(k+1)-sqrt(k)))


def main():
    checks=0
    for n in range(3,9):
        w=[F(i+2, (n+2)*(n+3)) for i in range(n-1)]
        old=kirchhoff_index(n,w)
        for p in range(n-2):
            for q in range(p+2,n):
                s=shortcut_sensitivity(n,w,p,q)
                r=sum((1/w[i-1] for i in range(p+1,q+1)),F(0))
                for z in (F(1,7),F(3,11)):
                    new=kirchhoff_index(n,w,p,q,z)
                    assert old-new==z*s/(1+z*r),(n,p,q,z)
                    checks+=1
    assert theta(3,0,2)==3
    assert abs(theta(4,0,3)-(F(11,3)+4/sqrt(3)))<2e-13
    assert abs(continuum(0,1)-(pi*pi/4-2))<2e-13
    assert abs(boundary_profile(0)-F(2,3))<1e-14
    assert .66<boundary_profile(0)<boundary_profile(1)<boundary_profile(4)<1
    n=1000
    assert abs(theta(n,0,n-1)/n**2-(pi*pi/4-2))<0.0001
    L=30
    assert abs(theta(n,0,L)/L**2-boundary_profile(0))<0.025
    assert abs(theta(n,L,2*L)/L**2-boundary_profile(1))<0.025
    assert abs(theta(n,300,300+L)/L**2-1)<0.045
    n=400
    assert abs(theta(n,80,280)/n**2-continuum(.2,.7))<0.002
    print('VERIFY_OK',checks,'exact rank-one identities; continuum and boundary checks')

if __name__=='__main__':main()
