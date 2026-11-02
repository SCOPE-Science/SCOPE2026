#!/usr/bin/env python3
"""Reproduce integer Hilbert and bidegree calculations (not a replacement for proof)."""
import math

def ehrhart(n,k):
    return math.comb(2*k+n-1,n-1)-n*math.comb(k+n-2,n-1)

def curve_hilbert(n,k):
    return sum((-1)**j*math.comb(n-2,j)*ehrhart(n,k-j)
               for j in range(n-1))

cases={4:(12,8),5:(80,30),6:(330,84),7:(1092,210)}
for n in range(4,13):
    v=2**(n-1)-n
    g=1+(n-4)*2**(n-3)
    h=2*v+2*g-2
    b=(n-1)*h-math.comb(n,2)*2*(n-3)
    assert (b,h)==(n*(n-1)*(2**(n-2)-n+1),n*(2**(n-2)-2))
    for k in range(n-2,n+5):
        assert curve_hilbert(n,k)==v*k+1-g
    if n in cases: assert (b,h)==cases[n]
    print(n, v, g, h, b)
print('VERIFY_OK')
