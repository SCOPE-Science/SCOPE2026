#!/usr/bin/env python3
"""Exact modular sanity checks for a positive-density prime-divisibility theorem."""

def h(r,k):
    assert r>=2 and k>=1
    return sum((-r)**j for j in range(2*k+1))

def is_prime(n):
    if n<2: return False
    d=2
    while d*d<=n:
        if n%d==0: return False
        d+=1
    return True

def order(a,p):
    assert is_prime(p) and a%p
    t=a%p; d=1
    while t!=1:
        t=t*a%p
        d+=1
        assert d<=p-1
    return d

assert pow(4,4,29)==(-5)%29
assert h(5,3)==13021 and h(5,3)%29==0
assert h(29,2)==683705 and h(29,2)%5==0
seen=0
for q in range(29,30000,40):
    if not is_prime(q): continue
    if pow(-5,(q-1)//4,q)!=1: continue
    d=order(-5,q)
    assert d%2==1 and d>=3
    a=(d-1)//2
    assert h(5,a)%q==0
    assert h(q,2)%5==0
    seen+=1
assert seen>2
print('VERIFY_OK',seen)
