#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
from itertools import product
import math

def stats_for_law(law, power):
    # law: dict tuple increments -> rational probability
    EMg=Fraction(0)
    ESg=Fraction(0)
    EDg=Fraction(0)
    ERg=Fraction(0)
    Eg=Fraction(0)
    EM=Fraction(0)
    ER=Fraction(0)
    for xs,p in law.items():
        s=0
        M=0
        m=0
        for x in xs:
            s+=x
            M=max(M,s)
            m=min(m,s)
        g=s**power
        EMg += p*M*g
        ESg += p*s*g
        EDg += p*(M-s)*g
        ERg += p*(M-m)*g
        Eg += p*g
        EM += p*M
        ER += p*(M-m)
    return EMg,ESg,EDg,ERg,Eg,EM,ER

def orbit(seed):
    r=tuple(reversed(seed))
    n=tuple(-x for x in seed)
    rn=tuple(-x for x in r)
    return sorted(set([tuple(seed),r,n,rn]))

def orbit_mixture(seeds,weights):
    out=defaultdict(Fraction)
    assert sum(weights,Fraction(0))==1
    for seed,w in zip(seeds,weights):
        o=orbit(seed)
        for x in o:
            out[x]+=w/Fraction(len(o))
    return dict(out)

def is_exchangeable_counterexample(law):
    # Check that one coordinate swap changes probability for at least one atom.
    for xs,p in law.items():
        if len(xs)>=3:
            ys=list(xs)
            ys[0],ys[1]=ys[1],ys[0]
            ys=tuple(ys)
            if law.get(ys,Fraction(0))!=p:
                return True
    return False

def iid_law(values,probs,n):
    out=defaultdict(Fraction)
    for inds in product(range(len(values)), repeat=n):
        p=Fraction(1)
        xs=[]
        for i in inds:
            xs.append(values[i])
            p*=probs[i]
        out[tuple(xs)]+=p
    return dict(out)

def simple_corr(n):
    # Exact joint count of (terminal, maximum).
    state={(0,0):1}
    for _ in range(n):
        nxt=defaultdict(int)
        for (s,m),c in state.items():
            for e in (-1,1):
                s2=s+e
                m2=max(m,s2)
                nxt[(s2,m2)]+=c
        state=nxt
    N=2**n
    ES=Fraction(0)
    EM=Fraction(0)
    ES2=Fraction(0)
    EM2=Fraction(0)
    EMS=Fraction(0)
    for (s,m),c in state.items():
        p=Fraction(c,N)
        ES+=p*s
        EM+=p*m
        ES2+=p*s*s
        EM2+=p*m*m
        EMS+=p*m*s
    cov=EMS-EM*ES
    varS=ES2-ES*ES
    varM=EM2-EM*EM
    return float(cov/math.sqrt(float(varS*varM))), cov, varS

def run():
    orbit_identity_checks=0
    nonexchangeable_checks=0
    iid_cov_checks=0
    asymptotic_checks=0

    laws=[
        orbit_mixture(
            [(2,-1,0,3), (1,4,-2,0)],
            [Fraction(2,5),Fraction(3,5)]
        ),
        orbit_mixture(
            [(3,0,-1,2,-4), (2,2,-3,0,1)],
            [Fraction(1,3),Fraction(2,3)]
        ),
        orbit_mixture(
            [(5,-2,1,-1,0,3), (2,-4,0,1,3,-1), (1,0,2,-3,4,-2)],
            [Fraction(1,6),Fraction(1,3),Fraction(1,2)]
        ),
    ]

    for law in laws:
        assert is_exchangeable_counterexample(law)
        nonexchangeable_checks+=1
        for power in (1,3,5):
            EMg,ESg,EDg,ERg,Eg,EM,ER=stats_for_law(law,power)
            assert Eg==0
            assert 2*EMg==ESg
            assert 2*EDg==-ESg
            assert ERg==0
            orbit_identity_checks+=4

    for n in range(1,13):
        law=iid_law([-1,1],[Fraction(1,2),Fraction(1,2)],n)
        EMg,ESg,_,_,Eg,EM,_=stats_for_law(law,1)
        varS=ESg  # S*g(S)=S^2 and ES=0
        assert Eg==0
        assert EMg==varS/2==Fraction(n,2)
        iid_cov_checks+=2

    for n in range(1,8):
        law=iid_law([-2,0,2],[Fraction(1,4),Fraction(1,2),Fraction(1,4)],n)
        EMg,ESg,_,_,Eg,EM,_=stats_for_law(law,1)
        # One-step variance is 2.
        assert Eg==0
        assert EMg==ESg/2==n
        iid_cov_checks+=2

    limit=1/(2*math.sqrt(1-2/math.pi))
    # Exact DP at increasing horizons; require approach from the observed side
    # and a small final error, not monotonicity at every single n.
    vals=[]
    for n in (20,50,100,200,400):
        corr,cov,varS=simple_corr(n)
        assert cov==varS/2==Fraction(n,2)
        vals.append(corr)
        asymptotic_checks+=2
    assert abs(vals[-1]-limit)<0.03
    assert abs(vals[-1]-limit)<abs(vals[0]-limit)
    asymptotic_checks+=2

    print(
        "VERIFY_OK "
        f"orbit_identity_checks={orbit_identity_checks} "
        f"nonexchangeable_checks={nonexchangeable_checks} "
        f"iid_cov_checks={iid_cov_checks} "
        f"asymptotic_checks={asymptotic_checks}"
    )

if __name__=="__main__":
    run()
