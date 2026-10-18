#!/usr/bin/env python3
"""Finite diagnostics for antilinear square-root q-numerical annulus formula.

The classification and sharp bounds are proved in RESULT.md. This program
checks explicit extremizers and randomized constrained kernel pairs; sampling
is not an exhaustive or infinite-dimensional proof.
"""
import cmath
import math
import random

rng = random.Random(260617)
count = 0

def close(actual, expected, tol=2e-11):
    global count
    assert abs(actual-expected) <= tol * max(1,abs(expected)), (actual,expected)
    count += 1

def inner(x,y):
    return x[0]*y[0].conjugate()+x[1]*y[1].conjugate()

def norm(x):
    return math.sqrt(inner(x,x).real)

def A(x,a,b):
    return (-b*x[1].conjugate(), a*x[0].conjugate())

def vperp(x):
    return (-x[1].conjugate(),x[0].conjugate())

def radii(a,b,q):
    if b>a: a,b=b,a
    k=math.sqrt(max(0,1-abs(q)**2))
    return max(0,(k*(a+b)-(a-b))/2),(k*(a+b)+(a-b))/2

def x_from_z(z):
    return (math.sqrt((1+z)/2),math.sqrt((1-z)/2))

def pair(x,q,phi):
    k=math.sqrt(max(0,1-abs(q)**2))
    v=vperp(x)
    y=(q.conjugate()*x[0]+k*cmath.exp(1j*phi)*v[0],
       q.conjugate()*x[1]+k*cmath.exp(1j*phi)*v[1])
    close(norm(x),1)
    close(norm(y),1)
    close(inner(x,y),q)
    return y

def mod_at_z(a,b,t,z,minus=False):
    x=x_from_z(z)
    y=pair(x,t,math.pi if minus else 0)
    return abs(inner(A(x,a,b),y))

for a,b in [(1.,1.),(2.,1.),(4.,1.),(4.,3.),(1.001,1.),(3.,0.1),(11.,2.)]:
    assert a>=b>0
    for t in [0,0.01,0.2,0.5,0.6,0.8,0.91,0.999999,1]:
        k=math.sqrt(max(0,1-t*t))
        r,R=radii(a,b,t)
        close(mod_at_z(a,b,t,k),R)
        if k*(a+b)>=a-b:
            close(mod_at_z(a,b,t,-k,True),r)
        else:
            if k==0:
                close(mod_at_z(a,b,t,1),0)
            else:
                lo,hi=-k,1.
                def gap(z):
                    return t*(a-b)*math.sqrt(max(0,1-z*z))-k*((a+b)+(a-b)*z)
                assert gap(lo)>=-1e-12 and gap(hi)<=1e-12
                for _ in range(65):
                    mid=(lo+hi)/2
                    if gap(mid)>0: lo=mid
                    else: hi=mid
                close(mod_at_z(a,b,t,(lo+hi)/2,True),0)
        for _ in range(500):
            u=rng.random()
            alpha=2*math.pi*rng.random()
            beta=2*math.pi*rng.random()
            x=(math.sqrt(u)*cmath.exp(1j*alpha),
               math.sqrt(1-u)*cmath.exp(1j*beta))
            phi=2*math.pi*rng.random()
            q=(1+0j if t==1 else 0j if t==0 else t*cmath.exp(1j*(2*math.pi*rng.random())))
            y=pair(x,q,phi)
            z=abs(inner(A(x,a,b),y))
            assert r-3e-11 <= z <= R+3e-11, (a,b,q,z,r,R)
            count+=1
            # The intrinsic antilinear square is the specified negative scalar.
            Az=A(x,a,b)
            A2=A(Az,a,b)
            close(A2[0],-a*b*x[0])
            close(A2[1],-a*b*x[1])
        # Exact phase boundary and canonical endpoints.
        threshold=2*math.sqrt(a*b)/(a+b)
        if abs(t-threshold)>1e-12:
            assert (r<=1e-12)==(t>=threshold)
    close(radii(a,b,0)[0],b)
    close(radii(a,b,0)[1],a)
    close(radii(a,b,1)[0],0)
    close(radii(a,b,1)[1],(a-b)/2)

# Explicit rational nonconformal example (a=4,b=1,q=3/5).
r,R=radii(4,1,3/5)
close(r,1/2)
close(R,7/2)
# q=4/5 is its exact origin-inclusion threshold.
close(radii(4,1,4/5)[0],0)
print('PASS:',count,'finite diagnostic assertions')
