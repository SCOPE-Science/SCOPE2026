#!/usr/bin/env python3
"""Exact rational checks for fourth-order Padé positivity on paths and cycles.

Python 3 standard library only. The proof for all graph orders and timesteps
is mathematical; finite tests here detect algebra/implementation mistakes.
"""
from fractions import Fraction as F


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a):
    n = len(a)
    aug = [[F(v) for v in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(a)]
    for col in range(n):
        p = next((r for r in range(col, n) if aug[r][col]), None)
        assert p is not None, 'singular denominator'
        aug[col], aug[p] = aug[p], aug[col]
        pivot = aug[col][col]
        aug[col] = [v / pivot for v in aug[col]]
        for r in range(n):
            if r != col:
                v = aug[r][col]
                aug[r] = [u - v * w for u, w in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def laplacian(kind, n):
    l = [[F(0) for _ in range(n)] for _ in range(n)]
    edges = [(j, j + 1) for j in range(n - 1)]
    if kind == 'cycle':
        edges += [(0, n - 1)]
    for i, j in edges:
        l[i][i] += 1
        l[j][j] += 1
        l[i][j] -= 1
        l[j][i] -= 1
    return l


def pade(l, h):
    n = len(l)
    l2 = mm(l, l)
    den = [[F(12 * (i == j)) + 6*h*l[i][j] + h*h*l2[i][j]
            for j in range(n)] for i in range(n)]
    num = [[F(12 * (i == j)) - 6*h*l[i][j] + h*h*l2[i][j]
            for j in range(n)] for i in range(n)]
    return mm(num, inverse(den))


def resist(kind, n, i, j):
    d = abs(i-j)
    return F(d) if kind == 'path' else F(d*(n-d),n)


def green_entry(kind, n, i, j):
    ri = sum((resist(kind,n,i,k) for k in range(n)),F()) / n
    rj = sum((resist(kind,n,j,k) for k in range(n)),F()) / n
    rbar = sum((resist(kind,n,a,b) for a in range(n) for b in range(n)),F()) / (n*n)
    return -(resist(kind,n,i,j)-ri-rj+rbar)/2


def r(z):
    return (12-6*z+z*z)/(12+6*z+z*z)


def multipartite_sizes(sizes, h):
    n = sum(sizes)
    l = [[F(0) for j in range(n)] for i in range(n)]
    part = [k for k, size in enumerate(sizes) for _ in range(size)]
    for i in range(n):
        for j in range(i+1,n):
            if part[i]!=part[j]:
                l[i][i]+=1; l[j][j]+=1; l[i][j]-=1; l[j][i]-=1
    P=pade(l,h)
    for i in range(n):
        for j in range(n):
            if i != j:
                if part[i]!=part[j]:
                    expected=(1-r(n*h))/n
                else:
                    s=sizes[part[i]]; k=n-s
                    expected=F(12*k*h,s)*(F(1,k*k*h*h+6*k*h+12)-F(1,n*n*h*h+6*n*h+12))
                assert P[i][j]==expected,(sizes,i,j,P[i][j],expected)
            else:
                assert P[i][i]>0
        assert sum(P[i])==1
    return True


def main():
    counts={'exact_matrix_instances':0,'pseudoinverse_identities':0,'c5_kernel_identities':0,'multipartite_checks':0}
    times=[F(1,100),F(1,2),F(1),F(2),F(10),F(100)]
    for n in range(2,11):
        for kind in ('path', 'cycle'):
            if kind=='cycle' and n<3:continue
            for h in times:
                P=pade(laplacian(kind,n),h)
                assert all(sum(row)==1 for row in P)
                assert all(P[i][i]>0 for i in range(n))
                if kind=='path' and n<=3 or kind=='cycle' and n<=5:
                    assert all(v>=0 for row in P for v in row),(kind,n,h)
                counts['exact_matrix_instances']+=1
            value=green_entry(kind,n,0,1)
            if kind=='path':
                expected=F((n-1)*(2*n-7),6*n)
            else:
                expected=F((n-1)*(n-5),12*n)
            assert value==expected,(kind,n,value,expected)
            counts['pseudoinverse_identities']+=1
            if kind=='path' and n>=4 or kind=='cycle' and n>=6:
                P=pade(laplacian(kind,n),F(10000))
                assert P[0][1]<0,(kind,n,P[0][1])
                counts['exact_matrix_instances']+=1
    for h in [F(1,10),F(1),F(3),F(100),F(10000)]:
        P=pade(laplacian('cycle',5),h)
        d=25*h**4+150*h**3+360*h*h+360*h+144
        expected=[(25*h**4+30*h**3+72*h*h+72*h+144)/d,
                  72*h*(h+2)/d,
                  12*h*h*(5*h+6)/d]
        for i,j in enumerate([0,1,2]):assert P[0][j]==expected[i]
        counts['c5_kernel_identities']+=3
    for sizes in [(1,1),(1,2),(2,2),(1,1,1),(2,1,3),(1,2,3,1),(3,3,2)]:
        for h in [F(1,7),F(3),F(100)]:
            multipartite_sizes(sizes,h)
            counts['multipartite_checks']+=1
    print('VERIFY_OK',counts)

if __name__=='__main__':main()
