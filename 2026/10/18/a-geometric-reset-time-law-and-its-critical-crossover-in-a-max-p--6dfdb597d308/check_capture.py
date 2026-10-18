"""Exact finite tests for the max-plus reset-time theorem.

Uses rational arithmetic. Finite tests corroborate but do not prove the
infinite distribution or the small-parameter total-variation limit.
"""
from fractions import Fraction as Q
from random import Random
from collections import Counter

def g(z, D, B):
    return B - D * max(z, Q(0))

def boundary_hit(z, D, B):
    for n in range(1, 160):
        z = g(z, D, B)
        if z == B:
            return n
    raise AssertionError('reference point may be exceptional')

def formula(hx, hy):
    if (hx-hy) % 2 == 0:
        return 2 * max(hx, hy)
    return 2*hx-1 if hx > hy else 2*hy+1

def reset_time(x, y, T, D, B):
    for j in range(250):
        if x <= 0 and y <= 0:
            return j+2
        x, y = y, B + T*max(y,Q(0)) - D*max(x,Q(0))
    return None

def iterate_pair(x, y, T, D, B):
    return (y+T*max(x,Q(0)), B-D*max(x,Q(0)))

def check_cycle(D, T, B):
    assert D > T*T+T+1
    points = [(B,B), (B*(1+T), B*(1-D)),
              (B*(1+T+T*T-D), B*(1-D*(1+T))),
              (B*(1-D*(1+T)), B)]
    assert len(set(points)) == 4
    for k in range(4):
        assert iterate_pair(*points[k],T,D,B) == points[(k+1)%4]
    assert points[2][0] < 0 and points[2][1] < 0

samples = 0
for D in (Q(6,5),Q(3,2),Q(2),Q(3),Q(7)):
    B = Q(3,2)
    Ts = (Q(0), Q(1,1000000))
    rng=Random(2024)
    for T in Ts:
        check_cycle(D,T,B)
    for i in range(320):
        x=B*(1-D + D*Q(rng.randint(1,999999),1000000))
        y=B*(1-D + D*Q(rng.randint(1,999999),1000000))
        hx=boundary_hit(x,D,B);hy=boundary_hit(y,D,B)
        expected=formula(hx,hy)
        actual=reset_time(x,y,Q(0),D,B)
        assert actual==expected,(D,x,y,hx,hy,expected,actual)
        samples+=1
    # Compare an exact finite sum against the independent-geometric mean.
    q=Q(1,D)
    N=80
    probabilities=[(1-q)*q**(n-1) for n in range(1,N+1)]
    truncated=sum((formula(i,j)*probabilities[i-1]*probabilities[j-1]
                   for i in range(1,N+1) for j in range(1,N+1)),Q(0))
    desired=2*D*(D+2)/(D*D-1)
    # Finite truncation necessarily undercounts a nonnegative tail.
    assert truncated <= desired
    assert desired-truncated < Q(1,1000)
print('EXACT_RESET_CYCLE_AND_GEOMETRIC_MOMENT_CHECK_OK',samples)
