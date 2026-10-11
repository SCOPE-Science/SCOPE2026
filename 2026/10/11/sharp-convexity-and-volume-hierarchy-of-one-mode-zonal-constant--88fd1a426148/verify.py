#!/usr/bin/env python3
"""Exact finite consistency checks for one-mode axial support functions.

Proof for all degrees is in RESULT.md. This script only checks four degrees.
Requires Python 3 and SymPy.
"""
import sympy as S
x, eps = S.symbols("x eps", real=True)
for ell in (3, 5, 7, 9):
    q = S.legendre(ell, x)
    lam = ell * (ell + 1)
    C = S.Rational(lam-2, 2)
    def c(j):
        return S.binomial(2*j, j)/S.Integer(4)**j
    coeff = {k: 2*c((ell+k)//2)*c((ell-k)//2)
             for k in range(1, ell+1, 2)}
    assert all(v>0 for v in coeff.values())
    assert sum(coeff.values()) == 1
    assert sum((k*k-1)*v for k,v in coeff.items()) == C
    assert S.diff(q,x).subs(x,1) == S.Rational(lam,2)
    az = 1 + eps*(q-x*S.diff(q,x))
    mer = az + eps*(1-x*x)*S.diff(q,x,2)
    # exact solid volume from 3V=int(h rho_az rho_mer) on S^2
    product = S.Poly(S.expand((1+eps*q)*az*mer), x)
    integral = sum(v*(1-(-1)**(pow+1))/S.Integer(pow+1)
                   for (pow,),v in product.terms())
    vol = S.simplify(S.Rational(2,3)*S.pi*integral)
    predicted = 4*S.pi/3 - 2*S.pi*(lam-2)*eps**2/(2*ell+1)
    assert S.simplify(vol-predicted)==0, (ell, vol, predicted)
    minvol=predicted.subs(eps,S.Rational(1,1)/C)
    assert S.simplify(minvol-(4*S.pi/3-8*S.pi/((2*ell+1)*(lam-2))))==0
    if ell==3:
        assert S.simplify(minvol-128*S.pi/105)==0
        assert coeff[3]==S.Rational(5,8)
print('ONE_MODE_LEGENDRE_EXACT_OK 3 5 7 9')
