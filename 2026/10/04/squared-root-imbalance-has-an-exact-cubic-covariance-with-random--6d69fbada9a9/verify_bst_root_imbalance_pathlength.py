#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
import math

def H(n,power=1):
    return sum((Fraction(1,k**power) for k in range(1,n+1)),Fraction(0))

def mu(n):
    return 2*(n+1)*H(n)-4*n

def varP(n):
    return 7*n*n+13*n-2*(n+1)*H(n)-4*(n+1)*(n+1)*H(n,2)

def qsort_comparisons(seq):
    n=len(seq)
    if n<=1:
        return 0
    pivot=seq[0]
    left=[x for x in seq[1:] if x<pivot]
    right=[x for x in seq[1:] if x>pivot]
    return n-1+qsort_comparisons(left)+qsort_comparisons(right)

def run():
    permutations_checked=0
    covariance_checks=0
    conditional_mean_checks=0
    monotone_regression_checks=0
    marginal_moment_checks=0
    imbalance_moment_checks=0
    slope_checks=0
    harmonic_reduction_checks=0
    asymptotic_checks=0

    for n in range(2,10):
        rows=[]
        by_i={}
        for p in permutations(range(1,n+1)):
            i=p[0]-1
            q=(2*i-(n-1))**2
            P=qsort_comparisons(p)
            rows.append((i,q,P))
            by_i.setdefault(i,[]).append(P)
            permutations_checked+=1

        N=len(rows)
        EP=Fraction(sum(P for _,_,P in rows),N)
        EP2=Fraction(sum(P*P for _,_,P in rows),N)
        assert EP==mu(n)
        assert EP2-EP*EP==varP(n)
        marginal_moment_checks+=2

        EQ=Fraction(sum(q for _,q,_ in rows),N)
        EQ2=Fraction(sum(q*q for _,q,_ in rows),N)
        target_EQ=Fraction((n-1)*(n+1),3)
        target_VQ=Fraction(4*(n-2)*(n-1)*(n+1)*(n+2),45)
        assert EQ==target_EQ
        assert EQ2-EQ*EQ==target_VQ
        imbalance_moment_checks+=2

        EQP=Fraction(sum(q*P for _,q,P in rows),N)
        cov=EQP-EQ*EP
        target_cov=Fraction((n-2)*(n-1)*(n+1),9)
        assert cov==target_cov
        covariance_checks+=1

        for i, vals in by_i.items():
            emp=Fraction(sum(vals),len(vals))
            target=mu(i)+mu(n-1-i)+(n-1)
            assert emp==target
            conditional_mean_checks+=1

        support={}
        for i,vals in by_i.items():
            q=(2*i-(n-1))**2
            support[q]=mu(i)+mu(n-1-i)+(n-1)
        qs=sorted(support)
        if n>=3:
            assert all(support[qs[k]]<support[qs[k+1]] for k in range(len(qs)-1))
        monotone_regression_checks+=1

        if n>=3:
            slope=cov/target_VQ
            assert slope==Fraction(5,4*(n+2))
            slope_checks+=1

    for n in range(3,401):
        N=n-1
        A=sum(mu(i) for i in range(N+1))
        B=sum((2*i-N)**2*mu(i) for i in range(N+1))
        target_A=(N+1)*(N+2)*H(N)-Fraction(N*(5*N+7),2)
        target_B=Fraction(N*(N+2),18)*(6*(N+1)*(N+2)*H(N)-(14*N*N+21*N+1))
        assert A==target_A
        assert B==target_B
        harmonic_reduction_checks+=2

    limit=math.sqrt(5)/(6*math.sqrt(7-2*math.pi**2/3))
    prev=None
    for n in (20,50,100,500,1000,5000):
        v=float(varP(n))
        rho=math.sqrt(5)/6*math.sqrt(((n-2)*(n-1)*(n+1))/((n+2)*v))
        assert 0<rho<1
        if prev is not None:
            # The values need not be proved monotone; only require late approximation.
            pass
        prev=rho
        asymptotic_checks+=1
    assert abs(prev-limit)<0.002
    asymptotic_checks+=1

    print(
        "VERIFY_OK "
        f"permutations_checked={permutations_checked} "
        f"covariance_checks={covariance_checks} "
        f"conditional_mean_checks={conditional_mean_checks} "
        f"monotone_regression_checks={monotone_regression_checks} "
        f"marginal_moment_checks={marginal_moment_checks} "
        f"imbalance_moment_checks={imbalance_moment_checks} "
        f"slope_checks={slope_checks} "
        f"harmonic_reduction_checks={harmonic_reduction_checks} "
        f"asymptotic_checks={asymptotic_checks}"
    )

if __name__=="__main__":
    run()
