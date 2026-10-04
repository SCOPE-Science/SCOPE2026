import math, random

def clip(x, lo, hi):
    return max(lo, min(x, hi))

def step(x, h, alpha0, beta1, beta2, lo, hi):
    g = h*x
    m = (1.0-beta1)*g
    v = (1.0-beta2)*g*g
    raw = alpha0/math.sqrt(v)
    eta = clip(raw, lo, hi)
    return x-eta*m, raw, eta

random.seed(7)

# Exact recurrence check.
for _ in range(500):
    h = 10.0**random.uniform(-2,2)
    alpha0 = 10.0**random.uniform(-5,-1)
    beta1 = random.uniform(0.0,0.99)
    beta2 = random.uniform(0.0,0.9999)
    lo = 10.0**random.uniform(-6,-2)
    hi = lo*10.0**random.uniform(0.0,5.0)
    x = (1 if random.random()<0.5 else -1)*10.0**random.uniform(-8,2)
    xn, raw, eta = step(x,h,alpha0,beta1,beta2,lo,hi)
    ratio = (xn/x)**2
    expected = (1.0-(1.0-beta1)*h*eta)**2
    assert abs(ratio-expected) < 2e-12*max(1.0,abs(expected))

# Safe side.
for _ in range(200):
    h = 10.0**random.uniform(-2,2)
    beta1 = random.uniform(0.0,0.95)
    beta2 = random.uniform(0.0,0.999)
    alpha0 = 10.0**random.uniform(-5,-1)
    hi = 2.0/((1.0-beta1)*h) * random.uniform(0.05,1.0)
    lo = hi*random.uniform(0.0,0.8)
    for xmag in (1e-12,1e-9,1e-6,1e-3,1.0,1e3):
        xn,_,_=step(xmag,h,alpha0,beta1,beta2,lo,hi)
        assert xn*xn <= xmag*xmag*(1.0+2e-12)

# Unsafe upper-clipped plateau.
for _ in range(200):
    h = 10.0**random.uniform(-1,1)
    beta1 = random.uniform(0.0,0.9)
    beta2 = random.uniform(0.0,0.999)
    alpha0 = 10.0**random.uniform(-5,-2)
    hi = 2.0/((1.0-beta1)*h) * random.uniform(1.01,10.0)
    lo = hi*random.uniform(0.0,0.5)
    r = alpha0/(math.sqrt(1.0-beta2)*h*hi)
    target=(1.0-(1.0-beta1)*h*hi)**2
    assert target > 1.0
    for frac in (1e-6,0.01,0.2,0.9,1.0):
        x=frac*r
        xn,raw,eta=step(x,h,alpha0,beta1,beta2,lo,hi)
        assert raw >= hi*(1.0-2e-12)
        assert abs(eta-hi) < 1e-12*max(1.0,hi)
        assert abs((xn/x)**2-target) < 2e-10*max(1.0,target)

# Paper-stated defaults.
beta1=0.9
beta2=0.999
alpha_star=0.1
alpha0=1e-3
h=1.0
u1=alpha_star*(1.0+1.0/(1.0-beta2))
hcrit=2.0/((1.0-beta1)*u1)
amp=(1.0-(1.0-beta1)*h*u1)**2
radius=alpha0/(math.sqrt(1.0-beta2)*h*u1)

assert abs(u1-100.1) < 2e-10
assert abs(hcrit-0.1998001998001998) < 2e-13
assert abs(amp-81.1801) < 2e-10
assert abs(radius-3.1591185416267526e-4) < 2e-16

xn,raw,eta=step(radius*0.5,h,alpha0,beta1,beta2,0.0,u1)
assert abs(eta-u1) < 1e-12
assert abs((xn/(radius*0.5))**2-81.1801) < 2e-10

print("verification passed")
