import math
import random

rng = random.Random(350068)

def step(x, a, b, h):
    f = 0.5*a*x*x
    if f > b:
        return (1.0-h)*x
    if f < b:
        return (1.0+h)*x
    return x

# Direct multiplicative formula and log rotation.
for _ in range(2000):
    a = 10**rng.uniform(-1,1)
    b = 10**rng.uniform(-1,1)
    h = rng.uniform(0.01,0.99)
    r = math.sqrt(2*b/a)
    x = (1 if rng.random()<0.5 else -1) * r * math.exp(rng.uniform(-5,5))
    if abs(abs(x)-r) < 1e-12*r:
        continue
    xp = step(x,a,b,h)
    A = math.log1p(h)
    B = -math.log1p(-h)
    u = math.log(abs(x)/r)
    up = math.log(abs(xp)/r)
    target = u+A if u<0 else u-B
    assert abs(up-target) < 3e-13*max(1.0,abs(target))

# Every generic orbit enters the invariant band.
for _ in range(500):
    a = 10**rng.uniform(-1,1)
    b = 10**rng.uniform(-1,1)
    h = rng.uniform(0.02,0.98)
    r = math.sqrt(2*b/a)
    x = r*math.exp(rng.uniform(-20,20))
    A=math.log1p(h)
    B=-math.log1p(-h)
    entered=False
    for _j in range(10000):
        u=math.log(abs(x)/r)
        if -B-1e-12 <= u < A+1e-12:
            entered=True
            break
        x=step(x,a,b,h)
    assert entered

# Golden-ratio resonance: an explicit non-boundary log orbit has period three.
h=(math.sqrt(5)-1)/2
A=math.log1p(h)
a=1.7
b=0.8
r=math.sqrt(2*b/a)
x0=r*math.exp(-A/2)
x=x0
vals=[]
for _ in range(3):
    vals.append(math.log(abs(x)/r)/A)
    x=step(x,a,b,h)
assert max(abs(v-t) for v,t in zip(vals,[-0.5,0.5,-1.5])) < 5e-13
assert abs(x-x0) < 5e-13*max(1.0,abs(x0))

# h=1: generic points collapse to zero; dyadic preimages hit the boundary.
# Choose a=2, b=1 so the flood radius is exactly 1 in binary floating point.
a=2.0
b=1.0
r=1.0
generic = [1.3*r, 0.83*r, 0.37*r, 0.11*r, 0.013*r, -0.73*r]
for x0 in generic:
    # Exclude accidental dyadic boundary hits numerically.
    q=abs(x0)/r
    assert all(abs(q*2**n-1)>1e-10 for n in range(20))
    x=x0
    for _ in range(50):
        x=step(x,a,b,1.0)
        if x==0.0:
            break
    assert x==0.0

for n in range(8):
    x=r/(2**n)
    for _ in range(n):
        x=step(x,a,b,1.0)
    assert abs(x-r) < 2e-14*max(1.0,r)
    assert step(x,a,b,1.0)==x

# Solve rho(h)=sqrt(2)-1, an irrational target, and test ergodic formulas.
target_rho=math.sqrt(2)-1
lo,hi=1e-8,1-1e-10
def rho(h):
    return math.log1p(h)/math.log((1+h)/(1-h))
# rho decreases continuously from 1/2 to 0.
for _ in range(100):
    mid=(lo+hi)/2
    if rho(mid) > target_rho:
        lo=mid
    else:
        hi=mid
h=(lo+hi)/2
assert abs(rho(h)-target_rho)<2e-15

a=1.0
b=1.0
r=math.sqrt(2)
A=math.log1p(h)
B=-math.log1p(-h)
L=A+B
# Rotate directly to avoid floating state drift from repeated exp/log.
s=(0.123456789*L) % L
N=400000
above=0
sumloss=0.0
for _ in range(N):
    u=s-B
    if u>0:
        above += 1
    sumloss += b*math.exp(2*u)
    s=(s+A) % L
emp_above=above/N
emp_mean=sumloss/N
theory_mean=b*h/math.atanh(h)
assert abs(emp_above-target_rho)<2e-5
assert abs(emp_mean-theory_mean)<5e-5

# Mean is strictly below the flood level.
assert theory_mean < b

print("verification passed")
