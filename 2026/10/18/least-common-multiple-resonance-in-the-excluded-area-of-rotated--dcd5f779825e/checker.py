#!/usr/bin/env python3
"""Independent finite checks for regular-polygon excluded-area identities.

Run: python3 checker.py
Requires only the Python standard library. These tests check finite cases;
the arbitrary-order theorem follows from the proof in RESULT.md.
"""
import math
import random


def hull(points):
    points = sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]
    for p in points:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0: low.pop()
        low.append(p)
    up=[]
    for p in points[::-1]:
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0: up.pop()
        up.append(p)
    return low[:-1]+up[:-1]


def area(pts):
    return abs(sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[i][1]*pts[(i+1)%len(pts)][0] for i in range(len(pts)))/2)


def predicted(n,m,r,s,phi):
    g=math.gcd(n,m)
    L=math.lcm(n,m)
    a=math.pi/L
    C=g*r*s*math.sin(math.pi/n)*math.sin(math.pi/m)/math.sin(a)
    A=n*r*r*math.sin(2*math.pi/n)/2+m*s*s*math.sin(2*math.pi/m)/2
    base=math.pi/n-phi-math.pi-((n//g)-1)*a
    delta=(base+a)%(2*a)-a
    return A+2*C*math.cos(delta)


def direct(n,m,r,s,phi):
    P=[(r*math.cos(2*math.pi*i/n),r*math.sin(2*math.pi*i/n)) for i in range(n)]
    Q=[(s*math.cos(phi+math.pi+2*math.pi*j/m),s*math.sin(phi+math.pi+2*math.pi*j/m)) for j in range(m)]
    pts=[(x+z,y+w) for x,y in P for z,w in Q]
    return area(hull(pts))


def main():
    rng=random.Random(72021)
    tests=0
    for n in range(3,20):
        for m in range(3,19):
            r=.35+1.3*rng.random();s=.45+1.4*rng.random()
            for k in range(5):
                phi=2*math.pi*(k+.41*rng.random())/5
                p=predicted(n,m,r,s,phi)
                d=direct(n,m,r,s,phi)
                assert abs(p-d)<2e-10*max(1,abs(d)), (n,m,phi,p,d)
                tests+=1
    # Checks in the source's equal-area normalization.
    for n,m in [(3,4),(4,5),(3,3),(4,4),(5,7),(20,21)]:
        r=math.sqrt(2/(n*math.sin(2*math.pi/n)))
        s=math.sqrt(2/(m*math.sin(2*math.pi/m)))
        g=math.gcd(n,m);L=math.lcm(n,m); a=math.pi/L
        C=g*r*s*math.sin(math.pi/n)*math.sin(math.pi/m)/math.sin(a)
        mx=2+2*C
        mn=2+2*C*math.cos(a)
        theta=math.pi/n-math.pi-(n//g-1)*a
        assert abs(predicted(n,m,r,s,theta)-mx)<2e-11
        assert abs(predicted(n,m,r,s,theta+a)-mn)<2e-11
        tests+=2
    # A trapezoidal sample of the Haar angular mean converges to the kinematic value.
    for n,m in [(3,4),(5,5),(6,9),(8,11)]:
        r,s=0.81,1.3
        K=10080
        ev=sum(predicted(n,m,r,s,2*math.pi*j/K) for j in range(K))/K
        mean=(n*r*r*math.sin(2*math.pi/n)+m*s*s*math.sin(2*math.pi/m))/2 + 2*n*m*r*s*math.sin(math.pi/n)*math.sin(math.pi/m)/math.pi
        assert abs(ev-mean)<1e-6
        tests+=1
    print('PASS:',tests,'finite independent polygon-hull, extremum, and mean checks')

if __name__=='__main__': main()
