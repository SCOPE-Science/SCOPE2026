#!/usr/bin/env python3
"""Reproducible checks for a past-position resetting run-and-tumble model.

Requirements: Python 3.10+, scipy.  Numerical checks are not proof of the limits.
"""
from fractions import Fraction as Q
from math import exp, log
from bisect import bisect_right
from random import Random
from scipy.integrate import solve_ivp

checks = 0
def check(condition, description):
    global checks
    assert condition, description
    checks += 1

def moments(v, gamma, r, eta, times):
    alpha=2*gamma+r
    beta=2*gamma+2*eta*r
    c=1-2*eta
    def rhs(t, y):
        m, j, second, integral = y
        recollection = c*r*j/t if t else 0.0
        second_recollection = r*integral/t if t else 0.0
        return (v-alpha*m+recollection, m-beta*j,
                2*v*m-r*second+second_recollection, second)
    s=solve_ivp(rhs, (0,max(times)), (0.,0.,0.,0.), method='DOP853',
                rtol=2e-11, atol=1e-13, dense_output=True)
    check(s.success, 'ODE integration')
    return {t:s.sol(t) for t in times}

# The single-event derivation of the short-time cubic: reversal-off reset
# integrates -t*s+s*s/3; reversal-on reset integrates -3*t*s+7*s*s/3.
for t in (Q(1),Q(2),Q(5,3)):
    # evaluate the antiderivatives at s=t
    reset_off=(-t*t*t/Q(2)+t*t*t/Q(9))/t**3
    reset_on=(-Q(3,2)*t*t*t+Q(7,9)*t*t*t)/t**3
    check(reset_off == -Q(7,18), 'no-reversal one-reset integral')
    check(reset_on == -Q(13,18), 'reversal one-reset integral')
    check(reset_on-reset_off == -Q(1,3), 'linear reversal contrast')

# The independent Poisson flip integral equals -2*gamma*t^3/3.
for t in (Q(1), Q(7,5)):
    one_flip=((Q(4,3)*t**3-2*t**3+t**3)/t -t*t)
    check(one_flip == -Q(2,3)*t*t, 'ordinary tumble path integral')

for eta in (0., 0.25, 0.5, 0.75, 1.):
    v,g,r=1.,1.,2.
    out=moments(v,g,r,eta,(0.1,1.,8.,100.,10000.))
    mstar=v/(2*g+r)
    slope=2*v*v/(r*(2*g+r))
    check(abs(out[10000.][0]-mstar)<2.e-5, 'mixed-moment plateau')
    est=(out[10000.][2]-out[100.][2])/log(100.)
    check(abs(est-slope)<3.e-4, 'logarithmic variance slope')
    for t in (0.1,1.,8.):
        m,j,second,H=out[t]
        check(second>=0 and H>=0, 'nonnegative moments')
        check(abs(m)<=v/(2*g)+1e-8, 'analytic uniform mixed-moment envelope')
        if eta == .5:
            check(abs(m-mstar*(1-exp(-(2*g+r)*t)))<1e-9,
                  'exact fair-orientation-reset solution')
    # cubic Taylor coefficient at t=0: independent path-event counting
    b=2*g/3+7*r/18+eta*r/3
    t=.001
    short=moments(v,g,r,eta,(t,))[t][2]
    approx=v*v*t*t-v*v*b*t**3
    check(abs(short-approx)<2.e-11, 'short-time cubic')

# Path-level Monte Carlo checks, independent of the moment equations above.
v,g,r,T=1.,1.,2.,8.
rng=Random(20261019)
for eta in (0., .5, 1.):
    n=12000
    mixed=second=0.
    for _ in range(n):
        sign=1 if rng.getrandbits(1) else -1
        starts=[0.];points=[0.];directions=[sign]
        t=x=0.
        while t<T:
            dt=rng.expovariate(g+r)
            if t+dt>=T:
                x+=v*sign*(T-t);break
            x+=v*sign*dt;t+=dt
            if rng.random()<g/(g+r):
                sign=-sign
            else:
                u=rng.random()*t
                j=bisect_right(starts,u)-1
                x=points[j]+v*directions[j]*(u-starts[j])
                if rng.random()<eta:sign=-sign
            starts.append(t);points.append(x);directions.append(sign)
        mixed+=x*sign;second+=x*x
    reference=moments(v,g,r,eta,(T,))[T]
    check(abs(mixed/n-reference[0])<.06, 'independent MC mixed moment')
    check(abs(second/n-reference[2])<.08, 'independent MC mean square position')

print(f'PASS: {checks} deterministic assertions, including fixed-seed path simulation.')
