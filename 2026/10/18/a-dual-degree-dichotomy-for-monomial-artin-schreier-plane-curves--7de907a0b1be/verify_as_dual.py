#!/usr/bin/env python3
"""Reproducible exact small-characteristic checks for monomial Artin--Schreier plane duals."""
import sympy as sp
x,u,v = sp.symbols('x u v')
for p,m,dual_degree in [(2,5,5),(3,5,15),(3,7,7)]:
    assert m>p and m%p
    mm=m%p
    f=x**(m-1)-u
    g=v**p-v-mm*x**p*u**p+(mm-1)*x*u
    R=sp.Poly(sp.resultant(f,g,x),u,v,modulus=p)
    assert R.total_degree()==p*m,(p,m,'wrong polar class',R.total_degree())
    if (m-1)%p==0:
        assert all(a%p==0 and b%p==0 for (a,b),c in R.terms()),(p,m,'not Frobenius cube')
        assert R.total_degree()//p==dual_degree
    else:
        assert R.total_degree()==dual_degree
        # Birationality follows separately from dv/du=x.
    print('CHECK',p,m,'resultant_total_degree',R.total_degree(),'gauss_degree',p if (m-1)%p==0 else 1,'dual_degree',dual_degree)
print('VERIFY_OK')
