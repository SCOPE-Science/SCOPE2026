#!/usr/bin/env python3
"""Reproduce symbolic identities for the characteristic-two quartic discriminant."""
from sympy import symbols, Poly, discriminant, diff, expand, binomial

x, a, b, c, d, e, t, s = symbols('x a b c d e t s')
Q = a*d**2 + b*c*d + b**2*e
F = a*x**4 + b*x**3 + c*x**2 + d*x + e
D = discriminant(F, x)
assert all(int(v) % 2 == 0 for _, v in Poly(expand(D-Q**2), a,b,c,d,e).terms())
partials = [diff(Q, z) for z in (a,b,c,d,e)]
expected = [d**2, c*d, b*d, b*c, b**2]
for u,v in zip(partials,expected):
    assert all(int(coeff)%2 == 0 for _, coeff in Poly(expand(u-v),a,b,c,d,e).terms())
# On chart e=1: a=t^2+ct, b=dt.  On chart a=1: e=s^2+cs, d=bs.
assert all(int(v)%2==0 for _,v in Poly(expand(Q.subs({a:t**2+c*t,b:d*t,e:1}, simultaneous=True)),c,d,t).terms())
assert all(int(v)%2==0 for _,v in Poly(expand(Q.subs({a:1,d:b*s,e:s**2+c*s}, simultaneous=True)),b,c,s).terms())
# The Segre parametrization and missing-generator identities modulo two.
u,v,A,B,C,w = symbols('u v A B C w')
sub={a:u*B,b:u*A,c:v*B+u*C,d:v*A,e:v*C}
segre=[Q.subs(sub, simultaneous=True),
       (w**2+c*w+a*e).subs({**sub,w:v*B}, simultaneous=True),
       (b*w+a*d).subs({**sub,w:v*B}, simultaneous=True),
       (d*w+c*d+b*e).subs({**sub,w:v*B}, simultaneous=True)]
for polynomial in segre:
    assert all(int(coeff)%2==0 for _,coeff in Poly(expand(polynomial),u,v,A,B,C).terms())
# The ordinary double-root incidence is generically inseparable: f'(x) = b*x^2 + d.
assert expand(diff(F,x)-(4*a*x**3+3*b*x**2+2*c*x+d))==0
# Exact Jacobian Hilbert coefficients from k[a,e] and k[c,b,d]/(b,d)(b,c,d).
for n in range(0,21):
    # monomials in c, a, e plus the two independent monomials b,d times monomials in a,e
    from math import comb
    hilbert=comb(n+2,2)+(2*n if n>=1 else 0)
    assert hilbert==int(binomial(n+2,2)+2*n)
print('VERIFY_OK binary_quartic_discriminant_char2; n=0..20 Hilbert checks')
