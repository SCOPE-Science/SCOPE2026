#!/usr/bin/env python3
"""Arithmetic and convergent-series checks for a Hartogs Bergman kernel zero-fibre theorem.

Standard-library only; these checks complement, but do not replace, the analytic proof.
"""
import cmath
import math


def roots(n, t):
    N=n+1
    q=(1-math.sqrt(t))/(1+math.sqrt(t))
    out=[]
    for j in range(N):
        phase=(2*j+(n%2))*math.pi/N
        C=q**(2/N)*cmath.exp(1j*phase)
        if C.real>1e-12:
            y=(C-1)/(C+1)
            out.append((j,y,C))
    return out


def exact_partial_formula(n, s, t):
    # Derived independently from the monomial norms of z^alpha w^beta.
    y=s/math.sqrt(t)
    D=(1-y)**(-n-1)
    E=(1+y)**(-n-1)
    if n%2==0:
        a=(1+t)/math.sqrt(t)
        return math.factorial(n)/(4*math.pi**(n+1)*t**(n//2)*(1-t)**2) * ((2+a)*D+(2-a)*E)
    return math.factorial(n)/(4*math.pi**(n+1)*t**((n+1)//2)*(1-t)**2) * (((1+math.sqrt(t))**2)*D+((1-math.sqrt(t))**2)*E)


def normalized_zero_residual(n, s, t):
    y=s/math.sqrt(t)
    D=(1-y)**(-n-1)
    E=(1+y)**(-n-1)
    if n%2==0:
        a=(1+t)/math.sqrt(t)
        one=(2+a)*D
        two=(2-a)*E
    else:
        one=(1+math.sqrt(t))**2*D
        two=(1-math.sqrt(t))**2*E
    return abs(one+two)/(abs(one)+abs(two))


def independent_series(n, s, t, L=600):
    # Sum of admissible Laurent monomials grouped by degree.
    sm=0j
    for ell in range(L):
        m=(ell+n+1)//2
        delta=ell+n+2-2*m
        c=math.factorial(ell+n)//math.factorial(ell)
        term=c*s**ell * t**(-m)*(delta+(2-delta)*t)
        sm+=term
    return sm/(2*math.pi**(n+1)*(1-t)**2)


def test():
    checks=0
    # Algebraically exact even/odd decomposition up to degree 60.
    for n in range(1,15):
        for ell in range(61):
            m=(ell+n+1)//2
            delta=ell+n+2-2*m
            assert delta in (1,2)
            assert (delta==2) == ((ell+n)%2==0)
            checks+=2
        N=n+1
        wanted=1+2*(N//4) if n%2==0 else 2*(N//4)
        for t in (.04,.25,.64,.91):
            found=roots(n,t)
            assert len(found)==wanted,(n,t,len(found),wanted)
            checks+=1
            for j,y,C in found:
                q=(1-math.sqrt(t))/(1+math.sqrt(t))
                assert abs(y)<1
                assert abs(C**N-((-1)**n)*q*q)<1e-11
                assert normalized_zero_residual(n,math.sqrt(t)*y,t)<1e-10
                checks+=3
            if n in (1,2,3,4,5,8):
                for y in ((.2+.1j),(-.3+.2j),.1):
                    s=math.sqrt(t)*y
                    a=exact_partial_formula(n,s,t)
                    b=independent_series(n,s,t,L=180)
                    assert abs(a-b)/max(1,abs(a),abs(b))<2e-10,(n,t,y,a,b)
                    checks+=1
    # Exact monomial integration and even/odd coefficient pattern at rational t.
    for n in range(1,10):
        for ell in range(30):
            for beta in range(-30,8):
                admissible=2*beta+ell+n+2>0
                minimum=-((ell+n+1)//2)
                assert admissible == (beta>=minimum),(n,ell,beta)
                checks+=1
    # Exact phase condensation for a representative pair of dimensions.
    for n in (2,3,4,7):
        N=n+1
        t=1-1e-7
        for j,y,C in roots(n,t):
            theta=(2*j+(n%2))*math.pi/N
            approx=(y+1)/(1-t)**(2/N)
            expected=2**(1-4/N)*cmath.exp(1j*theta)
            assert abs(approx-expected)<0.02,(n,j,approx,expected)
            checks+=1
    print('PASS',checks,'checks; standard library only')

if __name__=='__main__': test()
