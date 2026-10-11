#!/usr/bin/env python3
"""Finite sanity checks for the continuant extremum used in the accompanying proof.

The infinite bound is proved in RESULT.md; this script only exhausts positive
compositions through a stated cutoff and checks the explicit sharp witnesses.
"""

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def continuant(parts):
    if not parts:
        return 1
    km2,km1=1,parts[0]
    for a in parts[1:]:
        km2,km1=km1,a*km1+km2
    return km1

def compositions(n):
    if n==0:
        yield ()
        return
    for mask in range(1 << (n-1)):
        out=[]
        run=1
        for i in range(n-1):
            if (mask >> i) & 1:
                out.append(run)
                run=1
            else:
                run+=1
        out.append(run)
        yield tuple(out)

def M(c):
    if c % 3 == 2:
        return fib(c+1)-fib(c-4)
    return fib(c+1)

def witness(c):
    if c == 3:
        return (3,)
    if c % 3 != 2:
        return (2,) + (1,)*(c-4) + (2,)
    if c == 5:
        return (3,2)
    return (2,2) + (1,)*(c-6) + (2,)

for c in range(3,19):
    vals=[continuant(a) for a in compositions(c) if continuant(a) % 2 == 1]
    assert max(vals) == M(c), (c,max(vals),M(c))
    w=witness(c)
    assert sum(w)==c
    assert continuant(w)==M(c), (c,w,continuant(w),M(c))
    assert continuant(w)%2==1
print('VERIFY_OK c=3..18 exact_odd_continuant_max')
