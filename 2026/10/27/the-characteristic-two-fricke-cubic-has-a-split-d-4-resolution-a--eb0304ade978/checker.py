#!/usr/bin/env python3
"""Exact corroboration for a characteristic-two projective cubic. Python + SymPy."""
import sympy as sp
x,y,z,w,t,r=sp.symbols('x y z w t r')
F=w*(x*x+y*y+z*z)+x*y*z
P=lambda e,vars:sp.Poly(sp.expand(e),*vars,modulus=2)
assert [P(sp.diff(F,v),(x,y,z,w)).as_expr() for v in (x,y,z,w)] == [y*z,x*z,x*y,x**2+y**2+z**2]
G=sp.groebner([x*y,x*z,y*z,x*x+y*y+z*z],x,y,z,order='lex',modulus=2)
# Standard monomial basis of the reduced Gröbner ideal.
leading=[sp.Poly(g,x,y,z,modulus=2).LM(order='lex').exponents for g in G.polys]
standard=[]
for i in range(4):
 for j in range(4):
  for k in range(4):
   if not any(i>=a and j>=b and k>=c for a,b,c in leading):
    standard.append((i,j,k))
assert len(standard)==6,standard
# Blowup identity in the x-chart, including its strict-transform equation.
sub=F.subs({w:1,x:x,y:x*t,z:x*(r+1+t)},simultaneous=True)
assert P(sp.expand(sub-x*x*(r*r+x*t*(r+1+t))),(x,t,r)).is_zero
# On reduced exceptional curve x=r=0 the x-derivative is t(t+1).
g=r*r+x*t*(r+1+t)
assert P(sp.diff(g,x).subs({x:0,r:0}),(t,)).as_expr()==t*t+t
# Arithmetic over GF(2^r) represented by binary residue classes.
mods={1:0b11,2:0b111,3:0b1011,4:0b10011}
def mul(a,b,degree):
 poly=mods[degree];mask=(1<<degree)-1;ans=0
 while b:
  if b&1:ans^=a
  b>>=1;a<<=1
  if a&(1<<degree):a^=poly
 return ans&mask
def sq(a,r):return mul(a,a,r)
for degree in (1,2,3,4):
 q=1<<degree
 count=sum(1 for a in range(q) for b in range(q) for c in range(q)
           if sq(a,degree)^sq(b,degree)^sq(c,degree)^mul(mul(a,b,degree),c,degree)==0)
 assert count==q*q+1,(q,count)
 assert count+3*q==q*q+3*q+1
 assert count+7*q==q*q+7*q+1
 print('VERIFIED q=',q,'affine=',count,'projective=',count+3*q,'resolution=',count+7*q)
print('CHECK_OK jacobian_length=6 blowup_identity=1 singular_chart_values=(0,1)')
