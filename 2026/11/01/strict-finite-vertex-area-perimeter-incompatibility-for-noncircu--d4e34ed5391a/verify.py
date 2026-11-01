#!/usr/bin/env python3
"""Finite numerical checks of the ellipse polygon stationarity formula."""
import math
import random

rng=random.Random(198742)
count=0

def chk(ok,message):
    global count
    if not ok: raise AssertionError(message)
    count += 1

def point(a,b,theta):
    return (a*math.cos(theta),b*math.sin(theta))

def perimeter(a,b,angles):
    vertices=[point(a,b,t) for t in angles]
    return sum(math.hypot(x-u,y-v) for (x,y),(u,v) in zip(vertices,vertices[1:]+vertices[:1]))

def derivative_exact(a,b,n,phi,i):
    h=math.pi/n
    t=phi+2*math.pi*i/n
    def w(x):return (-math.sin(x),math.cos(x))
    wminus=w(t-h);wplus=w(t+h)
    def f(w):return math.hypot(a*w[0],b*w[1])
    fminus=f(wminus);fplus=f(wplus)
    B=a*a*wminus[0]*wplus[0]+b*b*wminus[1]*wplus[1]
    return (fminus-fplus)*(1-B/(fminus*fplus))/(2*math.cos(h))

def lower_gradient(a,b,n):
    h=math.pi/n
    N=n/math.gcd(n,4)
    return ((a*a-b*b)*b*b*math.sin(2*h)**3/(8*a*a*a*math.cos(h))
            *math.cos(math.pi/(2*N)))

for n in range(3,29):
    for j in range(30):
        a=1.05+10*rng.random(); b=.2+min(a-1.0,2)*rng.random()
        if b>=a: b=a/2
        phi=2*math.pi*rng.random()
        angles=[phi+2*math.pi*k/n for k in range(n)]
        i=rng.randrange(n)
        d=derivative_exact(a,b,n,phi,i)
        t=1e-5
        plus=angles.copy();plus[i]+=t
        minus=angles.copy();minus[i]-=t
        dn=(perimeter(a,b,plus)-perimeter(a,b,minus))/(2*t)
        chk(abs(d-dn)<3e-7*max(1,a),f'gradient {n} {i} {d} {dn}')
        G=lower_gradient(a,b,n)
        if n!=4:
            gmax=max(abs(derivative_exact(a,b,n,phi,k)) for k in range(n))
            chk(gmax>=G-2e-13*max(1,a),f'gradient bound {n} {gmax} {G}')
            k=max(range(n),key=lambda z:abs(derivative_exact(a,b,n,phi,z)))
            g=derivative_exact(a,b,n,phi,k)
            h=math.pi/n
            H=a*a/(b*math.sin(h/2))+2*a
            delta=math.copysign(min(h,G/H),g)
            pert=angles.copy();pert[k]+=delta
            improvement=perimeter(a,b,pert)-perimeter(a,b,angles)
            eta=.5*G*min(h,G/H)
            chk(improvement>=eta-2e-10*max(1,a),f'positive gap {n} {improvement} {eta}')

for ratio in [1.1,1.5,2,5,12]:
    a=ratio;b=1;n=4
    for phi in [0,math.pi/2,math.pi,3*math.pi/2]:
        chk(all(abs(derivative_exact(a,b,n,phi,k))<2e-14*a for k in range(n)), 'exceptional stationary')
    for phi in [0.11,0.5,0.9,1.4]:
        chk(any(abs(derivative_exact(a,b,n,phi,k))>1e-5 for k in range(n)), 'nonstationary quadrilateral')

print('VERIFY_OK',count)
