"""Exact-rational checks for scalar momentum augmented-Lagrangian feasibility risk.

Run with `python verify_malm.py`; Python standard library only.
Finite checks corroborate but do not replace the analytical proof.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt

count=0

def test(pred, msg):
    global count
    if not pred:
        raise AssertionError(msg)
    count+=1

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def solve_linear(mat, rhs):
    n=len(rhs)
    a=[row[:]+[rhs[i]] for i,row in enumerate(mat)]
    for col in range(n):
        pivot=next((j for j in range(col,n) if a[j][col]),None)
        if pivot is None: raise ValueError('singular Lyapunov system')
        a[col],a[pivot]=a[pivot],a[col]
        z=a[col][col]
        a[col]=[v/z for v in a[col]]
        for row in range(n):
            if row!=col:
                z=a[row][col]
                a[row]=[a[row][j]-z*a[col][j] for j in range(n+1)]
    return [a[i][-1] for i in range(n)]

def cov_exact(t,alpha):
    """Solve C = M C M^T + diag(0,0,alpha^2), independently."""
    zero=Q(0)
    M=[[1-t,-1,-1],[t*(1-t),1-t,-t],[zero,zero,1-alpha]]
    coords=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    bases=[]
    for i,j in coords:
        B=[[zero for _ in range(3)] for _ in range(3)]
        B[i][j]=1;B[j][i]=1
        bases.append(B)
    transformed=[matmul(matmul(M,B),transpose(M)) for B in bases]
    system=[]; target=[]
    for i,j in coords:
        system.append([B[i][j]-T[i][j] for B,T in zip(bases,transformed)])
        target.append(alpha*alpha if (i,j)==(2,2) else zero)
    return solve_linear(system,target)

def risk(t,a):
    return 2*a*a*(2-a-(1-a)*t)/(t*(2-a)*(4-3*t)*(a*a+(1-a*a)*t))

def log_deriv(t,a):
    return -(1-a)/(2-a-(1-a)*t)-1/t+3/(4-3*t)-(1-a*a)/(a*a+(1-a*a)*t)

def log_second(t,a):
    e=1-a; d=2-a; b=1-a*a
    return -(e/(d-e*t))**2+1/t**2+9/(4-3*t)**2+(b/(a*a+b*t))**2

for ai in range(1,20):
    a=Q(ai,20)
    test(log_deriv(Q(2,3),a)<0, 'lower bracket sign')
    test(log_deriv(Q(1),a)>0, 'upper bracket sign')
    for ti in range(1,22):
        t=Q(ti,17)
        test(t < Q(4,3) and log_second(t,a)>0, 'strict log convexity')
        C=cov_exact(t,a)
        test(C[0]==risk(t,a), f'exact covariance equality alpha={a}, t={t}')
        test(C[5]==a/(2-a), 'momentum variance')
        test(C[1]==(t/2)*C[0], 'primal-dual covariance relation')

# Uniqueness and minimizer bracket checked with rational bisection (not an infinite proof).
for ai in range(1,40):
    a=Q(ai,40)
    lo,hi=Q(2,3),Q(1)
    for j in range(45):
        mid=(lo+hi)/2
        if log_deriv(mid,a)>0:hi=mid
        else:lo=mid
    test(lo<hi and hi-lo<Q(1,10**10),'unique positive derivative root bracket')
    x=(lo+hi)/2
    test(risk(x,a)<risk(Q(2,3),a) and risk(x,a)<risk(Q(1),a),
         'interior optimum dominates endpoints')

# Seeded stationary simulations, independent of the Lyapunov solver.
rng=Random(20261017)
for a0,t0 in ((.25, .9), (.5, .7), (.75, 1.), (.8, 1.1)):
    x=u=v=0.0
    burn=15000; samples=150000
    sum_sq=0.0
    for j in range(burn+samples):
        xnew=(1-t0)*x-u-v
        unew=u+t0*xnew
        vnew=(1-a0)*v+a0*rng.gauss(0,1)
        x,u,v=xnew,unew,vnew
        if j>=burn:sum_sq+=x*x
    empirical=sum_sq/samples
    predicted=float(risk(Q(str(t0)),Q(str(a0))))
    test(abs(empirical/predicted-1)<.11,
         f'seeded stationary feasibility risk alpha={a0}, t={t0}')
print(f'PASS: {count} exact rational / seeded numerical checks')
print('The universal claim is proved algebraically, not by these finite checks.')
