#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, lcm

def age_ok(r,a,b,terminal):
    # Local Reid--Tai on the two non-smooth heavy charts.
    for m,c in ((a,b),(b,a)):
        if m==1:
            continue
        for k in range(1,m):
            age=Fraction(r*k + ((k*c) % m), m)
            if terminal:
                if not (age > 1):
                    return False
            else:
                if not (age >= 1):
                    return False
    return True

def triangle(r,a,b,terminal):
    d=b-a
    if terminal:
        return 0 <= d <= r-1 and 1 <= a <= r+d-1
    return 0 <= d <= r and 1 <= a <= r+d

def expected_max(r,terminal):
    if not terminal:
        return (2*r-1)*(3*r-1), {(2*r-1,3*r-1)}
    if r==2:
        return 6, {(2,3)}
    return (2*r-3)*(3*r-4), {(2*r-3,3*r-4)}

for r in range(2,61):
    # Check a box that extends beyond both feasible triangles.
    for a in range(1,2*r+4):
        for b in range(a,3*r+6):
            for terminal in (False,True):
                x=age_ok(r,a,b,terminal)
                y=triangle(r,a,b,terminal)
                assert x==y,(r,a,b,terminal,x,y)
    for terminal in (False,True):
        vals=[]
        for a in range(1,2*r+2):
            for b in range(a,3*r+2):
                if triangle(r,a,b,terminal):
                    vals.append((lcm(a,b),a,b))
        best=max(v[0] for v in vals)
        pairs={(a,b) for L,a,b in vals if L==best}
        exp,ep=expected_max(r,terminal)
        assert best==exp,(r,terminal,best,exp)
        assert pairs==ep,(r,terminal,pairs,ep)
        # Formula lcm(a,b)=a(a+d)/gcd(a,d).
        for L,a,b in vals:
            d=b-a
            assert L==a*(a+d)//gcd(a,d)
print('VERIFY_OK')
