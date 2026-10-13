from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mscale(c,A):
    return [[c*x for x in row] for row in A]

def frob2(A):
    return sum(x*x for row in A for x in row)

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

# 2x2 sharpness witness.
r=F(3,4)
M=F(2)
E=[[r,M],[F(0),r]]
E2=mm(E,E)
assert frob2(E2) > frob2(E)
assert frob2(E) == 2*r*r+M*M
assert frob2(E2) == 2*r**4+4*r*r*M*M

# Safe algebra spot checks in triangular form for |a|,|b| <= 1/2.
for a,b,z in [
    (F(1,2),F(1,2),F(7)),
    (F(1,2),F(-1,2),F(11)),
    (F(1,3),F(-1,4),F(5)),
]:
    T=[[a,z],[F(0),b]]
    assert frob2(mm(T,T)) <= frob2(T)

# 3x3 nilpotent exact-termination witness.
M=F(10)
N=[
    [F(0),M,F(0)],
    [F(0),F(0),M],
    [F(0),F(0),F(0)]
]
N2=mm(N,N)
N3=mm(N2,N)
N4=mm(N2,N2)
assert N2 == [
    [F(0),F(0),M*M],
    [F(0),F(0),F(0)],
    [F(0),F(0),F(0)]
]
assert N3 == [[F(0)]*3 for _ in range(3)]
assert N4 == [[F(0)]*3 for _ in range(3)]
assert frob2(N2)/frob2(N) == F(50)

I=eye(3)
X0=madd(I,mscale(F(-1),N))
# A=I: X_{k+1}=X_k(2I-X_k).
X1=mm(X0,madd(mscale(F(2),I),mscale(F(-1),X0)))
X2=mm(X1,madd(mscale(F(2),I),mscale(F(-1),X1)))
assert X1 == madd(I,mscale(F(-1),N2))
assert X2 == I

print("VERIFY_OK")
print("two_by_two_growth_ratio_sq", frob2(E2)/frob2(E))
print("nilpotent_frobenius_ratio_sq", frob2(N2)/frob2(N))
