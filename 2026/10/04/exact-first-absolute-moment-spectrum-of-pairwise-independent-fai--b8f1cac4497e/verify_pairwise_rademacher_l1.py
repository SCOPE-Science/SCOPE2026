#!/usr/bin/env python3
from fractions import Fraction

def lattice(n):
    return list(range(n % 2, n + 1, 2))

def bracket(n):
    vals = lattice(n)
    a = max(r for r in vals if r*r <= n)
    b = a + 2
    assert b <= n
    return a,b

def bounds(n):
    lo = Fraction(1) if n % 2 == 0 else Fraction(2*n,n+1)
    a,b = bracket(n)
    hi = Fraction(n+a*b,a+b)
    return lo,hi,a,b

def lower_R_law(n):
    if n % 2 == 0:
        return {0:Fraction(n-1,n), n:Fraction(1,n)}
    return {1:Fraction(n,n+1), n:Fraction(1,n+1)}

def upper_R_law(n):
    _,_,a,b=bounds(n)
    den=b*b-a*a
    pb=Fraction(n-a*a,den)
    pa=1-pb
    out={}
    if pa: out[a]=pa
    if pb: out[b]=pb
    return out

def E_abs(R):
    return sum(Fraction(r)*p for r,p in R.items())

def E_sq(R):
    return sum(Fraction(r*r)*p for r,p in R.items())

def count_law(n,R):
    S={}
    for r,p in R.items():
        if r==0:
            S[0]=S.get(0,Fraction(0))+p
        else:
            S[r]=S.get(r,Fraction(0))+p/2
            S[-r]=S.get(-r,Fraction(0))+p/2
    K={}
    for s,p in S.items():
        assert (n+s)%2==0
        k=(n+s)//2
        assert 0<=k<=n
        K[k]=K.get(k,Fraction(0))+p
    return K

def check_count(n,K):
    assert sum(K.values(),Fraction(0))==1
    e1=sum(Fraction(k)*p for k,p in K.items())
    e2=sum(Fraction(k*(k-1))*p for k,p in K.items())
    assert e1==Fraction(n,2)
    assert e2==Fraction(n*(n-1),4)

def pair_extrema(n):
    vals=lattice(n)
    cand=[]
    for i,a in enumerate(vals):
        for b in vals[i:]:
            if a==b:
                if a*a==n: cand.append(Fraction(a))
                continue
            if not (a*a<=n<=b*b): continue
            pb=Fraction(n-a*a,b*b-a*a)
            pa=1-pb
            if 0<=pa<=1 and 0<=pb<=1:
                cand.append(pa*a+pb*b)
    return min(cand),max(cand),len(cand)

def run():
    pointwise=0
    constructions=0
    for n in range(2,5001):
        lo,hi,a,b=bounds(n)
        for r in lattice(n):
            if n%2==0:
                assert Fraction(r)>=Fraction(r*r,n)
            else:
                assert Fraction(r)>=Fraction(r*r+n,n+1)
            assert Fraction(r)<=Fraction(r*r+a*b,a+b)
            pointwise+=2
        RL=lower_R_law(n); RU=upper_R_law(n)
        assert E_sq(RL)==n and E_sq(RU)==n
        assert E_abs(RL)==lo and E_abs(RU)==hi
        check_count(n,count_law(n,RL))
        check_count(n,count_law(n,RU))
        constructions+=2

    extreme_checks=0
    feasible_pairs=0
    for n in range(2,301):
        lo,hi,_,_=bounds(n)
        mn,mx,c=pair_extrema(n)
        assert mn==lo and mx==hi
        extreme_checks+=1
        feasible_pairs+=c

    print(
        "VERIFY_OK "
        f"pointwise_checks={pointwise} "
        f"construction_checks={constructions} "
        f"extreme_pair_checks={extreme_checks} "
        f"feasible_pair_laws={feasible_pairs}"
    )

if __name__=="__main__":
    run()
