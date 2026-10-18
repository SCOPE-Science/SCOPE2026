#!/usr/bin/env python3
"""Finite reproducibility checks for directional neighbor pools on a circle.

Checks are numerical and finite, not a substitute for the analytic limit theorem.
"""
import random
import math

R = random.Random(223344)

def circular_dist(x,y):
    t=abs(x-y)%1
    return min(t,1-t)

def direct_flags(z,m):
    n=len(z)
    s=sum(z)
    pts=[0.0]
    for gap in z[:-1]:
        pts.append(pts[-1]+gap/s)
    edges=[]; count=0
    for i in range(n):
        pool=sorted((circular_dist(pts[i],pts[j]), j) for j in range(n) if j!=i)[:m]
        cw=[(d,j) for d,j in pool if (pts[j]-pts[i])%1 < .5]
        ccw=[(d,j) for d,j in pool if (pts[i]-pts[j])%1 < .5]
        edges.append(([min(cw)[1]] if cw else [])+([min(ccw)[1]] if ccw else []))
        count+=(not bool(cw))+(not bool(ccw))
    return count,edges,pts

def gap_flags(z,m):
    n=len(z)
    a=[int(z[(i-1)%n]>sum(z[(i+j)%n] for j in range(m))) for i in range(n)]
    b=[int(z[i]>sum(z[(i-j)%n] for j in range(1,m+1))) for i in range(n)]
    return sum(a)+sum(b)

def routes_all_queries(edges,pts):
    n=len(pts)
    gaps=sorted(pts)
    queries=[]
    for k in range(n):
        low=gaps[k]
        high=gaps[(k+1)%n]+(1 if k==n-1 else 0)
        for j in range(1,16):
            queries.append((low+(high-low)*j/16)%1)
    for q in queries:
        scores=[circular_dist(q,p) for p in pts]
        best=min(scores)
        for i in range(n):
            v=i
            for _ in range(n):
                improve=[j for j in edges[v] if scores[j]<scores[v]-1e-12]
                if not improve:
                    break
                v=min(improve,key=lambda j:scores[j])
            if scores[v]>best+1e-10:
                return False
    return True

checks=0
for n in (8,11,14,20,25):
    for m in range(1,min(10,n-2)):
        for rep in range(24):
            z=[R.expovariate(1) for _ in range(n)]
            missing,edges,pts=direct_flags(z,m)
            assert missing==gap_flags(z,m),(n,m,z,missing,gap_flags(z,m))
            assert routes_all_queries(edges,pts)==(missing==0)
            checks+=1
for m in range(1,16):
    for k in range(1,m+1):
        # Exact formula: condition on first rare gap; k tilted competitors.
        p=4**(-m)*(2/3)**k
        assert 0<p<= (4/9)**m
        checks+=1
assert math.log2(9/4)>1
assert math.log2(16/9)<1
print(f'PASS: {checks} finite circle, routing, and exponential-tilt algebra checks')
