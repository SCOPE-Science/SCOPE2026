import math
import random

def sgn(x):
    return (x > 0.0) - (x < 0.0)

def yogi_v(beta2,G,T):
    s=1.0-beta2
    v=0.0
    out=[v]
    for _ in range(T):
        v = v - s*sgn(v-G*G)*G*G
        out.append(v)
    return out

from fractions import Fraction

def yogi_v_exact(beta2,G2,T):
    s=1-beta2
    v=Fraction(0,1)
    out=[v]
    for _ in range(T):
        diff=v-G2
        sign=(diff>0)-(diff<0)
        v=v-s*sign*G2
        out.append(v)
    return out

for beta2,N in ((Fraction(9,10),10),(Fraction(99,100),100),(Fraction(999,1000),1000)):
    G2=Fraction(9,1)
    vals=yogi_v_exact(beta2,G2,N+10)
    for t in range(N+1):
        assert vals[t] == t*(1-beta2)*G2
    for t in range(N,N+10):
        assert vals[t] == G2

for beta2 in (0.83,0.93,0.975,0.9973):
    G=2.5
    s=1.0-beta2
    q=1.0/s
    N=math.floor(q)
    phi=q-N
    low=G*G*(1.0-phi*s)
    high=G*G*(1.0+(1.0-phi)*s)
    vals=yogi_v(beta2,G,N+20)
    assert abs(vals[N]-low) < 2e-10
    assert abs(vals[N+1]-high) < 2e-10
    for j in range(10):
        assert abs(vals[N+2*j]-low) < 2e-10
        assert abs(vals[N+2*j+1]-high) < 2e-10
    assert abs((high-low)-s*G*G) < 2e-12

random.seed(590035)
for _ in range(500):
    s=random.uniform(0.002,0.4)
    q=1.0/s
    if abs(q-round(q)) < 1e-8:
        continue
    beta2=1.0-s
    G=10.0**random.uniform(-2,2)
    N=math.floor(q)
    phi=q-N
    low=G*G*(1.0-phi*s)
    high=G*G*(1.0+(1.0-phi)*s)
    vals=yogi_v(beta2,G,N+4)
    assert abs(vals[N]-low) <= 5e-10*max(1.0,G*G)
    assert abs(vals[N+1]-high) <= 5e-10*max(1.0,G*G)
    assert abs(vals[N+2]-low) <= 5e-10*max(1.0,G*G)

for beta2 in (0.7,0.9,0.99):
    G=2.0
    v=0.0
    for t in range(1,200):
        v=beta2*v+(1.0-beta2)*G*G
        closed=G*G*(1.0-beta2**t)
        assert abs(v-closed) < 2e-12

print("verification passed")
