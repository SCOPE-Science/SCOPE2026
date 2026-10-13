#!/usr/bin/env python3
"""Exact modular arithmetic checks for square multinomial sums.
Scientific object: S_L^(h)(n), sum of h-th powers of multinomial coefficients over all compositions of n into L nonnegative parts.
No packages besides Python standard library.
"""
from math import comb, factorial
from collections import Counter

LIMIT=512
L_MAX=32

# Direct coefficient triangle reduced modulo 8, independent of digit formula.
C = [[1]]
for n in range(1,LIMIT+1):
    prev=C[-1]
    C.append([1]+[(prev[k-1]+prev[k])%8 for k in range(1,n)]+[1])

def predicted(L,n,h=2):
    s=n.bit_count()
    if h>=4 and h%2==0:
        return pow(L,s,8)
    if h!=2: raise ValueError('only even heights >=2')
    u=pow(L,s,8)
    for i in range(max(n.bit_length()-1,0)):
        if (n>>(i+1))&1:
            b=(n>>i)&1
            u+=4*comb(L,2+b)*pow(L,s-1-b,8)
    return u%8

def simplified(L,n):
    s=n.bit_count()
    if L&1:
        return (pow(L,s,8)+4*((L-1)//2%2)*(s-(n&1)))%8
    is_nontrivial_power=(n>=2 and (n&(n-1))==0)
    return (pow(L,s,8)+4*(comb(L,2)%2)*is_nontrivial_power)%8

for height in (2,4,6,8):
    prev=[1]*(LIMIT+1) # level 1
    for L in range(1,L_MAX+1):
        if L>1:
            current=[]
            for n in range(LIMIT+1):
                current.append(sum(pow(C[n][k],height,8)*prev[n-k] for k in range(n+1))%8)
            prev=current
        for n,actual in enumerate(prev):
            assert actual==predicted(L,n,height),(height,L,n,actual,predicted(L,n,height))
            if height==2:
                assert actual==simplified(L,n),(L,n,actual,simplified(L,n))
    print(f'CHECK DP_HEIGHT={height} levels=1..{L_MAX} indices=0..{LIMIT} PASS')

# Exact brute factorial enumeration for first values, not using coefficient DP.
def comp(n,L):
    if L==1:
        yield (n,)
    else:
        for t in range(n+1):
            for z in comp(n-t,L-1):
                yield (t,)+z
for L in range(1,7):
    for n in range(0,11):
        total=0
        f=factorial(n)
        for t in comp(n,L):
            # Compute exact multinomial independently of the modular recurrence.
            denom=1
            for v in t: denom*=factorial(v)
            mult=f//denom
            total+=mult*mult
        assert total%8==predicted(L,n)
print('CHECK BRUTE_EXACT levels=1..6 indices=0..10 PASS')

# The one-carry count is independently enumerated from exact multinomial coefficients.
for L in range(1,7):
    for n in range(0,13):
        count=0
        fn=factorial(n)
        for t in comp(n,L):
            den=1
            for v in t: den*=factorial(v)
            mult=fn//den
            if mult%4==2: count+=1
        s=n.bit_count()
        formula=sum(comb(L,2+((n>>i)&1))*L**(s-1-((n>>i)&1)) for i in range(max(n.bit_length()-1,0)) if (n>>(i+1))&1)
        assert count==formula,(L,n,count,formula)
print('CHECK ONE_CARRY_EXACT levels=1..6 indices=0..12 PASS')

# For odd levels 3 mod 4, exact equidistribution on dyadic blocks.
for L in (3,7,11,15,19,23,27,31):
    for k in range(2,11):
        census=Counter(predicted(L,n) for n in range(1<<k))
        assert census==Counter({1:1<<(k-2),3:1<<(k-2),5:1<<(k-2),7:1<<(k-2)}),(L,k,census)
print('CHECK EQUIPARTITION levels=3,7,...31 dyadic_exponents=2..10 PASS')
print('VERIFY_OK all_checks_passed')
