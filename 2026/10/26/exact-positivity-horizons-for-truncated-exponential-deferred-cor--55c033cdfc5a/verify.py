#!/usr/bin/env python3
"""Exact rational checks of pure-birth transition-polynomial identities.

This is a finite consistency checker, not a proof of the universal theorem.
Only the Python standard library is needed.
"""
from fractions import Fraction as F
from math import factorial


def poly(m, z):
    return sum((z**j / factorial(j) for j in range(m + 1)), F(0))


def transient(p, k, h):
    return h**k / factorial(k) * poly(p-k, -h) if k <= p else F(0)


def absorption(p, r, h):
    if r > p:
        return F(0)
    return h**r / factorial(r-1) * sum(
        ((-h)**j / (factorial(j) * (r+j)) for j in range(p-r+1)), F(0))


def mult(a, b):
    n = len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def endpoint(p, d, h):
    n = d+1
    q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(d):
        q[i][i] = F(-1)
        q[i][i+1] = F(1)
    hq = [[h*a for a in row] for row in q]
    out = [[F(int(i==j)) for j in range(n)] for i in range(n)]
    power = [[F(int(i==j)) for j in range(n)] for i in range(n)]
    for ell in range(1,p+1):
        power = mult(power,hq)
        for i in range(n):
            for j in range(n):
                out[i][j] += power[i][j] / factorial(ell)
    return out


def bisect_odd(m):
    assert m % 2 == 1
    left, right = 0.0, float(max(m, 1)+2)
    for _ in range(75):
        mid = (left+right)/2
        if sum(((-mid)**j/factorial(j) for j in range(m+1))) > 0:
            left = mid
        else:
            right = mid
    return (left+right)/2


def bisect_even_return(m):
    assert m % 2 == 0
    left, right = 0.0001, float(m+5)
    for _ in range(75):
        mid=(left+right)/2
        pp=sum(((-mid)**j/factorial(j) for j in range(m+1)))
        if pp<1:
            left=mid
        else:
            right=mid
    return (left+right)/2


def run():
    checks=0
    for p in range(2,11):
        for d in range(1,9):
            for h in (F(1,10), F(7,12), F(1), F(4,3), F(2), F(3)):
                tab=endpoint(p,d,h)
                for i in range(d):
                    r=d-i
                    assert sum(tab[i], F(0)) == 1
                    for k in range(r):
                        assert tab[i][i+k] == transient(p,k,h), (p,d,h,i,k)
                    assert tab[i][d] == absorption(p,r,h), (p,d,h,i,'abs')
                    checks += r+2
                assert tab[d][-1] == 1
    # At the predicted integer boundaries, all d>=p become negative for h>1,
    # while the p-1 active case has threshold p/(p-1).
    for p in range(3,11):
        for d,h,expected in ((p,F(1),True),(p,F(11,10),False),
                             (p-1,F(p,p-1),True),
                             (p-1,F(p,p-1)+F(1,10),False)):
            tab=endpoint(p,d,h)
            assert all(x >= 0 for row in tab for x in row) == expected,(p,d,h)
            checks+=1
    # Odd exponential truncations have increasing positive roots.
    odd=[bisect_odd(m) for m in range(1,20,2)]
    assert all(odd[i]<odd[i+1] for i in range(len(odd)-1))
    # Check sample low-degree parity crossover.
    assert 2.7 < bisect_even_return(4) < 2.9
    assert 1.5 < bisect_odd(3) < 1.7
    assert 2.1 < bisect_odd(5) < 2.3
    print('VERIFY_OK exact polynomial matrix entries and sharp staircase; checks=',checks)
    print('p4,d1 H approx',format(bisect_even_return(4),'.12f'))
    print('p4,d2 H approx',format(bisect_odd(3),'.12f'))

if __name__ == '__main__':
    run()
