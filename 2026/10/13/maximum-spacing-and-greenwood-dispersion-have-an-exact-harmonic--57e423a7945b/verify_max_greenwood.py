#!/usr/bin/env python3
from fractions import Fraction
from math import comb, sqrt, log, pi

def harmonic(m, p=1):
    return sum(Fraction(1, j**p) for j in range(1, m+1))

def poly_mul(a, b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def one_minus_kt_pow(k, r):
    return [Fraction(comb(r,j)) * ((-k)**j) for j in range(r+1)]

def integrate_poly(poly, upper):
    u=Fraction(upper)
    return sum(c*u**(j+1)/Fraction(j+1) for j,c in enumerate(poly))

def term_integral(m,k):
    # bracket = k t^2 + 2kt(1-kt)/m + 2(1-kt)^2/(m+1)
    b=[Fraction(0),Fraction(0),Fraction(k)]
    second=poly_mul([Fraction(0), Fraction(2*k,m)], [Fraction(1), Fraction(-k)])
    third=[Fraction(2,m+1)*x for x in poly_mul([Fraction(1),Fraction(-k)],[Fraction(1),Fraction(-k)])]
    L=max(len(b),len(second),len(third))
    bracket=[Fraction(0)]*L
    for q in (b,second,third):
        for i,x in enumerate(q):
            bracket[i]+=x
    poly=poly_mul(one_minus_kt_pow(k,m-1), bracket)
    return integrate_poly(poly, Fraction(1,k))

def tail_integral_moment(m, power):
    # integral representation for E[M^power]:
    # power * integral t^(power-1) P(M>t) dt
    out=Fraction(0)
    for k in range(1,m+1):
        base=one_minus_kt_pow(k,m-1)
        poly=[Fraction(0)]*(power-1)+base
        val=Fraction(power)*integrate_poly(poly,Fraction(1,k))
        out += ((-1)**(k+1))*comb(m,k)*val
    return out

def run():
    term_checks=0
    mixed_checks=0
    harmonic_checks=0
    marginal_checks=0
    covariance_checks=0
    positivity_checks=0
    correlation_checks=0

    for m in range(2,81):
        H=harmonic(m)
        H2=harmonic(m,2)

        # Each beta-integral formula is checked from a fresh polynomial expansion.
        direct_terms=[]
        for k in range(1,m+1):
            got=term_integral(m,k)
            target=Fraction(2,m*(m+2))*(Fraction(1,k)+Fraction(1,(m+1)*k*k))
            assert got==target
            direct_terms.append(got)
            term_checks+=1

        mixed=sum(((-1)**(k+1))*comb(m,k)*direct_terms[k-1] for k in range(1,m+1))
        mixed_closed=Fraction(2,m*(m+2))*(H+Fraction(H*H+H2,2*(m+1)))
        assert mixed==mixed_closed
        mixed_checks+=1

        s1=sum(((-1)**(k+1))*Fraction(comb(m,k),k) for k in range(1,m+1))
        s2=sum(((-1)**(k+1))*Fraction(comb(m,k),k*k) for k in range(1,m+1))
        assert s1==H
        assert s2==Fraction(H*H+H2,2)
        harmonic_checks+=2

        EM=tail_integral_moment(m,1)
        EM2=tail_integral_moment(m,2)
        assert EM==H/Fraction(m)
        assert EM2==Fraction(H*H+H2,m*(m+1))

        EG=Fraction(2,m+1)
        EG2=Fraction(4*(m+5),(m+1)*(m+2)*(m+3))
        varM=EM2-EM*EM
        varG=EG2-EG*EG
        assert varM==Fraction(m*H2-H*H,m*m*(m+1))
        assert varG==Fraction(4*(m-1),(m+1)**2*(m+2)*(m+3))
        marginal_checks+=4

        cov=mixed-EM*EG
        closed_cov=Fraction(H*H+H2-2*H,m*(m+1)*(m+2))
        assert cov==closed_cov
        covariance_checks+=1
        assert cov>0
        positivity_checks+=1

        # Exact square of the displayed correlation.
        lhs=cov*cov/(varM*varG)
        A=H*H+H2-2*H
        rhs=(A*A)*Fraction((m+1)*(m+3),4*(m+2)*(m-1)*(m*H2-H*H))
        assert lhs==rhs
        correlation_checks+=1

    asymptotic_checks=0
    for m in (1000,10000,100000):
        h=sum(1.0/j for j in range(1,m+1))
        h2=sum(1.0/(j*j) for j in range(1,m+1))
        A=h*h+h2-2*h
        cov=A/(m*(m+1)*(m+2))
        vm=(m*h2-h*h)/(m*m*(m+1))
        vg=4*(m-1)/((m+1)**2*(m+2)*(m+3))
        corr=cov/sqrt(vm*vg)
        scale=(sqrt(6)/(2*pi))*(log(m)**2)/sqrt(m)
        ratio=corr/scale
        assert 0.85 < ratio < 1.15
        asymptotic_checks+=1

    print(
        "VERIFY_OK "
        f"term_integrals={term_checks} "
        f"mixed_moments={mixed_checks} "
        f"harmonic_identities={harmonic_checks} "
        f"marginal_checks={marginal_checks} "
        f"covariance_checks={covariance_checks} "
        f"positivity_checks={positivity_checks} "
        f"correlation_checks={correlation_checks} "
        f"asymptotic_checks={asymptotic_checks}"
    )

if __name__=="__main__":
    run()
