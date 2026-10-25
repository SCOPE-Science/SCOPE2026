#!/usr/bin/env python3
"""Exact independent base-b four-digit inverse-branch checks."""
from collections import Counter
from math import floor

def expected(b):
    out={}
    for u in range(1,b):
        for v in range(u+1):
            value=(b**3-1)*u+(b*b-b)*v
            if v==0: m=(b-u)*(12*u-4)
            elif v==u: m=6*(b-u)
            else: m=24*(b-u)*(u-v)
            assert value not in out
            out[value]=m
    return out

def direct(b):
    freq=Counter()
    for x in range(b**4):
        digits=[]; y=x
        for _ in range(4):
            digits.append(y%b); y//=b
        d=sorted(digits)
        hi=sum(d[i]*b**i for i in range(4))
        lo=sum(d[i]*b**(3-i) for i in range(4))
        freq[hi-lo]+=1
    del freq[0]
    return dict(freq)

def main():
    for b in range(2,23):
        exp=expected(b)
        obs=direct(b)
        assert obs==exp,(b,obs,exp)
        assert len(exp)==(b-1)*(b+2)//2
        assert sum(exp.values())==b**4-b
        maxf=max(exp.values())
        assert maxf==(8 if b==2 else 24*((b-1)**2//4)),(b,maxf)
        assert list(exp.values()).count(maxf)==(1 if b%2 else (1 if b==2 else 2)),b
    print('VERIFY_OK: 21 bases, complete four-digit direct-image and fiber enumeration, support, maximum and maximizing multiplicities')
if __name__=='__main__': main()
