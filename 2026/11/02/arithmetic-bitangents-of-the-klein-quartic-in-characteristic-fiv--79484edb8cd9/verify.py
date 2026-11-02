"""Exact characteristic-five bitangent calculation for the Klein plane quartic.

Run with Python 3 and SymPy 1.13 or later: python verify.py
No finite-field point sampling is used for the elimination certificate.
"""
import sympy as S
from collections import Counter

p=5
x,y,z,a,b,t=S.symbols('x y z a b t')
F=x**3*y+y**3*z+z**3*x
# A projective line [a:b:1] is z=-a*x-b*y.
q=S.Poly(S.expand(F.subs(z,-a*x-b*y)),x,y)
C=[S.expand(q.coeff_monomial(x**(4-i)*y**i)) for i in range(5)]
assert C==[-a**3, 1-3*a**2*b, -3*a*b**2, -a-b**3, -b],C
c0,c1,c2,c3,c4=C
f=S.expand(8*c0*c0*c3-c1*(4*c0*c2-c1*c1))
g=S.expand(64*c0*c0*c0*c4-(4*c0*c2-c1*c1)**2)
assert f==(-8*a**7+a**6*b**3+15*a**4*b**2-9*a**2*b+1)
assert g==(64*a**9*b-9*a**8*b**4-36*a**6*b**3-30*a**4*b**2+12*a**2*b-1)
G=S.groebner([f,g],b,a,modulus=p,order='lex')
P=a**28-a**21+2*a**14+2*a**7+1
H=S.groebner([b-a**26,P],b,a,modulus=p,order='lex')
assert [h.as_expr() for h in G.polys]==[h.as_expr() for h in H.polys]
assert [S.Poly(h,b,a,modulus=p).total_degree() for h in G.polys]==[26,28]
# In particular P(0)=1, so all 28 solutions have c0 != 0.
assert int(P.subs(a,0))%p==1
PP=S.Poly(P,a,modulus=p)
assert S.gcd(PP,PP.diff()).degree()==0
factor_coefficient, factors=S.factor_list(P,modulus=p)
assert int(factor_coefficient)%5==1
factor_degrees=sorted([S.degree(h,a) for h,e in factors for _ in range(e)])
assert factor_degrees==[1,3,6,6,6,6],factor_degrees
assert all(e==1 for _,e in factors)

def mod_power(base, exponent, modulus):
    """Polynomial modular powering over F5, without integer-root enumeration."""
    out=S.Poly(1,a,modulus=5)
    bb=base.rem(modulus)
    while exponent:
        if exponent & 1:
            out=(out*bb).rem(modulus)
        bb=(bb*bb).rem(modulus)
        exponent >>= 1
    return out

for h,e in factors:
    assert e==1
    hh=S.Poly(h,a,modulus=5)
    n=hh.degree()
    assert mod_power(S.Poly(a,a,modulus=5),5**n,hh)==S.Poly(a,a,modulus=5).rem(hh)
    for r in [r for r in (2,3,5) if n%r==0]:
        v=mod_power(S.Poly(a,a,modulus=5),5**(n//r),hh)-S.Poly(a,a,modulus=5)
        assert S.gcd(hh,v).degree()==0
# The only root in F5 is a=1, giving b=1.
assert [k for k in range(5) if int(P.subs(a,k))%5==0]==[1]
# Smoothness check: in characteristic 5, the partial-derivative equations
# force xyz !=0 and 1=(-3)^3=3, an impossibility; the origin is not a projective point.
assert (-3)**3%5==3 and 3!=1
assert S.expand(F.subs(z,-x-y)+(x*x+x*y+y*y)**2)==0
print('RESTRICTION_COEFFICIENTS_OK')
print('GROEBNER_IDEAL=(b-a^26,a^28-a^21+2a^14+2a^7+1)_OVER_F5')
print('ELIMINANT_SQUAREFREE_DEGREE_28_OK')
print('FROBENIUS_ORBIT_LENGTHS='+str(factor_degrees))
print('F5_BITANGENT=[1:1:1]; ALL_28_OVER_F5^6')
print('ZETA_RECIPROCAL=(1-T)(1-T^3)(1-T^6)^4')
print('VERIFY_OK')
