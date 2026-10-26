"""Exact GF(5) elimination certificate for bitangent fields of the Klein quartic."""
import sympy as sp
u,v,x,y=sp.symbols('u v x y')
A=u**3
B=1+3*u**2*v
C=3*u*v**2
D=u+v**3
E=v
P=sp.expand(8*A*A*D-4*A*B*C+B**3)
Q=sp.expand(64*A**3*E-(4*A*C-B**2)**2)
factors=[u+1,u**3+u**2+1,
         u**6-2*u**4+u**3+u**2+u+1,
         u**6-2*u**5+u**3+2*u**2+u+1,
         u**6+u**5-u**3-u**2-2*u+1,
         u**6-u**5+u**4-u**3+u**2-u+1]
H=sp.prod(factors)
R=sp.resultant(P,Q,v)
assert sp.Poly(R+4096*u**24*H,u,modulus=5).is_zero
assert [sp.degree(z,u) for z in factors]==[1,3,6,6,6,6]
assert all(sp.Poly(z,u,modulus=5).is_irreducible for z in factors)
assert sp.Poly(H,u,modulus=5).degree()==28
assert sp.Poly(H,u,modulus=5).gcd(sp.Poly(sp.diff(H,u),u,modulus=5)).degree()==0
pts=[(i,j) for i in range(1,5) for j in range(5)
     if int(P.subs({u:i,v:j}))%5==0 and int(Q.subs({u:i,v:j}))%5==0]
assert pts == [(4,4)],pts
assert sp.expand(x**3*y+y**3*(-x-y)+(-x-y)**3*x+(x*x+x*y+y*y)**2)==0
print('VERIFY_OK; irreducible orbit degrees 1,3,6,6,6,6; GF5 bitangent (u,v)=(-1,-1)')
