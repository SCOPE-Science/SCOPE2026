"""Exact certificate and finite consistency checks for a conditioned diagonal metric."""
from fractions import Fraction as Q
from math import sqrt, isclose
from itertools import permutations,product

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def det4(A):
    total=Q(0)
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        v=Q(-1 if inv%2 else 1)
        for i in range(4): v*=A[i][p[i]]
        total+=v
    return total

def eigenmax_from_weights(p):
    q=[p[i]/p[i+1] for i in range(3)]
    ss=sum(q)
    return sqrt((ss+sqrt(ss*ss-4*q[0]*q[2]))/2)

def R(K):
    return (1/sqrt(K)+sqrt(4+1/K))/4 if K<=2 else 2**(-1/3)*K**(-1/6)

def metric(K):
    return [1.,1.,float(K),float(K)] if K<=2 else [1.,(K/2)**(1/3),(2*K*K)**(1/3),float(K)]

# Rational generator and Lyapunov matrix.
p=[Q(1),Q(2),Q(8),Q(16)]
G=[[Q(-1 if i==j else 2 if j==i+1 else 0) for j in range(4)] for i in range(4)]
P=[[p[i] if i==j else Q(0) for j in range(4)] for i in range(4)]
GT=[[G[j][i] for j in range(4)] for i in range(4)]
PG=matmul(P,G);GTP=matmul(GT,P)
M=[[PG[i][j]+GTP[i][j] for j in range(4)] for i in range(4)]
assert M==[[Q(x) for x in row] for row in [[-2,2,0,0],[2,-4,4,0],[0,4,-16,16],[0,0,16,-32]]]
H=[[M[i][j]/p[i] for j in range(4)] for i in range(4)]
roots=[Q(0),Q(-1),Q(-3),Q(-4)]
assert all(det4([[ (Q(lam) if i==j else Q(0))-H[i][j] for j in range(4)] for i in range(4)])==0 for lam in roots)
assert len(set(roots))==4
assert max(p)/min(p)==16

# Closed-form all-budget formula versus independently derived characteristic roots.
for K in [1.,1.1,1.5,2.,3.,6.,16.,100.]:
    pstar=metric(K)
    assert min(pstar)>0
    assert isclose(max(pstar)/min(pstar),K,rel_tol=2e-14,abs_tol=2e-14)
    assert isclose(eigenmax_from_weights(pstar)/2,R(K),rel_tol=1e-13,abs_tol=1e-13)
    # Deterministic grid of alternate feasible diagonal metrics. Not a proof.
    options=[1.,K**(.25),K**(.5),K**(.75),K]
    for middle in product(options,repeat=2):
        alt=[1.,middle[0],middle[1],K]
        assert eigenmax_from_weights(alt)/2+1e-12>=R(K)

# Critical equation, including the nontrivial K=16 boundary.
assert isclose(R(2),1/sqrt(2),rel_tol=1e-14)
assert isclose(R(16),.5,rel_tol=1e-14)
assert R(15.999)>.5
assert R(16.001)<.5
assert isclose(R(1),(1+sqrt(5))/4,rel_tol=1e-14)
for c in [.25,.5,.6,.7,1/sqrt(2),.75,(1+sqrt(5))/4]:
    if c>= (1+sqrt(5))/4:
        K=1.
        assert R(K)<=c+1e-12
    elif c>=1/sqrt(2):
        K=(2*c-1/(2*c))**(-2)
        assert 1<=K<=2+1e-12
        assert isclose(R(K),c,rel_tol=1e-12,abs_tol=1e-12)
    else:
        K=1/(4*c**6)
        assert K>2
        assert isclose(R(K),c,rel_tol=1e-12,abs_tol=1e-12)
print('VERIFY_OK')
