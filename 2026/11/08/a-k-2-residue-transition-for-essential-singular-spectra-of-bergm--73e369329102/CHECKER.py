#!/usr/bin/env python3
"""Finite consistency checks for monomial k-slant Bergman commutators.

No external dependencies. Verifies independently evaluated basis actions,
Gram entries, residue arithmetic, and convergence of tail coefficients.
Finite checks do not establish the essential-spectrum theorem.
"""
import math

def gamma_norm(n, alpha):
    if n < 0:
        raise ValueError('negative monomial index')
    return math.exp(0.5*(math.lgamma(alpha+2)+math.lgamma(n+1)-math.lgamma(n+alpha+2)))

def B_image(n, a, k, alpha):
    s=n+a
    if s%k:
        return None
    m=s//k
    return m, gamma_norm(m,alpha)/gamma_norm(n,alpha)

def composed_image(n,a,b,k,alpha):
    first=B_image(n,b,k,alpha)
    if first is None:
        return None
    second=B_image(first[0],a,k,alpha)
    if second is None:
        return None
    return second[0],first[1]*second[1]

def row(m,a,b,k,alpha):
    result={}
    for h,sign in [(b+k*a,1),(a+k*b,-1)]:
        n=k*k*m-h
        if n>=0:
            v=gamma_norm(m,alpha)/gamma_norm(n,alpha)
            result[n]=result.get(n,0)+sign*v
    return {n:v for n,v in result.items() if abs(v)>1e-13}

def inner(u,v):
    return sum(x*v.get(n,0) for n,x in u.items())

def verify():
    tested=0
    cases=[(2,0,1),(2,1,5),(2,0,4),(2,5,9),(3,0,2),(3,2,11),(3,1,10),(4,1,3),(4,1,17),(5,0,25)]
    for k,a,b in cases:
        for alpha in (0.,1.,2.,-0.4):
            for m in (0,1,2,3,5,10,37,150):
                r=row(m,a,b,k,alpha)
                # Compute all candidate basis inputs using two independently chained W actions.
                for n in set(r)|{k*k*m-(b+k*a),k*k*m-(a+k*b)}:
                    if n<0: continue
                    v=0.
                    for p,q,sgn in ((a,b,1),(b,a,-1)):
                        im=composed_image(n,p,q,k,alpha)
                        if im is not None and im[0]==m: v+=sgn*im[1]
                    assert abs(v-r.get(n,0))<1e-9*max(1,abs(v)),(k,a,b,alpha,m,n)
                    tested+=1
            k2=k*k
            d=(k-1)*(a-b)
            same=(d%k2==0)
            m=200000
            rho=row(m,a,b,k,alpha)
            target=k**(alpha+1)
            # Each individual composition row approaches the same weight.
            for h in (b+k*a,a+k*b):
                n=k2*m-h
                assert abs(gamma_norm(m,alpha)/gamma_norm(n,alpha)/target-1)<2e-4,(k,alpha,h)
                tested+=1
            rho2=row(m+1,a,b,k,alpha)
            if not same:
                assert not (set(rho)&set(rho2))
                assert abs(inner(rho,rho)/(2*target*target)-1)<4e-4
                tested+=2
            else:
                shift=abs(d)//k2
                if shift>0:
                    rho_d=row(m+shift,a,b,k,alpha)
                    assert abs(inner(rho,rho_d)/(-target*target)-1)<4e-4, (k,a,b,alpha)
                    tested+=1
    print('SLANT_COMMUTATOR_ESSENTIAL_FINITE_OK',tested)
if __name__=='__main__': verify()
