#!/usr/bin/env python3
import math

def M(t,a,b):
    if t == float('-inf'):
        return min(a,b)
    if t == 0:
        return math.sqrt(a*b)
    if (a == 0 or b == 0) and t < 0:
        return 0.0
    return ((a**t+b**t)/2.0)**(1.0/t)

def e1_pair(p,a):
    A=((1+a)**p + 1-a**p)**(1/p)
    B=((1-a)**p + 1-a**p)**(1/p)
    return A,B

# Supplementary numerical stress test of the one-variable reduction used for e_1.
for p in (2.5,3.0,4.0,7.0):
    c=2**(1-1/p)
    for t in (float('-inf'),-2.0,0.0,1.0,p/2,p-1e-3):
        mx=0.0
        for k in range(10001):
            a=k/10000.0
            A,B=e1_pair(p,a)
            mx=max(mx,M(t,A,B))
        assert mx < c + 1e-9
    for t in (p,p+1,2*p,20.0):
        exact=2**(1-1/t)
        assert abs(M(t,0.0,2.0)-exact) < 1e-12
print('VERIFY_OK')
