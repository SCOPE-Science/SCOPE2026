"""Independent numerical checks of inverse-fiber counts for a star sine phase map.
This finite diagnostic is not an infinite proof. Requires scipy and numpy.
"""
import math
import numpy as np
from scipy.optimize import brentq


def scalar_f(c, s):
    return s - c*math.sin(s)


def one_step_preimages(c, t):
    """Find all preimages on the circle by splitting at exact critical points."""
    sc = math.acos(1/c) if c>1 else 0
    grid=[-math.pi,-sc,sc,math.pi] if c>1 else [-math.pi,math.pi]
    points=[]
    for lo,hi in zip(grid[:-1],grid[1:]):
        for target in [t]:
            flo=scalar_f(c,lo)-target; fhi=scalar_f(c,hi)-target
            if abs(flo)<1e-12: points.append(lo)
            if abs(fhi)<1e-12: points.append(hi)
            if flo*fhi<0: points.append(brentq(lambda s:scalar_f(c,s)-target,lo,hi,xtol=2e-14))
    uniq=[]
    for s in points:
        if not any(abs(s-x)<1e-10 for x in uniq): uniq.append(s)
    return sorted(uniq)


def all_preimages(c,t,n):
    pts=[t]
    for _ in range(n):
        pts2=[]
        for p in pts:
            pts2+=one_step_preimages(c,p)
        pts=sorted(pts2)
        assert all(abs(pts[i]-pts[i-1])>1e-9 for i in range(1,len(pts)))
    return pts


def network_step(d,h,u):
    v=np.sin(u)
    return u-h*(v+sum(v))


def preimage_test(d,c):
    h=c/(d+1)
    s_c=math.acos(1/c)
    a=math.sqrt(c*c-1)-s_c
    b=brentq(lambda x:scalar_f(c,x),s_c+1e-8,math.pi,xtol=1e-14)
    assert 0 < a < s_c < b < math.pi
    for n in range(1,8):
        pre=all_preimages(c,0,n)
        assert len(pre)==2*n+1,(d,c,n,len(pre))
        assert max(abs(scalar_f(c,s)) for s in pre)<math.pi
        for s in pre:
            inp=np.array([s]*d)
            out=network_step(d,h,inp)
            assert max(abs(out[0]-scalar_f(c,s)),abs(out[-1]-scalar_f(c,s)))<1e-12
    # Far enough from zero the number of exact n-step inverse fibers must settle.
    for t in [0.03,0.08,0.2,0.4,0.65,1.0]:
        counts=[len(all_preimages(c,t,n)) for n in range(1,9)]
        assert all(counts[j]<=counts[j+1] for j in range(len(counts)-1))
        if abs(t)>a: assert counts==[1]*len(counts)
    # For small nonzero targets, stable ancestor count has log singularity.
    slope=2/math.log(1/(c-1))
    def eventual_count(t):
        count=1; current=t
        while abs(current)<a:
            count+=2
            # central preimage on segment (-s_c,s_c)
            current=brentq(lambda s:scalar_f(c,s)-current,-s_c,s_c,xtol=1e-14)
        return count
    pairs=[(k,eventual_count(10**(-k))) for k in range(2,11)]
    errs=[(K-n*slope*math.log(10)) for n,K in pairs]
    assert abs((pairs[-1][1]-pairs[-4][1])-3*slope*math.log(10))<8, (c,errs)
    print('OK star dimension',d,'c',c,'a',a,'b',b,'depth-7 count',len(all_preimages(c,0,7)),'K(10^-10)',pairs[-1][1])

for d in (2,3,5,9):
    for c in (1.2,1.5,1.9):
        preimage_test(d,c)
print('ALL NUMERICAL DIAGNOSTICS PASSED')
