#!/usr/bin/env python3
"""Checks for stationary Markov group games and their annealed replicator."""
from math import exp, log, sqrt, comb

def stationary(j, group_size, a1, a2):
    if j == 0:
        return 0.0
    if j == group_size:
        return 1.0
    z = j / group_size
    return z**a2 / (1 - z**a1 + z**a2)

def gain(n, x, a1, a2, r_low, r_high):
    prob = [stationary(j, n, a1, a2) for j in range(n+1)]
    ds = [(k+1)*prob[k+1]-k*prob[k] for k in range(n)]
    return r_low - 1 + (r_high-r_low)*sum(comb(n-1,k)*x**k*(1-x)**(n-1-k)*ds[k] for k in range(n))

def main():
    a1,a2=0.01,7.0
    lo,hi=0.3,0.9
    u=stationary(1,3,a1,a2)
    v=stationary(2,3,a1,a2)
    assert u<1/20 and v>11/12
    assert (1-exp(-0.01)) > 1/101 > 19/2187
    assert 128/2187>11/200
    b=4*(v-u)
    a=3*(1+u-2*v)
    H=(1-lo)/(hi-lo)
    assert a<0 and 4*v>3+u
    apex=u-b*b/(4*a)
    assert max(u,3-2*v)<H<apex
    assert u < H and 3-2*v < H and (u+b/2+a/4)>H
    for x in [0,0.03,0.1,0.5,0.9,0.99,1]:
        F=u+b*x+a*x*x
        assert abs(gain(3,x,a1,a2,lo,hi)-(hi-lo)*(F-H))<1e-11
    disc=b*b-4*a*(u-H)
    assert disc>0
    x1=(-b+sqrt(disc))/(2*a)
    x2=(-b-sqrt(disc))/(2*a)
    x1,x2=sorted([x1,x2])
    assert 0<x1<0.5<x2<1
    assert b+2*a*x1>0 and b+2*a*x2<0
    print('p1=',format(u,'.14f'),'p2=',format(v,'.14f'))
    print('roots=',format(x1,'.14f'),format(x2,'.14f'))
    print('vertex=',format(-b/(2*a),'.14f'),'Fmax=',format(apex,'.14f'))
    for group in range(2,20):
        for alpha in [0.01,0.5,1,2,7,21]:
            p=[stationary(j,group,alpha,alpha) for j in range(group+1)]
            dd=[(k+1)*p[k+1]-k*p[k] for k in range(group)]
            assert all(dd[k+1]>dd[k] for k in range(group-1))
    for aa in [0.01,0.3,2,7,30]:
        for bb in [0.01,0.3,2,7,30]:
            p=stationary(1,2,aa,bb)
            assert 0<p<1 and 2-p>p
    print('All reproducibility checks passed; infinite-parameter statements rest on the paper proof.')

if __name__ == '__main__':
    main()
