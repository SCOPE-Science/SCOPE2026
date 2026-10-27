#!/usr/bin/env python3
"""Exact five-voter epistemic delegation checks (Python standard library only).

The electorate contains one compulsory voting expert and four identical
potential delegators. Boolean 1 denotes a correct signal. Every ordinary
voter independently delegates to the expert with probability d.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def reliability_direct(p, q):
    g = lambda n, minimum: sum(Q(comb(n, j)) * p**j * (1-p)**(n-j)
                               for j in range(minimum, n+1))
    return q*g(4, 2) + (1-q)*g(4, 3)


def reliability_one(p, q):
    return q*(1-(1-p)**3) + (1-q)*p**3


def formula(p, q, d):
    delta0 = reliability_direct(p, q)-q
    delta1 = reliability_one(p, q)-q
    return q+(1-d)**4*delta0+4*d*(1-d)**3*delta1


def enumerate_all(p, q, d, ordinary=4):
    total = Q(0)
    for delegated in product((0, 1), repeat=ordinary):
        m = sum(delegated)
        pd = d**m*(1-d)**(ordinary-m)
        for expert_right in (0, 1):
            pe = q if expert_right else 1-q
            for ordinary_right in product((0, 1), repeat=ordinary):
                ps = Q(1)
                for right in ordinary_right:
                    ps *= p if right else 1-p
                weighted_correct = (m+1)*expert_right + sum(
                    right for right, flag in zip(ordinary_right, delegated)
                    if not flag)
                if weighted_correct > (ordinary+1)//2:
                    total += pd*pe*ps
    return total


def thresholds(p):
    q2 = p*p/(p*p+(1-p)**2)
    q3 = p**3/(p**3+(1-p)**3)
    return q2,q3


def optimum(p,q):
    q2,q3=thresholds(p)
    if q<=q2: return Q(0)
    if q>=q3: return Q(1)
    a=reliability_direct(p,q)-q
    b=reliability_one(p,q)-q
    return (b-a)/(4*b-a)


def check_all():
    n=0
    for p in [Q(3,5),Q(2,3),Q(7,10),Q(4,5),Q(9,10)]:
        q2,q3=thresholds(p)
        assert p<q2<q3<1
        qs=[(p+q2)/2,q2,(q2+q3)/2,q3,(q3+1)/2]
        for q in qs:
            for d in [Q(0),Q(1,10),Q(1,4),Q(2,5),Q(1,2),Q(3,4),Q(9,10),Q(1),optimum(p,q)]:
                assert enumerate_all(p,q,d)==formula(p,q,d), (p,q,d)
                n+=1
            dstar=optimum(p,q)
            fstar=formula(p,q,dstar)
            if q2<q<q3:
                assert Q(0)<dstar<Q(1)
                assert fstar>formula(p,q,Q(0))
                assert fstar>formula(p,q,Q(1))
            elif q<=q2:
                assert dstar==0
                assert fstar>formula(p,q,Q(1))
            else:
                assert dstar==1
                assert fstar>formula(p,q,Q(0))
    p,q=Q(7,10),Q(9,10)
    dstar=optimum(p,q)
    assert dstar==Q(84,209)
    assert reliability_direct(p,q)==Q(11123,12500)
    assert reliability_one(p,q)==Q(91,100)
    assert formula(p,q,dstar)==Q(164718547,182586580)
    assert formula(p,q,dstar)-q==Q(78125,36517316)
    for p in [Q(3,5),Q(7,10),Q(4,5)]:
        for q in [(p+1)/2,Q(1)]:
            baseline=enumerate_all(p,q,Q(0),ordinary=2)
            for d in [Q(0),Q(1,3),Q(1,2),Q(1)]:
                observed=enumerate_all(p,q,d,ordinary=2)
                assert observed==(1-d)**2*baseline+(1-(1-d)**2)*q
    print('VERIFIED: {} independent five-voter exact enumerations, all phase boundaries, exact witness, and three-voter boundary'.format(n))

if __name__=='__main__':
    check_all()
