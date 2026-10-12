from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

A=[[F(1),-F(1,10),F(0)],[-F(1,10),F(8,5),-F(1,10)],[F(0),-F(1,10),F(8,5)]]
I=eye(3)
B=sub(scale(F(2),I),A)
assert A[0][0] == 1 and det2([row[:2] for row in A[:2]]) == F(159,100) and det3(A) == F(1267,500)
assert B[0][0] == 1 and det2([row[:2] for row in B[:2]]) == F(39,100) and det3(B) == F(73,500)
Ainv=[[F(1275,1267),F(80,1267),F(5,1267)],[F(80,1267),F(800,1267),F(50,1267)],[F(5,1267),F(50,1267),F(795,1267)]]
assert mm(A,Ainv)==I
assert all(x>0 for row in Ainv for x in row)
X0=I
X1=mm(X0,sub(scale(F(2),I),mm(A,X0)))
X2=mm(X1,sub(scale(F(2),I),mm(A,X1)))
expected1=[[F(1),F(1,10),F(0)],[F(1,10),F(2,5),F(1,10)],[F(0),F(1,10),F(2,5)]]
expected2=[[F(251,250),F(39,500),-F(1,500)],[F(39,500),F(267,500),F(9,100)],[-F(1,500),F(9,100),F(67,125)]]
assert X1==expected1
assert X2==expected2
assert X2[0][2]==-F(1,500)
R0=sub(I,mm(A,X0))
R1=sub(I,mm(A,X1))
R2=sub(I,mm(A,X2))
assert R1==mm(R0,R0)
assert R2==mm(R1,R1)
print('VERIFY_OK')
