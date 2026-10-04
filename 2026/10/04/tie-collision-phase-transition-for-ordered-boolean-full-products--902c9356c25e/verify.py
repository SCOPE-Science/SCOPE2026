#!/usr/bin/env python3
from itertools import product
from math import factorial, log, comb
from fractions import Fraction

N=30
S2=[[0]*(N+1) for _ in range(N+1)]; S2[0][0]=1
s1=[[0]*(N+1) for _ in range(N+1)]; s1[0][0]=1
for n in range(1,N+1):
    for k in range(1,n+1):
        S2[n][k]=S2[n-1][k-1]+k*S2[n-1][k]
        s1[n][k]=s1[n-1][k-1]-(n-1)*s1[n-1][k]
F=[sum(factorial(k)*S2[n][k] for k in range(n+1)) for n in range(N+1)]
def a(d,n): return sum(s1[n][k]*F[k]**d for k in range(1,n+1))
def b(d,n): return F[n]**d
# Stirling forward inversion
for d in range(1,6):
    for n in range(1,15):
        assert b(d,n)==sum(S2[n][k]*a(d,k) for k in range(1,n+1))
# d=1
for n in range(1,15): assert a(1,n)==factorial(n)
# d=2 A101370 after dividing n!
A101370=[1,4,24,196,2016,24976,361792,5997872,111969552,2324081728]
assert [a(2,n)//factorial(n) for n in range(1,11)]==A101370
# d=3 initial set-orbit/hyperarray values
A3=[1,13,353,17041,1284977,139389925,20564986865,3960685110625,965031884176401,290199167208506893]
assert [a(3,n)//factorial(n) for n in range(1,11)]==A3
# direct enumeration of weak orders as rank vectors for n<=4.
def weak_orders(n):
    out=[]
    # surjections onto 0..m-1 exactly encode ordered partitions
    for m in range(1,n+1):
        for w in product(range(m), repeat=n):
            if set(w)==set(range(m)):
                out.append(w)
    return out
for n in range(1,5):
    W=weak_orders(n)
    assert len(W)==F[n]
    for d in range(1,4):
        cnt=0
        for ws in product(W, repeat=d):
            ok=True
            for i in range(n):
                for j in range(i+1,n):
                    if all(w[i]==w[j] for w in ws):
                        ok=False; break
                if not ok: break
            cnt+=ok
        assert cnt==a(d,n),(n,d,cnt,a(d,n))
# numerical convergence checks (sanity only)
L=log(2)
# d=2 ratio should head toward exp(-L^2/2)
import math
target2=math.exp(-L*L/2)
for n in (10,15,20,25,30):
    r=a(2,n)/b(2,n)
    print('d2',n,r,target2,r-target2)
# d>=3 scaled deficit tends L^d/2
for d in (3,4,5):
    target=L**d/2
    vals=[]
    for n in (10,15,20,25,30):
        deficit=1-a(d,n)/b(d,n)
        vals.append(deficit*n**(d-2))
    print('d',d,'scaled',vals,'target',target)
print('A3',A3)
print('VERIFY_OK')
