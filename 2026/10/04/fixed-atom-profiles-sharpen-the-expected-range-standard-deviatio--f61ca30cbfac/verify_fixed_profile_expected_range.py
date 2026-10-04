#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, comb
import random

def K(n,u):
    return u**n + (1-u)**n

def profile(n,ps):
    P=Fraction(0)
    cs=[]
    zs=[]
    for p in ps:
        P0=P
        P+=p
        c=K(n,P)-K(n,P0)
        cs.append(c)
        zs.append(c/p)
    assert P==1
    return cs,zs

def expected_range(n,xs,ps):
    P=Fraction(0)
    emax=Fraction(0)
    emin=Fraction(0)
    for x,p in zip(xs,ps):
        P0=P
        P+=p
        emax += x*(P**n-P0**n)
        emin += x*((1-P0)**n-(1-P)**n)
    return emax-emin

def variance(xs,ps):
    mu=sum(p*x for x,p in zip(xs,ps))
    return sum(p*(x-mu)**2 for x,p in zip(xs,ps))

def global_B2(n):
    return n*n*(
        Fraction(2,2*n-1)
        - Fraction(2*factorial(n-1)**2, factorial(2*n-1))
    )

def derivative_coeffs(n):
    # K_n'(u)=n*u^(n-1)-n*(1-u)^(n-1)
    a=[Fraction(0) for _ in range(n)]
    for k in range(n):
        a[k] -= n*comb(n-1,k)*((-1)**k)
    a[n-1] += n
    return a

def poly_square(a):
    out=[Fraction(0)]*(2*len(a)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(a):
            out[i+j]+=x*y
    return out

def integral_poly(a,left,right):
    return sum(
        coef*(right**(k+1)-left**(k+1))/Fraction(k+1)
        for k,coef in enumerate(a)
    )

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def run():
    rng=random.Random(20261002)
    formula_checks=0
    monotonicity_checks=0
    bound_checks=0
    equality_checks=0
    deficit_checks=0
    global_norm_checks=0

    for _ in range(18000):
        n=rng.randrange(3,11)
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,31) for __ in range(m)])
        cs,zs=profile(n,ps)
        assert sum(cs,Fraction(0))==0
        assert sum(p*z for p,z in zip(ps,zs))==0

        assert all(zs[i]<zs[i+1] for i in range(m-1))
        monotonicity_checks+=m-1

        xs=[Fraction(0)]
        for __ in range(1,m):
            xs.append(xs[-1]+Fraction(rng.randrange(1,31),rng.randrange(1,11)))

        direct=expected_range(n,xs,ps)
        linear=sum(c*x for c,x in zip(cs,xs))
        assert direct==linear
        formula_checks+=1

        V=variance(xs,ps)
        C2=sum(c*c/p for c,p in zip(cs,ps))
        assert direct*direct<=C2*V
        bound_checks+=1

        xe=zs
        Re=expected_range(n,xe,ps)
        Ve=variance(xe,ps)
        assert Re*Re==C2*Ve
        assert Re==C2
        assert Ve==C2
        equality_checks+=3

        # Exact L2 cell deficit.
        f=derivative_coeffs(n)
        f2=poly_square(f)
        B2=global_B2(n)
        assert integral_poly(f2,Fraction(0),Fraction(1))==B2
        global_norm_checks+=1

        P=Fraction(0)
        residual=Fraction(0)
        for p,z in zip(ps,zs):
            P0=P
            P+=p
            cell=integral_poly(f2,P0,P)-p*z*z
            assert cell>0
            residual+=cell
            deficit_checks+=1
        assert B2-C2==residual
        assert C2<B2
        deficit_checks+=2

    print(
        "VERIFY_OK "
        f"formula_checks={formula_checks} "
        f"monotonicity_checks={monotonicity_checks} "
        f"bound_checks={bound_checks} "
        f"equality_checks={equality_checks} "
        f"deficit_checks={deficit_checks} "
        f"global_norm_checks={global_norm_checks}"
    )

if __name__=="__main__":
    run()
