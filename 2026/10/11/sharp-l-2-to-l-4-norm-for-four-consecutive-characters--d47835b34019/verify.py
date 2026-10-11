#!/usr/bin/env python3
import cmath, math, random

def q(r):
    return r*r*r + 3*r*r - 3*r - 3

lo, hi = 1.0, 2.0
for _ in range(120):
    mid=(lo+hi)/2
    if q(mid) <= 0:
        lo=mid
    else:
        hi=mid
rho=(lo+hi)/2

def h(r):
    return (3*r**4+4*r**3+12*r*r+3)/(2*(1+r*r)**2)
K=h(rho)
poly=208*K**3-1224*K*K+2268*K-1323
assert abs(q(rho)) < 2e-14
assert abs(poly) < 2e-11

def moment4(c):
    s=[0j]*7
    for i,x in enumerate(c):
        for j,y in enumerate(c):
            s[i+j]+=x*y
    return sum(abs(x)**2 for x in s)

def ratio4(c):
    norm2=sum(abs(x)**2 for x in c)
    return moment4(c)/(norm2*norm2)

ext=[1.0, rho, rho, 1.0]
assert abs(ratio4(ext)-K) < 5e-13

random.seed(420055)
worst=0.0
for _ in range(50000):
    c=[]
    for _ in range(4):
        radius=random.random()*2.0
        theta=random.random()*2*math.pi
        c.append(radius*cmath.exp(1j*theta))
    if sum(abs(x)**2 for x in c) < 1e-20:
        continue
    val=ratio4(c)
    worst=max(worst,val)
    assert val <= K + 5e-12

print(f"VERIFY_OK rho={rho:.15f} K={K:.15f} C4={K**0.25:.15f} random_cases=50000 worst_random={worst:.15f}")
