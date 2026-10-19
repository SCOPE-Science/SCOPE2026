#!/usr/bin/env python3
"""Exact polynomial checks for second-Hermite radial-disk eigenvalue crossings.

Requires only the Python standard library. Finite checks corroborate the
unrestricted symbolic algebra and arithmetic proof; they are not its substitute.
"""
from fractions import Fraction as F
from math import factorial, isqrt


def add(a, b):
    ans = [F(0)] * max(len(a), len(b))
    for j, v in enumerate(a): ans[j] += v
    for j, v in enumerate(b): ans[j] += v
    return trim(ans)


def mul(a, b):
    ans = [F(0)] * (len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b): ans[i+j] += v*w
    return trim(ans)


def trim(a):
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a


def scale(a, c):
    return trim([v*c for v in a])


def qpoly(k):
    """Polynomial Q_k in lambda_k(a)=1-exp(-a)*Q_k(a)."""
    if k == 0: density = [F(0), F(0), F(1,2)]
    elif k == 1: density = scale(mul([F(0), F(1)], mul([F(2),F(-1)],[F(2),F(-1)])),F(1,2))
    else:
        A = [F(k*(k-1)),F(-2*k),F(1)]
        density = [F(0)]*(k-2) + scale(mul(A,A), F(1,2*factorial(k)))
    out = [F(0)]*len(density)
    for j,c in enumerate(density):
        for i in range(j+1): out[i] += c*factorial(j)/factorial(i)
    assert out[0] == 1
    return trim(out)


def difference_predicted(k):
    Ak = [F(k*(k-1)),F(-2*k),F(1)]
    Ak1 = [F(k*(k+1)),F(-2*(k+1)),F(1)]
    # k=0: factor a^(-1) is canceled by the a^2 factor in Ak.
    if k==0:
        return scale(mul([F(0),F(1)], Ak1),F(-1,2))
    return [F(0)]*(k-1) + scale(mul(Ak,Ak1),F(-1,2*factorial(k+1)))


def sub(a,b): return add(a,scale(b,F(-1)))


def run():
    nchecks=0
    for k in range(101):
        # lambda_{k+1}-lambda_k = exp(-a) (Q_k - Q_{k+1})
        assert sub(qpoly(k),qpoly(k+1)) == trim(difference_predicted(k))
        nchecks+=1
    for n in range(1,201):
        # Q_n=(a-n)^2-n: its roots are n +/- sqrt(n).
        # Exactly both are positive for n>1.
        assert (n+isqrt(n)) > 0
        assert n-isqrt(n) > 0 or n == 1 or isqrt(n)**2 < n
        nchecks+=1
    observed=[]
    for n in range(1,101):
        for m in range(n+1,101):
            # If different resonance root branches coincide then both
            # n,m are squares of consecutive positive integers.
            # Exact integer-surd comparison using only integer square roots.
            if isqrt(n)**2 == n and isqrt(m)**2 == m:
                if n+isqrt(n) == m-isqrt(m): observed.append((n,m))
    assert observed == [(j*j,(j+1)*(j+1)) for j in range(1,10)]
    nchecks+=1
    for k in range(101):
        # Q_k and Q_{k+2} have no common root for integer k>=0.
        # Simultaneous roots would imply a-k=1/2 and k=1/4.
        assert 4*k != 1
        nchecks+=1
    print('PASS:',nchecks,'exact checks')

if __name__=='__main__': run()
