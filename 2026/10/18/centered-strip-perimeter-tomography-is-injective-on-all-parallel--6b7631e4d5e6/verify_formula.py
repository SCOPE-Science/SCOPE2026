#!/usr/bin/env python3
"""Independent clipping tests for three formulas for a parallelogram in a centered strip.
Uses only the Python standard library. The finite sample does not prove the theorem.
"""
import math
import random


def dot(p, q):
    return p[0]*q[0]+p[1]*q[1]

def norm(p):
    return math.hypot(p[0], p[1])

def det(p, q):
    return p[0]*q[1]-p[1]*q[0]

def add(p, q):
    return (p[0]+q[0],p[1]+q[1])

def sub(p, q):
    return (p[0]-q[0],p[1]-q[1])

def scale(s, p):
    return (s*p[0],s*p[1])

def clip(vertices, normal, threshold):
    result=[]
    for i,p in enumerate(vertices):
        q=vertices[(i+1)%len(vertices)]
        d1=dot(normal,p)-threshold
        d2=dot(normal,q)-threshold
        if d1<=0:
            result.append(p)
        if (d1<0<d2) or (d2<0<d1):
            result.append(add(p,scale(-d1/(d2-d1),sub(q,p))))
    return result

def geometric_perimeter(a,b,u,t):
    vertices=[add(a,b),sub(a,b),scale(-1,add(a,b)),sub(b,a)]
    vertices=clip(vertices,u,t)
    vertices=clip(vertices,scale(-1,u),t)
    return sum(norm(sub(vertices[(i+1)%len(vertices)],p)) for i,p in enumerate(vertices))

def formula(a,b,u,t):
    A,B,C=norm(a),norm(b),abs(det(a,b))
    U,V=abs(dot(u,a)),abs(dot(u,b))
    if U+t<V:
        return 4*(C+t*B)/V,'pure-b'
    if V+t<U:
        return 4*(C+t*A)/U,'pure-a'
    return 4*(A+B)-2*(U+V-t)*(A/U+B/V-C/(U*V)),'mixed'

def main():
    rng=random.Random(519)
    counts={'pure-a':0,'pure-b':0,'mixed':0}
    worst=0.0
    for k in range(12000):
        a=(2*rng.gauss(0,1),2*rng.gauss(0,1))
        b=(2*rng.gauss(0,1),2*rng.gauss(0,1))
        C=abs(det(a,b))
        if C<0.2:
            continue
        t=.67*C/max(norm(a),norm(b))
        angle=rng.uniform(-math.pi,math.pi)
        u=(math.cos(angle),math.sin(angle))
        expected,kind=formula(a,b,u,t)
        actual=geometric_perimeter(a,b,u,t)
        counts[kind]+=1
        worst=max(worst,abs(expected-actual))
        assert abs(actual-expected) < 1e-9*max(1,abs(actual)), (k,kind,actual,expected)
    assert min(counts.values())>0
    print('PASS',counts,'maximum absolute error',worst)

if __name__=='__main__':
    main()
