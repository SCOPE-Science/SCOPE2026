#!/usr/bin/env python3
"""Direct congruence tests for the monic degree-two Chebyshev preperiod theorem."""
from collections import Counter

def v2(z):
    if z == 0: return 10**9
    return (abs(z) & -abs(z)).bit_length()-1

def least_time(k,x):
    mod=1<<k
    y=x
    target=(mod-1) if x%2 else (2%mod)
    for t in range(2*k+10):
        if y==target: return t
        y=(y*y-2)%mod
    raise AssertionError((k,x))

def predicted(k,x):
    mod=1<<k
    if k==1:
        return 0
    if k==2:
        return 0 if x%mod in (2,3) else 1
    if x%2:
        if (x+1)%mod==0: return 0
        return 1+max(0,k-v2(x*x-1))
    if (x-2)%mod==0: return 0
    if x%4==2:
        s=v2(x*x-4)
        return 1+max(0,(k-s+1)//2)
    r=v2(x)
    return max(2,2+(k-1)//2-r)

def hist(k):
    if k==1: return {0:1},{0:1}
    if k==2: return {0:1,1:1},{0:1,1:1}
    odd={0:1,1:3}
    odd.update({t:(1<<t) for t in range(2,k-1)})
    if k==3: return odd,{0:1,1:1,2:2}
    if k==4: return odd,{0:1,1:3,2:4}
    L=(k-1)//2
    def A(q):
        if q<=5:return 1<<(k-2)
        if q<=k:return 1<<(k-q+3)
        return 0
    even={0:1,1:7}
    for t in range(2,k+1):
        a=A(k-2*t+2)-A(k-2*t+4)
        if t==2:
            b=1<<(k-max(2,L))
        elif 3<=t<=L:
            b=1<<(k-L-3+t)
        else:b=0
        if a+b: even[t]=a+b
    return odd,even

total=0
for k in range(1,18):
    M=1<<k
    direct=[Counter(),Counter()]
    for x in range(M):
        t=least_time(k,x)
        p=predicted(k,x)
        assert t==p, (k,x,t,p)
        direct[x%2][t]+=1
    odd,even=hist(k)
    assert dict(direct[1])==odd,(k,'odd',direct[1],odd)
    assert dict(direct[0])==even,(k,'even',direct[0],even)
    assert sum(odd.values())==M//2 and sum(even.values())==M//2
    total+=M
print('VERIFY_OK: full direct time and histogram matches for k=1..17; '+str(total)+' residues, two parity basins')
