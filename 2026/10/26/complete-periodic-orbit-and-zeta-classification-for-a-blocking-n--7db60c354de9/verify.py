"""Finite exact checks for the cyclic rule-56528 orbit classification.
This is a reproducibility supplement; the universal claims follow from the proof.
"""
from math import gcd

ONES = {int(w, 2) for w in ('0100','0110','0111','1010','1011','1100','1110','1111')}
checks = 0

def check(cond, desc):
    global checks
    checks += 1
    if not cond: raise AssertionError(desc)

def next_rule(x,n):
    out=0
    for i in range(n):
        bits=8*((x>>((i-1)%n))&1)+4*((x>>i)&1)+2*((x>>((i+1)%n))&1)+((x>>((i+2)%n))&1)
        out|=(bits in ONES)<<i
    return out

def next_conservation(x,n):
    out=0
    for i in range(n):
        a=(x>>((i-1)%n))&1;b=(x>>i)&1;c=(x>>((i+1)%n))&1;d=(x>>((i+2)%n))&1
        out|=(b-b*(1-c)*d+a*(1-b)*c)<<i
    return out

def contains(x,n,w):
    return any(all(((x>>((i+j)%n))&1)==int(c) for j,c in enumerate(w)) for i in range(n))

def shift(x,n):
    return sum(((x>>((i+1)%n))&1)<<i for i in range(n))

def a(n): return sum(not contains(x,n,'101') for x in range(1<<n))
def l(n): return sum(not contains(x,n,'00') for x in range(1<<n))

for n in range(1,13):
    A=a(n); L=l(n)
    check(A==sum(next_rule(x,n)==x for x in range(1<<n)),('fixed',n))
    if n>=4:check(A==2*a(n-1)-a(n-2)+a(n-3),('a-recurrence',n))
    if n>=3:check(L==l(n-1)+l(n-2),('lucas',n))
    for x in range(1<<n):
        y=next_rule(x,n)
        check(y==next_conservation(x,n),('truth',n,x))
        check(x.bit_count()==y.bit_count(),('conserved',n,x))
        if not contains(x,n,'00'):
            check(y==shift(x,n),('travel',n,x))
        else:
            for t in range(n):y=next_rule(y,n)
            check(y==next_rule(y,n),('absorb',n,x))
    for t in range(1, min(9,n+2)):
        points=0
        for x in range(1<<n):
            y=x
            for _ in range(t):y=next_rule(y,n)
            if y==x:points+=1
        check(points==A-1+l(gcd(n,t)),('fixed iterate',n,t,points,A-1+l(gcd(n,t))))
print(f'PASS {checks} exact-integer checks over ring sizes 1 through 12')
