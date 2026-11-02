#!/usr/bin/env python3
"""Reproducible checks for a two-column iid least-squares tail law.

Requires Python 3.10+ standard library only. Exact rational identities and
independent deterministic integrals test finite consequences; the asymptotic
and universal optimality claims require the analytic proof.
"""
from fractions import Fraction as F
import math
import random

RNG = random.Random(83021)
checks = 0


def check(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1


def simpson(fun, lo, hi, n=1000):
    assert n % 2 == 0
    step = (hi-lo)/n
    total = fun(lo)+fun(hi)
    for j in range(1, n):
        total += (4 if j%2 else 2)*fun(lo+step*j)
    return total*step/3


# Identity checked over exactly rational data and positive definite losses.
for m in range(2, 13):
    for sample in range(60):
        values = [F(RNG.randrange(-40,41), RNG.randrange(3,26)) for _ in range(m)]
        if len(set(values)) == 1:
            values[-1] += 1
        b11 = F(RNG.randrange(1, 15), 3)
        b12 = F(RNG.randrange(-7, 8), 11)
        b22 = b12*b12/b11 + F(RNG.randrange(1, 15), 5)
        s1, s2 = sum(values), sum(v*v for v in values)
        det = m*s2-s1*s1
        check(det > 0, 'non-degenerate finite sample')
        direct = (b11*s2-2*b12*s1+b22*m)/det
        mean = s1/m
        scatter = sum((x-mean)**2 for x in values)
        quad = b11*mean*mean - 2*b12*mean + b22
        geometric = quad/scatter+b11/m
        check(direct == geometric, 'exact trace identity')


# Check the sharp Holder minimum for several m, intervals and SPD metrics.
for m in [2,3,4,6,9]:
    alpha = (m-1)/2
    for L in [1.,3.,10.]:
        for b11,b12,b22 in [(1.,0.,1.), (2.,.5,3.), (1.,-.4,.9)]:
            def Q(t): return b11*t*t-2*b12*t+b22
            Z = simpson(lambda x: Q(x)**(-.5),-L,L,1200)
            target = Z**(1-m)
            optimal = simpson(lambda x: (Q(x)**(-.5)/Z)**m*Q(x)**alpha,-L,L,1200)
            uniform = simpson(lambda x: Q(x)**alpha/(2*L)**m,-L,L,1200)
            check(abs(optimal/target-1)<2e-8,'optimal integral equals bound')
            check(uniform >= target*(1-1e-9),'uniform cannot beat optimum')
            # Normalized smooth perturbation of the optimum.
            for eps in [-.3,.3]:
                norm = simpson(lambda x: Q(x)**(-.5)*(1+eps*x/L),-L,L,1200)
                changed = simpson(lambda x: ((Q(x)**(-.5)*(1+eps*x/L))/norm)**m*Q(x)**alpha,-L,L,1200)
                check(changed > target*(1+1e-5),'strict Holder gap')


# Independent deterministic two-dimensional integration of m=2 actual events.
# Coordinates x1=t+u/sqrt(2), x2=t-u/sqrt(2), S=u*u.
def exact_tail_m2(L, z, density):
    alpha = .5
    c = .5
    def outer(t):
        U = min(math.sqrt((1+t*t)/(z-c)), math.sqrt(2)*(L-t), math.sqrt(2)*(t+L))
        if U <= 0: return 0.
        def inner(u):
            return density(t+u/math.sqrt(2))*density(t-u/math.sqrt(2))
        return 2*math.sqrt(2)*simpson(inner,0.,U,40)
    return simpson(outer,-L,L,2000)

for L in [1.,3.]:
    Z = 2*math.asinh(L)
    families = [
        ('uniform',lambda x: 1/(2*L),simpson(lambda x: math.sqrt(1+x*x)/(2*L)**2,-L,L,2000)),
        ('optimal',lambda x: 1/(Z*math.sqrt(1+x*x)),1/Z)
    ]
    for name,p,J in families:
        K = 2*math.sqrt(2)*J
        for z in [2e4,1e5]:
            measured = exact_tail_m2(L,z,p)*math.sqrt(z)
            check(abs(measured/K-1)<.025, 'tail coefficient '+name)

# An exact integer-dimensional ball-volume and positivity test.
for m in range(2,21):
    alpha=(m-1)/2
    volume=math.pi**alpha/math.gamma(alpha+1)
    check(volume>0 and math.isfinite(volume),'tube volume')

# A nontrivial design comparison from the precise integral.
L=10.; m=4; alpha=(m-1)/2; Z=2*math.asinh(L)
uniform=simpson(lambda t:(1+t*t)**alpha/(2*L)**m,-L,L,4000)
opt=Z**(1-m)
ratio=uniform/opt
check(6.9 < ratio < 7.0,'four-sample tail gain')

print('PASS:',checks,'checks')
print('For [-10,10], B=I, m=4: uniform/optimal sharp tail constant =',format(ratio,'.12f'))
print('Warning: exact finite checks do not prove the limiting probability or Holder theorem.')
