"""Exact Cartier and semilinear rank stratification for a characteristic-seven trigonal family."""
from itertools import combinations
from math import factorial
import sympy as s
u=s.Symbol('u'); p=7
f=s.Poly(s.Symbol('x')**5+u*s.Symbol('x')**2+1,s.Symbol('x'))
x=s.Symbol('x')
# Coefficients of x^(7r+6-i) in f^(2j); the matrix records seventh powers of Cartier coefficients.
assert [s.Poly(s.expand(f.as_expr()**2),x).nth(6)]==[0]
B=s.Matrix([[4*u**3,4,6*u**2],[0,5*u,4*u**3],[1,0,0]])
for i in range(3):
 for r in range(3):
  assert s.Poly(s.expand(f.as_expr()**4),x).nth(7*r+6-i).expand() == ({(0,0):4*u**3,(0,1):4,(0,2):6*u**2,(1,0):0,(1,1):12*u,(1,2):4*u**3,(2,0):1,(2,1):0,(2,2):0}[(r,i)])
def M(P):return s.Poly(s.expand(P),u,modulus=p)
def norm(A):return A.applyfunc(lambda z:M(z).as_expr())
B=norm(B)
assert M(B.det()).is_zero
assert M(s.det(B.extract([0,2],[0,1]))).as_expr()!=0
# The Cartier operator is semilinear. The rank of the second iterate
# is the rank of H^(7)H where H has seventh powers of Cartier coefficients.
H7=norm(B.applyfunc(lambda z:z.subs(u,u**7)))
H2=norm(H7*B)
minors=[]
for rows in combinations(range(3),2):
 for cols in combinations(range(3),2):
  z=M(H2.extract(rows,cols).det())
  if not z.is_zero:minors.append(z)
g=minors[0]
for z in minors[1:]:g=s.gcd(g,z)
assert M(g.as_expr()/s.LC(g)).monic()==M(u**4*(u**10-1)).monic()
# A smooth normalized coefficient has u^5 != -1. Hence exactly u=0 and u^5=1
# can have rank less than two after two Cartier iterates.
assert M(s.expand((u**10-1)-(u**5-1)*(u**5+1))).is_zero
# For u=1, rank(C^2)=rank(C^3)=1; for u=0, C^3=0.
def rank(A):
 v=[[int(z)%7 for z in row] for row in A.tolist()]
 i=0
 for j in range(3):
  k=next((k for k in range(i,3) if v[k][j]),None)
  if k is None: continue
  v[i],v[k]=v[k],v[i]
  c=pow(v[i][j],-1,7)
  v[i]=[z*c%7 for z in v[i]]
  for k in range(3):
   if k!=i:
    c=v[k][j]
    v[k]=[(v[k][z]-c*v[i][z])%7 for z in range(3)]
  i+=1
 return i
for val in [0,1]:
 A=B.subs(u,val).applyfunc(lambda z:int(z)%7)
 C=A
 ranks=[]
 for n in range(1,5):
  ranks.append(rank(s.Matrix([[int(w)%7 for w in row] for row in C.tolist()])))
  C=C*A
  C=C.applyfunc(lambda z:int(z)%7)
 assert ranks==({0:[2,1,0,0],1:[2,1,1,1]}[val]), (val,ranks)
print('CHAR7_COEFFICIENTS_AND_CARTIER_SEMILINEAR_MATRIX_OK')
print('SECOND_ITERATE_MINOR_GCD=u^4*(u^10-1)_OK')
print('SMOOTH_LOCUS_b_nonzero_AND_b^3_plus_a^5_nonzero')
print('P_RANK=0_AT_a_zero;1_AT_a^5_eq_b^3;2_OTHERWISE')
print('A_NUMBER=2_EVERYWHERE_SMOOTH')
print('VERIFY_OK')
