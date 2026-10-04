#!/usr/bin/env python3
from fractions import Fraction

def eq(n):
    # Mean of sample variance for normalized shape with endpoints 0 and 1.
    esum2 = Fraction(n+1,3)
    mean_sum = Fraction(n,2)
    var_sum = Fraction(n-2,12)
    esumsq = mean_sum*mean_sum + var_sum
    return (esum2 - esumsq/Fraction(n,1))/Fraction(n-1,1)

def c_formula(n):
    return Fraction((n+1)*(n+2),12*n*(n-1))

def r_moment(n,t):
    # Integer t >= 0 for exact replay.
    return Fraction(n*(n-1),(n+t-1)*(n+t))

def cov_closed(n,q):
    return Fraction(
        q*(2*n*n + 2*n*q + 2*n + q - 1),
        6*(n+q-1)*(n+q)*(n+q+1)*(n+q+2)
    )

def run():
    normalized_mean_checks=0
    range_moment_checks=0
    covariance_identity_checks=0
    positivity_checks=0
    q1_checks=0

    for n in range(2,401):
        c=eq(n)
        assert c==c_formula(n)
        normalized_mean_checks+=1

        for t in range(0,17):
            # Compare the closed beta moment to an independent beta-function
            # product representation.
            prod=Fraction(1,1)
            for j in range(t):
                prod *= Fraction(n-1+j,n+1+j)
            assert r_moment(n,t)==prod
            range_moment_checks+=1

        for q in range(1,21):
            raw=c*(r_moment(n,q+2)-r_moment(n,q)*r_moment(n,2))
            closed=cov_closed(n,q)
            assert raw==closed
            assert closed>0
            covariance_identity_checks+=1
            positivity_checks+=1

        assert cov_closed(n,1)==Fraction(1,3*(n+1)*(n+3))
        q1_checks+=1

    print(
        "VERIFY_OK "
        f"normalized_mean_checks={normalized_mean_checks} "
        f"range_moment_checks={range_moment_checks} "
        f"covariance_identity_checks={covariance_identity_checks} "
        f"positivity_checks={positivity_checks} "
        f"q1_checks={q1_checks}"
    )

if __name__=="__main__":
    run()
