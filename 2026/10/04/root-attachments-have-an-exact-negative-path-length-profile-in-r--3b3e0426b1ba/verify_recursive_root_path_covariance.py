#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import Counter

def H(m, power=1):
    return sum((Fraction(1, k**power) for k in range(1, m+1)), Fraction(0))

def trees(n):
    for choices in product(*[range(1, j) for j in range(2, n+1)]):
        parent=[0]*(n+1)
        depth=[0]*(n+1)
        for j,p in enumerate(choices,start=2):
            parent[j]=p
            depth[j]=depth[p]+1
        root_degree=sum(parent[j]==1 for j in range(2,n+1))
        total_path=sum(depth)
        yield parent, root_degree, total_path

def cdf(counter, total, t):
    return Fraction(sum(v for x,v in counter.items() if x<=t), total)

def run():
    trees_enumerated=0
    local_cov_checks=0
    conditional_mean_checks=0
    stochastic_cdf_checks=0
    global_cov_checks=0
    marginal_moment_checks=0
    telescoping_checks=0

    for n in range(2,10):
        rows=list(trees(n))
        N=len(rows)
        trees_enumerated += N

        ER=Fraction(sum(r for _,r,_ in rows),N)
        ET=Fraction(sum(t for _,_,t in rows),N)
        ER2=Fraction(sum(r*r for _,r,_ in rows),N)
        ERT=Fraction(sum(r*t for _,r,t in rows),N)

        assert ER==H(n-1)
        assert ER2-ER*ER==H(n-1)-H(n-1,2)
        assert ET==n*(H(n)-1)
        marginal_moment_checks += 3

        global_cov=ERT-ER*ET
        target_global=H(n)-1-n*(H(n,2)-1)
        assert global_cov==target_global
        if n>=3:
            assert global_cov<0
        global_cov_checks += 1

        for j in range(2,n+1):
            EA=Fraction(1,j-1)
            EAT=Fraction(sum((1 if par[j]==1 else 0)*t for par,_,t in rows),N)
            cov=EAT-EA*ET
            target=-Fraction(n,j*(j-1))*(H(j-1)-1)
            assert cov==target
            local_cov_checks += 1

            if j>=3:
                one=[t for par,_,t in rows if par[j]==1]
                zero=[t for par,_,t in rows if par[j]!=1]
                mean_one=Fraction(sum(one),len(one))
                mean_zero=Fraction(sum(zero),len(zero))
                gap=mean_zero-mean_one
                target_gap=Fraction(n*(j-1),j*(j-2))*(H(j-1)-1)
                assert gap==target_gap
                assert gap>0
                conditional_mean_checks += 1

                c1=Counter(one); c0=Counter(zero)
                strict=False
                for t in range(min(min(one),min(zero)), max(max(one),max(zero))+1):
                    # Smaller in stochastic order means the CDF is everywhere larger.
                    f1=cdf(c1,len(one),t)
                    f0=cdf(c0,len(zero),t)
                    assert f1>=f0
                    if f1>f0:
                        strict=True
                    stochastic_cdf_checks += 1
                assert strict

    for n in range(2,501):
        lhs=sum((H(j-1)-1)/Fraction(j*(j-1),1) for j in range(2,n+1))
        rhs=H(n,2)-1-(H(n)-1)/n
        assert lhs==rhs
        telescoping_checks += 1

    print(
        "VERIFY_OK "
        f"trees_enumerated={trees_enumerated} "
        f"local_cov_checks={local_cov_checks} "
        f"conditional_mean_checks={conditional_mean_checks} "
        f"stochastic_cdf_checks={stochastic_cdf_checks} "
        f"global_cov_checks={global_cov_checks} "
        f"marginal_moment_checks={marginal_moment_checks} "
        f"telescoping_checks={telescoping_checks}"
    )

if __name__=="__main__":
    run()
