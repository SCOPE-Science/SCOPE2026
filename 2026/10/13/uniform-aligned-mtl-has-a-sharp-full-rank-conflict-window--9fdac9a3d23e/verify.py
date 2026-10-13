import math
import random
import numpy as np

def aligned_direction(g1,g2):
    G=np.stack([g1,g2],axis=1)
    H=G.T@G
    vals,V=np.linalg.eigh(H)
    assert vals[0]>0
    sig=np.sqrt(vals)
    smin=sig[0]
    Hm12=V@np.diag(1.0/sig)@V.T
    Ghat=smin*G@Hm12
    return Ghat@np.array([0.5,0.5])

def terms(a,b,rho):
    s=math.sqrt(max(0.0,1.0-rho*rho))
    return a+b*(rho+s), b+a*(rho+s)

random.seed(350075)
for _ in range(4000):
    rho=random.uniform(-0.999,0.999)
    q=10.0**random.uniform(-2,2)
    g1=np.array([q,0.0])
    g2=np.array([rho,math.sqrt(1-rho*rho)])
    d=aligned_direction(g1,g2)
    dots=(g1@d,g2@d)
    t=terms(q,1.0,rho)
    for x,y in zip(dots,t):
        if abs(y)>1e-8:
            assert x*y>0

for rho in (-0.72,-0.8,-0.9,-0.97):
    tau=-rho-math.sqrt(1-rho*rho)
    assert 0<tau<1
    tests=[
        (0.5*tau,(-1,1)),
        (tau,(0,1)),
        (1.0,(1,1)),
        (1.0/tau,(1,0)),
        (2.0/tau,(1,-1)),
    ]
    for q,expected in tests:
        g1=np.array([q,0.0])
        g2=np.array([rho,math.sqrt(1-rho*rho)])
        d=aligned_direction(g1,g2)
        dots=(g1@d,g2@d)
        signs=[]
        for x in dots:
            if abs(x)<2e-8:
                signs.append(0)
            elif x>0:
                signs.append(1)
            else:
                signs.append(-1)
        assert tuple(signs)==expected,(rho,q,dots,expected)

for rho in (-1/math.sqrt(2)+1e-6,-0.5,0.0,0.5,0.95):
    for q in (1e-4,0.01,1.0,100.0,1e4):
        g1=np.array([q,0.0])
        g2=np.array([rho,math.sqrt(1-rho*rho)])
        d=aligned_direction(g1,g2)
        assert g1@d>0 and g2@d>0

for rho in (-0.99,-0.8,-0.3,0.0,0.2,0.8,0.99):
    g1=np.array([1.0,0.0])
    g2=np.array([rho,math.sqrt(1-rho*rho)])
    d=aligned_direction(g1,g2)
    mean=0.5*(g1+g2)
    if rho<=0:
        assert np.linalg.norm(d-mean)<3e-12
    else:
        fac=math.sqrt((1-rho)/(1+rho))
        assert np.linalg.norm(d-fac*mean)<3e-12

print("verification passed")
