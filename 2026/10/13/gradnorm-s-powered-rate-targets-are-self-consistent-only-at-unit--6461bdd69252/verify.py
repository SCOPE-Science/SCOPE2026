import math
import random

def mean(xs):
    return sum(xs)/len(xs)

def residual(a, w, r, alpha):
    G=[wi*ai for wi,ai in zip(w,a)]
    Gbar=mean(G)
    s=[ri**alpha for ri in r]
    L=sum(abs(gi-Gbar*si) for gi,si in zip(G,s))
    return L/sum(G), Gbar, G, s

def weights_from_x(a,x):
    T=len(a)
    den=sum(xi/ai for xi,ai in zip(x,a))
    return [T*(xi/ai)/den for xi,ai in zip(x,a)]

random.seed(350072)

# Universal lower bound and sharpness.
for _ in range(4000):
    T=random.randint(2,12)
    a=[10.0**random.uniform(-2,2) for _ in range(T)]
    raw=[10.0**random.uniform(-2,2) for _ in range(T)]
    mr=mean(raw)
    r=[z/mr for z in raw]
    alpha=10.0**random.uniform(-1.3,0.7)
    s=[ri**alpha for ri in r]
    M=mean(s)

    # Arbitrary positive weights normalized to sum T.
    wr=[10.0**random.uniform(-2,2) for _ in range(T)]
    sw=sum(wr)
    w=[T*z/sw for z in wr]
    ratio,_,_,_=residual(a,w,r,alpha)
    assert ratio + 2e-12 >= abs(1.0-M)

    # Explicit equality construction.
    if M < 1.0:
        x=[si+(1.0-M) for si in s]
    elif M > 1.0:
        x=[si/M for si in s]
    else:
        x=s[:]
    assert abs(mean(x)-1.0) < 2e-12
    ws=weights_from_x(a,x)
    ratio2,_,_,_=residual(a,ws,r,alpha)
    assert abs(ratio2-abs(1.0-M)) < 2e-10
    assert all(z>0 for z in ws)
    assert abs(sum(ws)-T) < 2e-11

# Strict Jensen phase for heterogeneous positive rates of mean one.
for _ in range(1000):
    T=random.randint(2,10)
    raw=[10.0**random.uniform(-1,1) for _ in range(T)]
    # Force heterogeneity well above roundoff.
    raw[0]*=2.0
    mr=mean(raw)
    r=[z/mr for z in raw]
    assert max(r)-min(r) > 1e-6
    assert mean([z**0.3 for z in r]) < 1.0-1e-10
    assert abs(mean(r)-1.0) < 2e-15
    assert mean([z**1.7 for z in r]) > 1.0+1e-10

# Mean-renormalized powered target is exactly realizable.
for _ in range(2500):
    T=random.randint(2,12)
    a=[10.0**random.uniform(-2,2) for _ in range(T)]
    raw=[10.0**random.uniform(-2,2) for _ in range(T)]
    mr=mean(raw)
    r=[z/mr for z in raw]
    alpha=random.uniform(0.05,3.0)
    s=[z**alpha for z in r]
    M=mean(s)
    w=[T*(si/ai)/sum(sj/aj for sj,aj in zip(s,a)) for si,ai in zip(s,a)]
    G=[wi*ai for wi,ai in zip(w,a)]
    Gbar=mean(G)
    target=[Gbar*si/M for si in s]
    assert max(abs(x-y) for x,y in zip(G,target)) < 2e-10*max(1.0,max(G))
    assert abs(sum(w)-T) < 2e-11

print("verification passed")
