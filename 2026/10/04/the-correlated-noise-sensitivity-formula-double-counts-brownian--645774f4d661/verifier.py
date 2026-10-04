from fractions import Fraction as F


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def tr(A):
    return [list(x) for x in zip(*A)]

def eq(A,B):
    return A==B

def diag(vals):
    n=len(vals)
    return [[vals[i] if i==j else F(0) for j in range(n)] for i in range(n)]

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

I=diag([F(1),F(1),F(1)])
Fm=diag([F(-1),F(-1),F(-1)])
G=diag([F(1),F(2),F(3)])
R=[[F(1),F(1,2),F(1,4)],
   [F(1,2),F(1),F(1,3)],
   [F(1,4),F(1,3),F(1)]]
assert det3(R)>0
GG=matmul(G,tr(G))
Q=matmul(matmul(G,R),tr(G))
# For F=-I, the exact stationary covariance is one half of the diffusion covariance.
Wcorr=scale(F(1,2),Q)
Lcorr=add(add(matmul(Fm,Wcorr),matmul(Wcorr,tr(Fm))),Q)
assert eq(Lcorr, [[F(0)]*3 for _ in range(3)])
# The printed source-style forcing adds GG^T to Q, so its covariance differs by (1/2)GG^T here.
Wprinted=scale(F(1,2),add(GG,Q))
assert eq(add(Wprinted,scale(F(-1),Wcorr)), scale(F(1,2),GG))
Lprinted=add(add(matmul(Fm,Wprinted),matmul(Wprinted,tr(Fm))),add(GG,Q))
assert eq(Lprinted, [[F(0)]*3 for _ in range(3)])
# Independent limit: Q=GG^T, so printed covariance is exactly twice the correct one.
Qind=matmul(matmul(G,I),tr(G))
Wind=scale(F(1,2),Qind)
Wprinted_ind=scale(F(1,2),add(GG,Qind))
assert eq(Qind,GG)
assert eq(Wprinted_ind,scale(F(2),Wind))
print('VERIFY_OK')
