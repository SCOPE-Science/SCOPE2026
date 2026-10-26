#!/usr/bin/env python3
"""Reproduce exact renewal coefficients and conditional-survival diagnostics."""
from fractions import Fraction
from math import sqrt, pi


def series_test(eps, N=12):
    e=Fraction(eps)
    a=2-e
    p=4/(4+a*a)
    q=1-p
    lam=a*p
    assert q == p*a*a/4
    assert 1-p*e*e/4 == lam
    # h(z)=p*z+q*z*h(z)^2; h_{2j+1}=Catalan_j*p^(j+1)*q^j.
    h=[Fraction(0)]*(N+1)
    for j in range((N+1)//2):
        from math import comb
        cat=Fraction(comb(2*j,j),j+1)
        h[2*j+1]=cat*p**(j+1)*q**j
    # b(z)=1/(2-h(z)).
    b=[Fraction(0)]*(N+1)
    b[0]=Fraction(1,2)
    for n in range(1,N+1):
        b[n]=sum(h[k]*b[n-k] for k in range(1,n+1))/2
    f=[Fraction(0)]*(N+1)
    for n in range(1,N+1):
        f[n]=q*h[n-1]+p*(1-e)*b[n-1]
    # g(z)=1/(1-f(z)).
    g=[Fraction(0)]*(N+1)
    g[0]=Fraction(1)
    for n in range(1,N+1):
        g[n]=sum(f[k]*g[n-k] for k in range(1,n+1))
    # Exact finite-time state mass, retaining enough states for returns to zero.
    v=[Fraction(0)]*(N+2)
    v[0]=Fraction(1)
    survival=Fraction(1)
    for n in range(N+1):
        assert v[0] == g[n], ('renewal comparison',eps,n)
        if n==N: break
        surv_next=survival-p*e*v[0]
        nxt=[Fraction(0)]*(N+2)
        for j in range(N+1):
            nxt[j]+=p*v[j+1]
            if j>=1: nxt[j]+=q*v[j-1]
            nxt[j]+=p*(1-e)*v[0]/(2**(j+1))
        v=nxt
        survival=surv_next
    # Check the limiting QSD eigenrelation algebraically at initial cell.
    u0=e/4
    assert lam == 1-p*e*u0
    return N+1


def asymptotic_test(eps, nmax=800):
    e=float(eps)
    a=2-e
    p=4/(4+a*a)
    q=1-p
    lam=p*a
    C=4*sqrt(2/pi)*(1-e)/(e*a)
    v=[0.0]*(nmax+4)
    v[0]=1.0
    survival=1.0
    for n in range(1,nmax+1):
        old0=v[0]
        w=[0.0]*(nmax+4)
        for j in range(nmax+1):
            w[j]=p*v[j+1]+(q*v[j-1] if j else 0.0)
        t=p*(1-e)*old0/2
        for j in range(min(nmax+1,160)):
            w[j]+=t
            t/=2
        v=w
        survival-=p*e*old0
        # Accumulated subtraction can lose all relative precision at large n:
        # sum the positive mass instead (negligible tail beyond nmax states).
        survival=sum(v)
    ratio=survival/(C*(lam**nmax)/sqrt(nmax))
    predicted_u0=e/4
    conditional_u0=v[0]/survival
    assert abs(ratio-1)<.03,(eps,ratio)
    assert abs(conditional_u0-predicted_u0)<.01,(eps,conditional_u0,predicted_u0)
    return ratio,conditional_u0,predicted_u0

if __name__=='__main__':
    ntests=sum(series_test(e) for e in [Fraction(1,3),Fraction(1,2),Fraction(2,3)])
    print('EXACT_RENEWAL_AND_TRANSFER_COEFFICIENTS_PASS',ntests)
    for e in [.5,.8]:
        ratio,u,u0=asymptotic_test(e)
        print('CRITICAL_ASYMPTOTIC_DIAGNOSTIC_PASS',e,round(ratio,9),round(u,9),round(u0,9))
    print('CHECKS_PASS')
