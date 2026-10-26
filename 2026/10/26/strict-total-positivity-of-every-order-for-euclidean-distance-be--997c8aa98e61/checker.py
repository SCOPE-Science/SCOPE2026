#!/usr/bin/env python3
"""Finite numerical corroboration of a strict total-positivity theorem."""
import mpmath as mp
mp.mp.dps=65

def a(t,n):
    return mp.gamma(t+2*n+3)/(2*mp.pi*mp.gamma(t+1)*mp.gamma(2*n+2))

def series(t,s):
    return mp.fsum(a(t,n)*s**n for n in range(500))

def closed(t,s):
    if s==0:
        return (t+1)*(t+2)/(2*mp.pi)
    x=mp.sqrt(s)
    return (t+1)*((1-x)**(-t-2)-(1+x)**(-t-2))/(4*mp.pi*x)

for t,s in [(-mp.mpf('0.5'),mp.mpf('0.2')),(0,mp.mpf('0.6')),(2,mp.mpf('0.8'))]:
    assert abs(series(t,s)-closed(t,s)) < mp.mpf('1e-28')
for k in [2,3,4,5]:
    ts=[-mp.mpf('0.3')+mp.mpf('0.5')*i for i in range(k)]
    ss=[mp.mpf('0.15')*i for i in range(k)]
    mat=mp.matrix([[closed(t,s) for s in ss] for t in ts])
    det=mp.det(mat)
    assert det>0,(k,det)
print('CHECK_OK: closed-form moments and ordered minors of ranks 2–5')
