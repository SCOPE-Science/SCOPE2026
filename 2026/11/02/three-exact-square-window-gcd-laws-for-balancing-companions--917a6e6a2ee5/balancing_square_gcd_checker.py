#!/usr/bin/env python3
"""Exact integer checks for three balancing-square window gcd identities.

These are finite reproducibility checks, not a replacement for the proof.
"""
from math import gcd
from functools import reduce

def sequences(N):
    B = [0, 1]
    C = [1, 3]
    c = [-1, 1]
    for a in (B, C, c):
        for _ in range(N-1):
            a.append(6*a[-1]-a[-2])
    return B, C, c

def check(max_k=300, windows=25):
    B,C,c = sequences(max_k+windows+4)
    assert all(C[n]**2-8*B[n]**2 == 1 for n in range(max_k+windows+2))
    assert all(B[2*n]==2*B[n]*C[n] for n in range(1,(max_k+windows)//2+1))
    assert all(c[n]**2==(C[2*n-1]-1)//2 for n in range(1, (max_k+windows)//2))
    assert all((B[n] - (3*n if n%2==0 else n))%16 == 0 for n in range(max_k+windows+2))
    assert all(C[n]%16 == (1 if n%2==0 else 3) for n in range(max_k+windows+2))
    for k in range(1,max_k+1):
        h=gcd(k,B[k])
        targets=(h//2 if k%2==0 else h,h,3*h if k%2 and k%3==0 else h)
        for A,target in zip((B,C,c),targets):
            total=sum(x*x for x in A[1:k+1])
            d=total
            for n in range(windows-1):
                total += A[n+k+1]**2-A[n+1]**2
                d=gcd(d,total)
            assert d==target,(k, A[:3], d,target)
        # Sum of squares base-point identities.
        assert 16*sum(x*x for x in B[1:k+1]) == B[k]*C[k+1]-k
        assert 2*sum(x*x for x in C[1:k+1]) == B[k]*C[k+1]+k
        assert 2*sum(x*x for x in c[1:k+1]) == B[k]*C[k]-k
        # GCD of all window differences as proved symbolically.
        db=B[k]*(6 if k%2==0 else 1)
        dC=8*db
        dc=8*B[k]*(6 if k%2 else 1)
        assert reduce(gcd,(B[n+k+1]**2-B[n+1]**2 for n in range(2)),0)==db
        assert reduce(gcd,(C[n+k+1]**2-C[n+1]**2 for n in range(2)),0)==dC
        assert reduce(gcd,(c[n+k+1]**2-c[n+1]**2 for n in range(2)),0)==dc
    print(f"PASS: {max_k} lengths x 3 sequences x {windows} windows; "
          "sum identities and difference-gcd reductions confirmed.")

if __name__=="__main__":
    check()
