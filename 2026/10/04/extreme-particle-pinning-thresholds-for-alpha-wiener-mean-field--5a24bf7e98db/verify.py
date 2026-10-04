#!/usr/bin/env python3
import math

def v_closed(T,t,a):
    d=T-t
    if abs(a-0.5)<1e-14:
        return d*math.log(T/d)
    return d**(2*a)*(T**(1-2*a)-d**(1-2*a))/(1-2*a)

def v_midpoint(T,t,a,N=200000):
    h=t/N
    s=0.0
    for k in range(N):
        x=(k+0.5)*h
        s += ((T-t)/(T-x))**(2*a)
    return s*h

for a in (0.25,0.5,1.5):
    T=1.7; t=1.53
    vc=v_closed(T,t,a)
    vn=v_midpoint(T,t,a)
    if abs(vc-vn) > 5e-8*max(1.0,abs(vc)):
        raise SystemExit(f'variance mismatch a={a}: {vc} {vn}')

# The absolute-Gaussian centering is chosen so that n*P(|Z|>b_n+x/b_n) -> exp(-x).
def tail_abs(z):
    return math.erfc(z/math.sqrt(2.0))

for n in (10_000,1_000_000,100_000_000):
    L=math.log(n)
    b=math.sqrt(2*L)-(math.log(L)+math.log(math.pi))/(2*math.sqrt(2*L))
    for x in (-1.0,0.0,1.0):
        lam=n*tail_abs(b+x/b)
        target=math.exp(-x)
        # Slow logarithmic convergence is expected; this is only a normalization sanity check.
        if abs(lam/target-1.0) > 0.22:
            raise SystemExit(f'extreme-tail normalization mismatch n={n} x={x}: {lam} vs {target}')

# Check endpoint equivalent ratios at a very small terminal distance.
T=2.0; d=1e-10; t=T-d
for a in (0.25,1.5):
    v=v_closed(T,t,a)
    if a<0.5:
        asym=T**(1-2*a)/(1-2*a)*d**(2*a)
    else:
        asym=d/(2*a-1)
    if abs(v/asym-1.0)>1e-4:
        raise SystemExit('endpoint asymptotic mismatch')

print('VERIFY_OK')
