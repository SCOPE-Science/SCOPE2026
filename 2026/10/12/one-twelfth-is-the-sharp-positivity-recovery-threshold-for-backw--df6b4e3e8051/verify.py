from fractions import Fraction as F
from decimal import Decimal, getcontext

def invert(A):
    n=len(A)
    M=[row[:] + [F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        piv=next(i for i in range(col,n) if M[i][col] != 0)
        M[col],M[piv]=M[piv],M[col]
        q=M[col][col]
        M[col]=[x/q for x in M[col]]
        for i in range(n):
            if i==col: continue
            q=M[i][col]
            if q:
                M[i]=[x-q*y for x,y in zip(M[i],M[col])]
    return [row[n:] for row in M]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

# Four-point periodic exact witness.
N=4
W=[[F(0) for _ in range(N)] for _ in range(N)]
D=[[F(0) for _ in range(N)] for _ in range(N)]
for i in range(N):
    W[i][i]+=F(10,12)
    W[i][(i-1)%N]+=F(1,12)
    W[i][(i+1)%N]+=F(1,12)
    D[i][i]+=-2
    D[i][(i-1)%N]+=1
    D[i][(i+1)%N]+=1

sigma=F(1,100)
A=[[W[i][j]-sigma*D[i][j] for j in range(N)] for i in range(N)]
B=matmul(invert(A),W)
col0=[B[i][0] for i in range(N)]
assert col0 == [F(13217,13568),F(3,212),F(-33,13568),F(3,212)]
assert sum(col0)==1
assert col0[2] < 0

# Exact algebra behind the threshold.
for sigma in [F(1,1000),F(1,100),F(1,24),F(1,13)]:
    a=F(5,6)+2*sigma
    b=F(1,12)-sigma
    assert b > 0
    assert 10-a/b == -144*sigma/(1-12*sigma)

# Exact M-matrix margin at and above the threshold.
for sigma in [F(1,12),F(1,10),F(1,2),F(3)]:
    a=F(5,6)+2*sigma
    b=F(1,12)-sigma
    assert b <= 0
    assert a-2*abs(b) == 1

# Representative infinite-lattice sign replay using high precision.
getcontext().prec=60
for sn,sd in [(1,1000),(1,100),(1,24),(1,13)]:
    s=Decimal(sn)/Decimal(sd)
    a=Decimal(5)/Decimal(6)+2*s
    b=Decimal(1)/Decimal(12)-s
    disc=(a*a-4*b*b).sqrt()
    r=(-a+disc)/(2*b)
    C=1/disc
    k2=C*r*(1+10*r+r*r)/Decimal(12)
    closed=-Decimal(12)*C*s*r*r/(1-Decimal(12)*s)
    assert abs(k2-closed) < Decimal("1e-50")
    assert Decimal(-1) < r < 0
    assert k2 < 0

print("VERIFY_OK")
