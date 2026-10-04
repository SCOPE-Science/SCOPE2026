#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import random

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def formula(ps,n):
    s2=sum(p*p for p in ps)
    A=sum(p*(1-p)**(n-2) for p in ps)
    B=sum(p*p*(1-p)**(n-2) for p in ps)
    cov=2*s2*A-(1+s2)*B
    lower=s2*(1-s2)*A
    return s2,A,B,cov,lower

def enumerate_cov(ps,n):
    m=len(ps)
    EK=Fraction(0)
    EG=Fraction(0)
    EKG=Fraction(0)
    denom=Fraction(n*(n-1),2)

    for xs in product(range(m), repeat=n):
        prob=Fraction(1)
        for x in xs:
            prob*=ps[x]
        K=len(set(xs))
        collisions=0
        for i in range(n):
            for j in range(i+1,n):
                collisions += (xs[i]==xs[j])
        G=Fraction(1)-Fraction(collisions,denom)
        EK += prob*K
        EG += prob*G
        EKG += prob*K*G

    return EKG-EK*EG

def run():
    enumeration_checks=0
    formula_checks=0
    lower_bound_checks=0
    equality_checks=0
    strict_checks=0

    profiles=[
        [Fraction(1,2),Fraction(1,2)],
        [Fraction(1,2),Fraction(1,3),Fraction(1,6)],
        [Fraction(3,5),Fraction(1,5),Fraction(1,5)],
        [Fraction(1,4)]*4,
    ]

    for ps in profiles:
        max_n=6 if len(ps)<=3 else 5
        for n in range(2,max_n+1):
            exact=enumerate_cov(ps,n)
            s2,A,B,cov,lower=formula(ps,n)
            assert exact==cov
            assert B<=s2*A
            assert cov>=lower>0
            enumeration_checks+=1
            formula_checks+=2
            lower_bound_checks+=2

            uniform=len(set(ps))==1
            if n==2 or uniform:
                assert cov==lower
                equality_checks+=1
            else:
                assert cov>lower
                strict_checks+=1

    rng=random.Random(20261003)
    for _ in range(12000):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,40) for __ in range(m)])
        n=rng.randrange(2,25)
        s2,A,B,cov,lower=formula(ps,n)
        assert Fraction(0)<s2<Fraction(1)
        assert A>0
        assert B<=s2*A
        assert cov>=lower>0
        formula_checks+=2
        lower_bound_checks+=2
        uniform=len(set(ps))==1
        if n==2 or uniform:
            assert cov==lower
            equality_checks+=1
        else:
            assert cov>lower
            strict_checks+=1

    # Uniform closed form.
    for m in range(2,30):
        ps=[Fraction(1,m)]*m
        for n in range(2,20):
            _,_,_,cov,_=formula(ps,n)
            expected=Fraction((m-1)**(n-1),m**n)
            assert cov==expected
            equality_checks+=1

    print(
        "VERIFY_OK "
        f"enumeration_checks={enumeration_checks} "
        f"formula_checks={formula_checks} "
        f"lower_bound_checks={lower_bound_checks} "
        f"equality_checks={equality_checks} "
        f"strict_checks={strict_checks}"
    )

if __name__=="__main__":
    run()
