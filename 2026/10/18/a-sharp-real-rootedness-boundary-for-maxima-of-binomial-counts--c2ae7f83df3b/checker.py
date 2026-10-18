#!/usr/bin/env python3
"""Exact integer/rational checks for binomial-maximum real-rootedness results.

Run with Python 3 standard library: python checker.py
The infinite-domain arguments are in RESULT.md; tests here verify identities
and finite exact instances, not substitute for the proofs.
"""
from fractions import Fraction
from math import comb


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def neg(a):
    return [-x for x in a]


def sub(a, b):
    return add(a, neg(b))


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def power(a, n):
    out = [1]
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


def scale(a, c):
    return trim([c*x for x in a])


def probabilities(n, m):
    """Polynomial coefficients in p, for P(max of m Bin(n,p)=k)."""
    prev = [0]
    ans = []
    for k in range(n+1):
        cdf = [0]
        for j in range(k+1):
            component = mul(power([0, 1], j), power([1, -1], n-j))
            cdf = add(cdf, scale(component, comb(n, j)))
        nxt = power(cdf, m)
        ans.append(sub(nxt, prev))
        prev = nxt
    return ans


def discriminant_cubic(a, b, c, d):
    return add(add(sub(mul(mul(b,b),mul(c,c)), scale(mul(a,power(c,3)),4)),
                   sub(scale(mul(power(b,3),d),-4),scale(mul(power(a,2),power(d,2)),27))),
               scale(mul(mul(a,b),mul(c,d)),18))


def evalpoly(a,x):
    v=0
    for c in reversed(a):
        v=v*x+c
    return v


def main():
    cases = 0
    p = [0,1]
    one_minus_p = [1,-1]
    cs = probabilities(3,2)
    # Exact individual mass-polynomial formulas.
    expected=[power(one_minus_p,6),
              scale(mul(mul(p,power(one_minus_p,4)),[2,1]),3),
              scale(mul(mul(power(p,2),power(one_minus_p,2)),[2,2,-1]),3),
              mul(power(p,3),[2,0,0,-1])]
    assert cs == expected
    cases += 4
    # Full discriminant identity as an equality of integer polynomials.
    q=[-1,6,3,8,0,0,4]
    lhs=discriminant_cubic(*cs)
    rhs=scale(mul(mul(power(p,6),power(one_minus_p,12)),q),108)
    assert lhs == rhs, (lhs,rhs)
    cases += 1
    assert evalpoly(q,Fraction(1,10))<0
    assert evalpoly(q,Fraction(1,2))>0
    assert evalpoly(q,Fraction(150732,1000000))<0
    assert evalpoly(q,Fraction(150733,1000000))>0
    cases += 4
    # Leading p^k coefficient in each kth occupancy mass, and normalization.
    for n in range(1,9):
        for m in range(1,7):
            probs=probabilities(n,m)
            assert sum((evalpoly(x,Fraction(2,5)) for x in probs),Fraction(0))==1
            assert len(probs)==n+1
            assert probs[0][0]==1
            for k in range(1,n+1):
                assert len(probs[k])>=k+1
                assert all(probs[k][j]==0 for j in range(k))
                assert probs[k][k] == m*comb(n,k)
                cases+=2
            cases+=3
    # Check the degree-two discriminant, for all p in an exact rational grid.
    for m in range(1,36):
        for a in range(1,30):
            x=Fraction(a,30)
            C=probabilities(2,m)
            xx=[evalpoly(v,x) for v in C]
            disc=xx[1]**2 - 4*xx[0]*xx[2]
            qx=1-x
            rhs=qx**(2*m) * ((qx**m+(1+x)**m)**2-4)
            assert disc==rhs
            assert disc >= 0
            cases+=2
    print('PASS: %d exact algebraic/finite checks'%cases)

if __name__=='__main__':
    main()
