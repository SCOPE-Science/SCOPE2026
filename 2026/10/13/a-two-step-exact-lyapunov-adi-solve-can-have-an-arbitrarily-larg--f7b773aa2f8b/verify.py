from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def mt(A):
    return [list(x) for x in zip(*A)]

def madd(*Ms):
    return [[sum(M[i][j] for M in Ms) for j in range(len(Ms[0][0]))] for i in range(len(Ms[0]))]

def mscale(c,A):
    return [[c*x for x in row] for row in A]

def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

I=[[F(1),F(0)],[F(0),F(1)]]
BB=[[F(0),F(0)],[F(0),F(1)]]

for M in map(F,[1,2,6,10]):
    A=[[F(-1),M],[F(0),F(-1)]]
    ApI=madd(A,I)
    AmI=madd(A,mscale(F(-1),I))
    C=mm(ApI,inv2(AmI))
    assert C==[[F(0),-M/F(2)],[F(0),F(0)]]
    assert mm(C,C)==[[F(0),F(0)],[F(0),F(0)]]

    P=[[M*M/F(4),M/F(4)],[M/F(4),F(1,2)]]
    R=madd(mm(A,P),mm(P,mt(A)),BB)
    assert R==[[F(0),F(0)],[F(0),F(0)]]

    P1=[[M*M/F(8),M/F(4)],[M/F(4),F(1,2)]]
    R1=madd(mm(A,P1),mm(P1,mt(A)),BB)
    assert R1==[[M*M/F(4),F(0)],[F(0),F(0)]]

    D=madd(P,mscale(F(-1),P1))
    assert D==[[M*M/F(8),F(0)],[F(0),F(0)]]

    P2=madd(P1,D)
    assert P2==P

# Concrete residual amplification M=6.
M=F(6)
assert M*M/F(4)==F(9)

# Scalar boundary: |(a-s)/(a+s)| < 1 for positive rational a,s.
for a in map(F,[1,2,7]):
    for s in map(F,[1,3,5]):
        q=(a-s)/(a+s)
        assert abs(q)<1

print("VERIFY_OK")
print("M6_residual_factor", F(9))
