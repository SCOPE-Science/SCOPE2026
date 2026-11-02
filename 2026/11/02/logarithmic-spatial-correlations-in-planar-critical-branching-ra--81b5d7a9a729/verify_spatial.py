"""Finite rational checks for the exact two-site factorial-moment identity.

These checks test algebraic identities at finite generations; the asymptotic
statements additionally require the analytical heat-kernel estimates.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import exp, pi

MOVES = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))
MAX_T = 12
COUNTS = [{(0, 0): 1}]
for t in range(1, MAX_T + 1):
    d = defaultdict(int)
    for (x, y), count in COUNTS[-1].items():
        for dx, dy in MOVES:
            d[x+dx, y+dy] += count
    COUNTS.append(dict(d))

@lru_cache(None)
def p(t, xy):
    if t < 0 or t > MAX_T:
        raise ValueError('outside finite support table')
    return Fraction(COUNTS[t].get(xy, 0), 5**t)

@lru_cache(None)
def F_recurrence(t, x, y):
    """First-generation recursion for offspring variance one."""
    if t == 0:
        return Fraction(0)
    result = p(t, x) * p(t, y)
    for dx, dy in MOVES:
        xx = (x[0]-dx, x[1]-dy)
        yy = (y[0]-dx, y[1]-dy)
        result += F_recurrence(t-1, xx, yy)/5
    return result

def F_sum(t, x, y):
    """Independent genealogy summation over the most recent split time."""
    result = Fraction(0)
    for s in range(1, t+1):
        for z, count in COUNTS[t-s].items():
            xz = (x[0]-z[0], x[1]-z[1])
            yz = (y[0]-z[0], y[1]-z[1])
            result += Fraction(count, 5**(t-s))*p(s, xz)*p(s, yz)
    return result

assertions = 0
sites = ((0,0),(1,0),(0,1),(1,1),(2,0),(-1,1),(3,0))
for t in range(1, 7):
    for x in sites:
        for y in sites:
            assert F_recurrence(t,x,y) == F_sum(t,x,y), (t,x,y)
            assertions += 1

for s in range(1, 7):
    for x in sites:
        for y in sites:
            lhs = sum((p(s,(x[0]-z[0],x[1]-z[1])) *
                       p(s,(y[0]-z[0],y[1]-z[1]))
                       for z0 in COUNTS[s]
                       for z in ((x[0]-z0[0], x[1]-z0[1]),)), Fraction(0))
            rhs = p(2*s, (x[0]-y[0],x[1]-y[1]))
            assert lhs == rhs, (s,x,y)
            assertions += 1

# Gaussian convolution/product identity, with covariance (2/5) t I.
def g(t, x):
    if t <= 0:
        raise ValueError('positive heat time required')
    return 5/(4*pi*t)*exp(-5*(x[0]*x[0]+x[1]*x[1])/(4*t))
for s in (0.17,0.5,1.2):
    for x in ((0.3,-0.4),(0,0),(1,0.2)):
        for y in ((0.2,0.7),(-0.1,0),(0,0)):
            for z in ((0,0),(-0.3,0.3),(1,-1)):
                left = g(s,(x[0]-z[0],x[1]-z[1]))*g(s,(y[0]-z[0],y[1]-z[1]))
                mid = ((x[0]+y[0])/2,(x[1]+y[1])/2)
                right = g(2*s,(x[0]-y[0],x[1]-y[1]))*g(s/2,(z[0]-mid[0],z[1]-mid[1]))
                assert abs(left-right) <= 1e-12*max(left,right), (s,x,y,z)
                assertions += 1

print('PASS: %d finite rational and Gaussian product checks' % assertions)
