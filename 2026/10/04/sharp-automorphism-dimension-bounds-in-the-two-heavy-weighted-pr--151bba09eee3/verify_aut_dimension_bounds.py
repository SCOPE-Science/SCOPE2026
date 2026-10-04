#!/usr/bin/env python3
from math import comb
from fractions import Fraction

def B(r,m):
    return comb(r+m-1,r-1)

def H(r,a,b,m):
    total=0
    for i in range(m//a+1):
        rem=m-i*a
        for j in range(rem//b+1):
            total += B(r,rem-j*b)
    return total

def autdim(r,a,b):
    return r*H(r,a,b,1)+H(r,a,b,a)+H(r,a,b,b)-1

def can_triangle(r,a,b):
    d=b-a
    return d<=r and a<=r+d

def ter_triangle(r,a,b):
    d=b-a
    return d<r and a<r+d

def age_ok(r,a,b,terminal=False):
    for q,other in ((a,b),(b,a)):
        if q<=1:
            continue
        for k in range(1,q):
            age=Fraction(r*k,q)+Fraction((k*other)%q,q)
            if terminal:
                if age<=1:
                    return False
            elif age<1:
                return False
    return True

def can_closed(r):
    return r*r+comb(3*r-1,r-1)+comb(4*r-1,r-1)+comb(2*r-1,r-1)+1

def ter_closed(r):
    return r*r+comb(3*r-3,r-1)+comb(4*r-4,r-1)+comb(2*r-2,r-1)+1

for r in range(2,31):
    can=[]; ter=[]
    # The triangles themselves bound b by 3r and 3r-3, so this box is exhaustive.
    for a in range(1,2*r+1):
        for b in range(a,3*r+1):
            c=can_triangle(r,a,b)
            t=ter_triangle(r,a,b)
            assert age_ok(r,a,b,False)==c, (r,a,b,'canonical')
            assert age_ok(r,a,b,True)==t, (r,a,b,'terminal')
            if c: can.append((autdim(r,a,b),a,b))
            if t: ter.append((autdim(r,a,b),a,b))
    mc=max(x[0] for x in can)
    eqc=[x[1:] for x in can if x[0]==mc]
    assert mc==can_closed(r)
    assert eqc==[(2*r,3*r)]
    mt=max(x[0] for x in ter)
    eqt=[x[1:] for x in ter if x[0]==mt]
    if r==2:
        assert mt==15 and eqt==[(1,1),(1,2)]
    else:
        assert mt==ter_closed(r)
        assert eqt==[(2*r-2,3*r-3)]
print('VERIFY_OK')
