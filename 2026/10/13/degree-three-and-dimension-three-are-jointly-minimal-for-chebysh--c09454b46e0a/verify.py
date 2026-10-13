from fractions import Fraction as F

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def scale(c, A):
    return [[c * v for v in row] for row in A]

I = [[F(int(i == j)) for j in range(3)] for i in range(3)]
A = [[F(1), F(0), F(0)], [F(0), F(79,20), F(-1,20)], [F(0), F(-1,20), F(79,20)]]
b = [F(1), F(1), F(1,1000)]
a, c = F(79,20), F(-1,20)
assert sorted([F(1), a+c, a-c]) == [F(1), F(39,10), F(4)]
A2 = matmul(A, A)
Q3 = scale(F(2,365), add(add(scale(F(16), A2), scale(F(-120), A)), scale(F(273), I)))
x3 = matvec(Q3, b)
assert x3 == [F(338,365), F(304248,1140625), F(-6783,4562500)]
assert x3[0] > 0 and x3[1] > 0 and x3[2] < 0
x_exact = [F(1), F(6077,24000), F(83,24000)]
assert all(v > 0 for v in x_exact)
assert matvec(A, x_exact) == b
assert Q3[1][1] == F(2434,9125) and Q3[1][2] == F(-16,9125)
assert Q3[2][1] == F(-16,9125) and Q3[2][2] == F(2434,9125)
print('VERIFY_OK')
