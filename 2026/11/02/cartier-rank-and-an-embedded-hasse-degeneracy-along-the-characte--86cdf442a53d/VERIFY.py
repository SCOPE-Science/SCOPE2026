#!/usr/bin/env python3
"""Reproducible polynomial Cartier coefficient and rank verification."""
import math
from collections import Counter
from sympy import Poly, symbols, expand, Matrix
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import GF

x,u,a,b,c = symbols('x u a b c')
variables=(u,a,b,c)
p=5
basis=[(i,j) for j in range(4) for i in range(4) if 5*i+6*j <= 18]
assert basis==[(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)]
f=x**6+u*x**4+a*x**3+b*x**2+c*x
M=Matrix.zeros(10)
for col,(i,j) in enumerate(basis):
    for t in range(j+1):
        fac=(-1)**(j-t)*math.comb(j,t)
        for (power,),co in Poly(expand(x**i*f**(j-t)),x).terms():
            if power % 5 == 4:
                target=((power-4)//5,t)
                assert target in basis
                M[basis.index(target),col]+=fac*co
M=M.applyfunc(lambda z:Poly(z,*variables,modulus=5).as_expr())
nonzero={(i,j):M[i,j] for i in range(10) for j in range(10) if M[i,j]!=0}
expected={(0,4):-u,(0,5):-a,(0,6):-b,
 (0,7):2*a*c+b**2,(0,8):2*b*c,(0,9):2*b*c**2,
 (1,7):2*a,(1,8):2*b+u**2,(1,9):-a**3-a*b*u-b*c+2*c*u**2,
 (2,9):2*b+2*u**2,(4,7):-2*u,(4,8):-2*a,
 (4,9):a*c-2*b**2,(5,9):a,(7,9):2*u}
assert set(nonzero)==set(expected)
for ij,z in expected.items():
    assert Poly(M[ij]-z,*variables,modulus=5).is_zero,ij
P=a*a-u*b+2*u**3
T=Matrix([[M[1,7],M[1,8]],[M[4,7],M[4,8]]])
assert Poly(T.det()-P,*variables,modulus=5).is_zero
# Exhaustively check all 125 distinct coefficient triples; c cannot influence rank.
counts=Counter()
for uu in range(5):
 for aa in range(5):
  for bb in range(5):
   cc=3
   rows=[[int(M[i,j].subs({u:uu,a:aa,b:bb,c:cc}))%5 for j in range(10)] for i in range(10)]
   rank=DomainMatrix.from_list(rows,GF(5)).rank()
   pp=(aa*aa-uu*bb+2*uu**3)%5
   prediction=0 if (uu,aa,bb)==(0,0,0) else (3 if pp==0 else 4)
   assert rank==prediction,(uu,aa,bb,rank,prediction)
   counts[rank]+=1
assert counts=={0:1,3:24,4:100},counts
# The nonzero 4-by-4 minors must use row 0, exactly one of cols4,5,6,
# cols7,8,9, rows1 and4, and one of rows2,5,7.
for first_col,z in [(4,-u),(5,-a),(6,-b)]:
 for third_row,w in [(2,2*b+2*u*u),(5,a),(7,2*u)]:
  minor=M.extract([0,1,4,third_row],[first_col,7,8,9])
  assert Poly(minor.det()-z*P*w,*variables,modulus=5).is_zero
# These nine minors generate (P)*(u,a,b)*(a,b+u^2,u)=(P)*(u,a,b)^2.
print('VERIFY_OK: polynomial Cartier coefficient matrix (15 entries), 4x4 minors, GF5 125 triples; rank counts 0:1 3:24 4:100')
