import math
import random

def exact_values(gamma,A,B,n):
    EA=(A+gamma*B)/(1.0+gamma)
    EB=(gamma*A+B)/(1.0+gamma)
    even=EB*(1.0-gamma**(2*n))
    odd=EA-EB*gamma**(2*n-1)
    return odd,even,EA,EB

def onset(gamma,A,B):
    q=gamma*(A-B)/(gamma*A+B)
    return math.floor(math.log(q)/(2.0*math.log(gamma)))+1

random.seed(350065)

# Exact subsequence formulas.
for _ in range(2000):
    gamma=random.uniform(0.02,0.995)
    B=10.0**random.uniform(-3.0,1.0)
    A=B*(1.0+10.0**random.uniform(-3.0,3.0))
    e=0.0
    N=onset(gamma,A,B)
    first=None
    for t in range(1,401):
        norm=A if t%2 else B
        e=gamma*e+(1.0-gamma)*norm
        n=(t+1)//2 if t%2 else t//2
        odd,even,EA,EB=exact_values(gamma,A,B,n)
        target=odd if t%2 else even
        assert abs(e-target) <= 2e-12*max(1.0,A)
        if t%2:
            assert e < A
        else:
            if e > B and first is None:
                first=t//2
    if N <= 200:
        assert first == N

# Onset inequality is exact on a broad deterministic grid.
for gamma in (0.1,0.5,0.9,0.95,0.99):
    for qraw in (1.01,1.1,2.0,10.0,100.0,1e6):
        B=1.0
        A=qraw
        N=onset(gamma,A,B)
        EB=(gamma*A+B)/(1.0+gamma)
        assert EB*(1.0-gamma**(2*N)) > B
        if N > 1:
            assert EB*(1.0-gamma**(2*(N-1))) <= B

# Contrast law: increasing in raw contrast and below the sharp cap.
for gamma in (0.05,0.2,0.5,0.95,0.99):
    prev=1.0
    cap=(1.0+gamma)/gamma
    for qraw in (1.001,1.01,1.1,2.0,10.0,100.0,1e4,1e8):
        contrast=(1.0+gamma)*qraw/(gamma*qraw+1.0)
        assert contrast > prev
        assert contrast < cap
        prev=contrast
    assert abs((1.0+gamma)*1e12/(gamma*1e12+1.0)-cap) < 2e-9*cap

# Source main experimental gamma.
gamma=0.95
cap=(1.0+gamma)/gamma
floor_ratio=gamma/(1.0+gamma)
assert abs(cap-39.0/19.0) < 1e-15
assert abs(floor_ratio-19.0/39.0) < 1e-15

# A/B = 100 illustration.
A=100.0
B=1.0
N=onset(gamma,A,B)
contrast=(1.0+gamma)*A/(gamma*A+B)
assert N == 1
assert abs(contrast-2.03125) < 1e-14

print("verification passed")
