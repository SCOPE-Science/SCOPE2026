#!/usr/bin/env python3
"""Independent finite-extension cross-check, not the proof of geometric smoothness.

Tests gradient zeroes over F2, F4, F8, and F16 using explicit irreducible
polynomials. These samples agree with the rigorous Macaulay rank test.
"""
from itertools import product
from collections import Counter
M3=[(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),
    (1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3)]
M2=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
POLY={1:0b11,2:0b111,3:0b1011,4:0b10011}

def mult(x,y,m):
    r=0
    while y:
        if y&1:r^=x
        x<<=1
        if x&(1<<m):x^=POLY[m]
        y>>=1
    return r

def field_pow(x,n,m):
    out=1
    for _ in range(n):out=mult(out,x,m)
    return out

def points(m):
    q=1<<m
    for y,z in product(range(q), repeat=2):yield(1,y,z)
    for z in range(q):yield(0,1,z)
    yield(0,0,1)

def derivative_mask(f,axis):
    ans=0
    for i,mon in enumerate(M3):
        if ((f>>i)&1) and (mon[axis]%2):
            q=list(mon);q[axis]-=1
            ans^=1<<M2.index(tuple(q))
    return ans

# In contrast with the Macaulay computation, this checks gradient evaluations
# directly in four explicit extension fields.
BAD=set()
for m in (1,2,3,4):
    evals=[]
    for pt in points(m):
        ev=[]
        for mon in M2:
            t=1
            for x,e in zip(pt,mon):t=mult(t,field_pow(x,e,m),m)
            ev.append(t)
        evals.append(ev)
    for f in range(1,1024):
        if f in BAD:continue
        ds=[derivative_mask(f,axis) for axis in range(3)]
        if any(all(__import__('functools').reduce(int.__xor__,
                        (ev[i] for i in range(6) if (d>>i)&1),0)==0
                   for d in ds) for ev in evals):
            BAD.add(f)
    print('through degree',m,'singular detected',len(BAD))
assert len(BAD)==1023-336
print('independently retained smooth cubics',1023-len(BAD))
