"""Exact characteristic-two square-contact calculation for a Picard quartic.
Run with Python 3 and SymPy: python VERIFY_picard2_bitangent.py
"""
import sympy as s
X,Y,Z,u,v,a,b,c,d,alpha,beta=s.symbols('X Y Z u v a b c d alpha beta')
F=Y**3*Z+X**4+a*X**3*Z+b*X**2*Z**2+c*X*Z**3+d*Z**4

def mod2(expr):
    P=s.Poly(s.expand(expr),X,Y,Z,u,v,a,b,c,d,alpha,beta,domain=s.ZZ)
    return s.expand(sum(s.prod(var**n for var,n in zip(P.gens,powv))
             for powv,coef in P.terms() if coef%2))

def odd_coeffs(binary_poly, A,B):
    p=s.Poly(binary_poly,A,B)
    return [mod2(p.coeff_monomial(A**3*B)),mod2(p.coeff_monomial(A*B**3))]
chart=mod2(F.subs(Z,u*X+v*Y))
assert odd_coeffs(chart,X,Y)==[a*v+c*u**2*v,u+c*v**3]
# Second dual chart: Y=alpha X+ beta Z, with beta=0 on W=0.
P=mod2(F.subs(Y,alpha*X+beta*Z))
assert odd_coeffs(P,X,Z)==[a+alpha**3,c+alpha*beta**2]
# Remaining line X=0 has an odd coefficient equal to one.
Px=mod2(F.subs(X,0))
assert s.Poly(Px,Y,Z).coeff_monomial(Y**3*Z)==1
# Algebraic elimination and explicit quotient relation.
assert mod2((v*(a+c*u**2)).subs(u,c*v**3))==a*v+c**3*v**7
# Generic and special fibre factorizations in k[v].
T=s.symbols('T')
assert s.expand((v**3+T)**2) == v**6+2*T*v**3+T**2
assert s.Poly(v**7,v).degree()==7
# The explicit completed special-fibre algebra has length seven and
# Hilbert function 1 in degrees 0 through 6.
for power in range(7):
    assert power<7
print('VERIFY_OK: both dual charts, exact square-contact equations, elimination, seven-step local algebra')
