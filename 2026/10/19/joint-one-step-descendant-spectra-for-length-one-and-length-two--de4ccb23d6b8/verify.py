#!/usr/bin/env python3
"""Standalone exhaustive checks for mixed one- and two-symbol tandem duplication statistics."""
from itertools import product
from collections import Counter
from math import comb

def outputs(w,ell):
    return {w[:i+ell]+w[i:i+ell]+w[i+ell:] for i in range(len(w)-ell+1)}

def stats(w):
    n=len(w)
    return (1+sum(w[i]!=w[i+1] for i in range(n-1)),
            1+sum(w[i]!=w[i+2] for i in range(n-2)))

def predicted(q,n):
    # polynomial transfer on states (the adjacent pair is equal or unequal)
    p={(False,0,0):q,(True,1,0):q*(q-1)}
    for _ in range(n-2):
        z=Counter()
        for (different,a,b),v in p.items():
            if not different:
                z[(False,a,b)]+=v
                z[(True,a+1,b+1)]+=v*(q-1)
            else:
                z[(False,a,b+1)]+=v
                z[(True,a+1,b)]+=v
                z[(True,a+1,b+1)]+=v*(q-2)
        p=dict(z)
    z=Counter()
    for (_,a,b),v in p.items():z[(a+1,b+1)]+=v
    return z

def maxima(q,n):
    if q==2:return 2+(3*n-4)//2,(2 if n%2==0 else n+3)
    return 2*n-1,q*(q-1)*(q-2)**(n-2)

def run():
    count=0
    for q,maxn in [(2,12),(3,8),(4,6),(5,5)]:
        for n in range(2,maxn+1):
            hist=Counter()
            for w in product(range(q),repeat=n):
                actual=(len(outputs(w,1)),len(outputs(w,2)))
                assert actual==stats(w),(q,n,w,actual,stats(w))
                hist[actual]+=1
                count+=1
            assert hist==predicted(q,n),(q,n,hist,predicted(q,n))
            assert sum(hist.values())==q**n
            mx,num=maxima(q,n)
            assert max(sum(k) for k in hist)==mx,(q,n,mx)
            assert sum(v for k,v in hist.items() if sum(k)==mx)==num,(q,n,num)
            if n>=3:
                L=n-1
                for k in range(L+1):
                    conditional=sum((b-1)*v for (a,b),v in hist.items() if a-1==k)
                    den=sum(v for (a,b),v in hist.items() if a-1==k)
                    # rational expected (b-1)=[2k(L-k)+(q-2)k(k-1)/(q-1)]/L
                    assert conditional*L*(q-1)==den*(2*k*(L-k)*(q-1)+(q-2)*k*(k-1)),(q,n,k)
                # exact zero covariance
                m1=sum((a-1)*v for (a,b),v in hist.items())
                m2=sum((b-1)*v for (a,b),v in hist.items())
                c=sum((a-1)*(b-1)*v for (a,b),v in hist.items())
                assert c*q**n==m1*m2,(q,n,'cov')
                assert hist[(1,1)]==q,(q,n,'min')
    print(f'MIXED_TANDEM_SPHERE_PASS words={count} q=2..5 n_max=(12,8,6,5) exhaustive=true')
if __name__=='__main__':run()
