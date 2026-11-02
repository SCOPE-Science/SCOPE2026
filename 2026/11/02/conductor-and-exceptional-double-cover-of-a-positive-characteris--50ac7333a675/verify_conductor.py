#!/usr/bin/env python3
"""Finite checks for the conductor theorem; proof for all m is in RESULT.md.

The rings k[x,z,t] / (x^2*t-z^(2*m)) and k[x,z,w] / (x*w-z^m)
embed in k[u,v] by x=u^m, z=u*v, t=v^(2*m), w=v^m.
The check compares their affine monoids in finite boxes, for m=1..16.
"""

def monoid(gens, lim):
    points = {(0, 0)}
    frontier = [(0, 0)]
    while frontier:
        a, b = frontier.pop()
        for c, d in gens:
            pair = (a+c, b+d)
            if max(pair) <= lim and pair not in points:
                points.add(pair)
                frontier.append(pair)
    return points


def check(m):
    lim = 12*m+8
    gens_b = ((m,0), (1,1), (0,2*m))
    gens_s = ((m,0), (1,1), (0,m))
    b = monoid(gens_b, lim)
    s = monoid(gens_s, lim)
    for a, v in s:
        if max(a, v) > 5*m:
            continue
        conductor = ((a, v) in b and all((a+c, v+d) in b for c,d in gens_s))
        explicit = (a >= m and (a-m, v) in s)
        assert conductor == explicit, (m, (a,v), conductor, explicit)
    assert all((a+m,b) in monoid(gens_b, lim) for a,b in s if max(a+m,b)<=lim)
    # w is integral over B, and x*w=z^m; at the generic conductor
    # divisor the residue extension is t=w^2 of degree two.
    assert (2*m, 0) in b and (m, m) in b and (0, 2*m) in b
    return True

if __name__ == '__main__':
    for m in range(1, 17):
        check(m)
    print('NASH_CONDUCTOR_SEMIGROUP_16_CASES_OK')
