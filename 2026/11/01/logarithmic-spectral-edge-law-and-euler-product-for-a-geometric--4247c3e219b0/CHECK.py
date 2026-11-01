"""Supplementary exact arithmetic checks for the geometric random-walk Jacobi spectrum.

Run with Python 3.10+; uses only the standard library. The infinite-dimensional
assertions are proved analytically in RESULT.md, not by this finite checker.
"""
from fractions import Fraction as F
from math import prod, isclose

checks = 0
for q_int in (5, 6, 8, 11):
    q = F(q_int)
    N = 24
    c = lambda n: (1-q**(-n)) if n % 2 else q**(-n)
    a = lambda n: 1-c(n)
    h = [F(1)]
    for n in range(1,2*N+2):
        h.append(h[-1] * (F(1) if n == 1 else a(n-1)) / c(n))
    beta2 = [(1-q**(-1)) if k == 0 else (1-q**(-2*k))*(1-q**(-(2*k+1))) for k in range(N)]
    gamma2 = [q**(-(4*k+3)) for k in range(N)]
    for k in range(N):
        assert beta2[k] == a(2*k)*c(2*k+1) if k else beta2[k] == c(1)
        checks += 1
        assert gamma2[k] == a(2*k+1)*c(2*k+2)
        checks += 1
        if k >= 1:
            assert h[2*k] == q**(k+1)/(q-1) * prod((1-q**(-2*j))/(1-q**(-(2*j+1))) for j in range(1,k))
            checks += 1
    ds = [1-beta2[0]] + [1-beta2[k]-gamma2[k-1] for k in range(1,N)]
    assert all(t > 0 for t in ds)
    checks += 1
    for k in range(1,N):
        assert ds[k] == (1+1/q)*q**(-2*k)-(q+1/q)*q**(-4*k)
        checks += 1
    tr = (q*q+q-1)/(q*(q*q-1))
    # Error from omitting the last diagonal terms is bounded by a geometric series.
    assert 0 < tr - sum(ds) < (1+1/q)*q**(-2*N)/(1-q**(-2))
    checks += 1
    product_beta2 = prod(beta2)
    finite_euler = prod(1-q**(-n) for n in range(1,2*N))
    assert product_beta2 == finite_euler
    checks += 1
    tail_factor = prod(F(1)-q**(-n) for n in range(2*N,4*N))
    assert 0 < finite_euler*(1-tail_factor) < F(1,10**30)
    checks += 1
print('CHECK_OK', checks)
