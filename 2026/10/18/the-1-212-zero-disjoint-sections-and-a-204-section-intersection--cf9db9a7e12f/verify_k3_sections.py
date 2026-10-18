"""Exact arithmetic certificate for a specialized elliptic K3 section census.

Run with Python >=3.9: python verify_k3_sections.py
All calculations use integers and fractions; the bounded search is exhaustive.
"""
from collections import Counter
from fractions import Fraction as F
from math import isqrt

N = 12
M = [
    [8,-4,2,2,2,2],[-4,8,2,2,2,2],[2,2,8,2,2,2],
    [2,2,2,8,2,2],[2,2,2,2,8,2],[2,2,2,2,2,8]
]
Nblock = [
    [3,-3,-3,0,0,0],[-3,3,3,0,0,0],[3,-3,3,0,0,0],
    [0,0,0,3,3,0],[0,0,0,-3,3,0],[0,0,0,0,0,0]
]
oldQ = [[M[i%6][j%6] if i//6 == j//6 else
         (Nblock[i][j-6] if i < 6 else Nblock[j][i-6])
         for j in range(N)] for i in range(N)]
# The last new generator of each six-block replaces the sixth old generator.
# 2 Q1=-(P1-P3+P4-P5+P6), with the same primed relation.
T = [[F(int(i == j)) for j in range(N)] for i in range(N)]
for b in (0,6):
    for i,coeff in ((0,-1),(2,1),(3,-1),(4,1),(5,-1)):
        T[b+i][b+5] = F(coeff,2)
Q = [[sum(T[a][i]*oldQ[a][b]*T[b][j]
          for a in range(N) for b in range(N)) for j in range(N)]
     for i in range(N)]
assert all(x.denominator == 1 for row in Q for x in row)
Q = [[int(x) for x in row] for row in Q]
assert all(Q[i][j] == Q[j][i] for i in range(N) for j in range(N))

# Exact rational LDL^T decomposition, Q=L D L^T, with U=L^T.
d = [F(0)]*N
U = [[F(0) for _ in range(N)] for _ in range(N)]
for j in range(N):
    d[j] = F(Q[j][j]) - sum(d[k]*U[k][j]**2 for k in range(j))
    assert d[j] > 0
    U[j][j] = F(1)
    for i in range(j+1,N):
        U[j][i] = (F(Q[j][i])-
                   sum(d[k]*U[k][j]*U[k][i] for k in range(j)))/d[j]
assert [str(x) for x in d] == ['8','6','6','6','6','3/2','5','24/5','3','3','3','3/2']
from math import prod
assert prod(d) == 256 * 3**10
assert all(sum(U[k][i]*d[k]*U[k][j] for k in range(N)) == Q[i][j]
           for i in range(N) for j in range(N))

def ceil_fraction(x):
    return -(-x.numerator // x.denominator)

def short_vectors(bound):
    """Exhaust all integer v with v^T Q v <= bound.

    At descent coordinate i, exact square-completion gives
    d_i (x_i + sum_{j>i} U_ij x_j)^2 <= remaining.
    The integer cap contains every feasible integer, so no solutions are missed.
    """
    v = [0]*N
    found = []
    def descend(i,remaining):
        if i < 0:
            assert remaining >= 0
            found.append(tuple(v))
            return
        c = sum(U[i][j]*v[j] for j in range(i+1,N))
        rho = remaining/d[i]
        cap = ceil_fraction(abs(c)) + isqrt(ceil_fraction(rho)) + 1
        for z in range(-cap,cap+1):
            r = remaining - d[i]*(F(z)+c)**2
            if r >= 0:
                v[i] = z
                descend(i-1,r)
        v[i] = 0
    descend(N-1,F(bound))
    return found

def qbil(v,w):
    return sum(v[i]*Q[i][j]*w[j] for i in range(N) for j in range(N))

V = short_vectors(12)
height_counts = Counter(qbil(v,v) for v in V)
assert height_counts == {0:1, 8:204, 10:576, 12:432}, height_counts
assert len(set(V)) == 1213
# Each nonzero vector in these three shells gives a section disjoint from O.
# Local IV component labels in Z/3: unprimed (1,1), primed (1,-1).
def component(v):
    return sum(v)%3, (sum(v[:6])-sum(v[6:]))%3
assert Counter(component(v) for v in V if qbil(v,v) == 8) == {
    (1,1):51,(1,2):51,(2,1):51,(2,2):51}
assert Counter(component(v) for v in V if qbil(v,v) == 10) == {
    (1,0):144,(2,0):144,(0,1):144,(0,2):144}
assert Counter(component(v) for v in V if qbil(v,v) == 12) == {(0,0):432}

S = sorted(v for v in V if qbil(v,v) == 8)
assert len(S) == 204

def corr(a,b):
    if a == 0 or b == 0:
        return F(0)
    return F(2,3) if a == b else F(1,3)

pairs = Counter()
weighted_degrees = [0]*204
for i,v in enumerate(S):
    a,b = component(v)
    for j in range(i+1,204):
        w = S[j]
        c,e = component(w)
        # Shioda pairing for distinct sections on a K3 surface.
        intersection = F(2)-F(qbil(v,w),3)-corr(a,c)-corr(b,e)
        assert intersection >= 0 and intersection.denominator == 1
        m = int(intersection)
        assert (m == 4) == all(v[k] == -w[k] for k in range(N))
        pairs[m] += 1
        weighted_degrees[i] += m
        weighted_degrees[j] += m
assert pairs == {0:5868,1:8868,2:5868,4:102}, pairs
assert all(k == 206 for k in weighted_degrees)
assert sum(pairs.values()) == 204*203//2

# Exact 14-dimensional spectral certificate for weighted adjacency A.
# Let Vmat have rows the 204 section coordinates; s0 and s1 are component
# signs. Intersection matrix B=A-2I = J - Vmat*Q*Vmat^T/3 - (s0*s0^T+s1*s1^T)/6.
# Rank-nullity and its 14-dimensional Gram factor give all eigenvalues.
s0 = [1 if component(v)[0] == 1 else -1 for v in S]
s1 = [1 if component(v)[1] == 1 else -1 for v in S]
assert sum(s0) == sum(s1) == sum(a*b for a,b in zip(s0,s1)) == 0
assert all(sum(v[j] for v in S) == 0 for j in range(N))
assert all(sum(S[k][j]*s0[k] for k in range(204)) == 0 for j in range(N))
assert all(sum(S[k][j]*s1[k] for k in range(204)) == 0 for j in range(N))
R = [[sum(v[i]*v[j] for v in S) for j in range(N)] for i in range(N)]
RQ = [[sum(R[i][k]*Q[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def product(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
A120 = [[RQ[i][j]-(120 if i==j else 0) for j in range(N)] for i in range(N)]
A144 = [[RQ[i][j]-(144 if i==j else 0) for j in range(N)] for i in range(N)]
assert all(v == 0 for row in product(A120,A144) for v in row)
assert sum(RQ[i][i] for i in range(N)) == 1632 # 4*120+8*144
# Thus RQ eigenvalues 120^4 and 144^8. s0 and s1 each yield B=-34;
# constant vector yields B=204; 189 other vectors have B=0.
# Adding 2I yields A spectrum 206^1,2^189,(-32)^2,(-38)^4,(-46)^8.
assert 206 + 189*2 - 2*32 - 4*38 - 8*46 == 0
assert 1 + 189 + 2 + 4 + 8 == 204

# Non-isogeny check for E2 and E5 over Qbar. Their rational j-invariants
# are not algebraic integers, so neither has CM. At p=23 the good traces
# differ even up to sign; a Qbar isogeny of non-CM Q-curves would force
# a quadratic twist of Galois representations and traces +/- at good p.
def trace_at_23(z):
    p=23
    def rhs(x):return x*(x+(z*z+1)**2)*(x+(z*z-1)**2)
    squares = Counter((y*y)%p for y in range(p))
    points = 1+sum(squares[rhs(x)%p] for x in range(p))
    return p+1-points
assert trace_at_23(2) == 0
assert trace_at_23(5) == 8

def j_of_z(z):
    Az=z**8+14*z**4+1
    Bz=z*(z**4-1)
    return F(16*Az**3,Bz**4)
assert j_of_z(2).denominator > 1 and j_of_z(5).denominator > 1
print('Complete height shell counts (3h):',dict(sorted(height_counts.items())))
print('Nonzero sections disjoint from zero:',len(V)-1)
print('Minimum height section pair intersection counts:',dict(sorted(pairs.items())))
print('Weighted degree:',weighted_degrees[0])
print('Weighted spectrum: 206^1, 2^189, (-32)^2, (-38)^4, (-46)^8')
print('Exact nonisogeny trace test at p=23:',trace_at_23(2),trace_at_23(5))
print('PASS')
