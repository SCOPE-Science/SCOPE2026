#!/usr/bin/env python3
"""Corroborative checks for the commuting correlated zero-Stein-rate formulas."""
import itertools, math

def g(c, q, k):
    return c + (1.0-c)*(q**k)

def compositions(n):
    if n == 0:
        yield ()
        return
    for first in range(1, n+1):
        for rest in compositions(n-first):
            yield (first,) + rest

def extreme_overlap(c, q, blocks, mask):
    out = 1.0
    for k, zeta in zip(blocks, mask):
        out *= g(c,q,k) if zeta else q**k
    return out

def check():
    params=[(0.2,0.3),(0.35,0.8),(0.7,0.15),(0.9,0.95)]
    tol=2e-12
    for c,q in params:
        assert 0<c<1 and 0<q<1
        for a in range(1,9):
            for b in range(1,9):
                lhs=g(c,q,a+b)-g(c,q,a)*g(c,q,b)
                rhs=c*(1-c)*(1-q**a)*(1-q**b)
                assert abs(lhs-rhs) < tol
                assert lhs > -tol
        for n in range(1,9):
            target=g(c,q,n)
            mx=0.0
            for comp in compositions(n):
                for mask in itertools.product([False,True], repeat=len(comp)):
                    mx=max(mx,extreme_overlap(c,q,comp,mask))
            assert abs(mx-target) < tol
            for delta in [0.0,0.1,0.7,1.3,1.9,2.0]:
                lower=max(1.0,(1.0-delta/2.0)/target)
                s=min(1.0,delta/(2.0*(1.0-target)))
                alpha=1.0-s*(1.0-target)
                constructed=max(alpha/target,s)
                assert abs(lower-constructed) < tol
                distance=2.0*s*(1.0-target)
                assert distance <= delta+tol
            for eps in [0.0,0.2,0.8]:
                beta=(1.0-eps)*target
                assert 0.0 <= beta <= 1.0
    print("VERIFY_OK")

if __name__ == '__main__':
    check()
