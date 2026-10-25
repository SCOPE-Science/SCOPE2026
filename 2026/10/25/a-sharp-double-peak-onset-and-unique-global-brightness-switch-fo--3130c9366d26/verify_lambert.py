#!/usr/bin/env python3
"""Reproducible checks for a Lambert-sphere eccentric-orbit phase diagram.

Requires only Python 3 standard library. This is finite numerical corroboration,
not a substitute for the accompanying universal analytic proof.
"""
import math
import random

PI = math.pi


def U(x):
    return math.sin(x) - x * math.cos(x)


def T(x):
    return 2.0 * math.sin(x) / x - 3.0 * math.cos(x)


def Tprime(x):
    return ((3.0*x*x-2.0)*math.sin(x) + 2.0*x*math.cos(x))/(x*x)


def light(x, e):
    return (1.0+e*math.cos(x))**2 * U(x)/PI


def dlight(x, e):
    return (1.0+e*math.cos(x))*x*math.sin(x)*(1.0-e*T(x))/PI


def bisect(fun, low, high, n=78):
    a, b = fun(low), fun(high)
    assert a*b < 0, ('missing sign bracket', low, high, a, b)
    for _ in range(n):
        mid = (low+high)/2.0
        if fun(mid)*a > 0:
            low, a = mid, fun(mid)
        else:
            high = mid
    return (low+high)/2.0


TURN = bisect(Tprime, 2.7, 3.1)
E_FOLD = 1.0/T(TURN)


def peaks(e):
    if e <= E_FOLD:
        return []
    first = bisect(lambda x: T(x)-1.0/e, 0.01, TURN)
    if e < 1.0/3.0:
        second = bisect(lambda x: T(x)-1.0/e, TURN, PI)
        return [first, second]
    return [first]


def excess(e):
    first = peaks(e)[0]
    return light(first, e)-(1.0-e)**2


E_SWITCH = bisect(excess, E_FOLD+0.0001, 1.0/3.0-0.0001)
FIRST, SECOND = peaks(E_SWITCH)
assert abs(E_SWITCH - 0.3258362629061875) < 2e-13
assert abs(E_FOLD - 0.3248980089776666) < 2e-13
assert E_FOLD < E_SWITCH < 1.0/3.0
assert abs(light(FIRST, E_SWITCH)-(1-E_SWITCH)**2) < 3e-15
assert light(SECOND, E_SWITCH) < light(FIRST, E_SWITCH)

# The symbolic factorization is tested independently by differentiation of
# the uncollected product using a centered finite-difference stencil.
rng = random.Random(8675309)
for _ in range(4500):
    e = rng.uniform(0.0, .98)
    x = rng.uniform(.09, PI-.09)
    h = 2e-5
    numeric = (light(x-2*h,e)-8*light(x-h,e)+8*light(x+h,e)-light(x+2*h,e))/(12*h)
    analytic = dlight(x,e)
    assert abs(numeric-analytic) < 2e-9, (e,x,numeric,analytic)

# Test the complete local-extremum phase classification and its one-crossing
# ordering, across representative and randomly selected eccentricities.
trials = [0, .1, .3, E_FOLD-.0002, E_FOLD+.00001, .325, E_SWITCH-.00001,
          E_SWITCH+.00001, .329, 1/3-.00002, 1/3+.00002, .5, .95]
trials += [rng.uniform(0,.99) for _ in range(500)]
for e in trials:
    rr = peaks(e)
    if e < E_FOLD:
        assert len(rr)==0
    elif E_FOLD < e < 1/3:
        assert len(rr)==2 and 0 < rr[0] < TURN < rr[1] < PI
        assert dlight((rr[0]+rr[1])/2,e) < 0
        assert dlight((rr[1]+PI)/2,e) > 0
    elif e > 1/3:
        assert len(rr)==1 and 0 < rr[0] < TURN
        assert dlight((rr[0]+PI)/2,e) < 0
    if e < E_FOLD:
        actual = (1-e)**2
    else:
        actual = max(light(rr[0],e),(1-e)**2)
    grid_best = max(light(PI*j/3200,e) for j in range(3201))
    assert grid_best <= actual + 3e-14 and actual-grid_best < 3e-6, (e,actual,grid_best)
    if E_FOLD < e < E_SWITCH:
        assert excess(e) < 0
    if E_SWITCH < e < 1/3:
        assert excess(e) > 0

# Nonstandard envelope monotonicity: at the inner maximum the logarithmic
# off-full/full height ratio has the displayed positive derivative.
for e in [E_FOLD+.0003, E_SWITCH-.0001, E_SWITCH+.0002,.330,.332]:
    f = peaks(e)[0]
    h = min((1/3-e)/10,(e-E_FOLD)/10,1e-6)
    log_ratio = lambda ee: math.log(light(peaks(ee)[0],ee)/(1-ee)**2)
    num = (log_ratio(e+h)-log_ratio(e-h))/(2*h)
    formula = 2*(1+math.cos(f))/((1-e)*(1+e*math.cos(f)))
    assert abs(num-formula) < 1e-7, (e,num,formula)

print('PASS: 4,500 derivative checks; 513 global phase grids of 3,201 points;')
print('      sign and critical-level tests; strict envelope-derivative comparisons')
print('fold eccentricity : %.15f' % E_FOLD)
print('global switch     : %.15f' % E_SWITCH)
print('fold anomaly (rad): %.15f' % (PI-TURN))
print('off-full phase at switch (rad): %.15f' % (PI-FIRST))
print('intervening local-min phase (rad): %.15f' % (PI-SECOND))
print('common global brightness: %.15f' % light(FIRST,E_SWITCH))
print('local-min brightness: %.15f' % light(SECOND,E_SWITCH))
