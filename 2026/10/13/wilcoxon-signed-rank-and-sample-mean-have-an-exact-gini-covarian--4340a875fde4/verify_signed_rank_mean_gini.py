#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import sqrt, pi

def rank_w(xs):
    order=sorted(range(len(xs)), key=lambda i: abs(xs[i]))
    ranks=[0]*len(xs)
    for r,i in enumerate(order, start=1):
        ranks[i]=r
    return sum(ranks[i] for i,x in enumerate(xs) if x>0)

def walsh_w(xs):
    n=len(xs)
    return sum(1 for i in range(n) for j in range(i,n) if xs[i]+xs[j]>0)

def exact_signed_rank_moments(n):
    vals=[]
    for signs in product((-1,1), repeat=n):
        vals.append(sum((i+1) for i,s in enumerate(signs) if s>0))
    N=Fraction(len(vals),1)
    mean=sum(Fraction(v,1) for v in vals)/N
    var=sum((Fraction(v,1)-mean)**2 for v in vals)/N
    return mean,var

def theorem_cov_uniform(n):
    mu1=Fraction(1,2)
    delta=Fraction(2,3)
    return mu1/Fraction(2,1) + Fraction(n-1,4)*delta

def order_cov_uniform(n):
    # E A_(r)=r/(n+1) for |X|~Unif[0,1].
    return sum(Fraction(r*r, n+1) for r in range(1,n+1))/Fraction(2*n,1)

def rho_general(n, mu1, delta, sigma):
    return sqrt(6)*(2*mu1+(n-1)*delta)/(2*sigma*sqrt((n+1)*(2*n+1)))

def run():
    walsh_checks=0
    for n in range(1,13):
        mags=[2**i for i in range(n)]
        for signs in product((-1,1), repeat=n):
            xs=[signs[i]*mags[i] for i in range(n)]
            assert rank_w(xs)==walsh_w(xs)
            walsh_checks += 1

    moment_checks=0
    for n in range(1,15):
        m,v=exact_signed_rank_moments(n)
        assert m==Fraction(n*(n+1),4)
        assert v==Fraction(n*(n+1)*(2*n+1),24)
        moment_checks += 2

    uniform_cov_checks=0
    uniform_rho_checks=0
    normal_rho_checks=0
    for n in range(1,201):
        assert theorem_cov_uniform(n)==order_cov_uniform(n)
        uniform_cov_checks += 1
        rho_u=rho_general(n,0.5,2/3,1/sqrt(3))
        target_u=sqrt((2*n+1)/(2*n+2))
        assert abs(rho_u-target_u)<1e-14
        uniform_rho_checks += 1

        rho_n=rho_general(n,sqrt(2/pi),2/sqrt(pi),1.0)
        target_n=sqrt(6/pi)*(n-1+sqrt(2))/sqrt((n+1)*(2*n+1))
        assert abs(rho_n-target_n)<1e-14
        normal_rho_checks += 1

    assert abs(sqrt(3/pi)**2-3/pi)<1e-15

    print(
        "VERIFY_OK "
        f"walsh_identity_checks={walsh_checks} "
        f"exact_null_moment_checks={moment_checks} "
        f"uniform_covariance_checks={uniform_cov_checks} "
        f"uniform_correlation_checks={uniform_rho_checks} "
        f"normal_correlation_checks={normal_rho_checks}"
    )

if __name__=="__main__":
    run()
