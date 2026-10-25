#!/usr/bin/env python3
"""Exact-rational finite checks of a Dirichlet–multinomial covariance identity."""
from fractions import Fraction as F
from math import factorial, comb


def rising(x, n):
    v = F(1)
    for j in range(n):
        v *= x + j
    return v


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for j in range(n + 1):
        for tail in compositions(n-j, k-1):
            yield (j,) + tail


def check_count(n, k, a):
    a = F(a)
    d = rising(k*a,n)
    em1 = em2 = e12 = F(0)
    total = F(0)
    for x in compositions(n,k):
        wt = F(factorial(n),1)
        for v in x:
            wt *= rising(a,v)/factorial(v)
        wt /= d
        m1 = x.count(1); m2=x.count(2)
        em1 += wt*m1
        em2 += wt*m2
        e12 += wt*m1*m2
        total += wt
    assert total == 1
    p1 = n*a*rising((k-1)*a,n-1)/d
    p2 = comb(n,2)*rising(a,2)*rising((k-1)*a,n-2)/d
    p12 = F(n*comb(n-1,2),1)*a*rising(a,2)*rising((k-2)*a,n-3)/d
    assert em1 == k*p1
    assert em2 == k*p2
    assert e12 == k*(k-1)*p12
    ratio = F((k-1)*(n-2),k*n)*rising(k*a,n)*rising((k-2)*a,n-3)/(rising((k-1)*a,n-1)*rising((k-1)*a,n-2))
    assert (e12-em1*em2) == k*k*p1*p2*(ratio-1)
    return 1 if ratio>1 else (-1 if ratio<1 else 0)


def check_derivative(n,k,t):
    t=F(t)
    B=(k+(n-3)*t)*(k+(n-2)*t)*(k+(n-1)*t) / ((k-1+(n-3)*t)**2 * (k-1+(n-2)*t))
    ld=(F(n-3,k+(n-3)*t)+F(n-2,k+(n-2)*t)+F(n-1,k+(n-1)*t)
        -F(2*(n-3),k-1+(n-3)*t)-F(n-2,k-1+(n-2)*t))
    den=(k+(n-3)*t)*(k+(n-2)*t)*(k+(n-1)*t)*(k-1+(n-3)*t)*(k-1+(n-2)*t)
    c0=k*k*(k-1)*(2*k-3*n+6)
    c1=k*((6*n-14)*k*k+(-9*n*n+33*n-26)*k+6*n*n-24*n+22)
    c2=(n-2)*((6*n-16)*k*k+(-9*n*n+36*n-29)*k+3*n*n-12*n+9)
    c3=(n-3)*(n-2)*(2*k*(n-2)-3*n*n+10*n-7)
    assert ld == (c0+c1*t+c2*t*t+c3*t*t*t)/den
    assert c0>0 and c1>0 and c2>0 and c3>0
    assert B>0


def main():
    cases=0
    for n,k in [(4,5),(5,8),(6,12)]:
        assert check_count(n,k,F(1,1000)) == 1
        assert check_count(n,k,F(1,1)) == -1
        cases+=2
    for n in range(4,26):
        k=2+comb(n-1,2)
        for shift in [0,1,20]:
            for t in [F(0),F(1,10),F(7,2)]:
                check_derivative(n,k+shift,t)
                cases+=1
    print(f'PASS: {cases} exact-rational checks (six whole-distribution enumerations and derivative identities).')


if __name__=='__main__':
    main()
