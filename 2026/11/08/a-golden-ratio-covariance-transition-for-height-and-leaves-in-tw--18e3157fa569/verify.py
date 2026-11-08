#!/usr/bin/env python3
"""Independent exact finite-state and renewal-reward checks for two-lag trees."""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def finite_tree(n, bits):
    parent = [-1, 0]
    heights = [0, 1]
    children = [1] + [0] * n
    for k, b in enumerate(bits, 2):
        a = k - 1 if b else k - 2
        parent.append(a)
        heights.append(heights[a] + 1)
        children[a] += 1
    h = max(heights)
    leaf = sum(x == 0 for x in children)
    return h, leaf


def renewal_tree(n, bits):
    x = 1
    height = 1
    leaves = 1
    last = 1
    for b in bits:
        x = 1 if b else 1-x
        height += x
        leaves += int(last == 1 and b == 0)
        last = b
    return height, leaves


def brute_moments(n, p):
    q = 1-p
    vals = [F(0) for _ in range(6)]
    for bits in product((0,1), repeat=n-1):
        v = finite_tree(n, bits)
        assert v == renewal_tree(n, bits), (n, bits, v, renewal_tree(n,bits))
        w = p**sum(bits) * q**(n-1-sum(bits))
        moments = (1, v[0], v[1], v[0]**2, v[1]**2, v[0]*v[1])
        for j in range(6):
            vals[j] += w*moments[j]
    return tuple(vals)


def dp_moments(n, p):
    q = 1-p
    # S=(last increment, last Bernoulli choice); vector=(mass,H,L,H^2,L^2,HL).
    d = {(1,1): (F(1),F(1),F(1),F(1),F(1),F(1))}
    for idx in range(2, n+1):
        nd = {}
        for (x, old), z in d.items():
            m,h,l,h2,l2,hl=z
            for b,weight in ((0,q),(1,p)):
                dx = 1 if b else 1-x
                dl = int(old==1 and b==0)
                row = (m, h+dx*m, l+dl*m, h2+2*dx*h+dx*dx*m,
                       l2+2*dl*l+dl*dl*m, hl+dx*l+dl*h+dx*dl*m)
                state=(dx,b)
                if state not in nd: nd[state] = (F(0),)*6
                nd[state]=tuple(a+weight*t for a,t in zip(nd[state],row))
        d=nd
    return tuple(sum(z[i] for z in d.values()) for i in range(6))


def sigma(q):
    p=1-q
    return (p*q/(1+q)**3, p*q*(1-3*p*q),
            p*q*(q*q+q-1)/(1+q)**2)


def truncated_renewal(q, N=400):
    p=1-q
    rate_h=1/(1+q)
    rate_l=p*q
    vals=[F(0),F(0),F(0)]
    for k in range(N+1):
        weight=p*q**k
        t=k+1
        h=k//2+1
        l=int(k>0)
        a=h-rate_h*t
        b=l-rate_l*t
        vals[0]+=weight*a*a
        vals[1]+=weight*b*b
        vals[2]+=weight*a*b
    return tuple(p*x for x in vals)


def float_dp(n,p):
    d={(1,1):(1.,1.,1.,1.,1.,1.)}
    for idx in range(2,n+1):
        nd={}
        for (x,old),(m,h,l,h2,l2,hl) in d.items():
            for b,weight in ((0,1-p),(1,p)):
                dx=1 if b else 1-x
                dl=int(old==1 and b==0)
                vals=(m,h+dx*m,l+dl*m,h2+2*dx*h+dx*dx*m,
                      l2+2*dl*l+dl*dl*m,hl+dx*l+dl*h+dx*dl*m)
                key=(dx,b)
                old_vals=nd.get(key,(0.,)*6)
                nd[key]=tuple(a+weight*t for a,t in zip(old_vals,vals))
        d=nd
    m,h,l,h2,l2,hl=(sum(z[i] for z in d.values()) for i in range(6))
    return ((h2-h*h)/n,(l2-l*l)/n,(hl-h*l)/n)


def run():
    checks=0
    for p in (F(1,5),F(1,3),F(1,2),F(2,3),F(4,5)):
        for n in range(2,12):
            assert brute_moments(n,p)==dp_moments(n,p)
            checks+=1
    for q in (F(1,5),F(1,3),F(1,2),F(3,5),F(4,5)):
        actual=truncated_renewal(q, 400)
        expected=sigma(q)
        assert all(abs(float(a-b))<3.e-25 for a,b in zip(actual,expected)),(q,actual,expected)
        checks+=3
    for q in (0.2,0.5,0.8):
        theory=[float(z) for z in sigma(q)]
        measured=float_dp(2200,1-q)
        assert all(abs(a-b)<0.004 for a,b in zip(measured,theory)),(q,measured,theory)
        print('q=',q,'scaled finite moments=',tuple(round(x,8) for x in measured),'limit=',tuple(round(x,8) for x in theory))
        checks+=3
    q0=(sqrt(5)-1)/2
    assert abs(float(sigma(q0)[2]))<1.e-14
    assert float(sigma(0.5)[2])<0<float(sigma(0.8)[2])
    checks+=2
    print('PASS',checks,'families; exact paths, dynamic moments, renewal sum, and Gaussian covariance signs')

if __name__=='__main__':
    run()
