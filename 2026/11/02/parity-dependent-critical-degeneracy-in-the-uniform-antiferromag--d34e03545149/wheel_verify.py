#!/usr/bin/env python3
"""Independent exact verifier for antiferromagnetic wheel ground states.
Integer arithmetic is used for spin enumeration and minimum-plus ring transfer."""
from collections import Counter
from fractions import Fraction


def predicted(n, h):
    h=abs(Fraction(h))
    assert n>=4
    if n%2:
        L0,L1=2,1
        for _ in range(2,n+1): L0,L1=L1,L0+L1
        luc=L1
        if h<1:return (Fraction(1-n),2*n)
        if h==1:return (Fraction(1-n),luc+2*n)
        if h<n:return (-(n-1)*h,1)
        if h==n:return (-(n-1)*h,2)
        return (2*n-(n+1)*h,1)
    hc=Fraction(n,n-2)
    if h==0:return (Fraction(-n),4)
    if h<hc:return (-n-h,2)
    if h==hc:return (-n-h,3)
    if h<n:return (-(n-1)*h,1)
    if h==n:return (-(n-1)*h,2)
    return (2*n-(n+1)*h,1)


def spin_hist(n):
    vals=Counter()
    for mask in range(1<<n):
        ss=[1-2*((mask>>j)&1) for j in range(n)]
        R=sum(ss)
        ring=sum(ss[j]*ss[(j+1)%n] for j in range(n))
        for t in [-1,1]:
            vals[(ring+t*R,t+R)]+=1
    return vals

def enum(hist,h):
    h=Fraction(h); vals=Counter()
    for (e0,m),c in hist.items():vals[e0-h*m]+=c
    minimum=min(vals)
    return minimum,vals[minimum]


def dp(n,h):
    h=Fraction(h)
    best=None;total=0
    for t in (-1,1):
        # min-plus ring count with state tracking (first spin, previous spin)
        for first in (-1,1):
            z={(first,first):(Fraction(-h*t+(t-h)*first),1)}
            for i in range(1,n):
                q={}
                for (f,last),(energy,count) in z.items():
                    for cur in (-1,1):
                        e=energy+last*cur+(t-h)*cur
                        key=(f,cur)
                        if key not in q or e<q[key][0]:q[key]=(e,count)
                        elif e==q[key][0]:q[key]=(e,q[key][1]+count)
                z=q
            for (f,last),(e,count) in z.items():
                e=e+f*last
                if best is None or e<best:best,total=e,count
                elif e==best:total+=count
    return best,total


def check():
    c1=c2=0
    for n in range(4,17):
        hist=spin_hist(n)
        points={Fraction(0),Fraction(1,4),Fraction(3,4),Fraction(1),Fraction(5,4),Fraction(2),Fraction(3),Fraction(n),Fraction(n+1),Fraction(n,2),Fraction(n,3),Fraction(n,n-2)}
        for x in tuple(points):
            if x>0:points.add(x-Fraction(1,10000));points.add(x+Fraction(1,10000))
        for h in sorted(points):
            got=enum(hist,h);ref=predicted(n,h)
            assert got==ref,(n,h,got,ref)
            c1+=1
    for n in [17,18,19,20,25,26,33,34,49,50,71,72,101,102,201,202]:
        points={Fraction(0),Fraction(1,10),Fraction(1),Fraction(6,5),Fraction(3,2),Fraction(2),Fraction(3),Fraction(n),Fraction(n+1),Fraction(n,n-2)}
        for x in tuple(points):
            if x>0:points.add(x-Fraction(1,10000));points.add(x+Fraction(1,10000))
        for h in sorted(points):
            got=dp(n,h);ref=predicted(n,h)
            assert got==ref,(n,h,got,ref)
            c2+=1
    print(f'PASS {c1} exhaustive all-spin tests for rim lengths 4..16')
    print(f'PASS {c2} exact independent transfer-dynamic-programming tests for rim lengths 17..202')
    print('PASS exact transition boundaries and ground-state multiplicities; computations corroborate analytic proof, not substitute for it')

if __name__=='__main__':check()
