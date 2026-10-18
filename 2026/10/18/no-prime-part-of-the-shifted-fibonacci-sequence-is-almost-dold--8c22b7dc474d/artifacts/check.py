#!/usr/bin/env python3
"""Exact finite checks for the shifted Fibonacci prime-part obstruction."""
from math import isqrt

def isprime(n):
    if n < 2: return False
    for d in range(2,isqrt(n)+1):
        if n%d==0: return False
    return True

def fib_pair_mod(n,mod):
    a,b=0,1
    for bit in bin(n)[2:]:
        c=(a*(2*b-a))%mod
        d=(a*a+b*b)%mod
        a,b=(d,(c+d)%mod) if bit=='1' else (c,d)
    return a,b

def vp_fib_index(p,k,max_e=16):
    mod=p**max_e
    f=fib_pair_mod(k,mod)[0]
    if f==0: return max_e
    e=0
    while f%p==0:
        e+=1; f//=p
    return e

def rank(p):
    a,b=0,1
    for n in range(1,2*p+10):
        a,b=b%p,(a+b)%p
        if a==0: return n
    raise AssertionError('rank not found')

def witness(p):
    if p==2: return 5,2,7
    if p==5: return 19,2,4
    r=rank(p)
    q=2
    while True:
        if isprime(q) and q%r==r-1 and q%p==1:
            break
        q+=1
    e=vp_fib_index(p,r)
    target=p**e-1
    for k in (2,4,6,8):
        assert vp_fib_index(p,q**k+1)==0,(p,q,k,'even')
        assert vp_fib_index(p,q**(k-1)+1)==e,(p,q,k,'odd')
    return q,r,target

def main():
    rows=[]
    for p in range(2,54):
        if isprime(p):
            q,r,target=witness(p)
            if p==2:
                for k in (2,4,6,8):
                    assert vp_fib_index(2,5**k+1)==0
                    assert vp_fib_index(2,5**(k-1)+1)==3
            elif p==5:
                for k in (2,12,22):
                    assert vp_fib_index(5,19**k+1)==0
                    assert vp_fib_index(5,19**(k-1)+1)==1
            rows.append((p,q,r,target))
    assert len(rows)==16
    print('CHECK_OK', 'primes',len(rows), 'q_power_pairs', sum(4 if p!=5 else 3 for p,_,_,_ in rows))
    for row in rows:print(*row,sep=',')
if __name__=='__main__':main()
