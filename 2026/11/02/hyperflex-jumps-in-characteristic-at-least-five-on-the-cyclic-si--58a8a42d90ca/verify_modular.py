#!/usr/bin/env python3
"""Independent modular checks of the exceptional parameter scheme.
Requires SymPy. Checks exact field factors, squarefreeness, exceptional-point
uniqueness, nonsingularity and the special characteristic-eleven fiber.
"""
import sympy as S
u,r=S.symbols('u r')
G=u*u+r*u+1
h2=S.expand(3*(6*u+r)*G-4*u*(2*u+r)**2)
h3=S.expand(2*u*(2*u+r)**3-27*G**2)
P=11*r**4-1080*r**2+3888
L=33*r**4-704*r**2+2160
N=196*r**3-720*r
# A root u=N/L at each exceptional r must satisfy both tangency equations.
# Reduce numerators of substitution modulo P over finite fields.
for p,degree in ((5,4),(7,4),(11,2),(13,4),(17,4)):
    pp=S.Poly(P,r,modulus=p)
    if p==11: assert S.degree(pp.as_expr(),r)==2
    else: assert S.degree(pp.as_expr(),r)==4
    assert S.gcd(pp,pp.diff()).degree()==0
    assert S.gcd(pp,S.Poly(L,r,modulus=p)).degree()==0
    assert S.gcd(pp,S.Poly(r*(r*r-4),r,modulus=p)).degree()==0
    # Substitute u=N/L and clear denominators: h2 degree 3 and h3 degree 4 in u.
    for h in (h2,h3):
        d=S.degree(h,u)
        q=S.Poly(S.expand(sum(h.coeff(u,j)*N**j*L**(d-j) for j in range(d+1))),r,modulus=p)
        assert S.rem(q,pp).is_zero, (p,h,q)
    fac=S.factor_list(pp)[1]
    if p in (5,7): assert len(fac)==1 and fac[0][0].degree()==4 and fac[0][1]==1
    if p==11: assert len(fac)==1 and fac[0][0].degree()==2 and fac[0][1]==1
    print('p=',p, 'degree=',pp.degree(), 'irreducible_pattern=',[(f.degree(),e) for f,e in fac])
assert S.factor_list(S.Poly(P,r,modulus=11))[1][0][0].monic()==S.Poly(r*r+3,r,modulus=11)
print('MODULAR_HYPERFLEX_OK')
