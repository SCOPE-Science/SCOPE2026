import math
import random

rng = random.Random(350061)

def bhat(beta, t):
    return beta * (1.0 - beta**(t-1)) / (1.0 - beta**t)

def direct(beta1, beta2, G, eps, T):
    v = 0.0
    u = 0.0
    out = []
    for t in range(1, T+1):
        g = G if t == 1 else 0.0
        b1 = bhat(beta1, t)
        b2 = bhat(beta2, t)
        v = b1*v + (1.0-b1)*g
        u = b2*u + (1.0-b2)*g*g
        rms = math.sqrt(g*g / max(u, eps*eps))
        update_ratio = (1.0/max(1.0, rms)) * abs(v)/(math.sqrt(u)+eps)
        out.append((v,u,rms,update_ratio))
    return out

def cj(beta,t):
    return (1.0-beta)*beta**(t-1)/(1.0-beta**t)

def envelope(beta1,beta2,t):
    return (
        (1.0-beta1)/math.sqrt(1.0-beta2)
        * math.sqrt(1.0-beta2**t)/(1.0-beta1**t)
        * (beta1/math.sqrt(beta2))**(t-1)
    )

# Direct recurrence versus telescoped formulas.
for _ in range(500):
    b1 = rng.uniform(0.05,0.98)
    b2 = rng.uniform(0.05,0.999)
    G = math.copysign(10**rng.uniform(-2,5), rng.choice([-1.0,1.0]))
    eps = 10**rng.uniform(-10,-2)
    T = rng.randint(3,40)
    hist = direct(b1,b2,G,eps,T)
    for t,(v,u,rms,ratio) in enumerate(hist, start=1):
        assert abs(v-cj(b1,t)*G) < 5e-11*max(1.0,abs(v),abs(G))
        assert abs(u-cj(b2,t)*G*G) < 5e-10*max(1.0,abs(u),G*G)
        if t >= 2:
            assert rms == 0.0
            finite = cj(b1,t)*abs(G)/(math.sqrt(cj(b2,t))*abs(G)+eps)
            assert abs(ratio-finite) < 5e-12*max(1.0,finite)

# Fixed-t amplitude supremum approaches the exact envelope.
for _ in range(200):
    b1 = rng.uniform(0.1,0.95)
    b2 = rng.uniform(0.1,0.99)
    t = rng.randint(2,25)
    eps = 1e-6
    env = envelope(b1,b2,t)
    vals = [direct(b1,b2,10.0**k,eps,t)[-1][3] for k in (0,3,6,9)]
    assert vals == sorted(vals)
    assert vals[-1] <= env*(1+1e-10)
    assert abs(vals[-1]-env) < 2e-5*max(1.0,env)

# Unbounded side: envelope grows when beta1^2 > beta2.
for b1,b2 in [(0.9,0.5),(0.8,0.5),(0.7,0.4)]:
    assert b1*b1 > b2
    seq=[envelope(b1,b2,t) for t in (10,20,40,80)]
    assert seq[-1] > seq[-2] > seq[-3]
    assert seq[-1] > 10.0

# Bounded side: the analytic coarse bound is obeyed.
for b1,b2 in [(0.9,0.99),(0.9,0.9),(0.5,0.5),(0.8,0.64)]:
    assert b1*b1 <= b2 + 1e-15
    bound=1.0/math.sqrt(1.0-b2)
    for t in range(2,300):
        assert envelope(b1,b2,t) <= bound*(1+1e-12)

# Equality limit.
for b1 in (0.2,0.5,0.8,0.95):
    b2=b1*b1
    target=math.sqrt((1.0-b1)/(1.0+b1))
    got=envelope(b1,b2,10000)
    assert abs(got-target) < 2e-10*max(1.0,target)

# Source-discussed alternative: use v^2 in RMS numerator.
# The scalar normalized momentum update is always at most one base step.
for _ in range(20000):
    v=math.copysign(10**rng.uniform(-12,12),rng.choice([-1.0,1.0]))
    u=10**rng.uniform(-24,20)
    eps=10**rng.uniform(-12,-2)
    D=math.sqrt(max(u,eps*eps))
    rms_v=abs(v)/D
    ratio=(1.0/max(1.0,rms_v))*abs(v)/(math.sqrt(u)+eps)
    assert ratio <= 1.0 + 2e-14

# Paper-reported beta choices are on the bounded side for beta1=0.9.
for b2 in (0.9,0.95,0.98,0.99):
    assert 0.9**2 < b2

print("verification passed")
