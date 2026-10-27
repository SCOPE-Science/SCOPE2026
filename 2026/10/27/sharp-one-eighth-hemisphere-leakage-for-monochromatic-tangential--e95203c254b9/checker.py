#!/usr/bin/env python3
"""Reproduce finite tests for exact-degree tangential vector hemisphere concentration.

The analytical all-degree proof is in RESULT.md. Uses only Python standard library.
"""
import math
from fractions import Fraction

def central(k):
    return Fraction(math.comb(2*k,k),4**k)

def coupling_exact(l,m):
    assert l>=1 and 0<=m<=l
    if m==0 or (l+m)%2: return Fraction(0)
    a,b=(l+m)//2,(l-m)//2
    return Fraction(m*(2*l+1),2*l*(l+1))*central(a)*central(b)

def assoc_legendre(l,m,x):
    """Unnormalized Condon-Shortley associated Legendre P_l^m(x)."""
    pmm=1.0
    for j in range(1,m+1):
        pmm*=-(2*j-1)*math.sqrt(1-x*x)
    if l==m:return pmm
    pprev=pmm
    pcur=x*(2*m+1)*pmm
    if l==m+1:return pcur
    for ell in range(m+2,l+1):
        pnext=((2*ell-1)*x*pcur-(ell+m-1)*pprev)/(ell-m)
        pprev,pcur=pcur,pnext
    return pcur

def integral_coupling(l,m,n=4096):
    """Numerically integrate the hemispherical cross term via f*(df/dtheta).

    For Y_lm=f(theta) exp(im phi), <E_lm,J E_lm>_H
    equals (2*pi*i*m/(l(l+1)))*(f(pi/2)^2-f(0)^2).
    Here the integrand 4*pi*m*f*f'/(l(l+1)) is integrated by Simpson,
    separately from the equatorial evaluation.
    """
    assert n%2==0 and m>=1
    norm=math.sqrt((2*l+1)/(4*math.pi)*math.factorial(l-m)/math.factorial(l+m))
    h=math.pi/(2*n)
    sm=0.
    for j in range(n+1):
        th=max(j*h, 1.e-9) if j==0 else j*h
        x=math.cos(th)
        P=assoc_legendre(l,m,x)
        lower=assoc_legendre(l-1,m,x) if l>m else 0.0
        # (1-x^2) P'(x)=-l*x*P+(l+m)*P_(l-1)(x).
        dPdx=(-l*x*P+(l+m)*lower)/max(1-x*x,1.e-18)
        f=norm*P
        df=-math.sin(th)*norm*dPdx
        v=4*math.pi*m*f*df/(l*(l+1))
        sm+=(1 if j==0 or j==n else 4 if j%2 else 2)*v
    return sm*h/3

def main():
    max_eq_err=0.0
    max_quad_err=0.0
    tested=0
    for l in range(1,11):
        top=coupling_exact(l,l)
        assert top==Fraction(2*l+1,2*(l+1))*central(l)
        for m in range(0,l+1):
            g=coupling_exact(l,m)
            assert 0<=g<=top
            if m>=1 and (l+m)%2==0:
                pn=assoc_legendre(l,m,0.0)
                norm2=(2*l+1)/(4*math.pi)*math.factorial(l-m)/math.factorial(l+m)
                gt=2*math.pi*m*norm2*pn*pn/(l*(l+1))
                max_eq_err=max(max_eq_err,abs(gt-float(g)))
                if l<=8:
                    gi=integral_coupling(l,m)
                    max_quad_err=max(max_quad_err,abs(gi-float(g)))
                tested+=1
        if l>1: assert top < coupling_exact(l-1,l-1)
    assert coupling_exact(1,1)==Fraction(3,8)
    assert Fraction(1,2)+coupling_exact(1,1)==Fraction(7,8)
    assert max_eq_err < 1e-12, max_eq_err
    assert max_quad_err < 2e-5, max_quad_err
    print("check=PASS")
    print("exact_modes_checked="+str(tested))
    print("ell_1_max=7/8, ell_1_min=1/8")
    print("max_equator_formula_discrepancy=%.3e"%max_eq_err)
    print("max_hemispherical_quadrature_discrepancy=%.3e"%max_quad_err)
    print("maxima_ell_1_to_6="+str([str(Fraction(1,2)+coupling_exact(l,l)) for l in range(1,7)]))
if __name__=="__main__": main()
