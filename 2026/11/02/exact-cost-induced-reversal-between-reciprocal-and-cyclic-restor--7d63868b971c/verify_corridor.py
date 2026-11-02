#!/usr/bin/env python3
"""Reproduce exact identities and deterministic finite sanity checks for three-patch recruitment matrices.

Requires only Python >= 3.9. The finite checks do not replace the all-parameter proof.
"""
from fractions import Fraction as Q
from itertools import product


def det3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)


def f(lam,a,u,v):
    return lam**3 - 2*a*u*lam - a*a*v


def root(a,u,v):
    # The unique positive root of f, computed by bracketing and bisection.
    assert a>0 and u>=0 and v>=0 and u+v>0
    lo=0.0
    hi=1.0
    while f(hi,float(a),float(u),float(v))<=0:
        hi*=2
    for _ in range(115):
        mid=(hi+lo)/2
        if f(mid,float(a),float(u),float(v))>0:
            hi=mid
        else:
            lo=mid
    return (hi+lo)/2


def main():
    count_det=0
    count_anchor=0
    count_order=0
    count_threshold=0
    vals = [Q(1,2),Q(1),Q(2),Q(3)]
    budgets = [Q(1,4),Q(1),Q(3),Q(8),Q(27)]
    for a, cu, cr in product(vals, repeat=3):
        lam0=a*cu/cr
        b0=a*cu**3/cr**2
        for B in budgets+[b0]:
            observed=[]
            for t in [Q(0),Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(7,8),Q(1)]:
                u=t*B/(2*cu)
                v=(B-2*cu*u)/cr
                for lam in (Q(0),Q(1,2),Q(1),Q(2),Q(5)):
                    mat = [[lam,-u,-v],[-a,lam,-u],[Q(0),-a,lam]]
                    assert det3(mat)==f(lam,a,u,v)
                    count_det += 1
                # Algebraic anchor factor is allocation independent.
                assert f(lam0,a,u,v)==lam0**3-a*a*B/cr
                count_anchor += 1
                r=root(a,u,v)
                observed.append(r)
                if B<b0:
                    assert r<float(lam0)*(1+1e-10)
                elif B>b0:
                    assert r>float(lam0)*(1-1e-10)
                else:
                    assert abs(r-float(lam0))<1e-10*max(1,float(lam0))
                    count_threshold += 1
            if B<b0:
                assert all(observed[j]>observed[j+1]-1e-12 for j in range(6))
            if B>b0:
                assert all(observed[j]<observed[j+1]+1e-12 for j in range(6))
            if B==b0:
                assert max(observed)-min(observed)<1e-9*max(1,float(lam0))
            count_order += 1
            # At endpoints the spectral roots have explicit powers.
            assert abs(observed[0]**3-float(a*a*B/cr))<1e-9*max(1,float(a*a*B/cr))
            assert abs(observed[-1]**2-float(a*B/cu))<1e-9*max(1,float(a*B/cu))
        for r in [Q(1,4),Q(1,2),Q(1),Q(2),Q(4)]:
            budget=min(cr*r**3/a**2,cu*r**2/a)
            endmax=max(root(a,Q(0),budget/cr),root(a,budget/(2*cu),Q(0)))
            assert abs(endmax-float(r))<1e-9*max(1,float(r))
            count_threshold += 1

    # Exact examples with a=1, cu=2, cr=1.
    a,cu,cr=Q(1),Q(2),Q(1)
    assert a*cu/cr==2 and a*cu**3/cr**2==8
    assert f(Q(1,2),a,Q(0),Q(1,8))==0
    assert f(Q(1,4),a,Q(1,32),Q(0))==0
    assert f(Q(2),a,Q(1),Q(4))==0
    assert f(Q(4),a,Q(8),Q(0))==0
    print('PASS exact determinant identities:',count_det)
    print('PASS exact fixed-budget anchor identities:',count_anchor)
    print('PASS sampled monotonicity and endpoint checks:',count_order)
    print('PASS critical/target-budget checks:',count_threshold)
    print('PASS illustrative rational cases')
    print('Finite tests support, but do not establish, the proof for all positive real parameters.')


if __name__=='__main__':
    main()
