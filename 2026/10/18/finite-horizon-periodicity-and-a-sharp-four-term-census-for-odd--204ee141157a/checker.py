#!/usr/bin/env python3
"""Independent exact-integer checks for odd-greedy finite-horizon classes."""
from math import lcm
from fractions import Fraction


def odd_step(A, B):
    assert A > 0 and B > A and B % 2 == 1
    u = (B + A - 1) // A
    if u % 2 == 0:
        u += 1
    return A*u-B, B*u, u


def odd_length_within(a, d, max_steps):
    A,B=a,d
    for j in range(1, max_steps+1):
        A,B,_ = odd_step(A,B)
        if A == 0:
            return j
    return None


def period(a,h):
    p=1
    for j in range(h):
        upper=(2**j)*a
        L=1
        for t in range(1,upper+1):
            L=lcm(L,t)
        p *= 2*L
    return p


def run():
    classes={7,35,47,55}
    count = 0
    for d in range(5,100006,2):
        got=odd_length_within(2,d,4)
        expect=2 if (d%4==1 or d%12==3) else (4 if d%60 in classes else None)
        assert got==expect,(d,got,expect)
        count += 1
    print('PASS exact-length 2/4 and other cases over',count,'odd denominators')
    # Verify unreduced state invariance for translations by an explicit, nonminimal period.
    for a,h in ((1,2),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)):
        p=period(a,h)
        for d in range(a+1, 91):
            if d%2==0: continue
            left=odd_length_within(a,d,h)
            right=odd_length_within(a,d+p,h)
            assert left==right,(a,h,d,p,left,right)
        print('PASS periodicity',a,h,'P digits',len(str(p)))
    for d in range(5,500,2):
        A,B=2,d
        for step in range(4):
            if A==0: break
            old=A
            A,B,u=odd_step(A,B)
            assert 0<=A<2*old and u%2==1
    for p in (12,20,30):
        assert (7%60 in classes)!=((7+p)%60 in classes)
    print('PASS minimal period 60 and numerator bounds')
    # A separate reduced-Fraction implementation tests the unreduced recurrence.
    for a in range(1, 10):
        for d in range(a+1, 201):
            if d % 2 == 0: continue
            remaining = Fraction(a, d)
            exact = None
            for step in range(1, 6):
                N, D = remaining.numerator, remaining.denominator
                u = (D + N - 1) // N
                if u % 2 == 0: u += 1
                remaining -= Fraction(1, u)
                if remaining == 0:
                    exact = step
                    break
            assert exact == odd_length_within(a, d, 5), (a, d, exact)
    print('PASS reduced Fraction implementation, a=1..9, d<=200')

if __name__=='__main__':
    run()
