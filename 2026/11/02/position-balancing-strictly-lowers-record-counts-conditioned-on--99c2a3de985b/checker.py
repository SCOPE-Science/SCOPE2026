#!/usr/bin/env python3
"""Exact checks for fixed-point-conditioned record laws.
Run using Python 3's standard library: python checker.py.
The finite checks supplement the algebraic argument, not replace it.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def rising_polynomial(length):
    """Ascending coefficients of z(z+1)...(z+length-1)."""
    out = [1]
    for j in range(length):
        next_out = [0] * (len(out) + 1)
        for k, value in enumerate(out):
            next_out[k] += j * value
            next_out[k+1] += value
        out = next_out
    return out


def product(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def conditioned_counts(n,i):
    """Numerators (n-1)! P(R=k | pi(i)=i), k=0,...,n."""
    m=n-1
    base=rising_polynomial(m)
    extra=product(rising_polynomial(i-1),rising_polynomial(n-i))
    out=[0]*(n+1)
    for k,v in enumerate(base):out[k]+=v
    for k,v in enumerate(extra):
        out[k]-=v
        out[k+1]+=v
    return out


def records(perm):
    maximum=0;count=0
    for x in perm:
        if x>maximum:
            maximum=x;count+=1
    return count


def run():
    assertions=0
    for n in range(2,10):
        observed=[Counter() for _ in range(n)]
        for perm in permutations(range(1,n+1)):
            r=records(perm)
            for i,x in enumerate(perm):
                if x==i+1:
                    observed[i][r]+=1
        for i in range(1,n+1):
            predicted=conditioned_counts(n,i)
            for k in range(n+1):
                assert observed[i-1][k]==predicted[k], (n,i,k,observed[i-1][k],predicted[k])
                assertions+=1
    for n in range(2,81):
        m=n-1
        distributions=[conditioned_counts(n,i) for i in range(1,n+1)]
        for i,cnt in enumerate(distributions,1):
            assert all(x>=0 for x in cnt)
            assert sum(cnt)==factorial(m)
            assert cnt==distributions[n-i]
            assertions+=3
            assert sum(k*x for k,x in enumerate(cnt))*comb(m,i-1)==(sum(Fraction(1,j) for j in range(1,m+1))*comb(m,i-1)+1)*factorial(m)
            assertions+=1
        for i in range(1,n):
            a=i-1;b=n-i
            poly=product(rising_polynomial(a),rising_polynomial(b-1))
            coefficient=n-2*i
            diffs=[sum(distributions[i-1][t:])-sum(distributions[i][t:]) for t in range(n+1)]
            for t in range(n+1):
                expected=coefficient*(poly[t-1] if 0<=t-1<len(poly) else 0)
                assert diffs[t]==expected, (n,i,t,diffs[t],expected)
                assertions+=1
            if coefficient>=0:
                assert all(x>=0 for x in diffs)
                assertions+=1
            if coefficient>0:
                assert any(x>0 for x in diffs)
                assertions+=1
            if coefficient==0:
                assert all(x==0 for x in diffs)
                assertions+=1
            if coefficient>0:
                tv_numerator=sum(abs(distributions[i-1][k]-distributions[i][k]) for k in range(n+1))//2
                assert tv_numerator==coefficient*max(poly)
                w1_numerator=sum(diffs)
                assert w1_numerator==coefficient*factorial(a)*factorial(b-1)
                assertions+=2
    print(f"PASS: {assertions:,} exact arithmetic assertions; exhaustive permutations n=2..9; polynomial laws n=2..80.")

if __name__=='__main__':
    run()
