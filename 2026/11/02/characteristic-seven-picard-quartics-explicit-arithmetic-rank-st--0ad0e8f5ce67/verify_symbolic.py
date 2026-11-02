#!/usr/bin/env python3
"""Exact coefficient algebra and complete coefficient-marked census for Picard curves in F7.
Requires SymPy; verification is symbolic, not an extrapolation from test fields.
"""
import sympy as sp
from collections import Counter
x,a,b,c=sp.symbols('x a b c')
f=x**4+a*x**2+b*x+c
D=sp.discriminant(f,x)
P2=sp.Poly(sp.expand(f**2),x)
P4=sp.Poly(sp.expand(f**4),x)
q=lambda polynomial,degree:polynomial.coeff_monomial(x**degree)
A=q(P2,6)
B00=q(P4,6);B01=q(P4,5);B10=q(P4,13);B11=q(P4,12)
modzero=lambda t:sp.Poly(sp.expand(t),a,b,c,modulus=7).is_zero
assert modzero(A-2*a)
assert modzero(B00*B11-B01*B10-5*a*D)
assert modzero(sp.det(sp.Matrix([[A,0,0],[0,B00,B01],[0,B10,B11]]))-3*a*a*D)
# On a=0 the 2-by-2 block is the outer product (3*b*c,1)^t(4*b,4*c).
assert all(modzero(t.subs(a,0)-v) for t,v in ((B00,5*b*b*c),(B01,5*b*c*c),(B10,4*b),(B11,4*c)))
# The geometric stable-rank defect condition is 5*b^8*c+4*c^7=0;
# away from the discriminant b^4-3*c^3=0 it reduces to c=0 or b^4-4*c^3=0.
s=sp.Poly(sp.expand(c*(5*b**8+4*c**6)),b,c,modulus=7)
assert sp.Poly(sp.expand(c*(b**4-3*c**3)*(b**4-4*c**3)),b,c,modulus=7)==sp.Poly(sp.expand(c*(b**8-7*b**4*c**3+12*c**6)),b,c,modulus=7)
assert sp.Poly(s.as_expr()-5*c*(b**4-3*c**3)*(b**4-4*c**3),b,c,modulus=7).is_zero

# One-level enumeration confirms the exact F7 counts; smoothness is independently
# determined by a degree-four polynomial gcd in each case.
def smooth(aa,bb,cc):
    F=sp.Poly(x**4+aa*x**2+bb*x+cc,x,modulus=7)
    return F.gcd(F.diff()).degree()==0
C=Counter()
for aa in range(7):
    for bb in range(7):
        for cc in range(7):
            if not smooth(aa,bb,cc):
                C['singular']+=1
                continue
            if aa: C[(3,0)]+=1
            elif cc==0 or (bb**4-4*cc**3)%7==0:C[(0,2)]+=1
            else:C[(1,2)]+=1
assert C=={'singular':49,(3,0):252,(1,2):30,(0,2):12},C
print('SYMBOLIC_VERIFY_OK',dict(C))
