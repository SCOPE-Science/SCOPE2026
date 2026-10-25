#!/usr/bin/env python3
"""Reproducibility checks for the Gaussian Fock first-jet orbit theorem.
The universal asymptotic is proved analytically in RESULT.md; numerical tests are finite checks only.
"""
import cmath
import math

checks = 0

def check(condition, explanation):
    global checks
    assert condition, explanation
    checks += 1

def captured(N, m, lam):
    """Exact-moment formula numerically evaluated with a stable common scaling."""
    assert N >= 0 and m >= 1 and lam > 0
    r = N % m
    upper = max(N + 2 * m, int(lam + 30 * math.sqrt(lam + 1) + 250))
    js = list(range(r, upper + 1, m))
    logs = [j * math.log(lam) - math.lgamma(j + 1) for j in js]
    pivot = max(logs)
    ws = [math.exp(t - pivot) for t in logs]
    S = math.fsum(ws)
    mu = math.fsum(w * j for j, w in zip(js, ws)) / S
    var = math.fsum(w * (j - mu) ** 2 for j, w in zip(js, ws)) / S
    wn = math.exp(N * math.log(lam) - math.lgamma(N+1) - pivot)
    assert var > 0
    return (wn / S) * (1 + (N - mu)**2 / var)

def gram_projection(N,m,lam):
    """Independent complex Gram projection in truncated monomial Fock basis."""
    radius = math.sqrt(lam)
    maxj = max(N + 30, int(lam+23*math.sqrt(lam+1)+100))
    points = [radius*cmath.exp(2*math.pi*1j*k/m) for k in range(m)]
    # Matrix columns are value representers and derivative representers.
    B=[]
    for j in range(maxj+1):
        B.append([w.conjugate()**j * math.exp(-0.5 * math.lgamma(j+1)) for w in points] + [j*w.conjugate()**(j-1)*math.exp(-0.5 * math.lgamma(j+1)) if j else 0j for w in points])
    size=2*m
    G=[[sum(B[j][a].conjugate()*B[j][b] for j in range(maxj+1)) for b in range(size)] for a in range(size)]
    rhs=[B[N][a].conjugate() for a in range(size)]
    # Hermitian positive definite Gaussian elimination with pivoting.
    A=[list(G[i])+[rhs[i]] for i in range(size)]
    for i in range(size):
        p=max(range(i,size),key=lambda k:abs(A[k][i]))
        assert abs(A[p][i])>1e-11
        A[i],A[p]=A[p],A[i]
        divisor=A[i][i]
        for j in range(i,size+1):A[i][j]/=divisor
        for k in range(size):
            if k==i:continue
            c=A[k][i]
            for j in range(i,size+1):A[k][j]-=c*A[i][j]
    sol=[A[i][-1] for i in range(size)]
    norm=sum(abs(sum(B[j][a]*sol[a] for a in range(size)))**2 for j in range(maxj+1))
    return norm

for N in (4,6,9,13):
    for m in (1,2,3):
        for lam in (1.5,3.0,7.0):
            a=captured(N,m,lam)
            b=gram_projection(N,m,lam)
            check(abs(a-b)<5e-7,(N,m,lam,a,b))
            check(0<=a<=1+1e-10,('range',N,m,lam,a))

# For a single jet, the stationary radii are N-sqrt(N), N, N+sqrt(N).
def single(N,lam):
    return math.exp(-lam+N*math.log(lam)-math.lgamma(N+1)) * (1+(N-lam)**2/lam)

for N in (2,3,4,7,11,20,55,100):
    roots=(N-math.sqrt(N),N,N+math.sqrt(N))
    vals=[single(N,x) for x in roots]
    check(vals[0]>vals[1] and vals[2]>vals[1], ('stationary types',N,vals))
    for x in roots:
        h=1e-5*min(1,x)
        deriv=(single(N,x+h)-single(N,x-h))/(2*h)
        check(abs(deriv)<1e-7,('stationary derivative',N,x,deriv))

# Sparse-orbit asymptotic and the two shifted optimal windows.
for N,m in ((900,1),(1600,2),(2500,3),(3600,5),(6400,6)):
    for side in (-1,1):
        val=captured(N,m,N+side*math.sqrt(N))
        goal=2*m/math.sqrt(2*math.pi*math.e*N)
        check(abs(val/goal-1)<0.13,('two-peak asymptotic',N,m,side,val,goal))
    central=captured(N,m,N)
    check(central<captured(N,m,N-math.sqrt(N)),('off-center advantage',N,m))

print(f'PASS: {checks} finite consistency assertions.')
