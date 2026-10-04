#!/usr/bin/env python3
import math
from collections import defaultdict

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def laurent_power(base,n):
    p={0:1}
    for _ in range(n):
        q=defaultdict(int)
        for i,a in p.items():
            for j,b in base.items():
                q[i+j]+=a*b
        p=dict(q)
    return p

# Exact quartic certificates.
left1=[15,-32,18,0,-1]
right1=mul(mul([3,-1],[1,-2,1]),[5,1])
assert left1==right1
left2=[15,32,18,0,-1]
right2=mul(mul([5,-1],[1,2,1]),[3,1])
assert left2==right2

base={-1:1,0:1,1:1}
assert laurent_power(base,2)[0]==3
assert laurent_power(base,4)[0]==19

phi=(1+math.sqrt(5.0))/2.0
upper=25.0/16.0
assert phi>upper

def norms(L):
    ap=am=0.0
    for k in range(L):
        th=2.0*math.pi*k/L
        z=complex(math.cos(th),math.sin(th))
        ap += abs(1+z+z*z)
        am += abs(1+z-z*z)
    return ap/L,am/L

a3,b3=norms(3)
a4,b4=norms(4)
assert abs(a3-1.0)<1e-12 and abs(b3-5.0/3.0)<1e-12
assert abs(a4-1.5)<1e-12 and abs(b4-phi)<1e-12
minimum_gap=10.0
for L in range(5,1001):
    a,b=norms(L)
    assert a <= upper+2e-12
    assert b >= phi-2e-12
    assert b>a
    minimum_gap=min(minimum_gap,b-a)
print(f"orders_checked=998 minimum_observed_gap={minimum_gap:.15g}")
print("VERIFY_OK")
