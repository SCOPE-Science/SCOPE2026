#!/usr/bin/env python3
"""Numerical and algebraic reproduction of the two-habitat fast-season result.

Requires Python 3 and mpmath. Finite checks supplement the analytic proof.
"""
import mpmath as mp

mp.mp.dps = 65

def rate(m, T, epsilon=0):
    m,T,e=mp.mpf(m),mp.mpf(T),mp.mpf(epsilon)
    k=mp.sqrt(1+m*m)
    return -e-m+mp.asinh((m/k)*mp.sinh(k*T))/T

def growth_matrix(m,T,e):
    m,T,e=mp.mpf(m),mp.mpf(T),mp.mpf(e)
    Ap=mp.matrix([[1-e-m,m],[m,-1-e-m]])
    Am=mp.matrix([[-1-e-m,m],[m,1-e-m]])
    P=mp.expm(T*Am)*mp.expm(T*Ap)
    tr=P[0,0]+P[1,1]
    det=P[0,0]*P[1,1]-P[0,1]*P[1,0]
    return mp.log((tr+mp.sqrt(tr*tr-4*det))/2)/(2*T)

def g(z):
    return (z-mp.tanh(z))/(2*z*z) if z else mp.mpf(0)

def golden_min(fun, a, b, steps=165):
    ratio=(mp.sqrt(5)-1)/2
    c=b-ratio*(b-a);d=a+ratio*(b-a)
    fc=fun(c);fd=fun(d)
    for _ in range(steps):
        if fc<fd:
            b,d,fd=d,c,fc
            c=b-ratio*(b-a);fc=fun(c)
        else:
            a,c,fc=c,d,fd
            d=a+ratio*(b-a);fd=fun(d)
    return (a+b)/2

zstar=mp.findroot(lambda z: 2*mp.tanh(z)-z*(2-mp.tanh(z)**2), (mp.mpf('1.4'),mp.mpf('1.8')))
G=g(zstar)
assert mp.mpf('1.60')<zstar<mp.mpf('1.61')
assert mp.mpf('.132')<G<mp.mpf('.133')
assert abs(mp.diff(g,zstar)) < mp.mpf('1e-53')
assert mp.diff(g,zstar,2)<0

# Independent matrix exponentials verify the closed formula.
count=0
for m in ['0.075','0.7','2.5','15']:
    for T in ['0.04','0.23','0.95']:
        for epsilon in ['0','0.21']:
            diff=abs(rate(m,T,epsilon)-growth_matrix(m,T,epsilon))
            assert diff < mp.mpf('1e-40'),(m,T,epsilon,diff)
            count+=1

# Verify analytic local coefficient as a limit of a difference quotient.
for z in ['0.1','0.5','0.9575','1.3','3.0']:
    z=mp.mpf(z)
    for T in ['0.02','0.01']:
        T=mp.mpf(T)
        H=rate(z/T,T)/T
        assert abs(H-g(z)) < 2*T*T, (z,T,H,g(z))

# Small-T global optimizers lie near zstar and follow the O(T^2) scaling.
for T in ['0.24','0.12','0.06','0.03']:
    T=mp.mpf(T)
    zopt=golden_min(lambda z:-rate(z/T,T),mp.mpf('.7'),mp.mpf('3.0'))
    assert abs(zopt-zstar)<2*T*T,(T,zopt,zstar)
    maxenh=rate(zopt/T,T)
    assert abs(maxenh-G*T)<T**3,(T,maxenh,G*T)
    assert rate(zopt/T,T,G*T+T*T)<0
    assert rate(zopt/T,T,G*T-T*T)>0
print('PASS: 24 independent matrix-exponential comparisons; 10 local expansions; 4 optimized regimes.')
print('zstar =',mp.nstr(zstar,30))
print('G =',mp.nstr(G,30))
