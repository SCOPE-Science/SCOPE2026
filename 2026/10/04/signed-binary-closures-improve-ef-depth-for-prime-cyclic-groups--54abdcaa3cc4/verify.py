#!/usr/bin/env python3
import math

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def build(p):
    n = p.bit_length()-1
    assert (1<<n) < p < (1<<(n+1))
    a = p-(1<<n)
    b = (1<<(n+1))-p
    direct = a.bit_count() <= b.bit_count()
    c = a if direct else b
    bits = [1<<j for j in range(n) if (c>>j)&1]
    vals = [1<<j for j in range(n+1)]
    if len(bits) >= 2:
        s = bits[0]+bits[1]
        vals.append(s)
        for z in bits[2:]:
            s += z
            vals.append(s)
    return n,a,b,direct,bits,vals

count=0
for p in range(3,20000,2):
    if not is_prime(p):
        continue
    n = p.bit_length()-1
    if p == (1<<n):
        continue
    n,a,b,direct,bits,vals = build(p)
    h=min(a.bit_count(),b.bit_count())
    assert len(vals)==n+h
    assert h <= (n+1)//2
    assert 0 not in [v%p for v in vals]
    assert len(set(v%p for v in vals))==len(vals)
    if direct:
        assert ((1<<n)+sum(bits)) % p == 0
    else:
        assert ((1<<(n+1))-sum(bits)) % p == 0
    t=(a & -a).bit_length()-1
    assert a.bit_count()+((1<<n)-a).bit_count()==n-t+1
    count += 1

for p in [7,17,31,127]:
    assert is_prime(p)
    n=p.bit_length()-1
    a=p-(1<<n); b=(1<<(n+1))-p
    assert min(a.bit_count(),b.bit_count())==1
    assert n+1 == n+min(a.bit_count(),b.bit_count())

print(f"VERIFY_OK primes={count} max_p=19999 exact_examples=7,17,31,127")
