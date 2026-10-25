#!/usr/bin/env python3
"""Independent finite regression of an exact planar Minkowski-sum identity.
Requires Python 3 standard library only. This is not a universal proof.
"""
import math
import random

PI = math.pi

def polygon(n, radius, phase):
    return [(radius*math.cos(2*PI*j/n+phase),
             radius*math.sin(2*PI*j/n+phase)) for j in range(n)]

def hull(points):
    pts = sorted(points)
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    bot=[]
    for p in pts:
        while len(bot)>1 and cross(bot[-2],bot[-1],p)<=1e-11:
            bot.pop()
        bot.append(p)
    top=[]
    for p in reversed(pts):
        while len(top)>1 and cross(top[-2],top[-1],p)<=1e-11:
            top.pop()
        top.append(p)
    return bot[:-1]+top[:-1]

def shoelace(points):
    return abs(sum(x*y1-y*x1 for (x,y),(x1,y1) in zip(points, points[1:]+points[:1])))/2

def direct(m,n,r,s,phi):
    P=polygon(m,r,0);Q=polygon(n,s,phi)
    return hull([(x+u,y+v) for x,y in P for u,v in Q])

def analytical(m,n,r,s,phi):
    g=math.gcd(m,n);L=m*n//g
    center=PI/L if (m//g)%2 and (n//g)%2 else 0.0
    period=2*PI/L
    delta=((phi-center+period/2)%period)-period/2
    b=2*g*r*s*math.sin(PI/m)*math.sin(PI/n)/math.sin(PI/L)
    base=.5*m*r*r*math.sin(2*PI/m)+.5*n*s*s*math.sin(2*PI/n)
    return base+b*math.cos(delta)

def regression():
    rnd=random.Random(20261022);tests=0;worst=0
    for m in range(3,20):
        for n in range(3,20):
            for k in range(11):
                r=.5+2*rnd.random();s=.5+2*rnd.random()
                phi=(rnd.random()*14-7)*PI
                got=shoelace(direct(m,n,r,s,phi))
                expected=analytical(m,n,r,s,phi)
                err=abs(got-expected)
                assert err<3e-10*(1+expected), (m,n,got,expected)
                worst=max(worst,err);tests+=1
    # Verify the exact side-count transition for edge-normal coincidence.
    for m in range(3,19):
        for n in range(3,19):
            g=math.gcd(m,n);L=m*n//g
            center=PI/L if (m//g)%2 and (n//g)%2 else 0.0
            minphase=center+PI/L
            high=direct(m,n,1.0,1.25,center)
            low=direct(m,n,1.0,1.25,minphase)
            assert len(high)==m+n, ('max vertices',m,n,len(high),m+n)
            assert len(low)==m+n-g, ('min vertices',m,n,len(low),m+n-g)
            tests+=2
    # Absolute extrema and distribution moments: exact formulas vs finite sampling.
    for m,n in [(3,3),(3,4),(4,6),(7,13),(10,21)]:
        g=math.gcd(m,n);L=m*n//g;period=2*PI/L
        center=PI/L if (m//g)%2 and (n//g)%2 else 0
        r=1.2;s=.65
        maxima=analytical(m,n,r,s,center)
        minima=analytical(m,n,r,s,center+PI/L)
        assert maxima>minima
        areas=[analytical(m,n,r,s,center+j*period/10000) for j in range(10000)]
        avg=sum(areas)/len(areas)
        a0=.5*m*r*r*math.sin(2*PI/m)+.5*n*s*s*math.sin(2*PI/n)
        b=2*g*r*s*math.sin(PI/m)*math.sin(PI/n)/math.sin(PI/L)
        assert abs(avg-(a0+b*L/PI*math.sin(PI/L)))<5e-8
        tests+=1
    print('PASS:',tests,'independent convex-hull/face-count/moment regressions; worst area error:',worst)

if __name__=='__main__': regression()
