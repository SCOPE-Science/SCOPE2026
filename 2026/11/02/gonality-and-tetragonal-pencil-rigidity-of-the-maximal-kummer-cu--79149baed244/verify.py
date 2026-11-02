#!/usr/bin/env python3
"""Exact symbolic checks for the low-degree pencils of a cyclic Kummer curve.
The gonality lower bounds use the field-theoretic proofs in RESULT.md.
"""
from math import gcd
import sympy as s
T,X,W=s.symbols('T X W',nonzero=True)
I=s.I
x=(T-1/T)/2
z=(T+1/T)/2
assert s.cancel(z*z-x*x-1)==0
assert s.cancel(x*z-(T**4-1)/(4*T**2))==0
assert s.cancel((x*z)**2-x*x*(x*x+1))==0
# The involution x -> i W/x preserves W^2=x^4+x^2.
image=I*W/X
preservation=s.cancel((image**4+image**2-W**2).subs(W**4,(X**4+X**2)**2).subs(W**2,(X**4+X**2)))
assert s.factor(preservation)==0
# The two conjugate involution quotients are hyperelliptic.
u=X+I*W/X
v=X-I*W/X
assert s.factor(s.cancel((u*u+1-2*I*W)*X**2).subs(W**2,X**4+X**2))==0
assert s.factor(s.cancel((v*v+1+2*I*W)*X**2).subs(W**2,X**4+X**2))==0
for q in [3,5,7,9,11,13,17,19,23,25,27,29,31,37,41,43,47,49,81]:
    m=q+1; d=m//2
    genus=m-1-gcd(m,4)//2
    genus_biquad=(m-2)//2+2*((d-1)//2)
    assert genus==genus_biquad,(q,genus,genus_biquad)
    degree_t=d
    degree_y=4
    gonality={3:2,5:3}.get(q,4)
    assert gonality==min(degree_t,degree_y)
    if q>=9:
        assert genus>6 and (m-2)//2>=2 and (d-1)//2>=2
    if q>=13:
        assert genus>9
    print(f'q={q:2} m={m:2} d={d:2} genus={genus:3} '+' '.join([f'deg_y={degree_y}',f'deg_t={degree_t}',f'gonality={gonality}',f'quotient_genera={((m-2)//2,(d-1)//2,(d-1)//2)}']))
print('VERIFY_OK')
