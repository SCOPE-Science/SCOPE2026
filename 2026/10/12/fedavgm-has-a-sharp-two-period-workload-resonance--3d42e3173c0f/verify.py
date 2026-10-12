from fractions import Fraction
import math
import random

def matmul(A,B):
    return (
        (A[0][0]*B[0][0]+A[0][1]*B[1][0],
         A[0][0]*B[0][1]+A[0][1]*B[1][1]),
        (A[1][0]*B[0][0]+A[1][1]*B[1][0],
         A[1][0]*B[0][1]+A[1][1]*B[1][1])
    )

def matrix(beta,q,K):
    return ((beta+q**K,-beta),(1.0,0.0))

def eig_radius_2x2(A):
    tr=A[0][0]+A[1][1]
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    disc=complex(tr*tr-4*det)**0.5
    return max(abs((tr+disc)/2),abs((tr-disc)/2))

rng=random.Random(350057)

for _ in range(3000):
    beta=rng.random()*0.999
    q=-0.999+1.998*rng.random()
    k1=rng.randint(1,10)
    k2=rng.randint(1,10)

    M1=matrix(beta,q,k1)
    M2=matrix(beta,q,k2)
    assert eig_radius_2x2(M1) < 1.0 + 1e-11
    assert eig_radius_2x2(M2) < 1.0 + 1e-11

    P=matmul(M2,M1)
    product=(beta+q**k1)*(beta+q**k2)
    margin=product+(1-beta)**2
    rho=eig_radius_2x2(P)
    if abs(margin)>1e-9:
        assert (rho < 1.0) == (margin > 0.0)

# Exact rational witness.
beta=Fraction(1,2)
q=Fraction(-4,5)
a1=beta+q
a2=beta+q*q
assert a1 == Fraction(-3,10)
assert a2 == Fraction(57,50)
assert a1*a2 == Fraction(-171,500)
assert -(1-beta)**2 == Fraction(-1,4)
assert a1*a2 < -(1-beta)**2

M1=((a1,-beta),(Fraction(1),Fraction(0)))
M2=((a2,-beta),(Fraction(1),Fraction(0)))
P=matmul(M2,M1)
tr=P[0][0]+P[1][1]
det=P[0][0]*P[1][1]-P[0][1]*P[1][0]
assert tr == Fraction(-671,500)
assert det == Fraction(1,4)
disc=tr*tr-4*det
assert disc == Fraction(200241,250000)
rho=(671+math.sqrt(200241))/1000
assert rho > 1.0

# Each frozen workload has complex roots of modulus sqrt(beta).
for A in (a1,a2):
    assert A*A-4*beta < 0
assert abs(math.sqrt(float(beta))-1/math.sqrt(2)) < 1e-15

# Vanilla FedAvg under the same workload alternation.
assert q**3 == Fraction(-64,125)
assert abs(q**3) < 1

# Direct zero-momentum FedAvgM simulation excites the unstable mode.
x=Fraction(1)
v=Fraction(0)
magnitudes=[]
for t in range(24):
    K=1 if t%2==0 else 2
    h=1-q**K
    v=beta*v+h*x
    x=x-v
    if t%2==1:
        magnitudes.append(abs(x))
assert magnitudes[-1] > magnitudes[0]

print("verification passed")
