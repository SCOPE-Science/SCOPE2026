#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import random
import math

def phi(n,u):
    return (1-u)**(n-1)-u**(n-1)

def closed_cov(n,a,b,c,t):
    return (
        -a*(1-a)*phi(n,a)*t*t
        + a*c*(phi(n,c)-phi(n,a))*t*(1-t)
        + c*(1-c)*phi(n,c)*(1-t)*(1-t)
    )

def direct_cov(n,a,b,c,t):
    xs=[Fraction(0),t,Fraction(1)]
    ps=[a,b,c]
    eb=Fraction(0); er=Fraction(0); ebr=Fraction(0)
    for idxs in product(range(3),repeat=n):
        w=Fraction(1)
        vals=[]
        for j in idxs:
            w*=ps[j]; vals.append(xs[j])
        bar=sum(vals,Fraction(0))/n
        rg=max(vals)-min(vals)
        eb+=w*bar; er+=w*rg; ebr+=w*bar*rg
    return ebr-eb*er

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def run():
    rng=random.Random(20261002)
    enumeration_checks=0
    sign_checks=0
    reflection_checks=0
    root_checks=0
    identity_checks=0

    # Exhaustive sample enumeration at bounded n.
    for _ in range(3500):
        n=rng.randrange(2,7)
        a,b,c=normalize([rng.randrange(1,15) for __ in range(3)])
        t=Fraction(rng.randrange(1,40),40)
        if not (0<t<1):
            continue
        assert direct_cov(n,a,b,c,t)==closed_cov(n,a,b,c,t)
        enumeration_checks+=1

    for _ in range(40000):
        n=rng.randrange(2,15)
        a,b,c=normalize([rng.randrange(1,40) for __ in range(3)])
        t=Fraction(rng.randrange(1,100),100)
        C=closed_cov(n,a,b,c,t)

        # Reflection.
        assert C==-closed_cov(n,c,b,a,1-t)
        reflection_checks+=1

        # Four coefficient identities, assembled algebraically.
        m11=-a*(1-a)*phi(n,a)
        m22=c*(1-c)*phi(n,c)
        m21=-a*c*phi(n,a)
        m12=a*c*phi(n,c)
        assembled=t*t*m11+t*(1-t)*(m12+m21)+(1-t)*(1-t)*m22
        assert assembled==C
        identity_checks+=1

        if a>=Fraction(1,2):
            assert C>0
            sign_checks+=1
        elif c>=Fraction(1,2):
            assert C<0
            sign_checks+=1
        else:
            alpha=a*(1-a)*phi(n,a)
            beta=c*(1-c)*phi(n,c)
            delta=a*c*(phi(n,c)-phi(n,a))
            assert alpha>0 and beta>0
            # Product of the two roots is strictly negative.
            assert -beta/alpha<0
            disc=float(delta*delta+4*alpha*beta)
            r=(float(delta)+math.sqrt(disc))/(2*float(alpha))
            assert r>0
            ts=r/(1+r)
            tf=float(t)
            if abs(tf-ts)>1e-10:
                if tf<ts:
                    assert C>0
                else:
                    assert C<0
                sign_checks+=1
            root_checks+=1

    print(
        "VERIFY_OK "
        f"enumeration_checks={enumeration_checks} "
        f"identity_checks={identity_checks} "
        f"sign_checks={sign_checks} "
        f"reflection_checks={reflection_checks} "
        f"root_checks={root_checks}"
    )

if __name__=="__main__":
    run()
