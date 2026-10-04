#!/usr/bin/env python3
from fractions import Fraction

def ages(r,a,b):
    out=[]
    if a>1:
        out += [Fraction(r*k + ((k*b)%a), a) for k in range(1,a)]
    if b>1:
        out += [Fraction(r*k + ((k*a)%b), b) for k in range(1,b)]
    return out

def formula(r,a,b):
    vals=[]
    if a>1: vals.append(Fraction(r + (b%a), a))
    if b>1: vals.append(Fraction(r + (a%b), b))
    return min(vals) if vals else None

for r in range(2,61):
    eq=[]
    for d in range(0,r+1):
        for a in range(1,r+d+1):
            b=a+d
            vals=ages(r,a,b)
            if not vals:
                continue
            alpha=min(vals)
            assert alpha == formula(r,a,b), (r,a,b,alpha,formula(r,a,b))
            assert alpha >= 1, (r,a,b,alpha)
            terminal=(d<r and a<r+d)
            assert (alpha>1) == terminal, (r,a,b,alpha,terminal)
            if terminal:
                bound=Fraction(3*r-2,3*r-3)
                assert alpha >= bound, (r,a,b,alpha,bound)
                if alpha==bound: eq.append((a,b))
    assert eq == [(2*r-2,3*r-3)], (r,eq)
print('VERIFY_OK')
