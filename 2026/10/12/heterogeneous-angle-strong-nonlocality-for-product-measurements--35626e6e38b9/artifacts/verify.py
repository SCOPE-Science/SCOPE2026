#!/usr/bin/env python3
import math
import itertools

TOL = 5e-12

def bits(n):
    return list(itertools.product((0,1), repeat=n))

def overlap(theta, y, x):
    c, s = math.cos(theta), math.sin(theta)
    if y == 0:
        return c if x == 0 else s
    return s if x == 0 else -c

def direct_amp(thetas, y):
    w=len(thetas)
    total=0.0
    for x in bits(w):
        wt=sum(x)
        if wt % 2:
            continue
        coeff=(-1.0)**(wt//2) / math.sqrt(2.0**(w-1))
        a=coeff
        for th,yy,xx in zip(thetas,y,x):
            a *= overlap(th,yy,xx)
        total += a
    return total

def formula_amp(thetas,y):
    w=len(thetas)
    return math.cos(sum(thetas)-sum(y)*math.pi/2.0)/math.sqrt(2.0**(w-1))

def check_tuple(thetas):
    w=len(thetas)
    assert w>=2
    assert all(0.0 < t < math.pi/2.0 for t in thetas)
    assert abs(sum(thetas)-math.pi/2.0) < TOL
    for y in bits(w):
        a=direct_amp(thetas,y)
        b=formula_amp(thetas,y)
        assert abs(a-b) < 2e-11, (thetas,y,a,b)
        if sum(y)%2==0:
            assert abs(a)<2e-11
        else:
            assert abs(abs(a)-1.0/math.sqrt(2.0**(w-1)))<2e-11
    for mask in range(1,2**w-1):
        subset=[thetas[i] for i in range(w) if (mask>>i)&1]
        Theta=sum(subset)
        assert 0.0 < Theta < math.pi/2.0
        vals=[]
        for eps in itertools.product((-1,1), repeat=len(subset)):
            phase=sum(e*t for e,t in zip(eps,subset))
            vals.append(math.cos(phase))
        assert min(vals)>0.0
        assert min(vals) + TOL >= math.cos(Theta)

cases=[
    [math.pi/6, math.pi/3],
    [math.pi/12, math.pi/6, math.pi/4],
    [math.pi/20, 3*math.pi/20, math.pi/10, math.pi/5],
    [math.pi/30, math.pi/15, math.pi/10, 2*math.pi/15, math.pi/6],
]
for c in cases:
    check_tuple(c)
print('VERIFY_OK')
