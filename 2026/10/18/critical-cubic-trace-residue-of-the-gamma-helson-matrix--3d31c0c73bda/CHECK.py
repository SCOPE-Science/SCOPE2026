#!/usr/bin/env python3
"""Finite diagnostics for the cubic trace residue of a gamma Helson matrix.
Standard library only. These finite checks are not a proof of infinite limits.
"""
import math

def angular_simpson(n=20000, xmax=27.0):
    assert n % 2 == 0
    h=xmax/n
    def f(x):
        if x == 0: return 1.0
        return x/math.sinh(x)
    s=f(0)+f(xmax)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*f(j*h)
    return h*s/3

def cube_trace(beta, count):
    l=[math.log(n) for n in range(1,count+1)]
    inv=[1.0/n for n in range(1,count+1)]
    k=[[1.0/(1+l[i]+l[j])**beta for j in range(count)] for i in range(count)]
    s=0.0
    for i in range(count):
        for j in range(count):
            v=inv[i]*inv[j]*k[i][j]
            for h in range(count):
                s+=v*inv[h]*k[j][h]*k[h][i]
    return s

def main():
    target=math.pi*math.pi/4
    est=angular_simpson()
    assert abs(est-target)<2e-8,(est,target)
    for K in [2,3,4,8,15,25]:
        assert math.log1p(1.0/K)<=1.0/K
        assert 0<=1.0/K-math.log1p(1.0/K)<=1/(2*K*K)
    for beta in [1.2,1.5,2.0]:
        small=cube_trace(beta,7)
        big=cube_trace(beta,14)
        assert 0<small<big
    print('PASS: angular value, elementary logarithmic cells, positive finite trace monotonicity')
    print('angular integral:',repr(est),'analytic:',repr(target))
if __name__=='__main__':main()
