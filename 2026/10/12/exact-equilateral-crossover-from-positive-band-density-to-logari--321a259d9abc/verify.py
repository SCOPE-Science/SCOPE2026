#!/usr/bin/env python3
import math

def source_lhs(k,t,theta,ell):
    c=math.cos(math.pi*t/3.0)
    s=math.sin(math.pi*k)
    P6=72*ell**6*(c-1)**2*s**3
    P4=48*ell**4*(c*c-1)*s*(2-3*s*s)
    P2=8*ell**2*(c+1)**2*s*(-4+9*s*s)
    Pc=-32*ell**2*(c+1)*(3*k*k*ell*ell*(c-1)-(c+1))*s
    return k**6*P6+k**4*P4+k*k*P2+k*k*Pc*math.cos(theta)

def reduced_normalized(k,t,theta,ell):
    c=math.cos(math.pi*t/3.0)
    s=math.sin(math.pi*k)
    q=(1-c)/(1+c)
    y=k*k*ell*ell*q
    return 9*(y+1)**2*s*s+4*(3*y+1)*(math.cos(theta)-1)

def A(y):
    return (2*math.sqrt(2)/3.0)*math.sqrt(3*y+1)/(y+1)

maxerr=0.0
for ell in (0.7,1.0,1.9):
    for t in (0.07,0.3,0.8,1.0):
        for k in (0.37,1.23,2.71,7.41):
            for theta in (-2.2,-0.4,0.9,2.7):
                c=math.cos(math.pi*t/3.0)
                s=math.sin(math.pi*k)
                den=8*k*k*ell*ell*(c+1)**2*s
                lhs=source_lhs(k,t,theta,ell)/den
                rhs=reduced_normalized(k,t,theta,ell)
                maxerr=max(maxerr,abs(lhs-rhs))
assert maxerr < 2e-10, maxerr

for y in (0.0,0.02,1/3,1.0,10.0,1e4):
    lhs=1-A(y)**2
    rhs=(3*y-1)**2/(9*(y+1)**2)
    assert abs(lhs-rhs) < 2e-14
    assert A(y) <= 1+2e-14

ell=1.3
t=0.4
b=ell*math.tan(math.pi*t/6)
C=4*math.sqrt(6)/(3*math.pi*b)
for n in (200,500,1000,2000):
    p=(2/math.pi)*math.asin(A((b*n)**2))
    assert abs(n*p-C) < 0.02

tau=3.0
ell=1.1
a=math.pi*ell*tau/6
def profile(x):
    return (2/math.pi)*math.asin(A((a*x)**2))
N=200000
mid=sum(profile((j+0.5)/N) for j in range(N))/N
N2=100000
mid2=sum(profile((j+0.5)/N2) for j in range(N2))/N2
assert abs(mid-mid2) < 2e-8

print("VERIFY_OK", "max_identity_error=%.3e"%maxerr,
      "p0=%.12f"%((2/math.pi)*math.asin(2*math.sqrt(2)/3)),
      "scaled_profile=%.12f"%mid,
      "fixed_t_coeff=%.12f"%C)
