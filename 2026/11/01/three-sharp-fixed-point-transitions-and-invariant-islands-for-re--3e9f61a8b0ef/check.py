#!/usr/bin/env python3
"""Exact rational checks for fixed centers of reduced planar rotations."""
from fractions import Fraction as Q
from itertools import product


def centers(t, sign):
    """Analytic predicted nonzero fixed points for cot(theta/2)=sign*t."""
    p = []
    if t < 2:
        p.append((Q(1,2),t/2) if sign == 1 else (t/2,Q(1,2)))
    if t < 1:
        p.append(((1-t)/2,(1+t)/2) if sign == 1 else ((1+t)/2,(1-t)/2))
    if t < Q(1,2):
        p.append((1-t/2,Q(1,2)+t) if sign == 1 else (Q(1,2)+t,1-t/2))
    return p


def brute_fixed(t, sign):
    # tan(theta/2) sign convention, rational rotation matrix.
    c = (t*t-1)/(t*t+1)
    s = sign*(2*t)/(t*t+1)
    result = set()
    for a,b in product(range(-6,7),repeat=2):
        # Exact inverse: (I-R)^-1 (a,b)
        cot = sign*t
        x=(Q(a)-cot*Q(b))/2
        y=(cot*Q(a)+Q(b))/2
        if 0 <= x < 1 and 0 <= y < 1:
            assert (1-c)*x+s*y == a
            assert -s*x+(1-c)*y == b
            assert (x,y) not in result
            result.add((x,y))
    return result


def radius(z):
    x,y=z
    return min(x,1-x,y,1-y)


def predicted_radius(t,i):
    if i==0: return min(t,2-t)/2
    if i==1: return (1-t)/2
    return min(t/2,Q(1,2)-t)


def verify(t,sign):
    expected = {(Q(0),Q(0)),*centers(t,sign)}
    actual = brute_fixed(t,sign)
    assert expected == actual, (t, sign, expected, actual)
    nonzero=centers(t,sign)
    for i,z in enumerate(nonzero):
        assert radius(z) == predicted_radius(t,i)
        assert radius(z)>0
        c=(t*t-1)/(t*t+1)
        s=sign*(2*t)/(t*t+1)
        assert ((1-c)*z[0]+s*z[1], -s*z[0]+(1-c)*z[1]) in [(Q(a),Q(b)) for a,b in product(range(-6,7), repeat=2)]
    # Exact square-distance disjointness: strict for each pair of open disks.
    for i,z in enumerate(nonzero):
        for w in nonzero[i+1:]:
            dist2=(z[0]-w[0])**2+(z[1]-w[1])**2
            assert dist2 >= (radius(z)+radius(w))**2

cases = [Q(1,100),Q(1,4),Q(1,3),Q(2,5),Q(1,2),Q(3,4),Q(1),Q(6,5),Q(2),Q(5,2),Q(12)]
for sign,t in product((-1,1),cases):
    verify(t,sign)
assert brute_fixed(Q(0),1)=={(Q(a,2),Q(b,2)) for a,b in product(range(2),repeat=2)}
print(f"PASS: {2*len(cases)+1} exact center classifications, radius and disjointness checks")
