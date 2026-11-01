#!/usr/bin/env python3
"""Exact-rational witness checks for an interval-map Lyapunov lower bound.

The analytic proof of the universal bound is in RESULT.md; this code
independently checks rational parameters, periodic witnesses, and the
critical identity interval. No finite trial is used as an infinite proof.
"""
from fractions import Fraction as Q
from math import log


def branch(x, r, s):
    assert -s <= x <= s
    if x <= -1:
        return r * (x + 1), 'O', r
    if x < 0:
        return s * (x + 1), 'I', s
    if x < 1:
        return s * (x - 1), 'I', s
    return r * (x - 1), 'O', r


def itinerary(x, r, s, n):
    states, labels, multipliers = [], [], []
    for _ in range(n):
        assert x not in (-1, 0, 1), ('nondifferentiable orbit', x)
        states.append(x)
        x, typ, d = branch(x, r, s)
        labels.append(typ)
        multipliers.append(d)
    return x, states, ''.join(labels), multipliers


def check_family(r, s):
    assert 0 < r < 1
    L = (1+r+r*r)/(r*r)
    U = 1+(1+r+r*r)/(r*r*r)
    assert L < s < U
    P = s*r**3
    K = r+r*r+r**3
    assert r**3*s-r*(1+r+r*r) < 1
    assert r*r*s-r*(1+r) > 1
    u = (P-K)/(1+P)
    assert 0 < u < 1
    z, states, word, factors = itinerary(u, r, s, 8)
    assert z == u
    assert word == 'IOOOIOOO', word
    assert len(set(states)) == 8
    assert states[4] == -u
    assert states[5] == -states[1]
    assert states[6] == -states[2]
    assert states[7] == -states[3]
    multiplier = Q(1)
    for factor in factors:
        multiplier *= factor
    assert multiplier == P*P
    # Every 4-step subword of every checked regular trajectory has an I.
    for j in range(1, 190):
        x = -s + 2*s*Q(j, 191)
        if x in (-1, 0, 1):
            continue
        word = ''
        for i in range(128):
            if x in (-1,0,1):
                break
            x, typ, d = branch(x, r, s)
            word += typ
            if len(word) >= 4:
                assert word[-4:] != 'OOOO'
            if x not in (-1,0,1) and i+1 > 0:
                # For all completed prefixes, k>=floor(n/4).
                assert word.count('I') >= (i+1)//4
    return (r,s, u, P, L, U, word)


def critical_band():
    r=Q(2,5)
    s=Q(125,8)
    assert s*r**3 == 1
    d=1-r-r*r-r*r*r
    assert d == Q(47,125)
    for j in range(1,151):
        t = d*Q(j,151)
        v, states, labels, derivatives = itinerary(t,r,s,8)
        assert v == t
        assert labels == 'IOOOIOOO'
        assert states[4] == t-d
        for k in (1,2,4):
            assert states[k] != t
        der=Q(1)
        for dx in derivatives:
            der *= dx
        assert der == 1
    return d


def canonical():
    r,s=Q(4,5),Q(5)
    u=((s*r**3) -(r+r*r+r**3))/(1+s*r**3)
    assert u == Q(76,445)
    z, states, word, slopes=itinerary(u,r,s,8)
    assert [5*t for t in states] == [Q(z,89) for z in [76,-1845,-1120,-540,-76,1845,1120,540]]
    assert s*r**3 == Q(64,25)
    assert (s*r**3)**2 == Q(4096,625)
    return log(float(s*r**3))/4


def main():
    cases=[(Q(4,5),Q(5)),(Q(2,5),Q(12)),(Q(2,5),Q(125,8)),(Q(2,5),Q(20)),(Q(3,5),Q(7)),(Q(1,5),Q(100))]
    out=[]
    for r,s in cases:
        out.append(check_family(r,s)[:4])
    d=critical_band()
    lam=canonical()
    assert 0.235 < lam < 0.236
    print('PASS: six exact-rational parameter checks',out)
    print('PASS: 150 distinct exact neutral period-8 sample points; band length', d)
    print('PASS: exact unscaled 2023 eight-cycle; exact return multiplier 4096/625')
    print('PASS: canonical sharp minimal exponent %.15f' % lam)

if __name__ == '__main__':
    main()
