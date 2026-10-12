#!/usr/bin/env python3
"""Exact checks for bitangent-field theorem of the quartic X^4+Y^4+XZ^3=0.
Requires Python 3.10+ and SymPy 1.12+.
"""
from collections import Counter
from sympy import symbols, Poly, factor, simplify, sqrt, I, expand, rem, factor_list, primerange

k,c,t = symbols('k c t')
q = 24*k**2 + 12*k + 1
B=2*k+1/2
# Use rational exact everywhere
from sympy import Rational
B=2*k+Rational(1,2)
A=k**2-k-Rational(1,8)
v=expand(A*A-k**4)
assert simplify(2*A*B-4*k**3+q/8)==0
assert factor(rem(v+Rational(13,24)*k+Rational(11,192),q,k))==0
R=sqrt(3)
ap=(3+2*R)/12
am=(3-2*R)/12
kp=(-3+R)/12
km=(-3-R)/12
assert simplify(v.subs(k,kp)-am**3)==0
assert simplify(v.subs(k,km)-ap**3)==0
z12=(R+I)/2
z3=z12**4
gamma=(1+I)*(1+R)/2
assert simplify(gamma**4-ap/am)==0
assert simplify(z12**12-1)==0
P8=48*c**8-24*c**4-1
P16=2304*c**16+1152*c**12+624*c**8-24*c**4+1
P24=110592*c**24-17280*c**12-1
assert expand(P8*P16-P24)==0
assert Poly(P8,c).is_irreducible
assert Poly(P16,c).is_irreducible
T=symbols('T')
f4=2304*T**4+1152*T**3+624*T**2-24*T+1
assert Poly(f4,T).is_irreducible
assert simplify(f4.subs(T,ap*z3))==0
# The branch parameter k is uniquely recovered from c outside characteristic 13;
# no uniqueness-by-c is asserted in characteristic 13.
assert simplify(ap*am+Rational(1,48))==0
# Direct reconstruction of the quartic-square criterion.
# With x=c^4*t, y=c*(1+k*t), F/c^4 is the displayed quartic.
coef4=c**12+k**4
poly=coef4*t**4+4*k**3*t**3+6*k**2*t**2+(4*k+1)*t+1
square=(A*t**2+B*t+1)**2
D=Poly(expand(poly-square),t)
assert simplify(D.coeff_monomial(t**3)-q/8)==0 # sign? check below
assert simplify(D.coeff_monomial(t**4)-(c**12-v))==0
assert all(simplify(D.coeff_monomial(t**i))==0 for i in [0,1,2])

def square_nonvertical(p,m,c):
    # Coefficients of F(x,m*x+c,1) in x, as independent perfect-square check.
    if c==0:
        return False
    a0=pow(c,4,p)
    a1=(4*m*pow(c,3,p)+1)%p
    a2=(6*m*m*c*c)%p
    a3=(4*pow(m,3,p)*c)%p
    a4=(1+pow(m,4,p))%p
    u0=c*c%p
    u1=a1*pow(2*u0,-1,p)%p
    u2=(a2-u1*u1)*pow(2*u0,-1,p)%p
    return (2*u1*u2-a3)%p==0 and (u2*u2-a4)%p==0

def predicted(p):
    if p%12==5: return 2
    if p%12 in [7,11]: return 4
    assert p%12==1
    roots=[r for r in range(p) if r*r%p==3%p]
    assert len(roots)==2
    a=(3+2*roots[0])*pow(12,-1,p)%p
    fourth_powers={pow(x,4,p) for x in range(1,p)}
    return 28 if a in fourth_powers else 4

examples={}
for p in primerange(5,200):
    p=int(p)
    hyper=sum((pow(a,4,p)+a)%p==0 for a in range(p))
    normal=sum(square_nonvertical(p,m,c) for m in range(p) for c in range(p))
    N=hyper+normal
    assert N==predicted(p),(p,hyper,normal,N,predicted(p))
    examples[p]=(hyper,normal,N)
assert examples[5]==(2,0,2)
assert examples[7]==(4,0,4)
assert examples[11]==(2,2,4)
assert examples[13]==(4,0,4)
assert examples[37]==(4,24,28)
print('VERIFY_OK', 'exact polynomial identities, irreducible degree 8/16,',
      len(examples),'prime-field direct bitangent enumerations; examples:',
      {p:examples[p] for p in [5,7,11,13,17,23,37,61,73]})
