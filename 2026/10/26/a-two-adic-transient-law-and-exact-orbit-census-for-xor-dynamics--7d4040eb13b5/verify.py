#!/usr/bin/env python3
"""Independent exact arithmetic and state checks for binary XOR dynamics on wheels.
No external modules are needed. A wheel has n rim vertices plus hub.
"""
from collections import Counter
from math import gcd


def pdeg(a):
    return a.bit_length() - 1


def pmul(a, b):
    c=0
    while b:
        if b & 1: c ^= a
        b >>= 1; a <<= 1
    return c


def ppow(a, k):
    out=1
    while k:
        if k & 1: out=pmul(out,a)
        a=pmul(a,a); k >>= 1
    return out


def pdivmod(a,b):
    if not b: raise ZeroDivisionError
    q=0
    while a and pdeg(a)>=pdeg(b):
        sh=pdeg(a)-pdeg(b)
        q ^=1<<sh; a^=b<<sh
    return q,a


def pgcd(a,b):
    while b:
        a,b=b,pdivmod(a,b)[1]
    return a


def qpoly(n):
    k=n & -n
    q,rem=pdivmod((1<<n)|1, ppow(0b11,k))
    assert rem==0 and (n//k)%2==1
    return k,q


def wheel(n):
    mask=(1<<n)-1
    return [ (1<<n)|(1<<((i-1)%n))|(1<<((i+1)%n)) for i in range(n)] + [mask]


def compose(A,B):
    return [xor_selected(row,B) for row in A]


def xor_selected(row,B):
    y=0
    while row:
        a=row&-row; y^=B[a.bit_length()-1]; row^=a
    return y


def ranks(A,cap=36):
    n=len(A);cur=[1<<i for i in range(n)];out=[]
    for t in range(cap+1):
        out.append(rank(cur));cur=compose(cur,A)
    return out


def rank(rows):
    piv={}
    for row in rows:
        while row:
            i=row.bit_length()-1
            if i in piv: row^=piv[i]
            else: piv[i]=row;break
    return len(piv)


def theoretical_rank(n,t):
    k=n & -n
    if k==1:return n+1
    if t==0:return n+1
    if t==1:return n if k==2 else n-2
    if t==2:return n-1 if k==2 else n-3 if k==4 else n-4
    return n-min(2*t,k)


def fixed_points(n,t):
    k,q=qpoly(n)
    poly=ppow(0b101,t)^(1<<t)
    deg=pdeg(pgcd(q,poly))
    return 1 << (deg+(1 if (n%2 and t%2) else 2 if n%2 else 0))


def update(n,state):
    rows=wheel(n)
    ans=0
    for i,mask in enumerate(rows):
        if (state&mask).bit_count()&1: ans|=1<<i
    return ans


def brute(n):
    counts=Counter(); visited=set()
    for initial in range(1<<(n+1)):
        if initial in visited: continue
        hist={}; seq=[];x=initial
        while x not in hist:
            hist[x]=len(seq);seq.append(x);x=update(n,x)
        j=hist[x]; period=len(seq)-j
        # only record each starting point's true preperiod, not just orbit forward
        for i,s in enumerate(seq):
            counts['state '+str(s)]= (max(j-i,0),period)
            visited.add(s)
    tuples={x:counts['state '+str(x)] for x in range(1<<(n+1))}
    by_preperiod=Counter(pre for pre,per in tuples.values())
    by_period=Counter(per for pre,per in tuples.values() if pre==0)
    return by_preperiod,by_period


def main():
    nrank=0; nfixed=0; nbrute=0
    for n in range(3,61):
        rs=ranks(wheel(n), min(35,max(12,n//2+3)))
        for t,observed in enumerate(rs):
            expected=theoretical_rank(n,t)
            assert observed==expected,('rank',n,t,observed,expected)
            nrank+=1
        if n%2==0:
            inf=n-(n&-n)
            assert rs[-1]==inf
        for t in range(1,21):
            A=wheel(n);p=[1<<i for i in range(n+1)]
            for j in range(t):p=compose(p,A)
            T=[p[i]^(1<<i) for i in range(n+1)]
            direct=1<<(n+1-rank(T))
            predicted=fixed_points(n,t)
            assert direct==predicted,('fixed',n,t,direct,predicted)
            nfixed+=1
    for n in range(3,11):
        pre,period=brute(n)
        k=n&-n
        r_inf=n+1 if n%2 else n-k
        T=0 if n%2 else 3 if k in(2,4) else k//2
        total=sum(v for v in pre.values())
        assert total==(1<<(n+1)), (n, total)
        assert max(pre)==T,(n,pre,T)
        before=0
        for t in range(T+1):
            at_most=1<<(n+1-theoretical_rank(n,t)+r_inf)
            exact=at_most-before
            assert exact==pre[t],('preperiod',n,t,exact,pre[t])
            before=at_most
        period_total=sum(period.values())
        assert period_total==(1<<r_inf),(n,period_total,r_inf)
        for t in range(1,15):
            actual=sum(v for p,v in period.items() if t%p==0)
            assert actual==fixed_points(n,t),('period',n,t,actual,fixed_points(n,t))
        nbrute+=1
    print(f'VERIFY_OK rank_cases={nrank} fixed_cases={nfixed} fully_enumerated_wheels={nbrute}')
    for n in (3,4,5,6,8,10,12,16,24,32):
        k=n&-n
        print(f'n={n} reversible={n%2==1} recurrent_states={2**(n+1 if n%2 else n-k)} '
              f'longest_transient={0 if n%2 else 3 if k<=4 else k//2} '
              f'fixed_states={fixed_points(n,1)}')

if __name__=='__main__': main()
