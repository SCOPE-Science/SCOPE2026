"""Exact characteristic-7 elimination certificate for the Ciani Hasse intersection.
Requires SymPy >= 1.12. All coefficients and arithmetic are in GF(7).
"""
import sympy as sp

a,b,c,t=sp.symbols('a b c t')
P=7

def hasse(u,v,w):
    A=u*u-4
    C=v*v-4
    B=2*u*v-4*w
    return B*(B*B-A*C)

forms=[hasse(a,b,c),hasse(a,c,b),hasse(b,c,a)]
Delta=(a*a-4)*(b*b-4)*(c*c-4)*(a*a+b*b+c*c-a*b*c-4)
G=sp.groebner(forms+[t*Delta-1],t,a,b,c,order='lex',modulus=P)
# Check the full saturated ideal in three variables by elimination.
eliminated=[sp.Poly(p.as_expr(),a,b,c,modulus=P).monic() for p in G.polys if not p.as_expr().has(t)]
assert len(eliminated)==7
assert G.is_zero_dimensional
expected=[
 a**3-a+b**3*c**3+b**3*c+b*c**3-3*b*c,
 a*b-b**2*c**3-b**2*c-c**5-2*c**3+3*c,
 a*c-b**3*c**2-3*b**3-b*c**4+3*b,
 b**4-b**2-c**4+c**2,
 b**3*c**4-b**3*c**2-2*b**3-b*c**4+b*c**2+2*b,
 b*c**5-b*c**3-2*b*c,
 c**7-2*c**5-c**3+2*c,
]
assert all(p==sp.Poly(e,a,b,c,modulus=P).monic() for p,e in zip(eliminated,expected))
LM=[p.LM(order='lex').exponents for p in eliminated]
assert LM == [(3,0,0),(1,1,0),(1,0,1),(0,4,0),(0,3,4),(0,1,5),(0,0,7)]
standard=[]
for i in range(3):
 for j in range(4):
  for k in range(7):
   if not any(i>=u and j>=v and k>=w for u,v,w in LM):
    standard.append((i,j,k))
assert len(standard)==23
assert sorted(standard)==sorted([(0,0,k) for k in range(7)]+[(0,1,k) for k in range(5)]+[(0,2,k) for k in range(5)]+[(0,3,k) for k in range(4)]+[(1,0,0),(2,0,0)])
print('VERIFY_GROEBNER_OK: saturated lex basis 7, standard monomials 23, scheme length 23')
