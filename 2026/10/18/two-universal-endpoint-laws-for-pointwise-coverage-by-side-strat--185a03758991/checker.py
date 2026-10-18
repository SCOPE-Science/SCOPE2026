"""Reproducible finite checks for a parallelogram's side-stratified hull coverage depth.
Run: python3 checker.py. Uses only Python's standard library.
"""
import math
import random


def corner_probability(a, b):
    if a + b >= 1.0:
        return 0.0
    if a <= 0.0:
        return 1.0 - b
    if b <= 0.0:
        return 1.0 - a
    return 1 - a - b - a*b*math.log(((1-a)*(1-b))/(a*b))


def depth_full(x, y):
    return 1.0 - (corner_probability(x, y) + corner_probability(1-x, y)
                  + corner_probability(1-x, 1-y) + corner_probability(x, 1-y))


def depth_wedge(x, y):
    if x == 0.0:
        return 0.0
    return x * (2.0 + math.log((1-x)/x)
                + (2*y-1) * math.log((1-y)/y))


def det(u, v, w):
    return (v[0]-u[0])*(w[1]-u[1])-(v[1]-u[1])*(w[0]-u[0])


def in_polygon(z, q):
    return all(det(q[i],q[(i+1)%4],z)>=-1e-12 for i in range(4))


def simpson(f, a, b, n=2048):
    assert n%2==0
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+h*i) for i in range(1,n,2))
            +2*sum(f(a+h*i) for i in range(2,n,2)))*h/3


def left_threshold(e, y):
    if not y or depth_wedge(y,y)<=e:
        return y
    lo,hi=0.0,y
    for _ in range(54):
        mid=(lo+hi)/2
        if depth_wedge(mid,y)<=e:lo=mid
        else:hi=mid
    return (lo+hi)/2


def low_tail(e):
    return 8*simpson(lambda y:left_threshold(e,y),0.0,0.5,2048)


def polar_radius(e,theta):
    u,v=math.cos(theta),math.sin(theta)
    lo,hi=0.0,0.25
    for _ in range(55):
        mid=(lo+hi)/2
        if depth_full(.5+mid*u,.5+mid*v)>=1-e:lo=mid
        else:hi=mid
    return (lo+hi)/2


def high_tail(e):
    return .5*simpson(lambda theta:polar_radius(e,theta)**2,0.,2*math.pi,1024)


def affine(point):
    x,y=point
    return (1.7+2.4*x+0.7*y,-0.8+0.5*x+1.9*y)


def main():
    rng=random.Random(281014)
    for _ in range(3000):
        x=rng.uniform(.00001,.49999)
        y=rng.uniform(x,.5)
        assert abs(depth_full(x,y)-depth_wedge(x,y))<1e-11
        assert 0<=depth_wedge(x,y)<=1
    print('PASS: 3000 random exact-expression and symmetry comparisons')

    targets=[(.08,.13),(.2,.43),(.48,.49),(.5,.5),(.7,.15),(.9,.8)]
    trials=55000
    for z in targets:
        hits=0
        for _ in range(trials):
            v=[(rng.random(),0),(1,rng.random()),(rng.random(),1),(0,rng.random())]
            a=in_polygon(z,v)
            b=in_polygon(affine(z),[affine(p) for p in v])
            assert a==b
            hits+=a
        observed=hits/trials
        expected=depth_full(*z)
        assert abs(observed-expected)<.017,(z,observed,expected)
    print('PASS: 330000 direct hull-containment trials; affine invariance verified')

    for z in [(.005,.5),(.02,.25),(.1,.1),(.5,.5)]:
        assert 0<=depth_full(*z)<=1
    for z in [(.1,0),(.0,.8),(.7,1),(.9999,0)]:
        assert abs(depth_full(*z))<1e-10
    assert abs(depth_full(.5,.5)-1)<1e-12
    print('PASS: boundary values and certain center')

    # Finite numerical quadrature checks are not proofs of asymptotics.
    lows=[(k,low_tail(math.exp(-k))*k/math.exp(-k)) for k in (8,12,16)]
    assert lows[0][1]<lows[1][1]<lows[2][1]<4.0
    assert 3.0<lows[2][1]<3.5
    print('PASS: low-depth ratios (limit 4):',lows)

    highs=[(e,high_tail(e)/e) for e in (.015,.005,.001)]
    assert highs[0][1]>highs[1][1]>highs[2][1]>math.pi/4
    assert abs(highs[2][1]-math.pi/4)<.02
    print('PASS: high-depth ratios (limit pi/4):',highs)
    print('All finite checks passed; mathematical limits require the analytic proof.')

if __name__=='__main__':main()
