#!/usr/bin/env python3
"""Exact rational-polynomial checks of the root separation lemma for path Laplacians."""
import sympy as sp
from time import perf_counter
x=sp.Symbol('x')

def expected(n,d):
    F=sp.Poly(1,x,domain=sp.QQ)
    if d==1:
        if n%3==0:F*=sp.Poly(x-1,x)
        if n%6==0:F*=sp.Poly((x-2)*(x-3),x)
        if n%5==0:F*=sp.Poly(x*x-5*x+5,x)
    if d==2:
        if n%2==0:F*=sp.Poly(x-2,x)
        if n%3==0:F*=sp.Poly(x-3,x)
    if d==3 and n%3==0:F*=sp.Poly(x-3,x)
    return F.monic()

t0=perf_counter();U0=sp.Poly(1,x);U1=sp.Poly(2-x,x)
checks=0
for n in range(2,51):
    p=(sp.Poly(x,x)*U1) if n==2 else None
    if n>2:
        U2=sp.Poly(2-x,x)*U1-U0;U0,U1=U1,U2
        p=sp.Poly(x,x)*U1
    for d in (1,2,3):
        s=sp.Poly(p.as_expr().subs(x,x-d),x)
        g=sp.gcd(p,s).monic()
        assert g==expected(n,d),(n,d,g.as_expr(),expected(n,d).as_expr())
        checks+=1
print(f'PASS: {checks} exact polynomial gcd assertions n=2..50, d=1,2,3, elapsed {perf_counter()-t0:.2f}s')
