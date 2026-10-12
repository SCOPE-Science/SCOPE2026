from fractions import Fraction as F

A=[[F(9),F(0)],[F(0),F(1)]]
B=[[F(1,9),F(-1,6)],[F(-1,6),F(1)]]

def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

I=[[F(1),F(0)],[F(0),F(1)]]
AB=mm(A,B)
T=[[I[i][j]-AB[i][j] for j in range(2)] for i in range(2)]
assert T == [[F(0),F(3,2)],[F(1,6),F(0)]]

# B is SPD: positive first diagonal and determinant.
assert B[0][0] > 0
assert B[0][0]*B[1][1]-B[0][1]*B[1][0] == F(1,12) > 0

# C = A^(1/2) B A^(1/2), with sqrt(A)=diag(3,1).
S=[[F(3),F(0)],[F(0),F(1)]]
C=mm(mm(S,B),S)
assert C == [[F(1),F(-1,2)],[F(-1,2),F(1)]]
assert C[0][0]+C[1][1] == F(2)
assert C[0][0]*C[1][1]-C[0][1]*C[1][0] == F(3,4)

# Exact amplification on e2.
e2=[F(0),F(1)]
Te2=[T[0][1],T[1][1]]
assert Te2 == [F(3,2),F(0)]
assert sum(x*x for x in Te2) == F(9,4)

# delta*sqrt(kappa)=1/2*3=3/2.
assert F(1,2)*F(3) == F(3,2)

print("VERIFY_OK")
