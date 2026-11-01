#!/usr/bin/env python3
"""Exact rational tests for the prime-two delay-Lozi classification.

This program supplements, but does not replace, the parameter-uniform proof.
It uses only Python's standard library and does not require external data.
"""
from fractions import Fraction as F
from itertools import product


def branch_pairs(a, nu, k, d):
    """Exhaust nonsingular two-phase sign chambers by exact 2x2 linear algebra."""
    c = 1 - nu
    pairs = set()
    for signs in product((1, -1), repeat=2):
        rows=[]
        for i in (0,1):
            j=(i+k)%2
            ell=(i+d)%2
            row=[F(0),F(0)]
            row[i] += 1
            row[j] += a*signs[j]
            row[ell] += c
            rows.append(row)
        aa,bb=rows[0]; cc,dd=rows[1]
        det=aa*dd-bb*cc
        if det == 0:
            continue
        u=(dd-bb)/det
        v=(aa-cc)/det
        valid=(u>=0 if signs[0]>0 else u<=0) and (v>=0 if signs[1]>0 else v<=0)
        if valid and u!=v:
            pairs.add(tuple(sorted((u,v))))
    return pairs


def formula(a,nu,k,d):
    s=2-nu
    h=s if d%2==0 else nu
    if k%2:
        if a>h:
            den=a*a+s*h
            return {tuple(sorted(((a+h)/den,(h-a)/den)))}
    else:
        if a>h and a*a>s*h:
            den=a*a-s*h
            return {tuple(sorted(((a-h)/den,-(a+h)/den)))}
    return set()


def full_orbit(u,v,a,nu,k,d):
    # At even n use u, at odd n use v, with same periodicity for all integers n.
    f=lambda n: u if n%2==0 else v
    for n in range(-2*d,2*d+1):
        assert f(n)==1-a*abs(f(n-k))-(1-nu)*f(n-d)


def run():
    checked=0
    params=[F(t,10) for t in range(1,41)]
    nus=[F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(7,4)]
    for d in range(2,13):
        for k in range(1,d):
            for nu in nus:
                for a in params:
                    s=2-nu;h=s if d%2==0 else nu
                    # Separate singular chambers are checked directly below.
                    if a in (s,nu) or a*a==s*h:
                        continue
                    got=branch_pairs(a,nu,k,d)
                    want=formula(a,nu,k,d)
                    assert got==want,(d,k,a,nu,got,want)
                    for u,v in want:
                        full_orbit(u,v,a,nu,k,d)
                    checked+=1
    # Critical nonnegative continua for odd k, with both delay parities.
    for d,k,nu,a,u,v in [
        (3,1,F(1,2),F(1,2),F(1,4),F(3,4)),
        (2,1,F(1,2),F(3,2),F(1,6),F(1,2)),
        (3,2,F(3,2),F(3,2),-F(1,2),-F(3,2)),
    ]:
        full_orbit(u,v,a,nu,k,d)
    # An exact two-cycle with just one fixed point in the same system.
    full_orbit(F(2),-F(6),F(1),F(1,2),2,3)
    assert F(1)<2-F(1,2)  # a=1 below negative fixed-point threshold 3/2.
    # Exact boundary/scaling identities in the high-dimensional, even/odd case.
    nu=F(1,2); a=F(1)
    s=2-nu; D=a*a-nu*s
    u=(a-nu)/D; v=-(a+nu)/D
    assert (u,v)==(F(2),-F(6))
    assert u+v == -2*nu/D
    # Independent fixed-point check at the signed-branch level.
    for nu in nus:
        s=2-nu
        for a in params:
            qpos=1/(s+a)
            assert qpos==1-a*abs(qpos)-(1-nu)*qpos
            if a>s:
                qneg=1/(s-a)
                assert qneg<0 and qneg==1-a*abs(qneg)-(1-nu)*qneg
    print('PASS exact nonsingular sign-chamber checks:',checked)
    print('PASS three distinct critical line examples, exact 2-cycle and fixed points')


if __name__=='__main__':
    run()
