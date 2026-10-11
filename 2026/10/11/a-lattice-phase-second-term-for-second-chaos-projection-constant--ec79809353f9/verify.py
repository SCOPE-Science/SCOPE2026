#!/usr/bin/env python3
import math
from fractions import Fraction

def C(n,k):
    return 0 if k < 0 or k > n else math.comb(n,k)

def exact_boundary(N):
    a=math.ceil((N-math.sqrt(N))/2)
    return Fraction(4*C(N,2)*(C(N-2,a-1)-C(N-2,a-2)),2**N)

def exact_direct(N):
    total=0
    for k in range(N+1):
        s=N-2*k
        K=(s*s-N)//2
        total += abs(K)*C(N,k)
    return Fraction(total,2**N)

def boundary_float(N):
    a=math.ceil((N-math.sqrt(N))/2)
    r=N-2*a
    n=N-2
    k=(n-r)//2
    logp=math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)-n*math.log(2.0)
    p=math.exp(logp)
    return N*(N-1)*(r+1)/(N+r)*p,r

for N in range(2,401):
    x=exact_boundary(N)
    y=exact_direct(N)
    assert x == y, (N,x,y)
    a=math.ceil((N-math.sqrt(N))/2)
    r=N-2*a
    z=Fraction(N*(N-1)*(r+1)*C(N-2,(N-2-r)//2),(N+r)*2**(N-2))
    assert x == z, (N,x,z)

c=math.sqrt(2/(math.pi*math.e))
max_scaled=0.0
argmax=None
for N in range(100,20001):
    L,r=boundary_float(N)
    delta=math.sqrt(N)-r
    phase=c*(1/6-(delta-1)**2)
    scaled=math.sqrt(N)*abs((L-c*N)-phase)
    if scaled>max_scaled:
        max_scaled=scaled
        argmax=N
assert max_scaled < 0.08, (argmax,max_scaled)
print(f"VERIFY_OK exact_cases=399 phase_cases=19901 max_scaled_remainder={max_scaled:.12g} argmax={argmax}")
