#!/usr/bin/env python3
from fractions import Fraction
import random

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def profile(ps,n):
    P=[Fraction(0)]
    for p in ps:
        P.append(P[-1]+p)
    w=[P[i+1]**n-P[i]**n for i in range(len(ps))]
    score=[w[i]/ps[i] for i in range(len(ps))]
    return P,w,score

def mean_var(xs,ps):
    mu=sum(p*x for p,x in zip(ps,xs))
    var=sum(p*(x-mu)**2 for p,x in zip(ps,xs))
    return mu,var

def max_gap(xs,ps,n):
    P,w,score=profile(ps,n)
    em=sum(x*wi for x,wi in zip(xs,w))
    mu,var=mean_var(xs,ps)
    return em-mu,var

def lower_cut_sq(ps,n,j):
    P,_,_=profile(ps,n)
    q=P[j]
    num=q-q**n
    den=q*(1-q)
    return num*num,den

def upper_sq(ps,n):
    _,w,_=profile(ps,n)
    return sum(wi*wi/p for wi,p in zip(w,ps))-1

def run():
    rng=random.Random(20261002)
    identity_checks=0
    lower_checks=0
    upper_checks=0
    upper_equality_checks=0
    twopoint_checks=0
    boundary_checks=0
    decomposition_checks=0

    for _ in range(16000):
        m=rng.randrange(2,9)
        n=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,20) for __ in range(m)])
        gaps=[Fraction(rng.randrange(1,20),rng.randrange(1,8)) for __ in range(m-1)]
        xs=[Fraction(0)]
        for d in gaps:
            xs.append(xs[-1]+d)

        P,w,s=profile(ps,n)
        assert sum(w,Fraction(0))==1
        assert all(s[i]<s[i+1] for i in range(m-1))
        identity_checks += 2

        gap,var=max_gap(xs,ps,n)
        assert var>0 and gap>0
        # direct score covariance identity
        mu,_=mean_var(xs,ps)
        cov=sum(ps[i]*(xs[i]-mu)*(s[i]-1) for i in range(m))
        assert gap==cov
        identity_checks += 1

        # threshold decomposition of centered support
        y=[x-mu for x in xs]
        rec=[Fraction(0) for __ in range(m)]
        for j,d in enumerate(gaps, start=1):
            q=P[j]
            for i in range(m):
                v=(Fraction(1) if i>=j else Fraction(0))-(1-q)
                rec[i]+=d*v
        assert rec==y
        decomposition_checks += 1

        # Lower: gap^2 >= L_j^2 * var for every cut? This is not true for every
        # cut individually; only for the minimum cut. Check against minimum by
        # rational comparison without roots.
        cuts=[lower_cut_sq(ps,n,j) for j in range(1,m)]
        # choose j minimizing num/sqrt(den): compare squared ratios
        best=min(range(len(cuts)), key=lambda k: cuts[k][0]/cuts[k][1])
        num2,den=cuts[best]
        assert gap*gap*den >= num2*var
        if m>=3:
            assert gap*gap*den > num2*var
        lower_checks += 1

        usq=upper_sq(ps,n)
        assert gap*gap <= usq*var
        upper_checks += 1

        # score-affine upper equality
        xe=[Fraction(3,7)+Fraction(5,4)*si for si in s]
        ge,ve=max_gap(xe,ps,n)
        assert ge*ge==usq*ve
        upper_equality_checks += 1

    # two-point exact equality of both endpoints
    for n in range(2,10):
        for a in range(1,20):
            p=Fraction(a,20)
            ps=[p,1-p]
            xs=[Fraction(-7,3),Fraction(11,5)]
            g,v=max_gap(xs,ps,n)
            num2,den=lower_cut_sq(ps,n,1)
            assert g*g*den==num2*v
            assert g*g==upper_sq(ps,n)*v
            twopoint_checks += 1

    # boundary approach for random profiles: shrink all but a minimizing gap.
    for _ in range(4000):
        m=rng.randrange(3,8)
        n=rng.randrange(2,8)
        ps=normalize([rng.randrange(1,15) for __ in range(m)])
        cuts=[lower_cut_sq(ps,n,j) for j in range(1,m)]
        best=min(range(len(cuts)), key=lambda k: cuts[k][0]/cuts[k][1])
        jstar=best+1
        target_num2,target_den=cuts[best]
        prev=None
        for power in (2,4,6):
            eps=Fraction(1,10**power)
            gaps=[eps]*(m-1)
            gaps[jstar-1]=Fraction(1)
            xs=[Fraction(0)]
            for d in gaps:
                xs.append(xs[-1]+d)
            g,v=max_gap(xs,ps,n)
            ratio=float(g*g/v)
            target=float(target_num2/target_den)
            err=abs(ratio-target)
            if prev is not None:
                assert err < prev + 1e-18
            prev=err
            boundary_checks += 1

    print(
        "VERIFY_OK "
        f"identity_checks={identity_checks} "
        f"decomposition_checks={decomposition_checks} "
        f"lower_checks={lower_checks} "
        f"upper_checks={upper_checks} "
        f"upper_equality_checks={upper_equality_checks} "
        f"two_point_checks={twopoint_checks} "
        f"boundary_checks={boundary_checks}"
    )

if __name__=="__main__":
    run()
