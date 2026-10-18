#!/usr/bin/env python3
"""Finite exact checks for a theorem on monotone windows and descents.

Reproducible with Python 3.9+. This is mathematical verification of finite
identities only; asymptotic statements require the accompanying proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def tallies(perm, r):
    n = len(perm)
    d = sum(perm[j] > perm[j+1] for j in range(n-1))
    up = sum(all(perm[j] < perm[j+1] for j in range(i,i+r-1))
             for i in range(n-r+1))
    down = sum(all(perm[j] > perm[j+1] for j in range(i,i+r-1))
               for i in range(n-r+1))
    return d,up,down


def check_finite_covariances():
    checked=0
    permutations_count=0
    for n in range(2,9):
        total=factorial(n)
        all_perms=list(permutations(range(n)))
        permutations_count += len(all_perms)
        for r in range(2,n+1):
            ds=ups=downs=dus=dds=0
            for p in all_perms:
                d,u,v=tallies(p,r)
                ds+=d;ups+=u;downs+=v;dus+=d*u;dds+=d*v
            nwin=n-r+1
            expect_D=Fraction(n-1,2)
            expect_W=Fraction(nwin,factorial(r))
            expected_cov=-Fraction(r-1,2*factorial(r))* (
                Fraction(nwin,1)-Fraction(2*(n-r),r+1))
            covplus=Fraction(dus,total)-expect_D*expect_W
            covminus=Fraction(dds,total)-expect_D*expect_W
            assert Fraction(ds,total)==expect_D,(n,r,'E D')
            assert Fraction(ups,total)==expect_W,(n,r,'E W+')
            assert Fraction(downs,total)==expect_W,(n,r,'E W-')
            assert covplus==expected_cov,(n,r,'positive covariance',covplus,expected_cov)
            assert covminus==-expected_cov,(n,r,'negative covariance',covminus,expected_cov)
            checked+=5
    return checked,permutations_count


def check_pair_probabilities():
    checked=0
    counted_perm_sets=0
    for r in range(2,6):
        for d in range(1,r):
            m=r+d
            c_pp=c_pm=0
            for p in permutations(range(m)):
                first_up=all(p[i]<p[i+1] for i in range(r-1))
                second_up=all(p[i]<p[i+1] for i in range(d,d+r-1))
                second_dn=all(p[i]>p[i+1] for i in range(d,d+r-1))
                if first_up and second_up:c_pp+=1
                if first_up and second_dn:c_pm+=1
            counted_perm_sets+=factorial(m)
            assert Fraction(c_pp,factorial(m))==Fraction(1,factorial(r+d)),(r,d,'++')
            if d<=r-2:
                assert c_pm==0,(r,d,'+-')
            else:
                assert Fraction(c_pm,factorial(m))==Fraction(
                    1,(2*r-1)*factorial(r-1)**2),(r,d,'+-')
            checked+=2
    return checked,counted_perm_sets


if __name__=='__main__':
    x,np=check_finite_covariances()
    y,npp=check_pair_probabilities()
    print('FINITE_MOMENT_ASSERTIONS',x)
    print('OVERLAP_PROBABILITY_ASSERTIONS',y)
    print('FULL_PERMUTATION_ORDERS_2_TO_8',np)
    print('OVERLAP_PERMUTATIONS_ENUMERATED',npp)
    print('VERIFY_OK')
