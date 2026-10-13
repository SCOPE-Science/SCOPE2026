#!/usr/bin/env python3
import math

def simpson(f, a, b, N=200000):
    if N % 2:
        N += 1
    h = (b-a)/N
    s = f(a) + f(b)
    for i in range(1, N):
        s += (4.0 if i % 2 else 2.0)*f(a+i*h)
    return s*h/3.0

def beta(a,b):
    return math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))

def recip_closed(n,r):
    m=n-1
    x=r/(1.0+r)**2
    return 1.0/m - x**m/(m*m*beta(n,n-1))

def recip_integral(n,r):
    a=r/(1.0+r)
    Bnn=beta(n,n)
    f1=lambda t: (t**(n-2))*((1.0-t)**(n-1))
    f2=lambda t: (t**(n-1))*((1.0-t)**(n-2))
    I1=simpson(f1,a,1.0,40000)
    I2=simpson(f2,0.0,a,40000)
    return (I1+I2)/((2*n-1)*Bnn)

def risk_diff(n,r):
    return recip_closed(n,r)-math.log(n/(n-1.0))

def threshold(n):
    m=n-1
    q=(m*beta(n,n-1)*(1.0-m*math.log(n/m)))**(1.0/m)
    assert 0.0 < q < 0.25
    s=math.sqrt(1.0-4.0*q)
    return (1.0+s)/(1.0-s)

# Independent numerical integration against the closed form.
for n,r in [(2,0.2),(2,1.0),(3,4.0),(5,0.7),(8,3.0)]:
    a=recip_closed(n,r)
    b=recip_integral(n,r)
    assert abs(a-b) < 3e-10, (n,r,a,b)

# Sign and exact-root checks.
for n in range(2,81):
    rh=threshold(n)
    assert risk_diff(n,1.0) < 0.0
    assert risk_diff(n,1e8) > 0.0
    assert abs(risk_diff(n,rh)) < 5e-13, (n,rh,risk_diff(n,rh))
    assert risk_diff(n, rh*(1.0-1e-6)) < 0.0
    assert risk_diff(n, rh*(1.0+1e-6)) > 0.0

# Direct bisection of the risk equation as a second threshold calculation.
def bisect(n):
    lo,hi=1.0,1e4
    assert risk_diff(n,lo)<0 and risk_diff(n,hi)>0
    for _ in range(100):
        mid=(lo+hi)/2.0
        if risk_diff(n,mid)<0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

for n in (2,5,8,20):
    assert abs(bisect(n)-threshold(n)) < 2e-11

r2,r5,r8=(threshold(n) for n in (2,5,8))
print(f"VERIFY_OK rho2={r2:.12f} rho5={r5:.12f} rho8={r8:.12f}")
