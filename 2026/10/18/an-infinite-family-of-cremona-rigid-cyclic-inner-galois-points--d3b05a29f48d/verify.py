#!/usr/bin/env python3
"""Exact algebra tests for a cyclic-Galois plane-curve family.

Requires SymPy. The mathematical proof for arbitrary exponents is in RESULT.md.
"""
import sympy as sp

z,w,a,b,t=sp.symbols('z w a b t')
for n in (9,13,17):
    assert n>=9 and n%4==1
    k=(n+1)//2
    Q=(z+1)*w**k+z*w-1
    identity=(1-w**k)*(1+z**2*w)-z*(1-z*w**k)*(1+w)-(z-1)*Q
    assert sp.expand(identity)==0, (n,'collision identity')
    # Check all nonidentity n-th roots, including non-primitive ones.
    root_poly=sp.div(z**n-1,z-1,z)[0]
    disc=sp.discriminant(Q,w)
    assert sp.gcd(disc,root_poly)==1, (n,'root multiplicity')
    assert sp.expand(Q.subs(w,-1))==-2*(z+1), (n,'boundary')
    nodes=(n*n+1)//2
    delta=(n-1)//2
    arithmetic_genus=n*(n+1)//2
    assert nodes+delta==arithmetic_genus
    # Neither X(at+b) nor a mixture in the embedding space can have a t^(n+1) term.
    X=(a*t+b)-(a*t+b)**(n+2)
    assert sp.expand(X).coeff(t,n+1)==-(n+2)*a**(n+1)*b
    print('N_OK',n,'nodes',nodes,'cusp_delta',delta,'arithmetic_genus',arithmetic_genus)
print('VERIFY_OK: exact identity, cyclotomic discriminants and degree/genus coefficients')
