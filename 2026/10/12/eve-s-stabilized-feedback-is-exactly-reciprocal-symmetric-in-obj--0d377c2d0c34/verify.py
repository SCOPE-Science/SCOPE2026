import math
import random

def raw_from_gaps(a,b):
    return abs(a-b)/min(a,b)

def raw_from_ratio(q):
    return max(q,1.0/q)-1.0

def clip(x,c):
    return min(c,max(1.0/c,x))

def smooth(t,beta3,dhat):
    return dhat + (1.0-dhat)*(beta3**(t-1))

random.seed(350069)

# Exact ratio reduction and reciprocal symmetry.
for _ in range(10000):
    prev=10.0**random.uniform(-12.0,12.0)
    q=10.0**random.uniform(-8.0,8.0)
    cur=q*prev
    a=raw_from_gaps(cur,prev)
    b=raw_from_ratio(q)
    assert abs(a-b) <= 2e-12*max(1.0,a,b)
    assert abs(b-raw_from_ratio(1.0/q)) <= 2e-12*max(1.0,b)

# Smoothing recurrence closed form.
for _ in range(5000):
    c=10.0**random.uniform(0.01,2.0)
    beta3=random.uniform(0.0,0.999999)
    q=10.0**random.uniform(-4.0,4.0)
    dhat=clip(raw_from_ratio(q),c)
    state=1.0
    for t in range(2,30):
        state=beta3*state+(1.0-beta3)*dhat
        exact=smooth(t,beta3,dhat)
        assert abs(state-exact) < 3e-13*max(1.0,abs(state),abs(exact))

# Exact clipping regions.
for c in (1.1,2.0,10.0,100.0):
    lo=c/(c+1.0)
    hi=(c+1.0)/c
    assert abs(clip(raw_from_ratio(lo),c)-1.0/c) < 1e-14
    assert abs(clip(raw_from_ratio(hi),c)-1.0/c) < 1e-14
    assert abs(clip(raw_from_ratio(1.0/(c+1.0)),c)-c) < 2e-13
    assert abs(clip(raw_from_ratio(c+1.0),c)-c) < 2e-13

# On improving traces the limiting rate multiplier is weakly increasing in q.
def limit_multiplier(q,c):
    return 1.0/clip(raw_from_ratio(q),c)

for c in (2.0,10.0,50.0):
    qs=[10.0**(-6.0 + 6.0*i/1000.0) for i in range(1001)]
    vals=[limit_multiplier(q,c) for q in qs]
    assert all(vals[i] <= vals[i+1] + 2e-13 for i in range(len(vals)-1))

# Default c=10 exact landmarks.
c=10.0
assert abs(limit_multiplier(1.0,c)-10.0) < 1e-15
assert abs(limit_multiplier(0.1,c)-1.0/9.0) < 1e-15
assert abs(limit_multiplier(10.0,c)-1.0/9.0) < 1e-15
assert abs(limit_multiplier(1.0/11.0,c)-0.1) < 2e-15
assert abs(limit_multiplier(11.0,c)-0.1) < 2e-15
assert abs(limit_multiplier(10.0/11.0,c)-10.0) < 2e-14
assert abs(limit_multiplier(11.0/10.0,c)-10.0) < 2e-14

print('verification passed')
