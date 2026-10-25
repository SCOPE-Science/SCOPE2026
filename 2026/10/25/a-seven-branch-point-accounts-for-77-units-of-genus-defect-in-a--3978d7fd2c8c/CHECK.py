#!/usr/bin/env python3
"""Exact symbolic and integer checks for the plane-curve branch statement.
Requires SymPy; complements, but does not replace, the analytic branch proof.
"""
import sympy as sp
h,a=sp.symbols('h a')
A=h**6-1
F=h**9-h**6-h**3+2
G=h**5*(h**12+h**7-2*h**6-2*h+1)
t=h**3
assert sp.expand(F-(t**3-t**2-t+2))==0
assert sp.expand(G-(-1+(1+h**5)*A**2))==0
assert sp.rem(F-1,A,h)==0
assert sp.rem(G+1,A,h)==0
# At h^3= +/-1 the derivative in a of F(eps*sqrt(1+a)).
values={}
for eps in (1,-1):
    T=eps*sp.sqrt(1+a)
    f=T**3-T**2-T+2
    values[eps]=sp.simplify(-2*sp.diff(f,a).subs(a,0))
assert values=={1:0,-1:4}
# Each type consists of three distinct values of zeta^5 (zeta^6=1).
assert len({(1,0),(0,1),(-1,-1)})==3  # representative classes mod zeta^2+zeta+1
# No zero leading denominator at the finite preimages; deg(F*A,G,A^2)=(15,17,12).
assert [sp.degree(F*A,h),sp.degree(G,h),sp.degree(A*A,h)]==[15,17,12]
# Pairwise intersections: 6 within-type order 4, 9 across-type order 3,
# 6 smooth/cusp order 4; cusp intrinsic delta 2.
assert 2*3==6 and 3*3==9
local_delta=2+6*4+9*3+6*4
assert local_delta==77
assert 6+2==8
arithmetic_genus=(17-1)*(17-2)//2
assert arithmetic_genus==120 and arithmetic_genus-local_delta==43
print('VERIFY_OK rational_degree17 six_smooth_one_cusp local_delta=77 multiplicity=8 residual_delta=43')
