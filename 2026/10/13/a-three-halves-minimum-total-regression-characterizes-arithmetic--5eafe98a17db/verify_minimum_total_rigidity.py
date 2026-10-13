#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def mean(vals):
    return sum(vals, Fraction(0))/len(vals)

def moments(rows, idx):
    x=[Fraction(r[idx]) for r in rows]
    y=[Fraction(r[2]) for r in rows]
    ex=mean(x); ey=mean(y)
    vx=mean([(u-ex)**2 for u in x])
    vy=mean([(v-ey)**2 for v in y])
    cov=mean([(u-ex)*(v-ey) for u,v in zip(x,y)])
    return vx,vy,cov

def is_ap(z):
    d=z[1]-z[0]
    return all(z[i+1]-z[i]==d for i in range(len(z)-1))

def run():
    populations=0
    pair_rows=0
    regression_checks=0
    rigidity_checks=0
    max_checks=0
    covariance_checks=0
    correlation_checks=0

    universe=list(range(10))
    for N in range(3,10):
        for zt in combinations(universe,N):
            z=tuple(Fraction(v) for v in zt)
            populations+=1
            rows=[]
            for i,j in combinations(range(N),2):
                rows.append((z[i],z[j],z[i]+z[j]))
                pair_rows+=1

            residuals=[]
            for k in range(N-1):
                vals=[s for m,x,s in rows if m==z[k]]
                got=mean(vals)
                target=z[k]+mean(z[k+1:])
                assert got==target
                residuals.append(got-Fraction(3,2)*z[k])
                regression_checks+=1

            property_holds=all(r==residuals[0] for r in residuals)
            ap=is_ap(z)
            assert property_holds==ap
            rigidity_checks+=1

            if ap:
                max_res=[]
                for k in range(1,N):
                    vals=[s for m,x,s in rows if x==z[k]]
                    got=mean(vals)
                    target=z[k]+mean(z[:k])
                    assert got==target
                    max_res.append(got-Fraction(3,2)*z[k])
                    max_checks+=1
                assert all(r==max_res[0] for r in max_res)

                vm,vs,cov=moments(rows,0)
                assert cov==Fraction(3,2)*vm
                covariance_checks+=1
                assert cov*cov*4==3*vm*vs
                correlation_checks+=1

                vx,vs2,covx=moments(rows,1)
                assert vs2==vs
                assert covx*covx*4==3*vx*vs2
                correlation_checks+=1

    print(
        "VERIFY_OK "
        f"populations={populations} "
        f"pair_rows={pair_rows} "
        f"regression_checks={regression_checks} "
        f"rigidity_checks={rigidity_checks} "
        f"max_checks={max_checks} "
        f"covariance_checks={covariance_checks} "
        f"correlation_checks={correlation_checks}"
    )

if __name__=="__main__":
    run()
