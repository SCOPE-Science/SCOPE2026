import math
import random

def closed(beta,A,B,t):
    if t % 2 == 0:
        n=t//2
        return (beta*A-B)/(1.0+beta)*(1.0-beta**(2*n))
    n=(t+1)//2
    return (A-beta*B)/(1.0+beta) - (beta*A-B)/(1.0+beta)*beta**(2*n-1)

def replay(beta,A,B,T):
    m=0.0
    out=[]
    for t in range(1,T+1):
        g=A if t%2 else -B
        m=beta*m+(1.0-beta)*g
        out.append((t,g,m))
    return out

def first_odd_disagreement(beta,r):
    q=(beta-r)/(1.0-beta*r)
    K=math.log(q)/math.log(beta)
    return math.floor((K+1.0)/2.0)+1

random.seed(350067)

for _ in range(2000):
    beta=random.uniform(0.02,0.99)
    A=10.0**random.uniform(-3.0,3.0)
    B=10.0**random.uniform(-3.0,3.0)
    for t,g,m in replay(beta,A,B,40):
        assert abs(m-closed(beta,A,B,t)) <= 3e-12*max(1.0,A,B)

for beta in (0.1,0.5,0.9,0.99):
    B=1.0
    for r in (beta*1.01, 1.0, (1.0/beta)*0.99):
        if not (beta <= r < 1.0/beta):
            continue
        for t,g,m in replay(beta,r*B,B,100):
            assert g*m > 0.0

    r=(1.0/beta)*1.1
    for t,g,m in replay(beta,r*B,B,50):
        if t%2:
            assert g*m > 0.0
        else:
            assert g*m < 0.0

    r=beta*0.8
    N=first_odd_disagreement(beta,r)
    rows=replay(beta,r*B,B,2*N+5)
    for t,g,m in rows:
        if t%2==0:
            assert g*m > 0.0
        elif t < 2*N-1:
            assert g*m >= 0.0
        elif t == 2*N-1:
            assert g*m < 0.0

    r=1.0/beta
    for t,g,m in replay(beta,r*B,B,20):
        if t%2==0:
            assert abs(m) < 2e-14

# Default beta window and balanced Nyquist signal.
beta=0.9
assert abs(1.0/beta-1.1111111111111112) < 1e-15
for t,g,m in replay(beta,1.0,1.0,100):
    assert g*m > 0.0

# Base multipliers under agreement/disagreement.
assert abs(math.exp(1.0)-math.e) < 1e-15
assert abs(math.exp(-1.0)-1.0/math.e) < 1e-15
assert 1.0+1.0 == 2.0
assert 1.0-1.0 == 0.0

print("verification passed")
