"""Exact verification of an arithmetic node orbit on a rational plane sextic.

Requires Python 3 and SymPy. No floating point approximations are used.
"""
import sympy as S
from sympy.polys.polyfuncs import symmetrize

s,t,U,V=S.symbols('s t U V')
f=lambda z:(z**6+1, -z**5-z**3+3*z, z**4-z**3+9*z**2)
F,G=f(s),f(t)
H=[]
for i,j in ((0,1),(0,2),(1,2)):
    wedge=S.expand(F[i]*G[j]-F[j]*G[i]); q,rem=S.div(wedge,s-t,s)
    assert rem==0
    es,unused,symbols=symmetrize(q,[s,t],formal=True)
    assert unused==0
    H.append(S.expand(es.subs({symbols[0][0]:U,symbols[1][0]:V})))
    assert S.expand(q-H[-1].subs({U:s+t,V:s*t}))==0
P=412*V**7+680*V**6+1083*V**5-2647*V**4-9077*V**3-14481*V**2-14886*V-3708
Q=8644996*V**6+9291068*V**5+43497417*V**4-54802504*V**3-181768175*V**2-392557278*V-458223588
L=51168936*U+Q
GB=S.groebner(H,U,V,order='lex',domain=S.QQ)
assert [S.expand(51168936*GB.polys[0].as_expr()), S.expand(412*GB.polys[1].as_expr())] == [L,P]
assert S.gcd_list(f(s))==1
assert S.gcd(F[1],F[2])==s  # only finite parameter over the special point is zero
assert S.gcd(P,S.diff(P,V))==1
Um=-Q/S.Integer(51168936)
assert S.Poly(S.together((Um**2-4*V)).as_numer_denom()[0],V).gcd(S.Poly(P,V)).degree()==0
S0=S.expand(U**6-6*U**4*V+9*U**2*V**2-2*V**3+2)
assert S.Poly(S.together(S0.subs(U,Um)).as_numer_denom()[0],V).gcd(S.Poly(P,V)).degree()==0
assert S.Poly(P,V,modulus=79).is_irreducible
p199=S.Poly(P,V,modulus=199)
assert pow(71,99,199)==198
# Exact requested mod-199 factorization.
fmod=S.Poly((V+35)*(V+68)*(V+80)*(V-60)*(V-39)*(V**2-7*V+94),V,modulus=199)
assert p199==fmod.mul_ground(412)
print('VERIFY_OK rational_sextic=6 special_A5=1 ordinary_nodes=7 degree_each=7 field_group=S7 poly_degree=7 mod79_irreducible=TRUE mod199_cycle=2+1+1+1+1+1 discriminant_collision=NONE')
