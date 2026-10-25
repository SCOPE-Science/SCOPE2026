#!/usr/bin/env python3
"""Standalone integer-arithmetic checks for closed-neighbourhood conflict-free colorings.
Run with Python 3. No dependencies.
"""
from math import gcd

def direct_counts(n,k):
    # Exhaustively visit all maps 2n vertices -> two named colors.
    # Check unique occurrence directly rather than by a parity identity.
    N = [None]*(2*n)
    for i in range(n):
        N[i] = (i, (i-1)%n, (i+1)%n, i+n)
        N[n+i] = (i+n, ((i-k)%n)+n, ((i+k)%n)+n, i)
    total=0
    for b in range(1 << (2*n)):
        for quad in N:
            s=sum((b >> j)&1 for j in quad)
            if s not in (1,3):
                break
        else:
            total += 1
    return total

def reduced_counts(n,k):
    # Exhaust outer-ring labels; get inner-ring labels from each outer
    # closed neighbourhood, and CHECK direct uniqueness at inner vertices.
    total=0
    for b in range(1<<n):
        x = [((b>>i)&1) for i in range(n)]
        y = [1^x[(i-1)%n]^x[i]^x[(i+1)%n] for i in range(n)]
        valid = all(sum((x[i],y[i],y[(i-k)%n],y[(i+k)%n])) in (1,3) for i in range(n))
        if valid: total += 1
    return total

def predicted(n,k):
    # Polynomial arithmetic over F_2, via integer bit patterns.
    h=(1<<(k+1))
    for a in (-1,0,1):
        for b in (-k,0,k):
            h ^= 1<<(k+1+a+b)
    p=(1<<n)|1
    a,b=p,h
    while b:
        shift=a.bit_length()-b.bit_length()
        if shift<0: a,b=b,a
        else: a ^= b<<shift
    return 1<<(a.bit_length()-1)

if __name__=='__main__':
    print('Full direct all-labeling checks:')
    for n in range(3,9):
        for k in range(1, (n-1)//2+1):
            actual=direct_counts(n,k)
            expected=predicted(n,k)
            assert actual==expected, ('direct', n,k,actual,expected)
            print('n=%2d k=%d verified=%d' % (n,k,actual))
    print('Reduced exhaustive outer-label checks:')
    for n in range(3,18):
        for k in range(1,min((n-1)//2,6)+1):
            actual=reduced_counts(n,k)
            expected=predicted(n,k)
            assert actual==expected, ('reduced',n,k,actual,expected)
            if k in (1,2):print('n=%2d k=%d verified=%d' % (n,k,actual))
    print('PASS: every finite instance agrees with gcd-polynomial count.')
