"""Independent finite diagnostics for a cyclic-polygon perimeter theorem.

Run with Python 3: python verify.py
The mathematical proof is in RESULT.md; finite diagnostics alone do not
certify the universal assertions.
"""
from math import pi, sin, cos, sqrt, atan2, hypot
from random import Random


def radius_vertices(half_angles, radius=1.0):
    return [(radius*cos(t), radius*sin(t)) for t in half_angles + [t+pi for t in half_angles]]


def perimeter(u,v):
    return 2*(hypot(u[0]-v[0],u[1]-v[1])+hypot(u[0]+v[0],u[1]+v[1]))


def full_search(points):
    return max((perimeter(a,b),i,j) for i,a in enumerate(points) for j,b in enumerate(points))


def fast_search(points):
    angles=[atan2(y,x)%(2*pi) for x,y in points]
    order=sorted(range(len(points)),key=lambda i:angles[i])
    a=[angles[i] for i in order]
    n=len(points)
    aa=a+[t+2*pi for t in a]
    j=0
    best=(-1,None,None)
    for i in range(n):
        j=max(j,i+1)
        target=aa[i]+pi/2
        while j<i+n-1 and aa[j]<target:
            j+=1
        for z in [j-1,j]:
            if i<z<i+n:
                ii=order[i]
                jj=order[z%n]
                p=perimeter(points[ii],points[jj])
                if p>best[0]:best=(p,ii,jj)
    return best


def centroid_sample(points,rng):
    w=[rng.random() for _ in points]
    s=sum(w)
    return (sum(t*x for t,(x,y) in zip(w,points))/s,
            sum(t*y for t,(x,y) in zip(w,points))/s)


def diagnostics():
    rng=Random(71357)
    total=0
    for n in range(4,122,2):
        points=radius_vertices([2*pi*k/n for k in range(n//2)])
        expected=4*sqrt(2)*(1 if n%4==0 else cos(pi/(2*n)))
        exhaustive=full_search(points)[0]
        fast=fast_search(points)[0]
        assert abs(exhaustive-expected)<5e-12, (n,exhaustive,expected)
        assert abs(fast-exhaustive)<5e-12, (n,fast,exhaustive)
        total+=2
    for m in range(2,60):
        for trial in range(8):
            angles=sorted(pi*rng.random() for _ in range(m))
            points=radius_vertices(angles)
            exhaustive=full_search(points)[0]
            fast=fast_search(points)[0]
            assert abs(exhaustive-fast)<5e-12, (m,trial,exhaustive,fast)
            total+=1
            for _ in range(20):
                u=centroid_sample(points,rng)
                v=centroid_sample(points,rng)
                assert perimeter(u,v)<=exhaustive+1e-12
                total+=1
    print('VERIFY_OK',total)


if __name__=='__main__':
    diagnostics()
