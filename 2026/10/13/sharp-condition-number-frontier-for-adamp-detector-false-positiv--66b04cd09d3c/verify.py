import math
import random

def cosine_diag(eigs, x):
    num=sum(lam*u*u for lam,u in zip(eigs,x))
    nx=math.sqrt(sum(u*u for u in x))
    nHx=math.sqrt(sum((lam*u)**2 for lam,u in zip(eigs,x)))
    return num/(nx*nHx)

def min_cosine(kappa):
    return 2.0*math.sqrt(kappa)/(kappa+1.0)

def frontier(d, delta):
    tau=delta/math.sqrt(d)
    return ((1.0+math.sqrt(1.0-tau*tau))/tau)**2

random.seed(350064)

# Randomized universal lower bound in the eigenbasis.
for _ in range(3000):
    d=random.randint(2,12)
    logs=sorted(random.random()*8.0 for _ in range(d))
    eigs=[math.exp(z) for z in logs]
    mu=min(eigs)
    L=max(eigs)
    kappa=L/mu
    x=[random.gauss(0.0,1.0) for _ in range(d)]
    c=cosine_diag(eigs,x)
    assert c >= min_cosine(kappa)-2e-14

# Equality witness on extremal eigendirections.
for kappa in (1.1,2.0,10.0,100.0,1000.0,1e6):
    mu=1.0
    L=kappa
    x_mu=math.sqrt(L/(mu+L))
    x_L=math.sqrt(mu/(mu+L))
    c=cosine_diag([mu,L],[x_mu,x_L])
    assert abs(c-min_cosine(kappa)) < 2e-14
    assert abs((x_L*x_L)/(x_mu*x_mu)-mu/L) < 2e-14

# Exact strict threshold behavior.
for d in (1,2,3,16,64,256):
    delta=0.1
    ks=frontier(d,delta)
    tau=delta/math.sqrt(d)
    assert abs(min_cosine(ks)-tau) < 2e-12
    assert min_cosine(ks*(1.0-1e-7)) > tau
    assert min_cosine(ks*(1.0+1e-7)) < tau

expected={
    1:397.9974874213239,
    2:797.9987468651999,
    64:25597.999960934438,
    256:102397.9999902342,
}
for d,val in expected.items():
    assert abs(frontier(d,0.1)-val) < 5e-10*max(1.0,val)

# Large-d asymptotic at source delta.
for d in (1000,10000,100000):
    ks=frontier(d,0.1)
    approx=400.0*d-2.0
    assert abs(ks-approx) < 2e-3

print("verification passed")
