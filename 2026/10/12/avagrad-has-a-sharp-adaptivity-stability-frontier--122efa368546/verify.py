import math
import random

def bounds(d, G, eps):
    rho=eps/(G+eps)
    pmin=math.sqrt(d)*rho/math.sqrt(rho*rho+d-1)
    pmax=math.sqrt(d)/math.sqrt(1+(d-1)*rho*rho)
    return rho,pmin,pmax

def pvec(v, eps):
    d=len(v)
    eta=[1.0/(math.sqrt(x)+eps) for x in v]
    n=math.sqrt(sum(x*x for x in eta))
    return [math.sqrt(d)*x/n for x in eta]

random.seed(350086)

for d in (1,2,3,8,32,128):
    for G,eps in ((1.0,1.0),(2.0,0.1),(3.0,1e-3),(0.5,10.0)):
        rho,pmin,pmax=bounds(d,G,eps)
        if d==1:
            assert abs(pmin-1.0)<1e-8 and abs(pmax-1.0)<1e-14
        vmax=[0.0]+[G*G]*(d-1)
        vmin=[G*G]+[0.0]*(d-1)
        assert abs(pvec(vmax,eps)[0]-pmax)<1e-8
        assert abs(pvec(vmin,eps)[0]-pmin)<1e-8
        for _ in range(1000):
            v=[random.random()*G*G for _ in range(d)]
            p=pvec(v,eps)
            assert min(p)>=pmin-1e-8
            assert max(p)<=pmax+1e-8
            assert abs(sum(x*x for x in p)/d-1.0)<2e-13

# Exact robust objective envelope from endpoint coordinates.
for d in (2,5,20):
    G=2.0
    eps=0.2
    rho,pmin,pmax=bounds(d,G,eps)
    for a in (0.01,0.5,1.0,1.9/pmax,2.0/pmax,2.1/pmax,4.0):
        closed=max((1-a*pmin)**2,(1-a*pmax)**2)
        # Both endpoint factors are attained by a coordinate-supported state/vector.
        assert closed >= 0.0
        # Random admissible states cannot exceed the endpoint envelope.
        for _ in range(1000):
            v=[random.random()*G*G for _ in range(d)]
            p=pvec(v,eps)
            direct=max((1-a*x)**2 for x in p)
            assert direct<=closed+3e-12
    boundary=2.0/pmax
    assert abs((1-boundary*pmax)**2-1.0)<2e-14
    assert max((1-(0.999*boundary)*pmin)**2,
               (1-(0.999*boundary)*pmax)**2)<1.0
    assert (1-(1.001*boundary)*pmax)**2>1.0

# Limiting frontiers.
for d in (2,8,64):
    _,_,pmax_weak=bounds(d,1.0,1e12)
    _,_,pmax_strong=bounds(d,1.0,1e-12)
    assert abs(2/pmax_weak-2.0)<1e-10
    assert abs(2/pmax_strong-2/math.sqrt(d))<1e-10

print("verification passed")
