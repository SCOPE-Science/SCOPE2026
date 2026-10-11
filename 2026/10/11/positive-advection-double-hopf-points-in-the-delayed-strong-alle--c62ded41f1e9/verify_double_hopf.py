#!/usr/bin/env python3
import math

def H(y,j):
    return (math.acos(-y)+2.0*math.pi*j)/math.sqrt(1.0-y*y)

def G(x):
    return H(x,1)-H(9.0*x,0)

lo, hi = 0.10, 0.105
assert G(lo) > 0.0 and G(hi) < 0.0
for _ in range(100):
    mid=(lo+hi)/2.0
    if G(mid)>0.0: lo=mid
    else: hi=mid
x=(lo+hi)/2.0
r,K,L=1.0,4.0,8.0
a=r*(K-1.0)
d=768.0*x/(math.pi*math.pi)
tau=H(x,1)/a
mu1=a*x
mu2=9.0*a*x
mu3=25.0*a*x
w1=math.sqrt(a*a-mu1*mu1)
w2=math.sqrt(a*a-mu2*mu2)

def residual(mu,w):
    z=complex(0.0,w)+mu+a*complex(math.cos(-w*tau), math.sin(-w*tau))
    return abs(z)

print(f"x={x:.16f}")
print(f"d={d:.16f}")
print(f"tau={tau:.16f}")
print(f"mu1={mu1:.16f} mu2={mu2:.16f} mu3={mu3:.16f}")
print(f"omega1={w1:.16f} omega2={w2:.16f}")
print(f"G(x)={G(x):.3e}")
print(f"residual1={residual(mu1,w1):.3e}")
print(f"residual2={residual(mu2,w2):.3e}")
assert 1.0/25.0 < x < 1.0/9.0
assert mu1 < mu2 < a < mu3
assert abs(G(x)) < 1e-12
assert residual(mu1,w1) < 1e-12
assert residual(mu2,w2) < 1e-12
print("VERIFY_OK")
