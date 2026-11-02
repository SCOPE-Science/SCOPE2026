#!/usr/bin/env python3
"""Exact checks for Catalan cherry-count/root-split covariance. Python 3 stdlib only.
Run: python3 verify.py .  Exhaustive tests are finite cross-checks, not proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb

@lru_cache(None)
def cat(n):
    return comb(2*n,n)//(n+1)

def mean_cherries(n):
    return F(0) if n==0 else F(n*(n+1),2*(2*n-1))

@lru_cache(None)
def trees(n):
    if n==0:
        return (None,)
    return tuple((l,r) for k in range(n) for l in trees(k) for r in trees(n-1-k))

def cherries(t):
    if t is None: return 0
    l,r=t
    return (1 if l is None and r is None else 0) + cherries(l) + cherries(r)

def internal_size(t):
    return 0 if t is None else 1+internal_size(t[0])+internal_size(t[1])

def exact_expected_b(n):
    return F(4**(n-1),cat(n))-n

def exact_cov_cb(n):
    return F(n-2,4*(2*n-1))*F(4**(n-1),cat(n))

def exact_var_c(n):
    return F(n*(n-2)*(n-1)*(n+1),2*(2*n-3)*(2*n-1)**2)

def test():
    checks=0
    for n in range(2,11):
        ts=trees(n)
        assert len(ts)==cat(n)
        v=[(cherries(t),internal_size(t[0])*(n-1-internal_size(t[0]))) for t in ts]
        mc=F(sum(c for c,b in v),len(v)); mb=F(sum(b for c,b in v),len(v))
        mcb=F(sum(c*b for c,b in v),len(v))
        vc=F(sum(c*c for c,b in v),len(v))-mc*mc
        assert mc==mean_cherries(n)
        assert mb==exact_expected_b(n)
        assert mcb-mc*mb==exact_cov_cb(n)
        assert vc==exact_var_c(n)
        for i in range(n):
            sub=[c for c,b in v if False]  # allocation-free grouping below
            num=den=0
            for t in ts:
                if internal_size(t[0])==i:
                    num+=cherries(t); den+=1
            assert den==cat(i)*cat(n-1-i)
            assert F(num,den)==mean_cherries(i)+mean_cherries(n-1-i)
            checks+=1
        checks+=len(ts)*3+5
    for n in range(2,101):
        weights=[cat(i)*cat(n-1-i) for i in range(n)]
        assert sum(weights)==cat(n)
        EB=F(sum(weights[i]*i*(n-1-i) for i in range(n)),cat(n))
        ECB=F(sum(weights[i]*i*(n-1-i)*(mean_cherries(i)+mean_cherries(n-1-i)) for i in range(n)),cat(n))
        assert EB==exact_expected_b(n)
        assert ECB-mean_cherries(n)*EB==exact_cov_cb(n)
        assert -4*exact_cov_cb(n)==-F(n-2,2*n-1)*F(4**(n-1),cat(n))
        checks+=4
    print('PASS: %d exact tests, complete enumeration through n=10 (Catalan_10=16796), n=2..100 moment identities.'%checks)

if __name__=='__main__':test()
