#!/usr/bin/env python3
"""Exact coalition inequalities and optional unrestricted LP for binary plurality game."""
from fractions import Fraction as F
from itertools import combinations


def coalition_worth(c, w):
    if c+w==0: return F(0)
    if c>w: return F(1)
    if c==w: return F(1,2)
    return F(0)


def certificate(a,b):
    assert a>=0 and b>=0 and a+b>=1
    if a==0: return F(0), None, F(0)
    if b==0: return F(a-1,a), F(1,a), None
    if a<b:
        return F(a,a+1), F(1,a+1), -F(a,b*(a+1))
    if a==b:
        return F(2*a-1,2*(a+1)), F(3,2*(a+1)), -F(2*a-1,2*b*(a+1))
    if a<=2*b+1:
        return F(a-1,a+1), F(2,a+1), -F(a-1,b*(a+1))
    return F(a-b-1,a-b), F(1,a-b), -F(1,a-b)


def bounds(a,b):
    if a==0: return F(0)
    if b==0: return F(a-1,a)
    V=coalition_worth(a,b)
    one=F(a, a+1)-V/F(a+1)
    if a>=b+2:
        return max(one,F(a-b-1,a-b))
    return one


def exact_checks(limit):
    profiles=0; constraints=0
    for a in range(limit+1):
        for b in range(limit+1):
            if not a+b: continue
            eps,p,q=certificate(a,b)
            V=coalition_worth(a,b)
            assert a*(p or 0)+b*(q or 0)==V,(a,b,eps,p,q,V)
            assert eps==bounds(a,b),(a,b,eps,bounds(a,b))
            for c in range(a+1):
                for d in range(b+1):
                    if c+d==0 or (c==a and d==b):continue
                    e=coalition_worth(c,d)-c*(p or 0)-d*(q or 0)
                    assert e<=eps,(a,b,c,d,e,eps)
                    constraints+=1
            profiles+=1
    return profiles,constraints


def independent_lp(limit):
    try:
        from scipy.optimize import linprog
    except ImportError:
        return 0
    cases=0
    for a in range(limit+1):
        for b in range(limit+1):
            n=a+b
            if not (1<=n<=limit):continue
            V=float(coalition_worth(a,b))
            A=[]; rhs=[]
            for mask in range(1,(1<<n)-1):
                x=[int(bool(mask&(1<<i))) for i in range(n)]
                c=sum(x[:a]);d=sum(x[a:])
                A.append([-v for v in x]+[-1])
                rhs.append(-float(coalition_worth(c,d)))
            r=linprog([0]*n+[1],A_ub=A or None,b_ub=rhs or None,
                      A_eq=[[1]*n+[0]],b_eq=[V],bounds=[(None,None)]*n+[(0,None)],method='highs')
            assert r.success,(a,b,r.message)
            expected=float(certificate(a,b)[0])
            assert abs(r.x[-1]-expected)<1e-8,(a,b,r.x[-1],expected)
            cases+=1
    return cases

if __name__=='__main__':
    profiles,constraints=exact_checks(32)
    lp_cases=independent_lp(9)
    print('VERIFY_OK exact_parameter_profiles=%d exact_coalition_inequalities=%d unrestricted_full_LPs=%d'%(profiles,constraints,lp_cases))
