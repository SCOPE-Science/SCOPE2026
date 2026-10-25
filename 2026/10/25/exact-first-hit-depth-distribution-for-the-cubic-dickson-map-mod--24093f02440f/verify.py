#!/usr/bin/env python3
"""Exact residue-ring iteration and independent valuation-histogram verification."""
from collections import Counter

def v3(n,k):
    if n==0: return k
    c=0
    while c<k and n%3==0:
        n//=3;c+=1
    return c

def h(k,x):
    p=3**k;r=x%3
    if r==0:
        return k-v3(x,k)
    rho=2 if r==2 else -2
    a=v3((x-rho)%p,k)
    if a==k: return 0
    b=v3((x+rho//2)%p,k) # rho=2 => x+1; rho=-2 => x-1
    a1=a+2*b
    return 1+max(0,(k-a1+1)//2)

def polynomial(k):
    z=Counter({0:1})
    for a in range(1,k):
        z[k-a]+=2*3**(k-a-1)
    if k==1: return Counter({0:3})
    c=Counter({0:1,1:1})
    C=1+max(0,(k-3+1)//2)
    c[C]+=3**(k-2)
    for a in range(2,k):
        c[1+max(0,(k-a-2+1)//2)]+=2*3**(k-a-1)
    for b in range(2,k):
        c[1+max(0,(k-1-2*b+1)//2)]+=2*3**(k-b-1)
    for j,n in c.items():z[j]+=2*n
    return z

def main():
    for k in range(1,9):
        p=3**k; f=lambda x:(x*x*x-3*x)%p
        tally=Counter();basin=Counter()
        for x in range(p):
            rho={0:0,1:p-2,2:2}[x%3]
            cur=x;time=0
            while cur!=rho and time<=k:
                cur=f(cur); time+=1
            assert cur==rho,(k,x,cur,time)
            hp=h(k,x)
            assert time==hp,(k,x,time,hp)
            tally[time]+=1;basin[(x%3,time)]+=1
        expected=polynomial(k)
        assert tally==expected,(k,tally,expected)
        assert sum(expected.values())==p
        assert max(t for (r,t) in basin if r==0)==k-1 if k>=2 else True
        assert max(t for (r,t) in basin if r in (1,2))==k//2
        print('k=',k,'total=',p,'hist=',dict(sorted(tally.items())))
    print('VERIFY_OK: 9840 exact residue orbits, first-hit formulas, three basin classifications, and independent exact-depth histograms for k=1..8')
if __name__=='__main__':main()
