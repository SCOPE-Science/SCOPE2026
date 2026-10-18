"""Reproduce finite-dimensional checks for the sharp interval-functional theorem.
Requires Python 3 and numpy. Uses exact rational algebra for the symbolic
weights and floating-point eigenvalues only as supplementary spot checks.
"""
from fractions import Fraction
from math import sqrt
import random
import numpy as np

checks = 0
for k in range(1, 121):
    N = k + 1
    m, n = (N + 1) // 2, N // 2
    if k % 2:
        c = [Fraction(2 if i % 2 == 0 else 0, 1) for i in range(k)]
        r = [Fraction(1, 1) for _ in range(N)]
        r2 = Fraction(2, 1)   # twice-eigenvalue equation factor
    else:
        q = k // 2
        # Write c_i = alpha*d_i, and x_even/x_odd = alpha,
        # where alpha**2=q/(q+1). Verify eigen equations rationally.
        a2 = Fraction(q, q + 1)
        d = []
        for j in range(q):
            d.extend([Fraction(2 * (q-j),q), Fraction(2 * (j+1),q)])
        for j in range(N):
            if j % 2 == 0:
                # (c_(j-1)+c_j) x_odd = 2 x_even;
                # with c=alpha*d, x_even=alpha*x_odd.
                left = (d[j-1] if j else 0) + (d[j] if j < k else 0)
                assert left == 2
            else:
                # (c_(j-1)+c_j) x_even = 2 x_odd.
                left = d[j-1] + d[j]
                assert a2 * left == 2
            checks += 1
        c = [float(sqrt(float(a2))*z) for z in d]
    M = np.zeros((N,N))
    for i, z in enumerate(c):
        M[i, i+1] = M[i+1, i] = float(z)/2
    radius = float(np.linalg.eigvalsh(M)[-1])
    constant = 2 * sqrt(m*n)
    assert abs(radius - 1) < 2e-12, (k, radius)
    assert abs(sum(c)-constant) < 2e-12, (k, sum(c), constant)
    checks += 2

random.seed(781364)
for k in range(1, 15):
    N=k+1
    m,n=(N+1)//2,N//2
    constant=2*sqrt(m*n)
    for _ in range(200):
        a=[random.random()*2 for _ in range(k)]
        M=np.zeros((N,N))
        for i,z in enumerate(a): M[i,i+1]=M[i+1,i]=z/2
        radius=float(np.linalg.eigvalsh(M)[-1])
        assert sum(a) <= constant*radius+3e-12
        checks+=1
print(f'PASS: {checks} exact-equation, extremizer eigenvalue, and sample inequality checks')
