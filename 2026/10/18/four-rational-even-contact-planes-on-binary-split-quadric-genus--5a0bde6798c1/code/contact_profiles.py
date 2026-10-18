#!/usr/bin/env python3
"""Exact even-contact multiplicity profiles for three extremal representatives."""
import census_genus4_tritangents as c
import sympy as S
import ast


def restrict_smooth(F,M):
 a,b,d,e=M
 r=e|(b<<1);w=d|(a<<1)
 h=0
 for i in range(4):
  for j in range(4):
   if F>>(4*i+j)&1:
    h^=c.prod_bin(1<<i,c.prod_bin(c.bin_power(r,j),c.bin_power(w,3-j)))
 assert not h&0b101010
 return sum(1<<(k//2) for k in (0,2,4,6) if h>>k&1)


def profile_smooth(F,M):
 G=restrict_smooth(F,M)
 z=S.Symbol('z');g=sum(z**i for i in range(4) if G>>i&1)
 poly=S.Poly(g,z,modulus=2)
 fin=S.gcd(poly,poly.diff()).degree()
 inf=3-poly.degree()
 if fin==0 and inf<=1:return '2+2+2'
 if fin==2 or inf==3:return '6'
 return '4+2'


def fiber_cubic(F,pt,which):
 x,t=pt
 vals=[]
 for j in range(4):
  if which=='y':
   vals.append(sum(((F>>(4*i+j))&1)*x**i*t**(3-i) for i in range(4))%2)
  else:
   vals.append(sum(((F>>(4*j+i))&1)*x**i*t**(3-i) for i in range(4))%2)
 return sum((b<<i) for i,b in enumerate(vals))


def local_q_root_same(f,pt):
 x,t=pt
 L={(1,0):1,(0,1):2,(1,1):3}[pt]
 possible=[]
 for q in (1,2,3):
  if c.prod_bin(L,c.prod_bin(q,q))==f:
   possible.append(q)
 assert len(possible)==1,(f,pt,possible)
 q=possible[0]
 # q = (q&2)*r + (q&1)*w
 return (((q>>1)&1)*x+((q)&1)*t)%2==0


def profile_reducible(F,px,py):
 fy=fiber_cubic(F,px,'y');fx=fiber_cubic(F,py,'x')
 p_y=local_q_root_same(fy,py)
 p_x=local_q_root_same(fx,px)
 assert not(p_y and p_x)
 return '4+2' if p_y or p_x else '2+2+2'

if __name__=='__main__':
 for F in [0x29e3,0x2de6,0x7889]:
  prof=[]
  for name in c.tritangents(F):
   if name.startswith('smooth_'):
    M=ast.literal_eval(name[len('smooth_'):]);typ=profile_smooth(F,M)
   else:
    pair=ast.literal_eval(name[len('reducible_'):]);typ=profile_reducible(F,*pair)
   prof.append((name,typ))
  print(hex(F),prof)
