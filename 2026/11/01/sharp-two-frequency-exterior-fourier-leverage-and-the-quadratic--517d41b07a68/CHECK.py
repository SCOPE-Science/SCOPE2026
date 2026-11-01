"""Numerical supplementary checks for the two-frequency exterior leverage theorem.

Requires mpmath. The mathematical proof is independent of this program.
Run: python CHECK.py
"""
import mpmath as mp

mp.mp.dps = 65
checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def leverage(d, x):
    s = mp.sin(d)/d
    return (1-s*mp.cos(d*x))/(1-s*s)

def direct_leverage(d, x):
    s = mp.sin(d)/d
    return mp.cos(d*x/2)**2/(1+s) + mp.sin(d*x/2)**2/(1-s)

def cap(x):
    return (1+3*x*x)/2

def collision_coeff(x):
    return (15*x**4+6*x*x-5)/120

xs = [mp.mpf(t) for t in ['1', '1.01', '1.2','1.5','2','3','5','12']]
ds = [mp.mpf(t) for t in ['0.02','0.1','0.3','0.8','1.6','2.7','3.1','3.2','4','5','10','20','100']]
for x in xs:
    for d in ds:
        z = leverage(d,x)
        check(abs(z-direct_leverage(d,x))<mp.mpf('1e-58'), 'orthogonal Gram formula')
        check(z < cap(x), 'strict universal upper bound')
        check(z > 0, 'positive evaluation norm')
for x in xs:
    for d in map(mp.mpf, ['0.0001','0.0003','0.0007','0.001']):
        difference = (cap(x)-leverage(d,x))/d**2
        check(abs(difference-collision_coeff(x)) < mp.mpf('0.02'), 'collision coefficient')
        check(collision_coeff(x)>0,'quadratic gap sign')

# The fixed-gap maximizing representer gives norm and evaluation both K.
for d in map(mp.mpf,['0.25','1','2','4','9']):
    s=mp.sin(d)/d
    for x in map(mp.mpf,['1','1.3','2','3']):
        a=mp.cos(d*x/2)/(1+s)
        b=mp.sin(d*x/2)/(1-s)
        norm_squared=a*a*(1+s)+b*b*(1-s)
        at_x=a*mp.cos(d*x/2)+b*mp.sin(d*x/2)
        check(abs(norm_squared-leverage(d,x))<mp.mpf('1e-59'),'representer norm')
        check(abs(at_x-leverage(d,x))<mp.mpf('1e-59'),'representer evaluation')

# Gram form for non-optimal complex coefficients, evaluated without quadrature.
for d in map(mp.mpf,['0.2','0.9','2.5','5.3']):
    s=mp.sin(d)/d
    A=mp.mpc('0.32','-0.7')
    B=mp.mpc('1.2','0.4')
    norm_squared=(1+s)*abs(A)**2+(1-s)*abs(B)**2
    for x in xs:
        point=A*mp.cos(d*x/2)+B*mp.sin(d*x/2)
        check(abs(point)**2 <= (leverage(d,x)+mp.mpf('1e-52'))*norm_squared, 'Cauchy extremum')

print('PASS:',checks,'high-precision supplementary assertions')
