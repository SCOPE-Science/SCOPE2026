"""Exact, dependency-free checks for priced triangulations of complete graphs.

Run: python3 verify.py
The theorem's all-size proof is in RESULT.md; this is finite independent
matrix and arithmetic verification, not an infinite certificate.
"""
from fractions import Fraction as F
from itertools import combinations


def inverse(a):
    size = len(a)
    aug = [row[:] + [F(i == j) for j in range(size)] for i, row in enumerate(a)]
    for j in range(size):
        pivot = next((i for i in range(j, size) if aug[i][j]), None)
        assert pivot is not None
        aug[j], aug[pivot] = aug[pivot], aug[j]
        scale = aug[j][j]
        aug[j] = [z / scale for z in aug[j]]
        for i in range(size):
            if i != j and aug[i][j]:
                c = aug[i][j]
                aug[i] = [a - c * b for a, b in zip(aug[i], aug[j])]
    return [r[size:] for r in aug]


def trace_laplacian_pseudoinverse(n, x, y):
    edges = list(combinations(range(n), 2))
    m = len(edges)
    total = n + m
    L = [[F(0) for _ in range(total)] for _ in range(total)]
    def add_edge(i, j, z):
        for a, b, factor in ((i, i, 1), (j, j, 1), (i, j, -1), (j, i, -1)):
            L[a][b] += factor * z
    for k, (i, j) in enumerate(edges):
        add_edge(i, j, x)
        add_edge(i, n+k, y)
        add_edge(j, n+k, y)
    M = [[L[i][j] + F(1,total) for j in range(total)] for i in range(total)]
    inv = inverse(M)
    return sum(inv[i][i] for i in range(total)) - 1


def formula(n, x, y):
    m = n*(n-1)//2
    A = F(m-1,2) + F(1,n+1)
    C = F((n-1)*(n+2),2*n)
    return (A+C/(1+2*x/y))/y


def threshold(n):
    return F(8*(n+1), n*n+n+2)


def verify():
    check_count = 0
    for n in range(3, 7):
        for x,y in ((F(0),F(1)),(F(1,3),F(2,5)),(F(4,3),F(3,2))):
            assert trace_laplacian_pseudoinverse(n,x,y) == formula(n,x,y)
            check_count += 1
    for n in range(3, 101):
        m = n*(n-1)//2
        A = F(m-1,2)+F(1,n+1)
        C = F((n-1)*(n+2),2*n)
        assert 4*C/(A+C) == threshold(n)
        assert C/A == F(2*(n+1),n*(n-1))
        check_count += 2
    assert all(threshold(n)>1 for n in range(3,8))
    assert all(threshold(n)<1 for n in range(8,101))
    check_count += 2
    # Exact boundary derivative: P A + C(P-4Q) at t=0.
    for n in range(3, 101):
        m = n*(n-1)//2
        A = F(m-1,2)+F(1,n+1)
        C = F((n-1)*(n+2),2*n)
        P,Q = threshold(n),F(1)
        assert P*A + C*(P-4*Q) == 0
        check_count += 1
    print('PASS:',check_count,'exact arithmetic and full-matrix comparisons')


if __name__ == '__main__':
    verify()
