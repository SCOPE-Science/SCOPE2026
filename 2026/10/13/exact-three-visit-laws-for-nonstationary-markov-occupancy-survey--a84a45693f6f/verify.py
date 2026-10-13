#!/usr/bin/env python3
"""Exact arithmetic checks for three-occasion occupancy with Markov detections."""
from fractions import Fraction as F
from itertools import product

def law(psi, pi, a, b):
    # Binary words 000,...,111, for three ordered survey occasions.
    out = {}
    for v in product((0, 1), repeat=3):
        cond = (pi if v[0] else 1-pi)
        for old, new in zip(v, v[1:]):
            cond *= (b if new else 1-b) if old else (a if new else 1-a)
        out[''.join(map(str, v))] = psi*cond + ((1-psi) if v == (0,0,0) else 0)
    assert sum(out.values()) == 1
    assert all(0 < x < 1 for x in out.values())
    return out

def reconstruct(q):
    u = sum(q['1'+s] for s in ('00','01','10','11'))
    r = q['010']+q['011']
    b = (q['110']+q['111'])/u
    a = q['101']/(q['100']+q['101'])
    psi = u+r/a
    pi = u/psi
    return psi, pi, a, b

def constraints(q):
    psi,pi,a,b = reconstruct(q)
    u = sum(q['1'+s] for s in ('00','01','10','11'))
    r = q['010']+q['011']
    return (q['111']==u*b*b and q['011']==r*b and q['001']==r*(1-a)
            and all(0<t<1 for t in (psi,pi,a,b)))

def two_law(q):
    return {x+y:sum(q[x+y+z] for z in '01') for x in '01' for y in '01'}

def check():
    vals=[F(1,5),F(1,3),F(1,2),F(2,3),F(4,5)]
    count=0
    for p in product(vals,repeat=4):
        q=law(*p)
        assert reconstruct(q)==p
        assert constraints(q)
        count+=1
    orig=(F(3,5),F(2,5),F(1,3),F(2,3))
    alt=(F(12,25),F(1,2),F(1,2),F(2,3))
    assert two_law(law(*orig))==two_law(law(*alt))
    assert law(*orig)!=law(*alt)
    # A nonempty three-history perturbation violates an exact Markov constraint.
    q=law(*orig)
    eps=F(1,10000)
    q['011']+=eps
    q['010']-=eps
    assert not constraints(q)
    print('VERIFY_OK exact_parameter_tuples=',count,
          ' two_visit_alias=1 three_visit_identification=1 feasibility_constraints=1')

if __name__=='__main__':
    check()
