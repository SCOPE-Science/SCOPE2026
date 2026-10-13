import math
import random

def step(r,z,post):
    mult=abs(1.0-1.0/z)
    rn=mult*r
    zn=z+(rn*rn if post else r*r)/z
    return rn,zn

def run(r0,z0,post,n=200000):
    r,z=r0,z0
    hist=[(r,z)]
    for _ in range(n):
        r,z=step(r,z,post)
        hist.append((r,z))
        if r<1e-14:
            break
    return hist

# Exact one-step objective ratio and sharp barrier.
for post in (False,True):
    for z in (0.03,0.2,0.499,0.5,0.501,0.8,1.0,3.0,100.0):
        r=1.7
        rn,zn=step(r,z,post)
        ratio=(rn/r)**2
        closed=(1-1/z)**2
        assert abs(ratio-closed)<2e-13*max(1.0,closed)
        if z<0.5: assert ratio>1.0
        if z==0.5: assert abs(ratio-1.0)<1e-14
        if z>0.5: assert ratio<1.0

# Finite unsafe prefix and stated count bound.
for post in (False,True):
    for z0 in (0.01,0.05,0.2,0.49):
        for r0 in (0.05,0.2,1.0,4.0):
            h=run(r0,z0,post,20000)
            K=next(i for i,(r,z) in enumerate(h) if z>=0.5)
            bound=math.ceil((0.5-z0)/(2*r0*r0))
            assert K<=bound
            # Every earlier step increases objective and none after K does.
            for k in range(min(len(h)-1,K)):
                assert h[k+1][0] > h[k][0]
            for k in range(K,min(len(h)-1,K+500)):
                assert h[k+1][0] <= h[k][0]*(1+2e-13)

# Structural boundedness identities above z=1, checked directly.
random.seed(350088)
for post in (False,True):
    for _ in range(12000):
        z=10**random.uniform(0,3)
        r=10**random.uniform(-6,2)
        rn,zn=step(r,z,post)
        assert zn>=z
        if z>1.0+1e-12:
            # Radius decrease controls scale growth; this is the telescoping proof step.
            assert (r*r-rn*rn) >= (zn-z)-2e-10*max(1.0,r*r,zn)
        if z>=0.5:
            assert rn <= r*(1+2e-13)

# Representative aggressive starts cross the barrier, then remain monotone.
for post in (False,True):
    for z0,r0 in ((1e-3,1.0),(1e-2,0.3),(0.1,1.0),(0.3,0.2)):
        h=run(r0,z0,post,20000)
        assert (1/z0)>2.0
        assert h[1][0]>h[0][0]
        K=next(i for i,(r,z) in enumerate(h) if z>=0.5)
        for i in range(K,min(len(h)-1,K+2000)):
            assert h[i+1][0] <= h[i][0]*(1+2e-13)
        assert h[-1][0] < h[K][0]

print('verification passed')
