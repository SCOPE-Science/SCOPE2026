"""Exact-rational checks for scalar affine companion-GMRES residual identities.

Only Python standard library is needed. Finite checks corroborate, not prove,
claims about all iteration counts or asymptotic regimes.
"""
from fractions import Fraction as F


def solve(a, b):
    n = len(b)
    T = [list(a[i]) + [b[i]] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if T[i][k] != 0)
        T[k], T[pivot] = T[pivot], T[k]
        d = T[k][k]
        T[k] = [x / d for x in T[k]]
        for i in range(n):
            if i != k:
                fac = T[i][k]
                T[i] = [T[i][j] - fac * T[k][j] for j in range(n + 1)]
    return [T[i][-1] for i in range(n)]


def check(m, a, s):
    M = [[F(0) for _ in range(m)] for _ in range(m+1)]
    for j in range(m):
        M[j][j] = F(1) + (a*s if j == 1 else F(0))
        M[j+1][j] = -s
    G = [[sum(M[k][i]*M[k][j] for k in range(m+1))
          for j in range(m)] for i in range(m)]
    h = [M[0][i] for i in range(m)]
    y = solve(G,h)
    residual = [int(k==0)-sum(M[k][j]*y[j] for j in range(m))
                for k in range(m+1)]
    W = F(1)+s**(-2) + (F(1)+a*s)**2 * sum((s**(-2*j) for j in range(2,m+1)),F(0))
    w = [F(1),1/s]+[(1+a*s)*s**(-j) for j in range(2,m+1)]
    assert residual == [z/W for z in w]
    assert sum(z*z for z in residual) == 1/W
    x = y[0] - (a*y[1] if m>1 else F(0))
    phys = F(1)-(F(1)+a*s)*x
    assert phys == (1-a/s)/W
    assert (phys == 0) == (a==s)
    return 1


def main():
    count=0
    for m in range(1,9):
        for a in [F(1,5), F(1,2), F(1), F(3,2), F(2), F(3)]:
            for s in [F(1,3), F(1,2), F(1), F(3,2), F(2), F(3)]:
                count+=check(m,a,s)
    print(f'PASS: {count} exact-rational independent normal-equation and recovery checks')

if __name__=='__main__':
    main()
