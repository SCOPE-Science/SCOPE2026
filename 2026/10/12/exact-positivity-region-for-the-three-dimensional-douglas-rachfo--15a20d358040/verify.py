from fractions import Fraction as F
from decimal import Decimal, getcontext

def matmul(A,B):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(q)) for j in range(m)] for i in range(n)]

def kron(A,B):
    return [[A[i//len(B)][j//len(B[0])] * B[i%len(B)][j%len(B[0])]
             for j in range(len(A[0])*len(B[0]))]
            for i in range(len(A)*len(B))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def add(*Ms):
    n=len(Ms[0]); m=len(Ms[0][0])
    return [[sum(M[i][j] for M in Ms) for j in range(m)] for i in range(n)]

def scale(c,A):
    return [[c*x for x in row] for row in A]

# Exact n=2 directional resolvent at s=7/25.
s=F(7,25)
den=F(1)+4*s+3*s*s
d=(1+2*s)/den
o=s/den
assert d == F(975,1472)
assert o == F(175,1472)
P=[[d,o],[o,d]]
I2=eye(2)

Px=kron(kron(P,I2),I2)
Py=kron(kron(I2,P),I2)
Pz=kron(kron(I2,I2),P)
I8=eye(8)

Pxy=matmul(Px,Py)
Pxz=matmul(Px,Pz)
Pyz=matmul(Py,Pz)
Pxyz=matmul(Pxy,Pz)
R=add(I8, scale(F(3),Pxyz), scale(F(-1),Pxy), scale(F(-1),Pxz), scale(F(-1),Pyz))

mn=min(x for row in R for x in row)
assert mn == F(-3241875,3189506048)

# The same value comes from an exactly-one-coordinate-difference entry.
critical=o*(3*d*d-2*d)
assert critical == mn

# Exact n=2 threshold:
# D2 - (3/2)D1 = 3s^2 + s - 1/2.
# Positive root is (sqrt(7)-1)/6.
getcontext().prec=60
sqrt7=Decimal(7).sqrt()
tau2=(sqrt7-Decimal(1))/Decimal(6)
poly=lambda x: Decimal(3)*x*x+x-Decimal(1)/Decimal(2)
assert abs(poly(tau2)) < Decimal("1e-55")

def D(n,x):
    a=Decimal(1)
    if n==0: return a
    b=Decimal(1)+Decimal(2)*x
    if n==1: return b
    for k in range(2,n+1):
        a,b=b,(Decimal(1)+Decimal(2)*x)*b-x*x*a
    return b

def f(n,x):
    return D(n,x)-Decimal(3)*D(n-1,x)/Decimal(2)

def tau(n):
    lo=Decimal(0)
    hi=Decimal(1)
    for _ in range(220):
        mid=(lo+hi)/2
        if f(n,mid) <= 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

vals=[tau(n) for n in range(2,9)]
for a,b in zip(vals,vals[1:]):
    assert a < b

limit=(Decimal(3)-Decimal(6).sqrt())/Decimal(2)
assert vals[-1] < limit
assert limit-vals[-1] < Decimal("1e-7")
assert abs(vals[0]-tau2) < Decimal("1e-50")

# A safe rational step below tau2 has no negative entries.
s0=F(1,4)
den0=F(1)+4*s0+3*s0*s0
d0=(1+2*s0)/den0
o0=s0/den0
P0=[[d0,o0],[o0,d0]]
X=kron(kron(P0,I2),I2)
Y=kron(kron(I2,P0),I2)
Z=kron(kron(I2,I2),P0)
R0=add(I8, scale(F(3),matmul(matmul(X,Y),Z)),
       scale(F(-1),matmul(X,Y)), scale(F(-1),matmul(X,Z)),
       scale(F(-1),matmul(Y,Z)))
assert min(x for row in R0 for x in row) >= 0

print("VERIFY_OK")
print("min_bad_entry", mn)
print("tau2", tau2)
print("limit", limit)
