"""Exact independent checks for the edge-cover covariance and precision theorem.

This program uses only Python's standard library. Run: python edgecover_check.py
"""
from fractions import Fraction as F
from itertools import combinations

checks = 0

def assert_eq(a, b):
    global checks
    checks += 1
    assert a == b, (a, b)

def inverse(a):
    n = len(a)
    a = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        v = a[k][k]
        a[k] = [w/v for w in a[k]]
        for i in range(n):
            if i != k:
                v = a[i][k]
                a[i] = [x-v*y for x,y in zip(a[i],a[k])]
    return [row[n:] for row in a]

def closed(n,p):
    t=(1-p)/(2-p); h=t**n; z=1-2*h; u=1-2*t
    mu=(1-t-h)/z
    v=mu*(1-mu)
    a=-(t-h)**2/z**2
    b=h*(h-(1-2*t+2*t*t))/z**2
    c=h*(2*t*(1-t)-h)/z**2
    A=t-n*h
    B=A+2*(n-1)*t*h
    qdiag=z/(2*t)*(1/u+1)+z*h/(2*t)*(1/B+1/A)
    qa=z*(1/u-(n-1)*h*h/(A*B))
    qb=z*h/(2*t)*(1/B+1/A)
    qc=-z*(n-1)*h*h/(A*B)
    return (v,a,b,c),(qdiag,qa,qb,qc)

def brute(n,p):
    edges=[(i,j) for i in range(n) for j in range(2)]
    M=2*n
    weights=[F(0)]*(1<<M)
    z=F(0)
    for mask in range(1<<M):
        # Every column must be nonempty and both rows hit.
        if any((mask>>(2*i))&3 == 0 for i in range(n)):
            continue
        if not any(mask>>(2*i)&1 for i in range(n)):
            continue
        if not any(mask>>(2*i+1)&1 for i in range(n)):
            continue
        k=mask.bit_count()
        w=p**k*(1-p)**(M-k)
        z+=w
        weights[mask]=w
    mu=[sum((weights[mask] for mask in range(1<<M) if mask>>i&1),F(0))/z for i in range(M)]
    cov=[[sum((weights[mask] for mask in range(1<<M) if (mask>>i&1) and (mask>>j&1)),F(0))/z-mu[i]*mu[j] for j in range(M)] for i in range(M)]
    return cov

for n in range(2,7):
    for p in [F(1,5),F(1,2),F(4,5)]:
        pred,qpred=closed(n,p)
        cov=brute(n,p)
        for i in range(2*n):
            for j in range(2*n):
                value=(pred[0] if i==j else pred[1] if i//2==j//2 else pred[2] if i%2==j%2 else pred[3])
                assert_eq(cov[i][j], value)
        # Verify the precision formulas by full exact matrix multiplication,
        # independently of the Fourier decomposition used in the proof.
        Q=[[qpred[0] if i==j else qpred[1] if i//2==j//2 else qpred[2] if i%2==j%2 else qpred[3] for j in range(2*n)] for i in range(2*n)]
        for i in range(2*n):
            for j in range(2*n):
                assert_eq(sum((cov[i][k]*Q[k][j] for k in range(2*n)),F(0)),F(i==j))
        for k in (1,2,3):
            assert_eq((pred[k]>0), (k==3))
            assert_eq((qpred[k]>0), (k!=3))
print(f'EXACT_OK assertions={checks}')
