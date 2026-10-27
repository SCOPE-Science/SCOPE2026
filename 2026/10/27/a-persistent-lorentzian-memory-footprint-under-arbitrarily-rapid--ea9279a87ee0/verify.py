#!/usr/bin/env python3
"""Deterministic arithmetic checks for the stationary probe-memory covariance theorem.

Requires Python 3 standard library only. Exact Fractions test stationarity and
mode placement; floating checks independently evaluate the 2x2 semigroup and
large-reset limits. None of the finite tests substitutes for the proof.
"""
import math
from fractions import Fraction as F

count = 0

def check(condition, label):
    global count
    count += 1
    if not condition:
        raise AssertionError(label)

def exact(g, r):
    m = 2*(g*r+g+1)/(r*(g*r+2*g+1))
    k = (g*r+2*g+2)/(r*(g*r+2*g+1))
    q = (r+2)*(g*r+g+1)/(r*(g*r+2*g+1))
    return m,k,q

for g in [F(1,8),F(1,2),F(1),F(7,3),F(19)]:
    for r in [F(1,9),F(1),F(5,2),F(9),F(100)]:
        m,k,q = exact(g,r)
        check(-(2+r)*m+2*k+2==0, 'first stationary balance')
        check(m/g-(1+1/g+r)*k+q==0, 'cross stationary balance')
        check(2*k/g-2*q/g+2/g==0, 'bath stationary balance')
        d=(1+r)-k/m
        p=g*d*d-(g*(1+r)+1)*d+r
        formula=-g*r*(2*g*g*r*r+7*g*g*r+6*g*g+8*g*r+12*g+6)/(4*(g*r+g+1)**2)
        check(p==formula and p<0, 'positive mode weights')
        tau=(m+g*k)/(r*m)
        tau_formula=(g*g*r+2*g*g+2*g*r+4*g+2)/(2*r*(g*r+g+1))
        check(tau==tau_formula and tau>1/r, 'exact integrated lag')


def modes(g,r):
    m,k,_ = exact(g,r)
    z=1+r+1/g
    gap=math.sqrt((1+r-1/g)**2+4/g)
    fast=(z+gap)/2
    slow=(r/g)/fast
    d=1+r-k/m
    cs=m*(fast-d)/(fast-slow)
    cf=m-cs
    return m,k,slow,fast,cs,cf

# Independent matrix-exponential evaluation for the linear-observable generator.
for g in [.2,.7,1.,4.,12.]:
    for r in [.2,1.3,7.]:
        m,k,slow,fast,cs,cf=modes(g,r)
        check(0<slow<fast and 0<cs<m and 0<cf<m,'modal positivity')
        for t in [0.,.1,.7,2.]:
            b=(1+r+1/g)/2
            h=(fast-slow)/2
            E11=math.exp(-b*t)*(math.cosh(h*t)+(b-(1+r))*math.sinh(h*t)/h)
            E12=math.exp(-b*t)*math.sinh(h*t)/h
            direct=m*E11+k*E12
            spectral=cs*math.exp(-slow*t)+cf*math.exp(-fast*t)
            check(abs(direct-spectral)<2e-11*(1+m),'semigroup vs spectral')

# Strong-reset temporal and spectral limits; the analytic proof handles limits.
for g in [.5,1.,3.,9.]:
    r=100000.
    m,k,slow,fast,cs,cf=modes(g,r)
    check(abs(r*r*cs-1)<.003,'slow residue')
    check(abs(r*cf-2)<.003,'fast residue')
    check(abs(slow-1/g)<.0003,'slow rate')
    check(abs(fast/r-1)<.0003,'fast rate')
    for t in [.3,.9,1.7]:
        corr=cs*math.exp(-slow*t)+cf*math.exp(-fast*t)
        check(abs(r*r*corr-math.exp(-t/g))<.003,'fixed positive lag')
    for u in [0.,.4,1.,3.]:
        corr=cs*math.exp(-slow*u/r)+cf*math.exp(-fast*u/r)
        check(abs(r*corr-2*math.exp(-u))<.003,'microscopic lag')
    for nu in [0.,.25,1.,4.]:
        spect=2*(cs*slow/(slow*slow+nu*nu)+cf*fast/(fast*fast+nu*nu))
        lim=4+2*g/(1+(g*nu)**2)
        check(abs(r*r*spect-lim)<.003,'fixed-frequency spectrum')
    tau=(m+g*k)/(r*m)
    check(abs(r*tau-(1+g/2))<.003,'integrated lag asymptotic')
    cross=math.log(cf/cs)/(fast-slow)
    check(abs(r*cross/math.log(2*r)-1)<.003,'modal crossing asymptotic')

print(f'PASS: {count} deterministic checks (125 exact rational, remaining semigroup and asymptotic).')
