#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import math

def trees(n):
    ranges=[range(1,j) for j in range(2,n+1)]
    yield from product(*ranges)

def harmonic_table(N):
    H=[Fraction(0)]*(N+1)
    for k in range(1,N+1):
        H[k]=H[k-1]+Fraction(1,k)
    return H

def covariance_formula(n,v,H):
    return Fraction(n-v,2*(n-1)) - Fraction(v-1,n-1)*(H[n-2]-H[v-2])

def run():
    H=harmonic_table(5000)
    trees_checked=0
    leaf_mean_checks=0
    local_cov_checks=0
    aggregate_cov_checks=0
    convexity_checks=0
    threshold_checks=0
    asymptotic_checks=0

    for n in range(2,10):
        N=math.factorial(n-1)
        sumL=0
        sumD=[0]*(n+1)
        sumDL=[0]*(n+1)
        sumA=[[0]*(n+1) for _ in range(n+1)]
        sumAL=[[0]*(n+1) for _ in range(n+1)]

        count=0
        for parents in trees(n):
            out=[0]*(n+1)
            for j,p in enumerate(parents,start=2):
                out[p]+=1
            L=sum(1 for v in range(1,n+1) if out[v]==0)
            sumL+=L

            for v in range(2,n+1):
                d=out[v]
                sumD[v]+=d
                sumDL[v]+=d*L

            for j,p in enumerate(parents,start=2):
                if p>=2:
                    sumA[p][j]+=1
                    sumAL[p][j]+=L
            count+=1

        assert count==N
        trees_checked+=count
        EL=Fraction(sumL,N)
        assert EL==Fraction(n,2)
        leaf_mean_checks+=1

        for v in range(2,n+1):
            ED=Fraction(sumD[v],N)
            EDL=Fraction(sumDL[v],N)
            cov=EDL-ED*EL
            target=covariance_formula(n,v,H)
            assert cov==target
            aggregate_cov_checks+=1

            for j in range(v+1,n+1):
                EA=Fraction(sumA[v][j],N)
                EAL=Fraction(sumAL[v][j],N)
                local=EAL-EA*EL
                target_local=Fraction(j-2*v,2*(n-1)*(j-2))
                assert EA==Fraction(1,j-1)
                assert local==target_local
                local_cov_checks+=1

    # Exact finite sign and discrete convexity through n=500.
    for n in range(7,501):
        vals=[covariance_formula(n,v,H) for v in range(2,n+1)]
        assert vals[0]>0
        assert vals[-2]<0
        assert vals[-1]==0

        # Second difference is strictly positive on the interior.
        for i in range(len(vals)-2):
            assert vals[i+2]-2*vals[i+1]+vals[i] > 0
            convexity_checks+=1

        first_nonpos=next(i for i,x in enumerate(vals[:-1]) if x<=0)
        assert all(x>0 for x in vals[:first_nonpos])
        assert all(x<0 for x in vals[first_nonpos+1:-1])
        threshold_checks+=1

    rho=0.28466813704083846

    # Scaled profile and threshold sanity checks at growing sizes.
    for n in (100,300,1000,3000,5000):
        vals=[covariance_formula(n,v,H) for v in range(2,n)]
        tau=2+next(i for i,x in enumerate(vals) if x<=0)
        ratio=tau/n
        assert abs(ratio-rho)<0.04
        asymptotic_checks+=1

        for x in (0.15,0.25,0.35,0.60):
            v=max(2,min(n-1,round(x*n)))
            exact=float(covariance_formula(n,v,H))
            limit=(1-x)/2+x*math.log(x)
            assert abs(exact-limit)<0.05
            asymptotic_checks+=1

    # The largest sample is closer to rho than the smallest.
    def tau_ratio(n):
        vals=[covariance_formula(n,v,H) for v in range(2,n)]
        tau=2+next(i for i,x in enumerate(vals) if x<=0)
        return tau/n
    assert abs(tau_ratio(5000)-rho)<abs(tau_ratio(100)-rho)
    asymptotic_checks+=1

    print(
        "VERIFY_OK "
        f"trees_checked={trees_checked} "
        f"leaf_mean_checks={leaf_mean_checks} "
        f"local_cov_checks={local_cov_checks} "
        f"aggregate_cov_checks={aggregate_cov_checks} "
        f"convexity_checks={convexity_checks} "
        f"threshold_checks={threshold_checks} "
        f"asymptotic_checks={asymptotic_checks}"
    )

if __name__=="__main__":
    run()
