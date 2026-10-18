#!/usr/bin/env python3
"""Independent exact affine-chart Groebner verification of orbit representatives.

Requires SymPy in addition to verify_quartic_spectrum.py, which is in this package.
This is a secondary check, not the proof of the complete enumeration.
"""
import sympy as sp
from verify_quartic_spectrum import verify, MONS

X,Y,Z=sp.symbols('X Y Z')
for size,t,mask in verify():
    F=sp.Add(*(X**a*Y**b*Z**c for i,(a,b,c) in enumerate(MONS) if mask>>i&1))
    generators=[F,sp.diff(F,X),sp.diff(F,Y),sp.diff(F,Z)]
    for v in (X,Y,Z):
        other=[w for w in (X,Y,Z) if w!=v]
        local=[sp.Poly(p.subs(v,1),*other,modulus=2).as_expr() for p in generators]
        basis=sp.groebner(local,*other,modulus=2)
        assert list(basis)==[1],(mask,v,list(basis))
print('PASS: unit Groebner bases on all 3 charts of all 78 smooth orbit representatives')
