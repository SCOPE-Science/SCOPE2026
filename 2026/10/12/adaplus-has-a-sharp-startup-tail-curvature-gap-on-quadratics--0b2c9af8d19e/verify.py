import math
import random

rng = random.Random(350075)

def first_step(x, h, a, b1, b2, eps):
    g = h*x
    m = (1-b1)*g
    s = (1-b2)*(g-m)*(g-m) + eps
    mbar = b1*m + (1-b1)*g
    mhat = mbar/(1-b1)
    shat = s/(1-b2)
    return x - a*mhat/(math.sqrt(shat)+eps)

def closed_first_step(x, h, a, b1, b2, eps):
    den = math.sqrt(b1*b1*h*h*x*x + eps/(1-b2)) + eps
    return x*(1 - a*(1+b1)*h/den)

for _ in range(1000):
    b1 = rng.uniform(0.0,0.98)
    b2 = rng.uniform(0.0,0.9995)
    eps = 10**rng.uniform(-10,-3)
    a = 10**rng.uniform(-5,-1)
    h = 10**rng.uniform(-2,3)
    x = rng.uniform(-3,3)
    if abs(x) < 1e-9:
        x = 0.2
    u = first_step(x,h,a,b1,b2,eps)
    v = closed_first_step(x,h,a,b1,b2,eps)
    assert abs(u-v) <= 3e-12*max(1.0,abs(u),abs(v))

def matrix_entries(h,a,b1,b2,eps):
    D = math.sqrt(eps/(1-b2)) + eps
    tau = a/D
    A11 = 1-tau*(1-b1*b1)*h
    A12 = -tau*b1*b1
    A21 = (1-b1)*h
    A22 = b1
    return D,tau,A11,A12,A21,A22

for _ in range(500):
    b1 = rng.uniform(0.0,0.98)
    b2 = rng.uniform(0.0,0.999)
    eps = 10**rng.uniform(-10,-3)
    a = 10**rng.uniform(-5,-1)
    D = math.sqrt(eps/(1-b2))+eps
    hcrit = 2*(1+b1)*D/(a*(1-b1)*(1+2*b1))
    h = hcrit*rng.uniform(0.05,1.5)
    D,tau,A11,A12,A21,A22 = matrix_entries(h,a,b1,b2,eps)
    tr = A11+A22
    det = A11*A22-A12*A21
    j1 = 1-tr+det
    j2 = 1+tr+det
    j3 = 1-det
    assert abs(j1 - tau*(1-b1)*h) < 2e-10*max(1.0,abs(j1))
    assert abs(j2 - (2*(1+b1)-tau*(1-b1)*(1+2*b1)*h)) < 2e-10*max(1.0,abs(j2))
    assert abs(j3 - ((1-b1)*(1+tau*b1*h))) < 2e-10*max(1.0,abs(j3))
    stable = (j1>0 and j2>0 and j3>0)
    assert stable == (h < hcrit)

# Boundary root r=-1.
for b1 in (0.0,0.2,0.9,0.97):
    b2=0.999
    eps=1e-8
    a=1e-3
    D=math.sqrt(eps/(1-b2))+eps
    hcrit=2*(1+b1)*D/(a*(1-b1)*(1+2*b1))
    D,tau,A11,A12,A21,A22=matrix_entries(hcrit,a,b1,b2,eps)
    tr=A11+A22
    det=A11*A22-A12*A21
    pminus=1+tr+det
    assert abs(pminus) < 2e-12

# Published defaults.
a=1e-3
b1=0.9
b2=0.999
eps=1e-8
D=math.sqrt(eps/(1-b2))+eps
hstart=2*D/(a*(1+b1))
htail=2*(1+b1)*D/(a*(1-b1)*(1+2*b1))
ratio=htail/hstart
assert abs(hstart-3.3287238528088183) < 2e-13
assert abs(htail-42.916761102285136) < 3e-12
assert abs(ratio-12.892857142857148) < 2e-13

h=10.0
gain=a*(1+b1)*h/D
limit_ratio=(1-gain)**2
assert abs(limit_ratio-25.08315457587596) < 2e-12

# Small nonzero starts approach the stated limiting objective ratio.
for x in (1e-6,1e-8,1e-10,1e-12):
    x1=first_step(x,h,a,b1,b2,eps)
    rr=(x1/x)**2
    if x <= 1e-8:
        assert abs(rr-limit_ratio) < 2e-5

print("verification passed")
