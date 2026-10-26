#!/usr/bin/env python3
"""Independent symbolic recheck; requires SymPy 1.12 or newer."""
import sympy as s
u,v,l,t=s.symbols('u v l t')
F=u-l*v+u**5*v+v**5+l*v**3-u**3-u**3*v**3-v**3
assert s.Poly(s.diff(F,u)-(1-u**4*v),u,v,l,modulus=3).is_zero
assert s.Poly(s.diff(F,v)-(-l+u**5-v**4),u,v,l,modulus=3).is_zero
P7=u**7+u**5+u**4-u**3-1
P19=u**19+u**18+u**17-u**15-u**11-u**8+u**7-u**5-u**3+u+1
N=s.cancel(F.subs([(v,u**-4),(l,u**5-u**-16)])*u**28)
assert s.Poly(N+(u-1)**3*(u+1)**2*P7*P19,u,modulus=3).is_zero
Q7=t**7+t**6+t**4-t**3-1
Q19=t**19-t**18-t**16-t**15+t**14-t**11+t**9-t**8-t**7-t**5+t**3+t**2+1
for P,Q in [(P7,Q7),(P19,Q19)]:
    assert s.Poly(P,u,modulus=3).is_irreducible
    assert s.Poly(Q,t,modulus=3).is_irreducible
    lam=s.rem(u**5-s.invert(u**16,P,domain=s.GF(3)),P,domain=s.GF(3))
    h=s.Poly(0,u,modulus=3)
    kval=s.Poly(lam,u,modulus=3)
    modulus=s.Poly(P,u,modulus=3)
    for coef in s.Poly(Q,t,modulus=3).all_coeffs():
        h=(h*kval+s.Poly(coef,u,modulus=3)).rem(modulus)
    assert h.is_zero
    assert not s.Poly(s.rem(lam**3-lam,P,domain=s.GF(3)),u,modulus=3).is_zero
Hdet=s.diff(F,u,2)*s.diff(F,v,2)-s.diff(F,u,v)**2
# The Hessian relation is imposed on the critical equations, in the quotient ring:
assert s.Poly(Hdet-(u**3*v**4-u**8),u,v,l,modulus=3).is_zero
U,V=s.symbols('U V')
loc=F.subs(l,0).subs({u:1+U,v:1+V})
lowest=s.Poly(loc,U,V,modulus=3)
quad=sum(c*U**i*V**j for (i,j),c in lowest.terms() if i+j==2)
assert s.Poly(quad-(U+V)**2,U,V,modulus=3).is_zero
assert s.Poly(loc.subs({U:-V}),V,modulus=3)==s.Poly(V**3-V**5,V,modulus=3)
print('SYMBOLIC_VERIFY_OK')
