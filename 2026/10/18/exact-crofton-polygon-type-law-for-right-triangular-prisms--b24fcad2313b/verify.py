#!/usr/bin/env python3
"""Independent numerical and combinatorial checks for right-triangular-prism section law.
Only the standard Python library is needed. The accompanying proof, not this
finite test program, establishes the exact statements.
"""
import math, random
from itertools import combinations
PI=math.pi

def primitive(k,t):
    # Antiderivative of cos(t)*atan(k/cos(t)) on [-pi/2,pi/2].
    if not -PI/2-1e-9 <= t <= PI/2+1e-9: raise AssertionError((k,t))
    t=max(-PI/2,min(PI/2,t))
    s=math.hypot(1,k)
    if abs(abs(t)-PI/2)<1e-12:
        return math.copysign(PI/2*(1+k-s),t)
    return math.sin(t)*math.atan(k/math.cos(t))+k*t-s*math.atan2(k*math.sin(t),s*math.cos(t))

def arc(d,a,b,h):
    r=math.hypot(*d)
    delta=math.atan2(d[1],d[0]); k=h/r
    def t(x):
        v=x-delta
        return math.atan2(math.sin(v),max(0.0,math.cos(v)))
    ta,tb=t(a),t(b)
    assert ta<=tb+1e-8,(d,a,b,ta,tb)
    return r*(primitive(k,tb)-primitive(k,ta))

def partitions(v):
    breaks=[0.0,2*PI]
    for i,j in combinations(range(3),2):
        d=(v[j][0]-v[i][0],v[j][1]-v[i][1])
        alpha=(math.atan2(d[1],d[0])+PI/2)%(PI)
        breaks.extend([alpha,alpha+PI])
    return sorted(set(round(t,14) for t in breaks))

def integral_pent(v,h):
    ans=0.0
    for a,b in zip(partitions(v),partitions(v)[1:]):
        if b-a<1e-11: continue
        m=(a+b)/2
        order=sorted(range(3),key=lambda i:v[i][0]*math.cos(m)+v[i][1]*math.sin(m))
        i,j,k=order
        d1=tuple(v[j][n]-v[i][n] for n in (0,1))
        d2=tuple(v[k][n]-v[j][n] for n in (0,1))
        d3=tuple(v[k][n]-v[i][n] for n in (0,1))
        ans+=arc(d1,a,b,h)+arc(d2,a,b,h)-arc(d3,a,b,h)
    return ans

def full_law(v,h):
    L=sum(math.dist(v[i],v[(i+1)%3]) for i in range(3))
    p5=integral_pent(v,h)/(PI*(L+2*h))
    p3=p5+2*h/(L+2*h)
    p4=1-p3-p5
    return p3,p4,p5

def pent_equilateral(h):
    s=math.hypot(1,h)
    F90=PI/2*(1+h-s)
    F30=.5*math.atan2(2*h,math.sqrt(3))+h*PI/6-s*math.atan2(h,math.sqrt(3)*s)
    return 12*(F90-2*F30)/(PI*(3+2*h))

def simpson(f,a,b,n=500):
    if n%2:n+=1
    z=f(a)+f(b)
    step=(b-a)/n
    for i in range(1,n):z+=(4 if i%2 else 2)*f(a+i*step)
    return z*step/3

def alternate_p5(v,h):
    def f(t):
        values=sorted(x*math.cos(t)+y*math.sin(t) for x,y in v)
        p,q=values[1]-values[0],values[2]-values[1]
        def g(c):return c*math.atan2(h,c) if c>0 else 0.
        return g(p)+g(q)-g(p+q)
    knots=partitions(v)
    return sum(simpson(f,a,b,1400) for a,b in zip(knots,knots[1:]))

def count_cut(v,h,u,t):
    pts=[(x,y,z) for z in (0.0,h) for x,y in v]
    w=[u[0]*x+u[1]*y+u[2]*z-t for x,y,z in pts]
    edges=[(i,(i+1)%3) for i in range(3)]+[(i+3,(i+1)%3+3) for i in range(3)]+[(i,i+3) for i in range(3)]
    return sum(w[a]*w[b]<0 for a,b in edges)

def check():
    triangles=[[(0.,0.),(1.,0.),(.5,math.sqrt(3)/2)],[(0.,0.),(1.,0.),(.18,.76)],[(-.3,-.4),(1.9,0.),(.1,2.7)],[(.3,-.1),(2.6,.2),(.6,1.3)]]
    hs=[.05,.17,.4,math.sqrt(3)/2,1.,1.7,4.,12.]
    tests=0
    for v in triangles:
        for h in hs:
            law=full_law(v,h)
            assert all(0<p<1 for p in law) and abs(sum(law)-1)<2e-11,(v,h,law)
            raw=alternate_p5(v,h)
            assert abs(raw-integral_pent(v,h))<5e-10,(v,h,raw,integral_pent(v,h))
            if v is triangles[0]:assert abs(law[2]-pent_equilateral(h))<1e-11
            tests+=1
    rng=random.Random(461982)
    # Check the proposed entire OFFSET INTERVAL for five-edge sections,
    # independently enumerating cuts of all nine polyhedral edges.
    offset_checks=0
    for v in triangles:
        for h in (0.15,0.6,1.9,4.0):
            for k in range(225):
                uu=[rng.gauss(0,1) for _ in range(3)];norm=math.sqrt(sum(x*x for x in uu));u=[x/norm for x in uu]
                w=sorted(u[0]*x+u[1]*y for x,y in v)
                H=abs(h*u[2]); p,q=w[1]-w[0],w[2]-w[1]
                analytic=max(0,min(q,H)-max(0,H-p))
                six=sorted([u[0]*x+u[1]*y+u[2]*z for z in (0,h) for x,y in v])
                empirical=0.0
                for a,b in zip(six,six[1:]):
                    if b-a>1e-13 and count_cut(v,h,u,(a+b)/2)==5:empirical+=b-a
                assert abs(analytic-empirical)<1e-9*(1+h), (v,h,analytic,empirical,p,q,H)
                offset_checks+=1
    # Independently simulate the invariant-plane law with an unconditional
    # uniform offset in a common bounding interval, keeping intersecting planes.
    rng=random.Random(41522); n=180000
    v=triangles[1];h=.68
    rad=max(math.sqrt(x*x+y*y+z*z) for z in (0,h) for x,y in v)+0.01
    counts=[0,0,0];hits=0
    for i in range(n):
        uu=[rng.gauss(0,1) for _ in range(3)];norm=math.sqrt(sum(x*x for x in uu));u=[x/norm for x in uu]
        t=(2*rng.random()-1)*rad
        c=count_cut(v,h,u,t)
        if c:
            assert c in (3,4,5)
            counts[c-3]+=1;hits+=1
    law=full_law(v,h)
    probs=[c/hits for c in counts]
    assert max(abs(a-b) for a,b in zip(law,probs))<.014,(law,probs,hits)
    print('TRIANGULAR_PRISM_CHECK_OK', 'formula_tests=',tests,'offset_exhaustions=',offset_checks,
         'random_plane_trials=',n,'accepted=',hits,'law=',tuple(round(x,8) for x in law),
         'empirical=',tuple(round(x,8) for x in probs))

if __name__=='__main__':check()
