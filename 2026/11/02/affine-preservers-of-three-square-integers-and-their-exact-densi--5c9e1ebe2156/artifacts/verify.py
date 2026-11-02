#!/usr/bin/env python3
"""Exact small-case tests of affine three-square preservation."""
from math import isqrt

def good(n):
    if n<0: return False
    while n and n%4==0: n//=4
    return n%8!=7

def allowed(a,b):
    assert a>=1 and b>=0
    while a%4==0 and b%4==0:
        a//=4; b//=4
    if b==0: return a%8==1
    if a%4: return False
    if b%4 in (1,2): return True
    return a%8==0 and b%8==3

def sieve_3square(n):
    out=bytearray(n+1)
    sq=[i*i for i in range(isqrt(n)+1)]
    for s in sq:
        for t in sq:
            if s+t>n: break
            for u in sq:
                if s+t+u>n: break
                out[s+t+u]=1
    return out

if __name__=='__main__':
    limit=1200
    sat=sieve_3square(limit)
    assert all(bool(sat[n])==good(n) for n in range(limit+1))
    pairs=0; positives=0; negative=0
    for a in range(1,129):
        for b in range(0,129):
            expect=allowed(a,b)
            observed=True
            for n in range(0,1600):
                if good(n) and not good(a*n+b):
                    observed=False
                    break
            assert observed==expect,(a,b,expect,observed,n)
            pairs+=1
            positives+=expect
            negative+=not expect
    for X in (1,2,4,8,16,32,64,128,256,512):
        # exact by residue bucket + recursion against finite direct enumeration
        if X<=256:
            direct=sum(allowed(a,b) for a in range(1,X+1) for b in range(1,X+1))
            b12=sum(b%4 in (1,2) for b in range(1,X+1))
            b3=sum(b%8==3 for b in range(1,X+1))
            sub=sum(allowed(a,b) for a in range(1,X//4+1) for b in range(1,X//4+1))
            rhs=(X//4)*b12+(X//8)*b3+sub
            assert rhs==direct,(X,rhs,direct)
    print(f'VERIFY_OK tested_pairs={pairs} predicted_good={positives} predicted_bad={negative} three_square_sieve_through={limit} input_test_range=0..1599 exact_recursion_X_through=256')
