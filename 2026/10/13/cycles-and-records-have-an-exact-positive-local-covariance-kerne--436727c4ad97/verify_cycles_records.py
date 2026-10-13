#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction
from math import factorial, comb

def cycles(p):
    n=len(p)
    seen=[False]*n
    c=0
    for i in range(n):
        if not seen[i]:
            c+=1
            x=i
            while not seen[x]:
                seen[x]=True
                x=p[x]-1
    return c

def records(p):
    out=[]
    m=0
    for x in p:
        if x>m:
            out.append(1)
            m=x
        else:
            out.append(0)
    return out

def harmonic(n,power=1):
    return sum(Fraction(1,k**power) for k in range(1,n+1))

def run():
    perms_checked=0
    probability_checks=0
    local_covariance_checks=0
    positivity_checks=0
    total_covariance_checks=0
    variance_checks=0

    for n in range(2,10):
        total=factorial(n)
        sum_c=0
        sum_c2=0
        sum_r=[0]*n
        sum_cr=[0]*n
        sum_R=0
        sum_R2=0
        sum_cR=0

        for p in permutations(range(1,n+1)):
            c=cycles(p)
            r=records(p)
            R=sum(r)
            perms_checked+=1
            sum_c+=c
            sum_c2+=c*c
            sum_R+=R
            sum_R2+=R*R
            sum_cR+=c*R
            for j in range(n):
                sum_r[j]+=r[j]
                sum_cr[j]+=c*r[j]

        H=harmonic(n)
        H2=harmonic(n,2)
        ec=Fraction(sum_c,total)
        assert ec==H

        for j in range(1,n+1):
            pr=Fraction(sum_r[j-1],total)
            assert pr==Fraction(1,j)
            probability_checks+=1
            cov=Fraction(sum_cr[j-1],total)-ec*pr
            if j==1:
                target=Fraction(0)
            else:
                target=Fraction(j-1, n*j*comb(n-1,j-1))
            assert cov==target
            local_covariance_checks+=1
            if j>=2:
                assert cov>0
                positivity_checks+=1

        eR=Fraction(sum_R,total)
        assert eR==H
        cov_total=Fraction(sum_cR,total)-ec*eR
        target_total=sum(
            Fraction(j-1,n*j*comb(n-1,j-1))
            for j in range(2,n+1)
        )
        assert cov_total==target_total
        total_covariance_checks+=1

        vc=Fraction(sum_c2,total)-ec*ec
        vr=Fraction(sum_R2,total)-eR*eR
        target_var=H-H2
        assert vc==target_var
        assert vr==target_var
        variance_checks+=2

    print(
        "VERIFY_OK "
        f"permutations_checked={perms_checked} "
        f"probability_checks={probability_checks} "
        f"local_covariance_checks={local_covariance_checks} "
        f"positivity_checks={positivity_checks} "
        f"total_covariance_checks={total_covariance_checks} "
        f"variance_checks={variance_checks}"
    )

if __name__=="__main__":
    run()
