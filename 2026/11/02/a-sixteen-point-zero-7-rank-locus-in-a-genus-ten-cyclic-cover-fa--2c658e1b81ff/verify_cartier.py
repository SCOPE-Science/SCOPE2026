#!/usr/bin/env python3
"""Exact characteristic-seven Cartier and exceptional-parameter identities."""
from math import comb
import sympy as S
p=7
u,x=S.symbols('u x')
basis=[(j,i) for j in range(1,5) for i in range((6*j)//5)]
assert len(basis)==10
# Implement the trinomial expansion as an independent integer multinomial sum.
def coeff(N,exp):
    if exp<0 or exp%3: return S.Integer(0)
    t=exp//3
    z=S.Integer(0)
    for r in range(N+1): # choices of x^6
      s=t-2*r # choices of ux^3
      if 0<=s<=N-r:
        z+=S.Integer(comb(N,r)*comb(N-r,s))*u**s
    return S.Poly(z,u, modulus=p).as_expr()
H=S.zeros(10)
for c,(j,i) in enumerate(basis):
    j2=next(l for l in range(1,5) if (7*l-j)%5==0)
    N=(7*j2-j)//5
    for r,(J,I) in enumerate(basis):
        if J==j2: H[r,c]=coeff(N,7*(I+1)-1-i)
# All H entries are the pth powers of the Cartier coefficients.
nonzero={(basis[c],basis[r]):str(H[r,c]) for r in range(10) for c in range(10) if H[r,c]}
assert len(nonzero)==9,nonzero
D=S.Poly(-2*u**4+2*u**2+3,u,modulus=p)
assert S.Poly(D.as_expr()+2*(u*u-4)**2,u,modulus=p).is_zero
U=S.Poly((3*u*u-2)*(u**14+2)-4*u**8,u,modulus=p)
fac=S.factor_list(U.as_expr(), modulus=p)
assert [S.degree(f,u) for f,e in fac[1] for _ in range(e)]==[3,3,4,6]
assert S.gcd(U,S.Poly(u*u-4,u,modulus=p)).degree()==0
assert S.gcd(U,U.diff()).degree()==0
assert S.gcd(U,D).degree()==0
# The open smooth locus has rank 7. The Cartier four-cycle has stable rank
# four if and only if the scalar U is nonzero; the matrix's other arrows
# feed nilpotent chains of length at most four.
for a in range(7):
  if (a*a-4)%7==0: continue
  M=H.subs(u,a).applyfunc(lambda y:int(y)%7)
  def rankmod(A):
    A=[[int(A[i,j])%7 for j in range(A.cols)] for i in range(A.rows)]
    z=0
    for j in range(len(A[0])):
      h=next((i for i in range(z,len(A)) if A[i][j]),None)
      if h is None:continue
      A[z],A[h]=A[h],A[z]
      v=pow(A[z][j],-1,7)
      A[z]=[(x*v)%7 for x in A[z]]
      for i in range(len(A)):
        if i!=z:
          v=A[i][j]
          if v:A[i]=[(x-v*y)%7 for x,y in zip(A[i],A[z])]
      z+=1
    return z
  assert rankmod(M)==7,(a,rankmod(M))
  A=S.eye(10)
  for n in range(10):A=(M*A).applyfunc(lambda y:int(y)%7)
  assert rankmod(A)==4,(a,rankmod(A))
print('CARTIER_SYMBOLIC_OK: genus=10, rank=7, a-number=3, exceptional polynomial degrees=3+3+4+6')
print('Exceptional Q(u) mod 7:', U.as_expr())
print('Factorization:',[(str(f),e) for f,e in fac[1]])
print('Small field sanity: smooth a in F7 all p-rank 4')
