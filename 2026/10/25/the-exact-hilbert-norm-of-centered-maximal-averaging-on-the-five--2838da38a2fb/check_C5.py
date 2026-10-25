#!/usr/bin/env python3
"""Exact finite certificate for centered maximal averaging on the five-cycle.
Requires only the Python 3 standard library; no external data or dependencies.
"""
from fractions import Fraction as F
from itertools import product

N=5
Q=F(1463,1000)
BEST=(0,1,0,2,2)

def transform(p,s,rev):
    return tuple(p[(s+(-i if rev else i))%N] for i in range(N))

def orbit(p):
    return {transform(p,s,rev) for s in range(N) for rev in (0,1)}

def canon(p):
    return min(orbit(p))

def integer_matrix(p):
    # A(p)=M(p)/15. Values 0,1,2 mean radius 0,1,2.
    M=[]
    for i,r in enumerate(p):
        if r==0: M.append([15 if j==i else 0 for j in range(N)])
        elif r==1: M.append([5 if (j-i)%N in (0,1,4) else 0 for j in range(N)])
        else: M.append([3]*N)
    return M

def transpose_square(M):
    return [[sum(M[k][i]*M[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def det_bareiss(A):
    B=[row[:] for row in A]
    n=len(B)
    if n==0: return 1
    prev=1
    parity=1
    for k in range(n-1):
        if B[k][k]==0:
            j=next((j for j in range(k+1,n) if B[j][k]!=0),None)
            if j is None:return 0
            B[k],B[j]=B[j],B[k]
            parity=-parity
        pivot=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a=B[i][j]*pivot-B[i][k]*B[k][j]
                assert a%prev==0
                B[i][j]=a//prev
        for i in range(k+1,n):B[i][k]=0
        prev=pivot
    return parity*B[n-1][n-1]

def all_pd(B):
    return all(det_bareiss([row[:k] for row in B[:k]])>0 for k in range(1,N+1))

patterns=list(product(range(3),repeat=N))
unique={canon(p) for p in patterns}
assert len(patterns)==243
assert len(unique)==39
assert canon(BEST)==BEST
B_orb=orbit(BEST)
assert len(B_orb)==5
assert all(canon(p)==BEST for p in B_orb)
assert len(set().union(*(orbit(p) for p in unique)))==243

for p in unique:
    if p==BEST:continue
    M=integer_matrix(p)
    G=transpose_square(M)
    # Q*I - A^T A=(329175 I -1000 M^T M)/225000.
    S=[[329175*(i==j)-1000*G[i][j] for j in range(N)] for i in range(N)]
    assert all_pd(S), ('not strictly below threshold',p)

# Rational witness, better than separation threshold.
w=[7,2,7,1,1]
M=integer_matrix(BEST)
y=[sum(a*b for a,b in zip(row,w)) for row in M]
ray=F(sum(v*v for v in y),225*sum(v*v for v in w))
assert ray>Q,(ray,Q)

# The Gram matrix of the optimal mask has characteristic polynomial
# (z-1)(225 z^3-390 z^2+91 z-4), with an extra zero eigenvalue.
# Check characteristic coefficients with exact traces:
G=transpose_square(M)
# A has rank 3 (two duplicated rows). Power-trace Newton identities.
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
G2=mul(G,G);G3=mul(G2,G);G4=mul(G3,G)
p1=F(sum(G[i][i] for i in range(N)),225)
p2=F(sum(G2[i][i] for i in range(N)),225**2)
p3=F(sum(G3[i][i] for i in range(N)),225**3)
p4=F(sum(G4[i][i] for i in range(N)),225**4)
e1=p1;e2=(p1*p1-p2)/2;e3=(p1**3-3*p1*p2+2*p3)/6
e4=(e3*p1-e2*p2+e1*p3-p4)/4
assert (e1,e2,e3,e4)==(F(615,225),F(481,225),F(95,225),F(4,225)), (e1,e2,e3,e4)
# The cubic has exactly one root above Q, by positive derivative for t>=Q.
# At Q its polynomial is negative and derivative positive, hence largest root > Q.
def poly(t):return 225*t**3-390*t*t+91*t-4
assert poly(Q)<0
assert poly(F(1467,1000))>0
assert 675*Q*Q-780*Q+91>0
assert 1350*Q-780>0
print('PASS: 243 patterns; 39 dihedral classes; 1 top class of size 5;')
print('38 exact integer Sylvester positivity certificates, rational Rayleigh witness',ray)
print('characteristic cubic 225*z^3-390*z^2+91*z-4; threshold 1463/1000.')
