import math
import random

def agc_grad(x,h,lam,eps):
    if x == 0.0:
        return 0.0
    g=h*x
    wstar=max(abs(x),eps)
    if abs(g)/wstar > lam:
        return lam*wstar*(1.0 if g>0.0 else -1.0)
    return g

def step(x,h,lam,eps,eta):
    return x-eta*agc_grad(x,h,lam,eps)

random.seed(350072)

# Exact three-zone formula.
for _ in range(5000):
    h=10.0**random.uniform(-2.0,3.0)
    lam=h*random.uniform(0.001,0.999)
    eps=10.0**random.uniform(-6.0,2.0)
    a=lam*eps/h
    x=(1.0 if random.random()<0.5 else -1.0)*eps*10.0**random.uniform(-4.0,3.0)
    g=agc_grad(x,h,lam,eps)
    if abs(x) <= a:
        target=h*x
    elif abs(x) < eps:
        target=lam*eps*(1.0 if x>0.0 else -1.0)
    else:
        target=lam*x
    assert abs(g-target) < 2e-12*max(1.0,abs(target))

# Strict magnitude contraction below eta*h=2.
for _ in range(1000):
    h=10.0**random.uniform(-2.0,2.0)
    lam=h*random.uniform(0.01,0.99)
    eps=10.0**random.uniform(-5.0,1.0)
    eta=random.uniform(1e-9,1.999999/h)
    a=lam*eps/h
    probes=[a*0.2,a,a*1.2,(a+eps)/2.0,eps,eps*2.0,eps*100.0]
    for sign in (-1.0,1.0):
        for mag in probes:
            x=sign*mag
            xn=step(x,h,lam,eps,eta)
            assert abs(xn) < abs(x)+2e-14*max(1.0,abs(x))

# Endpoint and interior two-cycles.
for _ in range(1500):
    h=10.0**random.uniform(-2.0,2.0)
    lam=h*random.uniform(0.01,0.99)
    eps=10.0**random.uniform(-5.0,1.0)
    eta=random.uniform(2.0/h,2.0/lam)
    a=lam*eps/h
    s=eta*lam*eps
    lo=max(a,s-eps)
    hi=min(eps,s-a)
    assert lo <= hi + 2e-13*max(1.0,eps)
    for x in (lo,(lo+hi)/2.0,hi):
        y=step(x,h,lam,eps,eta)
        z=step(y,h,lam,eps,eta)
        assert abs(z-x) < 3e-11*max(1.0,eps)

# The exact lower endpoint is the raw-gradient sign-flip cycle at x=a.
for h,lam,eps in [(5.0,1.0,0.001),(100.0,0.01,0.001),(2.0,0.7,3.0)]:
    a=lam*eps/h
    eta=2.0/h
    assert abs(step(a,h,lam,eps,eta)+a) < 1e-14*max(1.0,eps)

# The exact upper endpoint is the outer sign-flip cycle at x=eps.
for h,lam,eps in [(5.0,1.0,0.001),(100.0,0.01,0.001),(2.0,0.7,3.0)]:
    eta=2.0/lam
    assert abs(step(eps,h,lam,eps,eta)+eps) < 1e-13*max(1.0,eps)

# Above eta*lambda=2, large outer points diverge geometrically.
for _ in range(500):
    h=10.0**random.uniform(-2.0,2.0)
    lam=h*random.uniform(0.01,0.99)
    eps=10.0**random.uniform(-5.0,1.0)
    eta=random.uniform(2.000001/lam,5.0/lam)
    x=100.0*eps
    factor=abs(1.0-eta*lam)
    for _ in range(6):
        xn=step(x,h,lam,eps,eta)
        assert abs(abs(xn)/abs(x)-factor) < 2e-13
        x=xn
        assert abs(x) >= eps

# Formal floorless comparison.
for _ in range(1000):
    h=10.0**random.uniform(-2.0,2.0)
    lam=h*random.uniform(0.01,0.99)
    eta=random.uniform(1e-8,1.999999/lam)
    x=(1.0 if random.random()<0.5 else -1.0)*10.0**random.uniform(-5.0,5.0)
    assert abs(step(x,h,lam,0.0,eta)-(1.0-eta*lam)*x) < 2e-11*max(1.0,abs(x))

print("verification passed")
