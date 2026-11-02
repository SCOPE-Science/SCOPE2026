"""Exact finite algebra check for the sum-system Dirichlet rational identity.

This program does not establish the infinite pole-replication or oscillation theorem.
"""
from math import factorial
from fractions import Fraction


def stirling_table(nmax):
    t = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    t[0][0] = 1
    for n in range(1, nmax + 1):
        for k in range(1, n + 1):
            t[n][k] = k * t[n - 1][k] + t[n - 1][k - 1]
    return t


def polynomial_product(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            z[i + j] += c * d
    return z


def check_stirling_generating_series():
    st = stirling_table(60)
    cases = 0
    for m in range(2, 11):
        q = [1]
        for j in range(1, m):
            q = polynomial_product(q, [1, -j])
        coeff = [0] * 61
        # Solve Q(z) B(z) = m! z^m coefficient by coefficient.
        for n in range(61):
            rhs = factorial(m) if n == m else 0
            coeff[n] = rhs - sum(q[k] * coeff[n-k] for k in range(1, min(n, len(q)-1) + 1))
            expected = factorial(m) * st[n-1][m-1] if n >= m else 0
            assert coeff[n] == expected, (m, n, coeff[n], expected)
            cases += 1
    return cases


def divisors_ge_two(n):
    return [d for d in range(2, n + 1) if n % d == 0]


def dirichlet_convolution(a, b, N):
    c = [0]*(N+1)
    for n in range(1, N+1):
        c[n] = sum(a[d]*b[n//d] for d in range(1,n+1) if n%d==0)
    return c


def check_coefficient_convolution():
    N=125
    z=[0]*(N+1)
    for n in range(2,N+1):z[n]=1
    basis=[[0]*(N+1) for _ in range(12)]
    basis[0][1]=1
    for k in range(1,12):
        basis[k]=dirichlet_convolution(basis[k-1],z,N)
    st=stirling_table(13)
    comparisons=0
    for m in range(2,8):
        q=[1]
        for j in range(1,m):q=polynomial_product(q,[1,-j])
        # Coefficients of the rational generating function Q(z)F(z)=m!z^m.
        # Recover Q^{-1} by exact recursive Dirichlet convolution.
        f=[0]*(N+1)
        for n in range(2,N+1):
            numerator=factorial(m)*basis[m][n]
            for h in range(1,len(q)):
                numerator-=q[h]*sum(basis[h][d]*f[n//d] for d in range(2,n+1) if n%d==0)
            f[n]=numerator
            direct=sum(factorial(m)*st[k-1][m-1]*basis[k][n] for k in range(m,12))
            assert f[n] == direct,(m,n,f[n],direct)
            comparisons+=1
    return comparisons


if __name__=='__main__':
    a=check_stirling_generating_series()
    b=check_coefficient_convolution()
    print(f'VERIFY_OK formal_coefficients={a} exact_dirichlet_coefficients={b} rational_arithmetic=yes')
