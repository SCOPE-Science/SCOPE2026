#!/usr/bin/env python3
import math, random

C = 4.0*math.sqrt(3.0)/9.0
R = 0.5

def points_from_half_arcs(xs):
    theta=[0.0]
    for x in xs[:-1]:
        theta.append(theta[-1]+2*x)
    return [(R*math.cos(t),R*math.sin(t)) for t in theta]

def dist(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])

def support_widths(P):
    out=[]
    for i in range(4):
        ax,ay=P[i]; bx,by=P[(i+1)%4]
        dx,dy=bx-ax,by-ay
        L=math.hypot(dx,dy)
        nx,ny=-dy/L,dx/L
        vals=[nx*x+ny*y for x,y in P]
        out.append(max(vals)-min(vals))
    return out

def formula_widths(P):
    a=dist(P[0],P[1]); b=dist(P[1],P[2]); c=dist(P[2],P[3]); d=dist(P[3],P[0])
    p=dist(P[0],P[2]); q=dist(P[1],P[3])
    return [max(b*p,d*q), max(c*q,a*p), max(d*p,b*q), max(a*q,c*p)]

def test_random(n=30000):
    worst=0.0
    for _ in range(n):
        ys=[random.expovariate(1.0) for _ in range(4)]
        s=sum(ys)
        xs=[math.pi*y/s for y in ys]
        P=points_from_half_arcs(xs)
        w1=support_widths(P); w2=formula_widths(P)
        assert max(abs(a-b) for a,b in zip(w1,w2)) < 2e-12
        w=min(w1)
        worst=max(worst,w)
        assert w <= C + 1e-12
    return worst

def test_equality_family():
    s=math.asin(math.sqrt(2.0/3.0))
    rem=math.pi-2*s
    lo=max(1e-8,rem-s)
    hi=min(s,rem-1e-8)
    vals=[]
    for j in range(11):
        u=lo+(hi-lo)*j/10.0
        xs=[s,u,rem-u,s]
        P=points_from_half_arcs(xs)
        w=min(support_widths(P))
        vals.append(w)
        assert abs(w-C) < 3e-12
    return min(vals),max(vals),s,lo,hi

def test_lassak_exemplar():
    P=[(0.5,0.0),(-1.0/6.0,math.sqrt(2.0)/3.0),(-0.5,0.0),(-1.0/6.0,-math.sqrt(2.0)/3.0)]
    w=min(support_widths(P))
    assert abs(w-C) < 2e-12
    return w

if __name__=='__main__':
    random.seed(20261003)
    worst=test_random()
    lo,hi,s,a,b=test_equality_family()
    ex=test_lassak_exemplar()
    print('VERIFY_OK widest inscribed quadrilateral')
    print('constant',repr(C))
    print('random_max',repr(worst))
    print('equality_range',repr(lo),repr(hi))
    print('s0',repr(s),'split_interval',repr(a),repr(b))
    print('source_exemplar',repr(ex))
