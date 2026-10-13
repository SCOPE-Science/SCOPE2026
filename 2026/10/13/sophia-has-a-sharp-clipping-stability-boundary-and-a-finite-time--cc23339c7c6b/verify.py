import math
import random

def clip(z):
    return max(-1.0, min(1.0, z))

def practical_step(x, h, eta, gamma, eps):
    g=h*x
    denom=max(gamma*h, eps)
    return x-eta*clip(g/denom)

def reduced_step(x, eta, gamma):
    return x-eta*clip(x/gamma)

def entry_time(x0, eta, gamma):
    return max(0, math.ceil((abs(x0)-gamma)/eta))

rng=random.Random(350089)

# Curvature cancellation.
for h in (1e-6,1e-2,1.0,17.0,1e6):
    for gamma in (1e-3,0.2,2.0,100.0):
        eps=0.5*gamma*h
        for eta in (0.1*gamma,0.7*gamma,1.0*gamma,1.8*gamma):
            for x in (-100*gamma,-1.2*gamma,-0.3*gamma,0.2*gamma,1.7*gamma,50*gamma):
                a=practical_step(x,h,eta,gamma,eps)
                b=reduced_step(x,eta,gamma)
                assert abs(a-b) < 2e-12*max(1.0,abs(a),abs(b))

# Exact entry and post-entry law in stable range.
for _ in range(10000):
    gamma=10**rng.uniform(-2,2)
    eta=rng.uniform(1e-4,1.9999)*gamma
    x0=rng.uniform(-100.0,100.0)*gamma
    n=entry_time(x0,eta,gamma)
    x=x0
    for _ in range(n):
        x=reduced_step(x,eta,gamma)
    assert abs(x) <= gamma + 1e-9*max(1.0,gamma)
    q=1.0-eta/gamma
    y=x
    for _ in range(8):
        y2=reduced_step(y,eta,gamma)
        assert abs(y2-q*y) < 2e-9*max(1.0,abs(y2),abs(q*y))
        y=y2

# Strict objective descent on random diagonal quadratics.
for _ in range(3000):
    d=5
    gamma=10**rng.uniform(-2,2)
    eta=rng.uniform(1e-4,1.9999)*gamma
    h=[10**rng.uniform(-3,3) for _ in range(d)]
    x=[rng.uniform(-20,20)*gamma for _ in range(d)]
    def F(z):
        return 0.5*sum(hh*zz*zz for hh,zz in zip(h,z))
    y=[reduced_step(xx,eta,gamma) for xx in x]
    if any(abs(xx)>1e-12 for xx in x):
        assert F(y) < F(x) + 1e-9*max(1.0,F(x))

# Exact two-cycle at and above boundary.
for gamma in (0.1,1.0,10.0):
    for eta in (2.0*gamma,2.1*gamma,5.0*gamma,100.0*gamma):
        x=eta/2.0
        y=reduced_step(x,eta,gamma)
        z=reduced_step(y,eta,gamma)
        assert abs(y+x) < 2e-12*max(1.0,abs(x))
        assert abs(z-x) < 2e-12*max(1.0,abs(x))

# Resonance eta=gamma: repeated soft thresholding on deterministic cases.
for gamma in (0.125,1.0,8.0):
    for mult in (-10.3,-3.0,-1.2,-1.0,-0.3,0.0,0.3,1.0,1.2,3.0,10.3):
        x0=mult*gamma
        x=x0
        for t in range(20):
            if x0>0:
                closed=max(x0-t*gamma,0.0)
            elif x0<0:
                closed=-max(-x0-t*gamma,0.0)
            else:
                closed=0.0
            assert abs(x-closed) < 2e-12*max(1.0,abs(x0),gamma)
            x=reduced_step(x,gamma,gamma)

print('verification passed')
