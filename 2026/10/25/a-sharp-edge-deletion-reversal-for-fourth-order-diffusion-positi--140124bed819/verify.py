"""Exact checks for fourth-order diffusion on crown graphs; Python 3 + SymPy."""
from fractions import Fraction as F
from math import factorial
import sympy as s

n,h=s.symbols('n h', integer=True, positive=True)
R=lambda x: 1-x+x**2/s.Integer(2)-x**3/s.Integer(6)+x**4/s.Integer(24)
a,b,c=R(n*h),R((n-2)*h),R(2*(n-1)*h)
edge=s.factor((1-c-a+b)/(2*n))
within=s.factor((1+c-a-b)/(2*n))
paired=s.factor((1-c+(n-1)*(a-b))/(2*n))
diag=s.factor((1+c+(n-1)*(a+b))/(2*n))
m,z=s.symbols('m z',positive=True)
A=(2*m*m-m+1)/(6*m*m)
expect_edge=h*((1-z)*(1+A*z*z)+z*z/3)
expect_within=h*h*(n-2)*((7*(n-1)**2+1)*h*h-12*(n-1)*h+12)/24
expect_pair=h**3*(n-2)*(n-1)*(1-(n-1)*h)/6
assert s.simplify(edge.subs({n:m+1,h:z/m})-expect_edge.subs(h,z/m))==0
assert s.simplify(within-expect_within)==0
assert s.simplify(paired-expect_pair)==0
assert s.simplify(s.discriminant((7*m*m+1)*z*z-12*m*z+12,z) + 48*(4*m*m+1))==0
q=s.symbols('q'); Q=q**3-4*q**2+12*q-24
assert Q.subs(q,s.Rational(8,3))==-s.Rational(40,27) and Q.subs(q,3)==3
assert s.discriminant(s.diff(Q,q),q)<0


def mul(A,B):
 N=len(A)
 return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def direct_L(n):
 N=2*n
 L=[[F(0) for _ in range(N)] for _ in range(N)]
 for i in range(n):
  for j in range(n):
   if i!=j:
    L[i][n+j]=L[n+j][i]=-F(1)
 for i in range(N):L[i][i]=F(n-1)
 return L


def RK4(L,h):
 N=len(L)
 T=[[F(int(i==j)) for j in range(N)] for i in range(N)]
 P=[[F(int(i==j)) for j in range(N)] for i in range(N)]
 X=[[-h*L[i][j] for j in range(N)] for i in range(N)]
 for k in range(1,5):
  P=mul(P,X)
  for i in range(N):
   for j in range(N):T[i][j]+=P[i][j]/factorial(k)
 return T

checks=0
for N in range(3,12):
 L=direct_L(N)
 H=F(1,N-1)
 for h0 in [F(0),H/3,H*F(3,4),H,H*F(5,4)]:
  T=RK4(L,h0)
  aa=F(1)-N*h0+(N*h0)**2/F(2)-(N*h0)**3/F(6)+(N*h0)**4/F(24)
  bb=F(1)-(N-2)*h0+((N-2)*h0)**2/F(2)-((N-2)*h0)**3/F(6)+((N-2)*h0)**4/F(24)
  cc=F(1)-2*(N-1)*h0+(2*(N-1)*h0)**2/F(2)-(2*(N-1)*h0)**3/F(6)+(2*(N-1)*h0)**4/F(24)
  val_diag=(1+cc+(N-1)*(aa+bb))/F(2*N)
  val_edge=(1-cc-aa+bb)/F(2*N)
  val_within=(1+cc-aa-bb)/F(2*N)
  val_paired=(1-cc+(N-1)*(aa-bb))/F(2*N)
  for i in range(2*N):
   for j in range(2*N):
    if i==j: val=val_diag
    elif i//N==j//N:val=val_within
    elif i%N==j%N:val=val_paired
    else:val=val_edge
    assert T[i][j]==val,(N,h0,i,j,T[i][j],val)
    checks+=1
  assert all(T[i][j]>=0 for i in range(2*N) for j in range(2*N)) == (h0<=H)
  if h0==H:
   assert val_paired==0 and val_edge>0 and val_within>0 and val_diag>0
  if h0>H:assert val_paired<0
print('VERIFY_OK:',3,'symbolic orbit identities; nonnegativity certificates; ',checks,'exact direct matrix entries for n=3..11, 5 steps per n')
