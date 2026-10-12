#!/usr/bin/env python3
from math import factorial, isqrt
FAC=[factorial(i) for i in range(0,1001)]

def predicted(a,c):
    if (a,c)==(1,0): return 2
    if c in (1,2): return FAC[a-1] if a>=4 else None
    if c>=3 and a<=c:
        if c%a==0 and (a,c)!=(3,3): return FAC[a-1]+(FAC[c]-c)//a
        return None
    if c>=3 and a>c and (FAC[c]-c)%a==0:
        return FAC[a-1]+(FAC[c]-c)//a
    return None

def direct_pair(a,c):
    num=FAC[a]+FAC[c]-c
    if num%a: return None
    b=num//a
    return b if b>=2 and a<b and c<b and a*b+c==FAC[a]+FAC[c] else None

pairs=0
for a in range(1,61):
    for c in range(0,61):
        pairs+=1
        assert direct_pair(a,c)==predicted(a,c),(a,c,direct_pair(a,c),predicted(a,c))

obs=[]
for b in range(2,101):
    for a in range(1,b):
        for c in range(0,b):
            if a*b+c==FAC[a]+FAC[c]: obs.append((b,a,c))
want=[]
for a in range(1,101):
    for c in range(0,100):
        pb=predicted(a,c)
        if pb is not None and pb<=100: want.append((pb,a,c))
assert sorted(obs)==sorted(want),(set(obs)-set(want),set(want)-set(obs))

def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return out
for c in range(4,7):
    # brute leading digits through the largest possible class-4 divisor
    cap=FAC[c]-c
    actual=sum(1 for a in range(1,cap+1) if predicted(a,c) is not None)
    expected=len(divisors(c))+sum(1 for a in divisors(cap) if a>c)
    assert actual==expected,(c,actual,expected)
print('VERIFY_OK',f'digit_pairs={pairs}',f'base_window=2..100',f'observed={len(obs)}',f'fixed_trailing=4..6',f'first={sorted(obs)[:12]}')
