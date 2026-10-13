import math
import random

def pretrust(x,A,B,eps):
    return [A*z/(B*abs(z)+eps) for z in x]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm(a):
    return math.sqrt(dot(a,a))

def cosine(x,r):
    return dot(x,r)/(norm(x)*norm(r))

def step(x,eta,A,B,eps):
    r=pretrust(x,A,B,eps)
    nr=norm(r)
    nx=norm(x)
    return [z-eta*nx*q/nr for z,q in zip(x,r)]

def ratio(x,eta,A,B,eps):
    y=step(x,eta,A,B,eps)
    return dot(y,y)/dot(x,x)

random.seed(350084)

# Exact ratio identity and universal cosine bound.
for d in range(1,129):
    lower=1/math.sqrt(d)
    for _ in range(200):
        x=[random.uniform(-10,10) for _ in range(d)]
        if norm(x)<1e-12:
            x[0]=1.0
        A=10**random.uniform(-2,2)
        B=10**random.uniform(-2,2)
        eps=10**random.uniform(-8,1)
        r=pretrust(x,A,B,eps)
        c=cosine(x,r)
        assert c >= lower-2e-12
        eta=random.uniform(1e-4,2.0)
        closed=1-2*eta*c+eta*eta
        assert abs(ratio(x,eta,A,B,eps)-closed)<3e-12*max(1.0,abs(closed))

# Sharp family approaches 1/sqrt(d).
for d in (2,3,5,10,50,200):
    target=1/math.sqrt(d)
    vals=[]
    for M in (10.0,100.0,1e4,1e8):
        x=[M*M]+[M]*(d-1)
        r=pretrust(x,1.7,0.8,0.3)
        vals.append(cosine(x,r))
        assert vals[-1]>=target-2e-12
    assert abs(vals[-1]-target)<2e-7

# Sharp descent boundary: below is safe for all tested states; above has a sharp-family witness.
for d in (1,2,4,16,100):
    eta_star=2/math.sqrt(d)
    for eta in (0.25*eta_star,0.75*eta_star,eta_star):
        for _ in range(100):
            x=[random.uniform(-50,50) for _ in range(d)]
            if norm(x)<1e-12: x[0]=1.0
            assert ratio(x,eta,2.0,3.0,0.7) <= 1.0+3e-12
    eta=1.01*eta_star
    M=1e10
    x=[M*M]+[M]*(d-1) if d>1 else [M]
    assert ratio(x,eta,1.0,1.0,0.1)>1.0

print('verification passed')
