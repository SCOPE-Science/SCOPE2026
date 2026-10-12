#!/usr/bin/env python3
"""Deterministic sanity checks; the accompanying analytic proof carries the theorem."""
import math

def phi(t):
    return t*(-math.log(t))/((1-t)*(-math.log1p(-t)))

def log_deriv_scaled(t):
    return 1-(1-t)/(-math.log(t))-t/(-math.log1p(-t))

def q(a,u):
    return math.log(-math.log1p(-math.exp(math.log(u)/a)))

def qp(a,u):
    t = math.exp(math.log(u)/a)
    return t/(a*u*(1-t)*(-math.log1p(-t)))

count=0
for k in range(1,2000):
    t=k/2000
    assert log_deriv_scaled(t)<0
    count+=1
for a,b in [(0.3,0.7),(0.7,1.0),(1.0,2.0),(2.0,3.0),(3.0,10.0),(10.0,100.0)]:
    for k in range(1,1000):
        u=k/1000
        assert qp(b,u)<qp(a,u)
        count+=1
    for k in range(1,95,3):
        u=k/100;v=(k+4)/100
        assert q(b,v)-q(b,u)<q(a,v)-q(a,u)
        count+=1
N=20000
last=float('inf')
for n in range(1,9):
    vals=[q(n,(k+0.5)/N) for k in range(N)]
    mean=sum(vals)/N
    variance=sum((v-mean)**2 for v in vals)/N
    assert 0<variance<last
    last=variance
    print('n=',n,'approximate variance=',format(variance,'.9f'))
    count+=1
print('PASS',count,'finite checks; universal inequality is proved analytically.')
