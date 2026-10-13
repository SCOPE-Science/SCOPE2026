#!/usr/bin/env python3
import math

def transpose(A):
    return [list(x) for x in zip(*A)]

def matmul(A,B):
    Bt=transpose(B)
    return [[sum(x*y for x,y in zip(row,col)) for col in Bt] for row in A]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def gaussian_solve(A,b):
    A=[row[:] + [rhs] for row,rhs in zip(A,b)]
    n=len(A)
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(A[i][k]))
        assert abs(A[p][k])>1e-14
        A[k],A[p]=A[p],A[k]
        piv=A[k][k]
        for j in range(k,n+1):
            A[k][j]/=piv
        for i in range(n):
            if i==k: continue
            f=A[i][k]
            if f:
                for j in range(k,n+1):
                    A[i][j]-=f*A[k][j]
    return [A[i][n] for i in range(n)]

def lyapunov(F,C):
    # Solve F W + W F^T + C = 0 for all 9 entries.
    n=3
    M=[[0.0]*(n*n) for _ in range(n*n)]
    rhs=[0.0]*(n*n)
    def idx(i,j): return i*n+j
    for i in range(n):
        for j in range(n):
            r=idx(i,j)
            rhs[r]=-C[i][j]
            for k in range(n):
                M[r][idx(k,j)] += F[i][k]
                M[r][idx(i,k)] += F[j][k]
    x=gaussian_solve(M,rhs)
    return [[x[idx(i,j)] for j in range(n)] for i in range(n)]

def maxabs(A):
    return max(abs(x) for row in A for x in row)

def sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

Lam=1.0
mu=0.2
beta=0.1
epsd=0.05
gamma=0.1
delta=0.25
alpha=0.001
sigma=[0.6,0.8,0.7]

# Positive endemic root from the exact equilibrium reduction.
qa=mu*(mu+gamma+epsd)*alpha/beta
qb=(mu+epsd)+mu*gamma/(mu+delta)
qc=mu*(mu+gamma+epsd)/beta-Lam
disc=qb*qb-4.0*qa*qc
I=(-qb+math.sqrt(disc))/(2.0*qa)
S=(mu+gamma+epsd)*(1.0+alpha*I*I)/beta
R=gamma*I/(mu+delta)

assert abs(S-3.503615825968239)<1e-12
assert abs(I-1.0164118917951583)<1e-12
assert abs(R-0.2258693092878130)<1e-12

dinc_dS=beta*I/(1.0+alpha*I*I)
dinc_dI=beta*S*(1.0-alpha*I*I)/(1.0+alpha*I*I)**2
F=[
    [-mu-dinc_dS,-dinc_dI,delta],
    [ dinc_dS,dinc_dI-(mu+gamma+epsd),0.0],
    [0.0,gamma,-(mu+delta)],
]
G=[
    [-sigma[0]*S,0.0,0.0],
    [0.0,-sigma[1]*I,0.0],
    [0.0,0.0,-sigma[2]*R],
]
Gt=transpose(G)
I3=[[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]

def covariance(Rc):
    C=matmul(matmul(G,Rc),Gt)
    return lyapunov(F,C)

Wind=covariance(I3)
expected=[
 [10.284417372,-3.208357070,-0.916161615],
 [-3.208357070,6.679116995,1.275481364],
 [-0.916161615,1.275481364,0.311216195],
]
assert maxabs(sub(Wind,expected))<5e-9

# Adjoint Lyapunov equation F^T P + P F + I = 0.
P=lyapunov(transpose(F),I3)
H=matmul(matmul(Gt,P),G)
base=trace(H)
a=2.0*H[0][1]
b=2.0*H[0][2]
c=2.0*H[1][2]

assert abs(base-17.27475056240875)<2e-10
assert abs(a-5.39530312013)<2e-10
assert abs(b-0.537604148434)<2e-10
assert abs(c-0.152951296895)<2e-10
assert a > b*c/(b-c)

ones=[1.0,1.0,1.0]
sign=[1.0,-1.0,-1.0]
Rplus=[[ones[i]*ones[j] for j in range(3)] for i in range(3)]
Rminus=[[sign[i]*sign[j] for j in range(3)] for i in range(3)]

Wplus=covariance(Rplus)
Wminus=covariance(Rminus)
tplus=trace(Wplus)
tminus=trace(Wminus)
assert abs(tplus-23.36060912786898)<2e-10
assert abs(tminus-11.49479459073953)<2e-10
assert abs(tplus/tminus-2.03227721413)<2e-10

# Literal printed forcing GG^T + Q, with Q = G Rplus G^T.
GGt=matmul(G,Gt)
Qplus=matmul(matmul(G,Rplus),Gt)
Wprinted=lyapunov(F,add(GGt,Qplus))
assert maxabs(sub(Wprinted,add(Wind,Wplus)))<2e-10
assert abs(trace(Wprinted)-40.63535969027773)<2e-10
assert abs(trace(Wprinted)/tplus-1.73948202583)<2e-10

print("VERIFY_OK")
