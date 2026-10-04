#!/usr/bin/env python3
from math import gcd

def primes_upto(n):
    bs = bytearray(b"\x01")*(n+1)
    if n >= 0: bs[0] = 0
    if n >= 1: bs[1] = 0
    p = 2
    while p*p <= n:
        if bs[p]:
            start = p*p
            bs[start:n+1:p] = b"\x00"*(((n-start)//p)+1)
        p += 1
    return [i for i in range(2,n+1) if bs[i]]

P = primes_upto(1_000_000)

def counts(X):
    total = duff = bad = 0
    for i,p in enumerate(P):
        if p*p >= X:
            break
        for q in P[i+1:]:
            if p*q > X:
                break
            total += 1
            sig = (p+1)*(q+1)
            actual = (gcd(p*q, sig) == 1)
            local = (p != 2 and (q+1) % p != 0)
            assert actual == local
            if actual:
                duff += 1
            else:
                bad += 1
    return total,duff,bad

expected = {
    10_000:(2600,1541,1059),
    100_000:(23313,15143,8170),
    1_000_000:(209867,143981,65886),
}
for X,e in expected.items():
    got = counts(X)
    assert got == e, (X,got,e)
    print(f"X={X} total={got[0]} duffinian={got[1]} exceptional={got[2]}")
print("VERIFY_OK")
