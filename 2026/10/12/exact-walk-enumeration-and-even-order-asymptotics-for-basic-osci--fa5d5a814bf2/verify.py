#!/usr/bin/env python3
from itertools import product
from math import cos, log, pi, sqrt

WEIGHTS={-2:1,-1:2,0:3,1:2,2:1}
EXPECTED=[1,3,6,20,43,149,331,1169,2645,9447,21626,77816,179579,649589]

def wcount(L,h):
    states={h:1}
    for _ in range(L):
        nxt={}
        for x,c in states.items():
            for d,m in WEIGHTS.items():
                y=x+d
                if y>=0:
                    nxt[y]=nxt.get(y,0)+c*m
        states=nxt
    return sum(states.values())

def formula(n):
    if n%2==0:
        m=n//2
        return wcount(m-1,0)
    m=(n-1)//2
    return 2*wcount(m-1,0)+wcount(m-1,1)

def brute(n):
    ranges=[range(1,max(k,n-k)+1) for k in range(1,n)]
    count=0
    for f in product(*ranges):
        if not all(abs(f[k]-f[k-1])<=1 for k in range(1,n-1)):
            continue
        if not all(f[k-1]+f[n-k-1]>=n for k in range(1,n)):
            continue
        count+=1
    return count

for n in range(2,10):
    assert brute(n)==formula(n), (n,brute(n),formula(n))

assert [formula(n) for n in range(2,16)]==EXPECTED

# Numerical cross-check of the exact logarithmic-integral evaluation.
N=200000
s=0.0
for j in range(N):
    theta=-pi+(j+0.5)*(2*pi/N)
    phi=((1+2*cos(theta))/3.0)**2
    s+=log(1-phi)
avg=s/N
from_integral=(2.718281828459045)**(-0.5*avg)
exact=3*sqrt(2-sqrt(3))
assert abs(from_integral-exact)<2e-4, (from_integral,exact)
print('CHECK_OK')
