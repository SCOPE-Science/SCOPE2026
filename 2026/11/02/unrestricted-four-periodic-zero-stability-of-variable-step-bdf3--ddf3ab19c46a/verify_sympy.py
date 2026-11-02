#!/usr/bin/env python3
"""Independent SymPy reconstruction of BDF3 and the degree-20 certificates."""
import sympy as s
from verify import schur_polynomials
x,y,z,w=s.symbols('x y z w')
h=[x,y,z,w];M=s.eye(2); denominator=s.Integer(1);eps=s.Integer(1)
for i in range(4):
    a,b,c=h[i],h[(i-1)%4],h[(i-2)%4]
    d=3*a*a+4*a*b+2*a*c+b*b+b*c
    D=b*c*(b+c)*d
    P=a*a*c*(a*a+4*a*b+2*a*c+3*b*b+3*b*c+c*c)
    U=a*a*b*(a+b)**2
    M=s.Matrix([[P,-U],[D,0]])*M
    denominator*=D;eps*=U
tr=s.trace(M)
pieces={'minus':denominator-tr+eps,'plus':denominator+tr+eps,'det':denominator-eps}
refs=schur_polynomials()
for k,p in pieces.items():
    poly=s.Poly(p,x,y,z,w)
    assert dict(poly.terms())==refs[k],k
    print('PASS',k,len(poly.terms()),'nonnegative integer coefficients')
# Independent direct four-step rational transfer matrix for the sharp geometric path.
r=s.symbols('r',positive=True);h=[s.Integer(1),r,r**2,r**3]
F=s.eye(2)
for i in range(4):
    a,b,c=h[i],h[(i-1)%4],h[(i-2)%4]
    d=3*a*a+4*a*b+2*a*c+b*b+b*c
    P=a*a*c*(a*a+4*a*b+2*a*c+3*b*b+3*b*c+c*c)
    U=a*a*b*(a+b)**2
    D=b*c*(b+c)*d
    F=s.Matrix([[P/D,-U/D],[1,0]])*F
T=s.cancel(s.trace(F)); E=s.cancel(F.det())
assert s.limit(T,r,0)==-1
assert s.limit((T+1)/r,r,0)==6
assert s.limit(E/r,r,0)==0
assert s.limit(E/r**5,r,0)==s.Rational(1,3)
print('PASS: geometric boundary trace -1+6r+O(r^2), det r^5/3+O(r^6)')
