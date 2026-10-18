#!/usr/bin/env python3
"""Independent finite Fourier checks for the coordinate-star Turan theorem.
Uses only the Python standard library; analytic proof covers all orders.
"""
import math, cmath, itertools, random

rng=random.Random(260114)
CASES=[(3,),(4,),(5,),(6,),(3,5),(4,4),(5,5),(5,6),(6,8),(7,8,12),(3,4,5),(4,6,8)]
EPS=4e-10
checks=0

def q(n,z):
    return -min((z*cmath.exp(2j*math.pi*k/n)).real for k in range(n))

def spectrum(orders,aa):
    return [1+2*sum((a*cmath.exp(2j*math.pi*k/n)).real for n,a,k in zip(orders,aa,kk))
             for kk in itertools.product(*(range(n) for n in orders))]

def constants(orders):
    odds=[n for n in orders if n%2]
    m=min(odds) if odds else None
    c=math.cos(math.pi/m) if m else 1.
    return m,c

for orders in CASES:
    m,c=constants(orders)
    target=1+1/c
    d=len(orders)
    endpoints=[]
    if m:
        for j,n in enumerate(orders):
            if n==m:
                a=[0j]*d;a[j]=1/(2*c);endpoints.append(a)
    else:
        for j,n in enumerate(orders):
            for sg in [-1,1]:
                a=[0j]*d;a[j]=.5+.5j*sg*math.tan(math.pi/n);endpoints.append(a)
    assert len(endpoints)==(sum(n==m for n in orders) if m else 2*d)
    for a in endpoints:
        sp=spectrum(orders,a)
        assert min(sp)>-EPS and abs(min(sp))<EPS
        assert abs(1+2*sum(z.real for z in a)-target)<EPS
        checks+=1
    for _ in range(25):
        weights=[rng.random() for a in endpoints]
        s=sum(weights)
        a=[sum(w*row[j] for w,row in zip(weights,endpoints))/s for j in range(d)]
        sp=spectrum(orders,a)
        assert min(sp)>-EPS
        assert abs(1+2*sum(z.real for z in a)-target)<EPS
        checks+=1
    for _ in range(130):
        aa=[(rng.uniform(-1,1)+1j*rng.uniform(-1,1)) for n in orders]
        Q=sum(q(n,a) for n,a in zip(orders,aa))
        rate=rng.random()/(2*Q)
        a=[rate*z for z in aa]
        sp=spectrum(orders,a)
        assert min(sp)>-EPS
        mass=1+2*sum(z.real for z in a)
        delta=target-mass
        assert delta>-EPS
        if m:
            left=(2/c)*sum((math.sin(math.pi/m)*abs(z.imag) if n==m else ((math.cos(math.pi/n)-c) if n%2 else ((1-c)*math.cos(math.pi/n)))*abs(z)) for n,z in zip(orders,a))
            assert delta+EPS>=left, (orders,delta,left)
        checks+=1
print('PASS',checks,'finite group/optimizer/stability checks across',len(CASES),'cases')
