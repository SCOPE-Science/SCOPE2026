#!/usr/bin/env python3
from fractions import Fraction
import random
import itertools

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def moments(ps,xs):
    mu=sum(p*x for p,x in zip(ps,xs))
    var=sum(p*(x-mu)**2 for p,x in zip(ps,xs))
    return mu,var

def f(u,N):
    return u**N+(1-u)**N

def range_scores(ps,N):
    P=Fraction(0)
    ss=[]
    for p in ps:
        Q=P+p
        ss.append((f(Q,N)-f(P,N))/p)
        P=Q
    return ss

def expected_range_gap(ps,xs,N):
    P=Fraction(0)
    out=Fraction(0)
    for j,p in enumerate(ps[:-1]):
        P+=p
        a=1-P**N-(1-P)**N
        out+=a*(xs[j+1]-xs[j])
    return out

def expected_range_extremes(ps,xs,N):
    P=Fraction(0)
    emax=Fraction(0)
    emin=Fraction(0)
    for p,x in zip(ps,xs):
        Q=P+p
        emax += x*(Q**N-P**N)
        emin += x*((1-P)**N-(1-Q)**N)
        P=Q
    return emax-emin

def lower2(ps,N):
    P=Fraction(0)
    vals=[]
    for p in ps[:-1]:
        P+=p
        a=1-P**N-(1-P)**N
        vals.append(a*a/(P*(1-P)))
    return min(vals)

def upper2(ps,N):
    ss=range_scores(ps,N)
    return sum(p*s*s for p,s in zip(ps,ss))

def direct_expected_range(ps,xs,N):
    out=Fraction(0)
    m=len(ps)
    for inds in itertools.product(range(m), repeat=N):
        prob=Fraction(1)
        vals=[]
        for i in inds:
            prob*=ps[i]
            vals.append(xs[i])
        out += prob*(max(vals)-min(vals))
    return out

def run():
    rng=random.Random(20261002)
    gap_checks=0
    extreme_checks=0
    covariance_checks=0
    lower_checks=0
    upper_checks=0
    score_order_checks=0
    upper_equality_checks=0
    lower_strict_checks=0
    boundary_checks=0
    direct_enum_checks=0
    binary_checks=0

    for _ in range(18000):
        m=rng.randrange(2,8)
        N=rng.randrange(3,9)
        ps=normalize([rng.randrange(1,31) for __ in range(m)])
        xs=[Fraction(0)]
        for __ in range(1,m):
            xs.append(xs[-1]+Fraction(rng.randrange(1,25),rng.randrange(1,9)))

        er1=expected_range_gap(ps,xs,N)
        er2=expected_range_extremes(ps,xs,N)
        assert er1==er2
        gap_checks+=1
        extreme_checks+=1

        ss=range_scores(ps,N)
        assert sum(p*s for p,s in zip(ps,ss))==0
        assert all(ss[i]<ss[i+1] for i in range(m-1))
        score_order_checks+=1

        cov=sum(p*x*s for p,x,s in zip(ps,xs,ss))
        assert cov==er1
        covariance_checks+=1

        _,V=moments(ps,xs)
        L2=lower2(ps,N)
        U2=upper2(ps,N)
        assert er1*er1 >= L2*V
        assert er1*er1 <= U2*V
        lower_checks+=1
        upper_checks+=1

        if m==2:
            assert er1*er1==L2*V==U2*V
            binary_checks+=1
        else:
            assert er1*er1>L2*V
            lower_strict_checks+=1

        # Exact upper equality at the range-score support.
        _,Vs=moments(ps,ss)
        ers=expected_range_gap(ps,ss,N)
        assert ers*ers==U2*Vs and ers>0
        upper_equality_checks+=1

        # Lower endpoint approach by one dominant minimizing gap.
        if m>=3:
            P=Fraction(0)
            vals=[]
            for j,p in enumerate(ps[:-1]):
                P+=p
                a=1-P**N-(1-P)**N
                vals.append((a*a/(P*(1-P)),j))
            _,jstar=min(vals)
            eps=Fraction(1,10**8)
            xb=[Fraction(0)]
            for j in range(m-1):
                xb.append(xb[-1]+(Fraction(1) if j==jstar else eps))
            erb=expected_range_gap(ps,xb,N)
            _,Vb=moments(ps,xb)
            # Relative squared excess over L^2 tends to zero.
            rel=(erb*erb-L2*Vb)/(L2*Vb)
            assert rel>0 and rel<Fraction(1,10000)
            boundary_checks+=1

    # Small direct enumeration against all iid tuples.
    for _ in range(600):
        m=rng.randrange(2,5)
        N=rng.randrange(3,6)
        ps=normalize([rng.randrange(1,12) for __ in range(m)])
        xs=[Fraction(0)]
        for __ in range(1,m):
            xs.append(xs[-1]+Fraction(rng.randrange(1,10),rng.randrange(1,5)))
        assert direct_expected_range(ps,xs,N)==expected_range_gap(ps,xs,N)
        direct_enum_checks+=1

    print(
        "VERIFY_OK "
        f"gap_checks={gap_checks} "
        f"extreme_checks={extreme_checks} "
        f"covariance_checks={covariance_checks} "
        f"lower_checks={lower_checks} "
        f"upper_checks={upper_checks} "
        f"score_order_checks={score_order_checks} "
        f"upper_equality_checks={upper_equality_checks} "
        f"lower_strict_checks={lower_strict_checks} "
        f"boundary_checks={boundary_checks} "
        f"direct_enum_checks={direct_enum_checks} "
        f"binary_checks={binary_checks}"
    )

if __name__=="__main__":
    run()
