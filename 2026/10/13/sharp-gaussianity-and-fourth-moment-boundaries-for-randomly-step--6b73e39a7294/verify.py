#!/usr/bin/env python3
"""Exact rational consistency checks for randomized stochastic theta discretization."""
from fractions import Fraction as F
from itertools import product

def calc(theta, lam, sig, law):
    assert 0 <= theta <= 1 and lam > 0 and sig > 0
    assert law and all(h > 0 and w > 0 for h, w in law)
    assert sum(w for _, w in law) == 1
    r2 = r4 = s2 = s4 = cross = F(0)
    for h,w in law:
        r = (1-(1-theta)*lam*h)/(1+theta*lam*h)
        z = sig*sig*h/(1+theta*lam*h)**2
        r2 += w*r*r
        r4 += w*r**4
        s2 += w*z
        s4 += w*z*z
        cross += w*r*r*z
        # Unrounded stochastic theta equation and fixed-h OU variance identity.
        assert (1+theta*lam*h)*r == 1-(1-theta)*lam*h
        assert (1+theta*lam*h)**2 * z == sig*sig*h
    assert r2 < 1
    v = s2/(1-r2)
    target = sig*sig/(2*lam)
    delta = -(2*theta-1)*sig*sig*lam*sum(w*h*h/(1+theta*lam*h)**2 for h,w in law)/(2*(1-r2))
    assert v-target == delta
    if r4 < 1:
        fourth = (6*cross*v+3*s4)/(1-r4)
        q = [((1-(1-theta)*lam*h)/(1+theta*lam*h))**2*v+sig*sig*h/(1+theta*lam*h)**2 for h,w in law]
        mean_q = sum(w*z for (_,w),z in zip(law,q))
        var_q = sum(w*(z-mean_q)**2 for (_,w),z in zip(law,q))
        assert mean_q == v
        assert fourth-3*v*v == 3*var_q/(1-r4)
        assert fourth >= 3*v*v
        return r2,r4,v,fourth,var_q
    return r2,r4,v,None,None

def main():
    one = F(1)
    law_a = [(F(1,2),F(1,2)),(F(3,2),F(1,2))]
    law_b = [(F(11,12),F(36,37)),(F(4),F(1,37))]
    for law in [law_a,law_b]:
        assert sum(h*w for h,w in law)==1
        assert sum(h*h*w for h,w in law)==F(5,4)
    assert calc(F(0),one,one,law_a)==(F(1,4),F(1,16),F(4,3),F(92,15),F(1,4))
    assert calc(F(0),one,one,law_b)==(F(1,4),F(1261,576),F(4,3),None,None)
    moment_three = sum(w*abs(1-h)**3 for h,w in law_b)
    assert moment_three == F(1297,1776) < 1 < F(1261,576)
    checked = 0
    for theta,lam,sig in product([F(0),F(1,4),F(1,2),F(3,4),F(1)], [F(1,2),F(1),F(3,2)], [F(1),F(2)]):
        for hs in [[F(1,8),F(3,8)], [F(1,4),F(1,2)], [F(1,3),F(2,3)], [F(1,2),F(3,4)]]:
            result=calc(theta,lam,sig,[(hs[0],F(1,3)),(hs[1],F(2,3))])
            assert result[3] is not None
            if theta==F(1,2):
                assert result[2]==sig*sig/(2*lam)
                assert result[4]==0
            else:
                assert result[4]>0
            checked+=1
        for h in [F(1,8),F(1,3),F(1,2)]:
            result=calc(theta,lam,sig,[(h,one)])
            assert result[4]==0
            checked+=1
    print('VERIFY_OK exact matched moments and fourth-moment split; 210 symbolic-rational parameter checks',checked)

if __name__=='__main__':
    main()
