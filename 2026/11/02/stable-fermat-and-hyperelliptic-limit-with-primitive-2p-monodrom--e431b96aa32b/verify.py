#!/usr/bin/env python3
"""Exact finite symbolic checks for the stable t=-2 Kuribayashi--Komiya fiber.
Python 3 with SymPy. This script supplements, not replaces, the global stable-reduction proof.
"""
import sympy as sp

U,V,W,a,b,e,s,T,r,q=sp.symbols('U V W a b e s T r q')
Q=lambda U,V,W,t: U**2+V**2+W**2+t*(U*V+U*W+V*W)
assert sp.expand(Q(U,V,W,-2)-((U-V-W)**2-4*V*W))==0
assert sp.expand(Q(r**2,q**2,(r+q)**2,-2))==0
F_local=Q(1+a+b**5,1,b**5,-2+e)
assert sp.expand(F_local - (a*a-4*b**5+e*(1+a+3*b**5+a*b**5+b**10)))==0
for p in [5,7,11,13,17,19]:
    h=(p-1)*(p-2)//2
    tail=(p-1)//2
    total=(p-1)*(2*p-1)
    assert h+3*p*tail==total
    assert (2*p-1)*(p-1)-3*p*tail==h
    A,B=sp.symbols('A B')
    F=Q(1+A+B**p,1,B**p,-2+e)
    expected=A*A-4*B**p+e*(1+A+3*B**p+A*B**p+B**(2*p))
    assert sp.expand(F-expected)==0
    # With e=s^(2p), A=s^p a, B=s^2 b, the rescaled equation
    # has constant term a^2 - 4*b^p + 1.
    scaled=sp.expand(expected.subs({A:s**p*a,B:s**2*b,e:s**(2*p)}) / s**(2*p))
    assert sp.expand(scaled.subs(s,0)-(a*a-4*b**p+1))==0
    assert sp.gcd(sp.Poly(4*b**p-1,b),sp.Poly(4*p*b**(p-1),b)).degree()==0
    # The nontrivial local eigenvalues are all primitive 2p-th roots.
    exponents={j for k in range(1,(p+1)//2) for j in (k,p-k)}
    assert exponents==set(range(1,p))
    assert sp.div(T**p+1,T+1,T)[1]==0
    assert sp.expand(sp.div(T**p+1,T+1,T)[0]-sp.cyclotomic_poly(2*p,T))==0
    assert (p-1)*(p-2)+3*p*(p-1)==2*total
    print('CHECK_OK', p, 'central_genus',h,'tails',3*p,'tail_genus',tail,
          'generic_genus',total,'monodromy_order',2*p)
print('VERIFY_OK')
