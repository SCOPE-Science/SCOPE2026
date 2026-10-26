#!/usr/bin/env python3
"""Exact independent finite checks for a one-sentinel path transmission model.

This verifier checks finite instances only; the unrestricted result follows
from the accompanying mathematical proof.
"""
from fractions import Fraction as Q
import json


def conditional_terms(n, j, p):
    F = sum((p ** abs(i-j) for i in range(1,n+1) if i != j), Q(0))
    G = sum((abs(i-j)*p ** abs(i-j) for i in range(1,n+1) if i != j), Q(0))
    return F, G


def direct_terms(n, j, p):
    """Enumerate each bond configuration, not merely infection paths."""
    D = Q(0)
    G = Q(0)
    for mask in range(1<<(n-1)):
        opened = mask.bit_count()
        wt = p**opened*(1-p)**(n-1-opened)
        for seed in range(1,n+1):
            if seed == j:
                continue
            lo,hi = sorted((seed,j))
            necessary = ((1<<(hi-lo))-1)<<(lo-1)
            if mask & necessary == necessary:
                D += wt
                G += (hi-lo)*wt
    return D,G


def m_minus_mu_sign(n, j, p):
    d = n - 2*j
    assert j >= 2 and d >= 1
    F,G = conditional_terms(n,j,p)
    M = Q(j) - Q(d)*p**d/(1-p**d)
    return M-G/F


def threshold_interval(n,j,k=20):
    a,b=0,1<<k
    for _ in range(k):
        mid=(a+b)//2
        if m_minus_mu_sign(n,j,Q(mid,1<<k)) > 0: a=mid
        else: b=mid
    return (a,b,1<<k)


def run():
    configurations=0
    tuples=0
    for n in range(2,10):
        for j in range(1,n+1):
            for p in (Q(1,4),Q(1,3),Q(2,3),Q(3,4)):
                F,G=conditional_terms(n,j,p)
                A,B=direct_terms(n,j,p)
                assert (A,B)==(F,G),(n,j,p,A,B,F,G)
                tuples+=1
        configurations += (1<<(n-1))*n*4
    thresholds={}
    for n in range(5,25):
        k=(n+1)//2
        prev=None
        cells=[]
        for j in range(2,k):
            a,b,den=threshold_interval(n,j)
            assert b==a+1
            assert m_minus_mu_sign(n,j,Q(a,den))>0
            assert m_minus_mu_sign(n,j,Q(b,den))<0
            if prev is not None: assert a>prev
            prev=b
            cells.append(dict(position=j,interval=[a,b,den]))
        thresholds[str(n)]=cells
    for n in range(3,25):
        for p in [Q(1,9),Q(1,3),Q(1,2),Q(2,3),Q(9,10)]:
            fs=[conditional_terms(n,j,p) for j in range(1,n+1)]
            center=n//2 # zero-index left center
            assert fs[center][0]==max(f for f,_ in fs)
            mus=[g/f for f,g in fs]
            opt=[j+1 for j,m in enumerate(mus) if m==min(mus)]
            assert min(opt)>=2 and max(opt)<=n-1
            assert all(n+1-j in opt for j in opt)
            a=[(j,m) for j,m in enumerate(mus[:(n+1)//2],start=1)]
            # Any optimal left-side position is predicted by switches at threshold roots.
            predicted=2
            for j in range(2,(n+1)//2):
                if m_minus_mu_sign(n,j,p)<0: predicted=j+1
                else: break
            assert predicted in opt,(n,p,predicted,opt)
    five=thresholds['5'][0]
    assert five['position']==2
    # n=5 switch is the positive root of p*p+2*p-1.
    low=Q(five['interval'][0],five['interval'][2])
    high=Q(five['interval'][1],five['interval'][2])
    assert low*low+2*low-1<0<high*high+2*high-1
    return {
        'model':'one-step independent bond-transmission on a path, uniform initial seed excluding monitor',
        'exact_direct_bond_enumerations':tuples,
        'total_labeled_bond_configurations_considered':configurations,
        'rational_parameters':['1/4','1/3','2/3','3/4'],
        'path_orders_for_direct_check':[2,3,4,5,6,7,8,9],
        'threshold_brackets_denominator':1<<20,
        'sample_threshold_brackets':{n:thresholds[str(n)] for n in range(5,13)},
        'all_thresholds_bracketed_and_ordered_through_n':24,
        'additional_objective_optima_checks':22*5,
        'n5_conditional_formula':{'position_2':'(2+2p+3p^2)/(2+p+p^2)','position_3':'(2+4p)/(2+2p)','threshold_polynomial':'p^2+2p-1'},
        'status':'EXACT_FINITE_CHECKS_PASSED',
        'limits':'No finite enumeration proves the all-n theorem; proof is mathematical in RESULT.md.'
    }

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,separators=(',',':')))
