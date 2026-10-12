import itertools
import math
import random

rng = random.Random(350063)

def epoch_direct(x, h, b, order):
    q = 1.0-h
    for s in order:
        x = q*x + h*s*b
    return x

# Exact epoch maps.
for _ in range(1000):
    h = rng.uniform(0.001,1.999)
    b = 10**rng.uniform(-1,1)
    x = rng.uniform(-5*b,5*b)
    r = (1-h)**2
    delta = h*h*b
    y_pm = epoch_direct(x,h,b,(1,-1))
    y_mp = epoch_direct(x,h,b,(-1,1))
    assert abs(y_pm-(r*x-delta)) < 2e-12*max(1.0,abs(x),b)
    assert abs(y_mp-(r*x+delta)) < 2e-12*max(1.0,abs(x),b)

# Variance identity and equality with the N=2 exact quadratic MSD formula
# in the defining source.
for _ in range(1000):
    h = rng.uniform(0.001,1.999)
    b = 10**rng.uniform(-1,1)
    r = (1-h)**2
    delta = h*h*b
    var = delta*delta/(1-r*r)
    source = h*h * (
        2.0/(2*h-h*h)
        - (1-(1-h)**2)/(h*h*(1+(1-h)**2))
    ) * b*b
    assert abs(var-source) < 3e-10*max(1.0,var)

# Cantor-regime first-level and finite-depth separation plus exact gap.
for h in (0.4,0.6,0.9,1.0,1.1,1.4,1.6):
    r=(1-h)**2
    if r >= 0.5:
        continue
    b=1.3
    delta=h*h*b
    g=delta*(1-2*r)/(1-r) if r>0 else delta
    if r == 0:
        assert abs(g-b) < 1e-15
        continue
    # Enumerate depth-12 cylinders and bound each remaining tail.
    n=12
    tail=delta*(r**n)/(1-r)
    vals=[]
    for signs in itertools.product((-1,1), repeat=n):
        s=sum(delta*(r**j)*signs[j] for j in range(n))
        vals.append((s-tail,s+tail))
    for lo,hi in vals:
        assert hi <= -g + 2e-12 or lo >= g - 2e-12
    assert any(abs(hi+g) < 1e-9 for lo,hi in vals) or any(abs(lo-g) < 1e-9 for lo,hi in vals)

# At r=1/2, the two affine images exactly tile the invariant interval.
for h in (1-1/math.sqrt(2), 1+1/math.sqrt(2)):
    r=(1-h)**2
    assert abs(r-0.5) < 1e-14
    b=0.9
    delta=h*h*b
    M=delta/(1-r)
    left=(-r*M-delta, r*M-delta)
    right=(-r*M+delta, r*M+delta)
    assert abs(left[0]+M) < 1e-12
    assert abs(left[1]) < 1e-12
    assert abs(right[0]) < 1e-12
    assert abs(right[1]-M) < 1e-12
    assert abs(M-2*delta) < 1e-12

# Support connectivity threshold translated to the normalized step.
for _ in range(1000):
    h=rng.uniform(0.001,1.999)
    r=(1-h)**2
    avoid = r < 0.5
    band = (1-1/math.sqrt(2) < h < 1+1/math.sqrt(2))
    assert avoid == band

print("verification passed")
