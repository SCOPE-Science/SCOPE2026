"""Exact, standalone verification of the three-habitat calendar-reversal witness.

All calculations use fractions, with no external dependencies.  The general
all-dimensional theorem is proved in RESULT.md; this checks its finite witness.
"""
from fractions import Fraction as Q
from itertools import permutations

def mul(A, B):
    return [[sum(A[i][h]*B[h][j] for h in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]

def matprod(*mats):
    X = eye(len(mats[0]))
    for M in mats:
        X = mul(X, M)
    return X

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))]
            for i in range(len(A))]

def scale(A, c):
    return [[c*x for x in row] for row in A]

def characteristic(A):
    n=len(A); B=eye(n); cs=[]
    for k in range(1,n+1):
        AB=mul(A,B)
        c=-tr(AB)/k
        cs.append(c)
        B=[[AB[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
    return cs

P=[[Q(1,2),Q(2,5),Q(1,10)],
   [Q(1,10),Q(1,2),Q(2,5)],
   [Q(2,5),Q(1,10),Q(1,2)]]
D=[[[Q(3 if j==i else 1) if i==h else Q(0) for h in range(3)]
      for i in range(3)] for j in range(3)]
assert all(sum(P[i][j] for i in range(3))==1 for j in range(3))
assert all(sum(row)==1 for row in P)
assert all(x>0 for row in P for x in row)
A=matprod(P,D[2],P,D[1],P,D[0])
B=matprod(P,D[0],P,D[1],P,D[2])
assert tr(A)==Q(329,100) and tr(B)==Q(91,20)
assert characteristic(A)==[-Q(329,100),-Q(1118287,1000000),-Q(59319,1000000)]
assert characteristic(B)==[-Q(91,20),-Q(888967,1000000),-Q(59319,1000000)]
row2A=[sum(row) for row in mul(A,A)]
row2B=[sum(row) for row in mul(B,B)]
assert row2A == [Q(689659,62500),Q(7339579,500000),Q(7807529,500000)]
assert row2B == [Q(14338799,500000),Q(8340079,500000),Q(5840221,250000)]
gap=min(row2B)-max(row2A)
assert gap==Q(10651,10000) and gap>0
# A single common scaling of each season reverses the persistence threshold.
c=Q(17,27)
scaled_upper=c**6 * max(row2A)
scaled_lower=c**6 * min(row2B)
assert scaled_upper < 1 < scaled_lower
assert P[1][0]*P[2][1]*P[0][2]!=P[0][1]*P[1][2]*P[2][0]
# Direct chronological application, avoiding any convention ambiguity.
def calendar(migration, seasons):
    X=eye(len(migration))
    for growth in seasons:
        X=mul(mul(migration,growth),X)
    return X

assert calendar(P,D)==A
assert calendar(P,list(reversed(D)))==B
# Any two factors commute cyclically at the level of the characteristic polynomial.
for a,b in permutations(range(3),2):
    X=calendar(P,[D[a],D[b]]); Y=calendar(P,[D[b],D[a]])
    assert characteristic(X)==characteristic(Y)
# Two nontrivial symmetrizable migration laws: one symmetric, one asymmetric.
S=[[Q(1,2),Q(1,4),Q(1,4)],
   [Q(1,4),Q(1,2),Q(1,4)],
   [Q(1,4),Q(1,4),Q(1,2)]]
W=[[Q(3),Q(1),Q(2)],[Q(1),Q(4),Q(1)],[Q(2),Q(1),Q(5)]]
cols=[sum(W[i][j] for i in range(3)) for j in range(3)]
T=[[W[i][j]/cols[j] for j in range(3)] for i in range(3)]
assert T[0][2]!=T[2][0]
assert all(T[i][j]*cols[j] == T[j][i]*cols[i] for i in range(3) for j in range(3))
for migration in [S,T]:
    for k in range(1,8):
        sequence=[D[(2*j+1)%3] for j in range(k)]
        assert characteristic(calendar(migration,sequence)) == characteristic(calendar(migration,list(reversed(sequence))))
print('VERIFIED: 3x3 exact characteristic polynomials, strict positive spectral-gap bounds, nonreversibility, two-season minimality, reversible examples')
print('forward_tr', tr(A), 'reverse_tr', tr(B))
print('A2_row_sums', list(map(str,row2A)))
print('B2_row_sums', list(map(str,row2B)))
print('strict_square_row_gap', gap)
print('scaled_forward_square_upper', scaled_upper)
print('scaled_reverse_square_lower', scaled_lower)
