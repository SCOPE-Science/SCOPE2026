#!/usr/bin/env python3
"""Exact rational independent checks of a three-location two-facility distortion law."""
from fractions import Fraction
from itertools import combinations
from random import Random


def direct(A, B, C, gap_left, gap_right):
    """Enumerate labeled facility pairs, retaining zero-weight duplicate pairs."""
    x = [0]*A + [gap_left]*B + [gap_left+gap_right]*C
    n=len(x)
    total_weight=0
    weighted_cost=0
    for i,j in combinations(range(n),2):
        weight=abs(x[i]-x[j])
        total_weight+=weight
        weighted_cost += weight*sum(min(abs(v-x[i]), abs(v-x[j])) for v in x)
    assert total_weight>0
    # For points on a line, two optimal centers can be chosen among reports.
    offline=min(sum(min(abs(v-u),abs(v-w)) for v in x)
                for u,w in combinations(sorted(set(x)),2))
    assert offline>0
    return Fraction(weighted_cost,total_weight*offline)


def expression(A,B,C,a,b):
    Z=A*B*a + B*C*b + A*C*(a+b)
    offline=min(A*a,B*min(a,b),C*b)
    return Fraction(A*B*C*(2*a*b+(a+b)*min(a,b)),Z*offline)


def theoretical(n):
    N=n-1
    collapsed=Fraction(3*(n-2),n-1)
    same=max(Fraction(4*A*B,A*B+B+2*A)
             for A in range(1,N) for B in [N-A])
    return max(collapsed,same),collapsed,same


def run():
    checks=0
    for n in range(3,19):
        upper,collapsed,same=theoretical(n)
        assert (same < collapsed) if n<=14 else (same > collapsed), (n,same,collapsed)
        for A in range(1,n-1):
            for B in range(1,n-A):
                C=n-A-B
                for a,b in ((1,1),(1,2),(1,7),(2,1),(7,1),(3,5),(5,3)):
                    value=direct(A,B,C,a,b)
                    assert value == expression(A,B,C,a,b),(n,A,B,C,a,b,value)
                    assert value <= upper,(n,A,B,C,a,b,value,upper)
                    checks+=1
    for n in (19,20,25,30,40):
        upper,_,_=theoretical(n)
        for A in range(1,n-1):
            for B in range(1,n-A):
                C=n-A-B
                for a,b in ((1,1),(1,100),(100,1)):
                    value=expression(A,B,C,a,b)
                    assert value <= upper
                    checks+=1
    rng=Random(604204)
    for _ in range(2500):
        n=rng.randint(3,65)
        A=rng.randint(1,n-2)
        B=rng.randint(1,n-A-1)
        C=n-A-B
        a=rng.randint(1,100000)
        b=rng.randint(1,100000)
        assert expression(A,B,C,a,b) <= theoretical(n)[0]
        checks+=1
    for n in range(3,15):
        # Limit b/a -> infinity with (1,n-2,1).
        A,B,C=1,n-2,1
        limit=Fraction(3*(n-2),n-1)
        assert expression(A,B,C,1,10**12)<limit
        assert limit-expression(A,B,C,1,10**12) < Fraction(10,10**12)
    for n in range(15,66):
        N=n-1
        bestA=min(range(1,N),key=lambda a:Fraction(1,a)+Fraction(2,N-a))
        attained=expression(bestA,N-bestA,1,1,1)
        assert attained == theoretical(n)[0]
        checks+=1
    print('PASS exact direct-enumeration/formula/bound checks:',checks)
    print('Critical transition:',[(n,str(theoretical(n)[0])) for n in (13,14,15,16,20)])

if __name__ == '__main__':run()
