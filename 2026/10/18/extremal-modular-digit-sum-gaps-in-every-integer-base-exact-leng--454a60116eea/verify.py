#!/usr/bin/env python3
"""Independent finite checks for the extremal modular digit-sum run theorem."""
from fractions import Fraction

def digit_sum(n,b):
    s=0
    while n:
        n,r=divmod(n,b)
        s+=r
    return s

def trailing(n,d,b):
    t=0
    while n and n%b==d:
        n//=b
        t+=1
    return t

def prediction(start,b):
    if start%b!=1 or start<1:
        return False
    q=(start-1)//b+1
    m=b+1
    if b%2:
        return (digit_sum(q-1,b)%m==0
                and digit_sum(q,b)%m==1
                and digit_sum(q+1,b)%m==2)
    if q%b != b-1:
        return False
    t=trailing(q,b-1,b)
    h=(q+1)//(b**t)
    return t%m==b//2 and h%b!=0 and digit_sum(h-1,b)%m==0

def density(b):
    m=b+1
    if b%2==0:
        return Fraction(b-1,m*b*b) * Fraction(1,b**(b//2)) / (1-Fraction(1,b**m))
    k=m//2
    return (Fraction(b-2,m*b*b)
            +Fraction(2*(b-1),m*b*b*(b**k-1)))

def checks():
    all_counts=0
    for b in range(2,13):
        m=b+1
        L=(4 if b%2==0 else 3)*b-2
        N= max(15000,min(500000,b**6+1500))
        d=[0]*(N+2)
        for n in range(1,N+2):
            d[n]=d[n//b]+n%b
        pref=[0]*(N+2)
        for n in range(1,N+2):
            pref[n]=pref[n-1]+int(d[n]%m==0)
        ext_count=0
        for a in range(1,N-L+2):
            actual=(pref[a+L-1]-pref[a-1]==0)
            if actual!=prediction(a,b):
                raise AssertionError(('maximal start mismatch',b,a,L,actual))
            if actual:
                ext_count+=1
        for a in range(1,N-L+1):
            if pref[a+L]-pref[a-1]==0:
                raise AssertionError(('too long run',b,a,L+1))
        all_counts += (N-L+1)
        print('base',b,'length',L,'checked_starts',N-L+1,
              'longest_count',ext_count,'density_limit',density(b))
    for b in range(2,31):
        L=(4 if b%2==0 else 3)*b-2
        if b%2==0:
            q=b**(b//2)-1
            start=b*(q-1)+1
        else:
            start=1
        if start<1 or not prediction(start,b):
            raise AssertionError(('witness formula',b,start))
        if any(digit_sum(start+j,b)%(b+1)==0 for j in range(L)):
            raise AssertionError(('witness contents',b,start))
        if digit_sum(start-1,b)%(b+1)!=0 and start>1:
            raise AssertionError(('left boundary',b))
        if digit_sum(start+L,b)%(b+1)!=0:
            raise AssertionError(('right boundary',b))
    print('PASS: full interval/prediction comparisons:',all_counts,
          'and explicit witnesses for 29 bases')

if __name__=='__main__':
    checks()
