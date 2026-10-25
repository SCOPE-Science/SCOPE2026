#!/usr/bin/env python3
"""Independent numerical checks for fixed-dose SIRVS equilibrium envelopes.

Python 3 standard library only. Analytical inequalities and uniqueness are proved
in RESULT.md; numerical finite tests here do not substitute for the proof.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import exp, expm1, isclose


def extremal_laws(lo: Q, hi: Q, mean: Q, variance: Q):
    assert lo < mean < hi and 0 < variance < (mean-lo)*(hi-mean)
    right = mean + variance/(mean-lo)
    left = mean - variance/(hi-mean)
    wlo = variance / ((mean-lo)**2+variance)
    whi = variance / ((hi-mean)**2+variance)
    small_B = ((lo,wlo),(right,1-wlo))
    large_B = ((left,1-whi),(hi,whi))
    return small_B,large_B


def check_moments(law,mean,variance):
    assert sum((p for _,p in law),Q(0))==1
    assert sum((p*t for t,p in law),Q(0))==mean
    assert sum((p*(t-mean)**2 for t,p in law),Q(0))==variance
    assert min(t for t,_ in law)>0


def B(law,v):
    assert v>0
    return sum(float(p)*(-expm1(-v*float(t)))/v for t,p in law)


def solve(R,infectious_mean,vaccine_mean,dose_flux,law):
    # R is R_0; v is the per-eligible-individual vaccination hazard.
    k = 1.0-1.0/R-dose_flux*vaccine_mean
    assert k>0 and dose_flux>0 and R>1
    def g(hazard):
        bb = B(law,hazard)
        return hazard*(1.0/R+k*bb/(infectious_mean+bb))
    left,right=0.0, dose_flux*R
    assert g(right)>=dose_flux
    for _ in range(90):
        mid=(left+right)/2.0
        if g(mid)<dose_flux: left=mid
        else: right=mid
    hazard=(left+right)/2.0
    bb=B(law,hazard)
    incidence=k/(infectious_mean+bb)
    s=1.0/R
    infected=incidence*infectious_mean
    recovered=incidence*bb
    vaccinated=dose_flux*vaccine_mean
    assert isclose(s+infected+recovered+vaccinated,1.0,rel_tol=0,abs_tol=1e-12)
    assert isclose(hazard*(s+recovered),dose_flux,rel_tol=0,abs_tol=1e-12)
    # Independent fixed-hazard source equilibrium formula (per-susceptible force of infection).
    phi=(R-1-hazard*vaccine_mean)/(infectious_mean+(1+hazard*vaccine_mean)*bb)
    assert phi>0 and isclose(phi,R*incidence,rel_tol=0,abs_tol=1e-12)
    return hazard,incidence,bb


def verify():
    count=0
    lo,hi,mean,var=Q(1),Q(7),Q(3),Q(4)
    low,high=extremal_laws(lo,hi,mean,var)
    middle=((Q(1),Q(1,3)),(Q(3),Q(1,2)),(Q(7),Q(1,6)))
    for law in (low,middle,high):
        check_moments(law,mean,var);count+=4
    assert low==((Q(1),Q(1,2)),(Q(5),Q(1,2)))
    assert high==((Q(2),Q(4,5)),(Q(7),Q(1,5)))
    count+=2
    for v in (0.0001,0.003,0.1,0.3,0.7,1.,2.3,5.,10.):
        bsmall,bmiddle,bbig=(B(law,v) for law in (low,middle,high))
        assert bsmall < bmiddle < bbig;count+=2
        # Fixed-mean and fixed-variance Laplace bounds also hold at each rate.
        for s in (0,1,2,3,4,5,6,7,8,9,10):
            w=s/10
            law=tuple((t,p*w) for t,p in low)+tuple((t,p*(1-w)) for t,p in high)
            bv=B(law,v)
            assert bsmall-1e-13<=bv<=bbig+1e-13;count+=2
    R,a,b,f=3.0,0.5,1.0,0.4
    results=[solve(R,a,b,f,law) for law in (low,middle,high)]
    hazard=[x[0] for x in results]
    inc=[x[1] for x in results]
    assert hazard[0]>hazard[1]>hazard[2];count+=2
    assert inc[0]>inc[1]>inc[2];count+=2
    exact_num=[(0.7853507020102211,0.1813468072896836),
               (0.7805607737645018,0.1750958197120916),
               (0.7767098359188233,0.17001433095845214)]
    for val,expect in zip(results,exact_num):
        assert isclose(val[0],expect[0],abs_tol=2e-11,rel_tol=0)
        assert isclose(val[1],expect[1],abs_tol=2e-11,rel_tol=0)
        count+=2
    # Wider parameter sweep; all equal moments, but different distributions.
    for r in (1.2,1.5,2.,3.,5.,10.):
        for am in (0.2,0.5,1.,2.,8.):
            for vm in (0.3,1.,2.):
                for share in (0.1,0.3,0.6,0.9):
                    f=(1-1/r)/vm*share
                    v0,j0,_=solve(r,am,vm,f,low)
                    v1,j1,_=solve(r,am,vm,f,middle)
                    v2,j2,_=solve(r,am,vm,f,high)
                    assert v0>v1>v2 and j0>j1>j2
                    count+=4
    # Direct second-moment envelope test with other supports/means/variances.
    for a0,b0,mu,vr in [(Q(1,2),Q(9),Q(3),Q(2)),
                         (Q(1),Q(4),Q(2),Q(1)),
                         (Q(3),Q(12),Q(7),Q(4)),
                         (Q(1,10),Q(5),Q(2),Q(3))]:
        E0,E1=extremal_laws(a0,b0,mu,vr)
        for E in (E0,E1): check_moments(E,mu,vr)
        for v in (0.05,0.25,0.8,3.0):
            assert B(E0,v)<B(E1,v)
            h0,j0,_=solve(3.0,0.7,1.0,0.35,E0)
            h1,j1,_=solve(3.0,0.7,1.0,0.35,E1)
            assert h0>h1 and j0>j1
            count+=3
    print(f"PASS {count} explicit numerical assertions")
    print("Exact rational extremal laws:",low,high)
    print("Sample [lower-B, interior, upper-B] hazard/incidence:",results)
    print("Theorem's global inequalities depend on the analytical proof, not this sweep.")

if __name__=='__main__':
    verify()
