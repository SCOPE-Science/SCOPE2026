#!/usr/bin/env python3
import math

def simpson(f,a,b,N):
    if N%2: N+=1
    h=(b-a)/N
    s=f(a)+f(b)
    for i in range(1,N): s+=(4.0 if i%2 else 2.0)*f(a+i*h)
    return s*h/3.0

def H(k,t):
    m=k-1
    return sum(((-1)**(j+1))*math.comb(m,j)*(j*t+1.0)*math.exp(-j*t)/(j*(j+1.0)) for j in range(1,m+1))

def H_quad(k,t):
    m=k-1
    def outer(x):
        lo=x+t
        if lo>=22.0: return 0.0
        def inner(y):
            fm=m*math.exp(-y)*(1.0-math.exp(-y))**(m-1)
            return (y-x)*fm
        return math.exp(-x)*simpson(inner,lo,22.0,400)
    return simpson(outer,0.0,17.0,400)

for k,t in [(2,0.7),(3,1.1),(4,2.0)]:
    assert abs(H(k,t)-H_quad(k,t))<2e-6,(k,t,H(k,t),H_quad(k,t))

def rd(k,n,t):
    K=k*(n-1)
    return (1.0-2.0*K*H(k,t))/(n*n*K*(K+1.0))

def rd2(k,n,t):
    K=k*(n-1); EA=(1.0+H(k,t))/n
    a=1.0/(n*K); b=1.0/(n*(K+1.0))
    return (-2*a*EA*K+a*a*K*(K+1))-(-2*b*EA*K+b*b*K*(K+1))

for k,n,t in [(2,3,1.2),(3,5,4.0),(5,2,3.0)]:
    assert abs(rd(k,n,t)-rd2(k,n,t))<2e-15

def threshold(k,n):
    target=1.0/(2.0*k*(n-1)); lo,hi=0.0,20.0
    assert H(k,lo)>target and H(k,hi)<target
    for _ in range(100):
        mid=(lo+hi)/2
        if H(k,mid)>target: lo=mid
        else: hi=mid
    return (lo+hi)/2

for k in range(2,8):
    for n in (2,3,5,10):
        t=threshold(k,n)
        assert rd(k,n,t*(1-1e-7))<0
        assert abs(rd(k,n,t))<2e-15
        assert rd(k,n,t*(1+1e-7))>0

vals=[threshold(3,n) for n in (3,5,10,15)]
targets=[4.111450606420002,4.9611811353194035,5.923005815333269,6.436753036096322]
for a,b in zip(vals,targets): assert abs(a-b)<2e-12,(a,b)
print(f"VERIFY_OK k3n3={vals[0]:.12f} k3n5={vals[1]:.12f} k3n10={vals[2]:.12f} k3n15={vals[3]:.12f}")
