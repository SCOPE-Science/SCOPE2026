#!/usr/bin/env python3
"""Exact independent replay of the Hessian intersection on the characteristic-7 Klein quartic.
Requires sympy. Run: python verify.py
"""
from sympy import symbols, Poly, groebner, hessian, Matrix, diff, factor, expand
from itertools import product
x,y,z,u,v=symbols('x y z u v')
p=7
F=x**3*y+y**3*z+z**3*x
H=Poly(hessian(F,(x,y,z)).det(),x,y,z,modulus=p)
h=x**5*z+2*x**2*y**2*z**2+x*y**5+y*z**5
assert H==Poly(-54*h,x,y,z,modulus=p)
fa=F.subs(x,1); ha=h.subs(x,1)
G=groebner([fa,ha],y,z,order='lex',modulus=p)
assert G.is_zero_dimensional
Gexpect=[y**2+3*y*z**3-2*z**13-2*z**6,
         y*z**7+3*y-2*z**10+z**3,
         z**15-z**8+2*z]
assert [Poly(g,y,z,modulus=p) for g in G.polys]==[Poly(g,y,z,modulus=p) for g in Gexpect]
assert Poly(z**15-z**8+2*z,z,modulus=p)==Poly(z*(z-4)**14,z,modulus=p)
# For Groebner lead monomials (y², yz⁷, z¹⁵), standard monomials number 15+7=22.
assert sum(1 for i in range(2) for j in range(15) if not(i and j>=7))==22
assert Poly(fa.subs(z,4),y,modulus=p).eval(2)==0
assert Poly(ha.subs(z,4),y,modulus=p).eval(2)==0
assert Poly(fa.subs(z,4),y,modulus=p).eval(3)==0
assert Poly(ha.subs(z,4),y,modulus=p).eval(3)!=0
assert Poly(fa.subs(z,0),y,modulus=p)==Poly(y,y,modulus=p)
assert Poly(ha.subs(z,0),y,modulus=p)==Poly(y**5,y,modulus=p)
# Local algebra at cusp (u,v)=(0,0), where y=u+2,z=v+4.
fc=Poly(fa.subs({y:u+2,z:v+4}),u,v,modulus=p).as_expr()
hc=Poly(ha.subs({y:u+2,z:v+4}),u,v,modulus=p).as_expr()
def colength(polys):
    B=groebner(polys,u,v,order='lex',modulus=p)
    leaders=[Poly(q,u,v,modulus=p).LM(order='lex').exponents for q in B.polys]
    a=min(i for i,j in leaders if j==0)
    b=min(j for i,j in leaders if i==0)
    return sum(1 for i in range(a) for j in range(b) if not any(i>=s and j>=t for s,t in leaders))
lengths=[0]
for k in range(1,15):
    lengths.append(colength([fc,hc]+[u**i*v**(k-i) for i in range(k+1)]))
assert lengths==[0,1,3,5,7,9,11,13,15,16,17,18,19,20,21], lengths
hilbert=[lengths[k+1]-lengths[k] for k in range(14)]
assert hilbert==[1,2,2,2,2,2,2,2,1,1,1,1,1,1],hilbert
# The remaining three coordinate points have length 1, by independent chart orders;
# F=0 near [1:0:0] gives y=-y³z-z³, so h=z+ O(m²).
# Cyclic symmetry transfers this to [0:1:0] and [0:0:1].
# On their tangent coordinate line F has vanishing order exactly three.
assert Poly(F.subs(y,0),x,z,modulus=p)==Poly(x*z**3,x,z,modulus=p)
assert Poly(F.subs(z,0),x,y,modulus=p)==Poly(x**3*y,x,y,modulus=p)
assert Poly(F.subs(x,0),y,z,modulus=p)==Poly(y**3*z,y,z,modulus=p)
assert sum(hilbert)==21 and 21+3==4*6
print('VERIFY_OK: Hessian, Groebner basis, support, local Hilbert function, Bezout, flex contacts')
