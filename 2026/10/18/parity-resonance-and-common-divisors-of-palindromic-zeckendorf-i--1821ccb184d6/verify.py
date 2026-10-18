#!/usr/bin/env python3
"""Reproducible exact arithmetic checks for fixed-length Zeckendorf palindromes.

Independent finite enumeration supplements, but never replaces, the proof.
"""
from math import gcd


def fibonacci(n):
    f = [0, 1]
    for _ in range(2, n + 1):
        f.append(f[-1] + f[-2])
    return f[n]


def length_total(n):
    if n == 1:
        return 1
    if n % 2:
        return fibonacci((n + 1) // 2)
    return fibonacci(n // 2 - 1)


def imbalance(n):
    if n % 3 == 0:
        return length_total(n)
    return {1:-1,2:0,4:1,5:0,7:-1,8:-2,10:1,11:2}[n % 12]


def value(bits):
    F=[0,1]
    for _ in range(len(bits)+2): F.append(F[-1]+F[-2])
    return sum((bit=='1')*F[i+2] for i,bit in enumerate(bits[::-1]))


def predicted_gcd(n):
    if n==2: return None
    if n in (1,3,4,5,6): return {1:1,3:4,4:6,5:3,6:14}[n]
    return 2 if n%3==0 else 1


def direct_words(length):
    h=(length+1)//2
    for mask in range(1<<(h-1)):
        left='1'+format(mask,'0'+str(h-1)+'b') if h>1 else '1'
        bits=left+(left[-2::-1] if length%2 else left[::-1])
        if '11' not in bits:
            yield bits


def greedy_zeckendorf(n):
    F=[0,1]
    while F[-1] <= n:
        F.append(F[-1]+F[-2])
    bits=[]
    for j in range(len(F)-1,1,-1):
        x=1 if F[j]<=n else 0
        bits.append(str(x))
        if x:n-=F[j]
    assert n == 0
    return ''.join(bits).lstrip('0')


def signed_dp(n):
    if n==1:return -1
    if n==2:return 0
    h=n//2
    A,B=0,(-1 if (fibonacci(n+1)+1)%2 else 1)
    for j in range(2,h+1):
        sign=-1 if (fibonacci(n+2-j)+fibonacci(j+1))%2 else 1
        A,B=A+B,sign*A
    if n%2==0:return A
    center_sign=-1 if fibonacci(h+2)%2 else 1
    return (1+center_sign)*A+B


def main():
    nvalues=0; direct_checks=0
    for length in range(1,26):
        words=list(direct_words(length))
        vals=[value(w) for w in words]
        E=sum(n%2==0 for n in vals)
        O=len(vals)-E
        g=0
        for n in vals:g=gcd(g,n)
        assert len(vals)==length_total(length),(length, len(vals))
        assert E-O==imbalance(length),(length,E,O,imbalance(length))
        assert g==(predicted_gcd(length) or 0),(length,g,predicted_gcd(length))
        assert signed_dp(length)==E-O,(length,'matrix')
        nvalues+=len(vals)
        if length <= 22:
            top=fibonacci(length+2)
            from_greedy=[]
            for n in range(1,top):
                b=greedy_zeckendorf(n)
                if len(b)==length and b==b[::-1]:
                    from_greedy.append(n)
            assert from_greedy==sorted(vals),(length,from_greedy[:5],sorted(vals)[:5])
            direct_checks+=top-1
    for length in range(1,1001):
        assert signed_dp(length)==imbalance(length),length
    for length in range(13,400):
        F=lambda i:fibonacci(i)
        P={k:F(k)+F(length+3-k) for k in range(4,8)}
        assert P[4]-P[5]-P[6]==-10
        assert P[5]-P[6]-P[7]==-16
        B=F(length+1)+1
        if length%3==2:assert B%2
        if length%3==1:assert (B+P[4])%2
    print('ZECKENDORF_PALINDROME_EXACT_OK lengths=1..25 words=',nvalues,
          'independent_greedy=',direct_checks, 'matrix_lengths=1000 witnesses=387')

if __name__=='__main__': main()
