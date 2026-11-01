#!/usr/bin/env python3
"""Numerical cross-checks for normalized Gaussian quotient curvature.

The universal inequalities and uniqueness are proved analytically in RESULT.md;
finite tests in this script are not substitutes for those proofs.
"""
import mpmath as mp

mp.mp.dps = 65
CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def moments(t, shift=0, terms=75):
    k = list(range(-terms, terms + 1))
    weights = [mp.exp(-t * (mp.mpf(i) + shift)**2) for i in k]
    z = sum(weights)
    mean = sum((mp.mpf(i) + shift) * w for i,w in zip(k, weights)) / z
    v = sum(((mp.mpf(i) + shift)-mean)**2 * w for i,w in zip(k, weights)) / z
    return mean, v

def scalars(t):
    m = moments(t)[1]
    k = list(range(-28,29))
    w = [mp.exp(-t*i*i) for i in k]
    z = sum(w)
    fourth = sum(i**4 * wi for i,wi in zip(k,w))/z
    v = fourth - m*m
    return m,v,4*t*t*m,2*m-t*v

lo, hi = mp.mpf('2.2'), mp.mpf('2.5')
check(scalars(lo)[3]>0 and scalars(hi)[3]<0, 'root bracket')
for _ in range(180):
    mid=(lo+hi)/2
    if scalars(mid)[3]>0:
        lo=mid
    else:
        hi=mid
root=(lo+hi)/2
alpha=scalars(root)[2]
check(abs(root-mp.mpf('2.3530152894481316488653'))<mp.mpf('1e-20'),'root value')
check(abs(alpha-mp.mpf('3.5502766159922244816281'))<mp.mpf('1e-20'),'maximum')
check(alpha>2*mp.pi/mp.e,'strict improvement')
for t in [mp.mpf(i)/12 for i in range(1,81)]:
    m,v,a,g=scalars(t)
    check(a>0, 'positive curvature')
    check((g>0)==(t<root), 'derivative sign grid')
    check(a<=alpha+mp.mpf('1e-40'), 'sampled upper bound')
    for z in [mp.mpf('0.07'),mp.mpf('0.21'),mp.mpf('0.5')]:
        check(moments(t,z)[1]+mp.mpf('1e-38')>=m, 'shifted covariance')
for t in [mp.mpf('0.2'),mp.mpf('0.7'),mp.mpf('1'),mp.mpf('2'),mp.mpf('2.7'),mp.mpf('5'),mp.mpf('7')]:
    T=mp.pi**2/t
    m,v,a,g=scalars(t)
    check(abs(t*t*m-(t/2-mp.pi**2*scalars(T)[0]))<mp.mpf('1e-45'), 'Jacobi identity')
for sides in [(1,1,1),(1,2,3),(mp.mpf('0.4'),1,mp.mpf('1.5'))]:
    settings=[root]*len(sides)
    result=min(scalars(t)[2]/(a*a) for t,a in zip(settings,sides))
    check(abs(result-alpha/max(sides)**2)<mp.mpf('1e-40'),'box law')
print('t_star =',mp.nstr(root,30))
print('variance_parameter =',mp.nstr(1/(2*root),30))
print('alpha_star =',mp.nstr(alpha,30))
print('checks passed =',CHECKS)
