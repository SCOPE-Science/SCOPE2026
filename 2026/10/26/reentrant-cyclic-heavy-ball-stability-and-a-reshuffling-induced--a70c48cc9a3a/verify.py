"""Exact rational reproducibility checks for the two-loss heavy-ball theorem.

Run: python3 verify.py. Uses only the Python standard library.
Analytical inequalities and universal quantifiers are established in RESULT.md.
"""
from fractions import Fraction as F

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def trans(A):return [[A[j][i] for j in range(2)] for i in range(2)]
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def trace(A):return A[0][0]+A[1][1]
def T(c,h,b):return [[1+b-h*c,-b],[F(1),F(0)]]

def scaleadd(A,B):return [[(A[i][j]+B[i][j])/2 for j in range(2)] for i in range(2)]

# Source algorithm: x_{j+1}=(1+beta-eta*c)x_j-beta*x_{j-1}.
a,b,eta,beta=F(1),F(10),F(31,20),F(1,2)
P=mul(T(b,eta,beta),T(a,eta,beta))
Q=mul(T(a,eta,beta),T(b,eta,beta))
assert P==[[F(1,5),F(7)],[-F(1,20),-F(1,2)]]
assert Q==[[F(1,5),F(1,40)],[-F(14),-F(1,2)]]
assert trace(P)==trace(Q)==-F(3,10)
assert det(P)==det(Q)==F(1,4)
# Discriminant -91/100: eigenvalues (-3 +/- sqrt(91) i)/20, modulus 1/2.
assert trace(P)**2-4*det(P)==-F(91,100)
K=scaleadd(mul(trans(P),P),mul(trans(Q),Q))
assert K==[[F(78433,800),F(843,200)],[F(843,200),F(79201,3200)]]
D=[[K[i][j]-(F(49,2) if i==j else F(0)) for j in range(2)] for i in range(2)]
assert D[0][0]==F(58833,800)
assert det(D)==F(1643697,2560000)>0
assert D[0][0]>0 and D[1][1]>0

# Check symbolic formulas on an extensive rational set; proof is separately analytic.
checks=0
for a0 in range(1,9):
 for b0 in range(1,9):
  for beta0 in [F(0),F(1,4),F(1,2),F(3,4)]:
   for eta0 in [F(1,100),F(1,5),F(1,2),F(1),F(3,2),F(3)]:
    A,B,be,h=F(a0),F(b0),beta0,eta0
    U=mul(T(B,h,be),T(A,h,be));V=mul(T(A,h,be),T(B,h,be))
    tau=1+be*be-h*(1+be)*(A+B)+h*h*A*B
    assert trace(U)==trace(V)==tau
    assert det(U)==det(V)==be*be
    assert 1+be*be-tau==h*((1+be)*(A+B)-h*A*B)
    assert 1+be*be+tau==A*B*h*h-(1+be)*(A+B)*h+2*(1+be*be)
    checks+=1
print(f'VERIFY_OK exact frozen-order matrices, complex roots, mean-square divergence certificate; {checks} rational trace/determinant cases')
