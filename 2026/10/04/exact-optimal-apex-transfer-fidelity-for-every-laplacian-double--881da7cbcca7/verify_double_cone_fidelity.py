#!/usr/bin/env python3
import cmath, math

def amp(n,t):
    return 1/(n+2)+n/(2*(n+2))*cmath.exp(-1j*(n+2)*t)-0.5*cmath.exp(-1j*n*t)

def closed(n):
    if n%4==2: return 1.0
    if n%2: return math.cos(math.pi/(2*(n+2)))**2
    return math.cos(math.pi/(n+2))**2

def candidates(n):
    vals=[]
    # sin(t)=0 family over one 2pi period
    for k in range(3): vals.append(abs(amp(n,k*math.pi))**2)
    # nt = 2 pi k
    for k in range(n+1): vals.append(abs(amp(n,2*math.pi*k/n))**2)
    # (n+2)t = 2 pi k
    for k in range(n+3): vals.append(abs(amp(n,2*math.pi*k/(n+2)))**2)
    return max(vals)

checks=0
for n in range(1,201):
    c=closed(n); q=candidates(n)
    assert abs(c-q)<2e-12,(n,c,q)
    # dense grid can only lie below analytic critical maximum
    for j in range(2001):
        t=2*math.pi*j/2000
        assert abs(amp(n,t))**2 <= c+3e-10,(n,t)
        checks+=1
print('VERIFY_OK')
print('n_range = 1..200')
print('grid_checks =',checks)
