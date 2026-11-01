#!/usr/bin/env python3
"""Reproduce finite checks for a planar cross-polytope projection law.
Run with Python 3.10+ (standard library only). Numerical diagnostics do not replace the proof.
"""
import math
import random


def frame(n, rng):
    a=[rng.gauss(0,1) for _ in range(n)]
    ar=math.sqrt(sum(x*x for x in a)); u=[x/ar for x in a]
    z=[rng.gauss(0,1) for _ in range(n)]; inner=sum(x*y for x,y in zip(u,z))
    z=[x-inner*y for x,y in zip(z,u)]
    zr=math.sqrt(sum(x*x for x in z)); v=[x/zr for x in z]
    return list(zip(u,v))


def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def area(vertices):
    pts=sorted(set(vertices))
    if len(pts)<3:return 0.0
    lower=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    h=lower[:-1]+upper[:-1]
    return abs(sum(cross((0.0,0.0),h[i],h[(i+1)%len(h)]) for i in range(len(h))))/2


def minors(v):
    return [abs(cross((0,0),v[i],v[j])) for i in range(len(v)) for j in range(i+1,len(v))]


def beta_moment(n,k):
    return math.factorial(k)*math.factorial(n-2)/math.factorial(n+k-2)


def run():
    checks=0
    for n in range(3,14):
        for k in range(0,9):
            # The two independent Beta factors for the projected coordinate minor.
            b1=math.gamma(1+k/2)*math.gamma(n/2)/math.gamma((n+k)/2)
            b2=math.gamma((1+k)/2)*math.gamma((n-1)/2)/(math.sqrt(math.pi)*math.gamma((n-1+k)/2))
            assert abs(b1*b2-beta_moment(n,k))<1e-11
            checks+=1
    rng=random.Random(881201)
    threshold=math.sqrt(2/3)
    eps=.18
    for n in (3,4,5,6):
        N=24000
        count=0
        qsum=0
        q2sum=0
        event_mismatch=0
        high_pair_count=0
        for _ in range(N):
            v=frame(n,rng)
            q=minors(v)
            aq=area(v+[(-x,-y) for x,y in v])
            assert abs(sum(x*x for x in q)-1)<2e-12
            checks+=1
            maxq=max(q)
            if maxq>=threshold:
                assert abs(aq-2*maxq)<3e-11
                assert sum(x>=threshold for x in q)==1
                high_pair_count+=1
                checks+=2
            if aq>=2-eps:count+=1
            if (aq>=2-eps)!=(maxq>=1-eps/2):event_mismatch+=1
            qsum+=q[0];q2sum+=q[0]*q[0]
        expected=math.comb(n,2)*(eps/2)**(n-2)
        obs=count/N
        sigma=math.sqrt(expected*(1-expected)/N)
        assert abs(obs-expected)<6*sigma+0.0003,(n,obs,expected,sigma)
        assert event_mismatch==0,(n,event_mismatch)
        assert abs(qsum/N-beta_moment(n,1))<.024
        assert abs(q2sum/N-beta_moment(n,2))<.024
        checks+=4
        print('dimension',n,'frames',N,'upper-tail observed',round(obs,6),
              'exact-law prediction',round(expected,6),'high-pair cases',high_pair_count)
    # An exact parametrized small graph near a coordinate plane.
    for n in (3,4,5,8):
        vv=[(1.0,0.0),(0.0,5/math.sqrt(26)),(0.0,1/math.sqrt(26))]+[(0.0,0.0)]*(n-3)
        assert abs(area(vv+[(-x,-y) for x,y in vv])-10/math.sqrt(26))<2e-12
        checks+=1
    print('PASS:',checks,'deterministic analytical or finite-frame checks')

if __name__=='__main__':
    run()
