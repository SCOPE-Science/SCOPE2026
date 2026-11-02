#!/usr/bin/env python3
"""Stand-alone finite symbolic spot checks of radial derivative identities.

These checks do not prove the asymptotic theorem or any infinite-domain statement.
Requires sympy 1.12 or later.
"""
import sympy as sp

rho, z = sp.symbols('rho z', positive=True)
b, c = sp.symbols('b c', real=True)
for d in [1, 2, 3, 5, 9]:
    h = sp.Function('h')
    v = rho**(-d)*h(sp.log(rho))
    lhs = sp.diff(v, rho, 2)+(d-1)*sp.diff(v,rho)/rho
    rhs = rho**(-d-2)*(sp.diff(h(z),z,2)-(d+2)*sp.diff(h(z),z)+2*d*h(z)).subs(z,sp.log(rho))
    assert sp.simplify(lhs-rhs)==0, ('radial transformation',d)
    a = d+2
    g = z**(-b/a)*sp.log(z)**(-c/a)
    deriv = -b/a/z-c/a/(z*sp.log(z))
    assert sp.simplify(sp.diff(g,z)/g-deriv)==0, ('slow logarithmic derivative',d)
    assert sp.simplify(-a*deriv-(b/z+c/z/sp.log(z)))==0, ('potential leading term',d)
print('PASS: 15 exact symbolic identities in dimensions 1,2,3,5,9')
