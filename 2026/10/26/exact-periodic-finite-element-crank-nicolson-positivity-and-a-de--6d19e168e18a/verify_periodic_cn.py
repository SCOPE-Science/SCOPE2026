"""Standalone finite checks for the exact periodic P1-FEM Crank--Nicolson theorem.

Standard library only. This script checks finite examples and identities;
the unbounded-in-n assertions require the analytic proof in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, pi, sqrt


def inverse(A):
    n = len(A)
    W = [[F(a) for a in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(A)]
    for i in range(n):
        k = next(k for k in range(i, n) if W[k][i])
        W[i], W[k] = W[k], W[i]
        pivot = W[i][i]
        W[i] = [x / pivot for x in W[i]]
        for j in range(n):
            if j != i:
                s = W[j][i]
                if s:
                    W[j] = [a - s*b for a,b in zip(W[j], W[i])]
    return [row[n:] for row in W]


def matrices(n, r):
    r = F(r)
    m = [[F(4 if i == j else 0) for j in range(n)] for i in range(n)]
    k = [[F(2 if i == j else 0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in ((i-1) % n, (i+1) % n):
            m[i][j] += 1
            k[i][j] -= 1
    a = [[m[i][j]+3*r*k[i][j] for j in range(n)] for i in range(n)]
    b = [[m[i][j]-3*r*k[i][j] for j in range(n)] for i in range(n)]
    ai = inverse(a)
    p = [[sum(ai[i][q]*b[q][j] for q in range(n)) for j in range(n)] for i in range(n)]
    return a, ai, p


def spectral_return(n, r):
    total=0.0
    for j in range(n):
        cs=cos(2*pi*j/n)
        m=4+2*cs
        k=2-2*cs
        total+=(m-3*r*k)/(m+3*r*k)
    return total/n


def threshold(n):
    lo,hi=1/3,5.
    for _ in range(70):
        mid=(lo+hi)/2
        if spectral_return(n,mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def test():
    cases=0
    rows=[]
    rinfty=(5+sqrt(33))/12
    assert abs(rinfty - 0.895380220544836)<1e-14
    for n in range(3,14):
        rho=threshold(n)
        assert rho>rinfty
        if n>3:
            assert rho < threshold(n-1)
        rows.append((n,rho))
        rs = [F(0), F(1,100),F(1,12),F(1,6),F(1,3),F(1,2),F(2,3),F(4,5),F(9,10),F(1),F(4)]
        for r in rs:
            a, ai, p = matrices(n,r)
            predicted = r == 0 or (n == 3 and r <= 1) or (n>=4 and F(1,3)<=r and float(r)<rho)
            observed=all(x>=0 for row in p for x in row)
            assert predicted==observed,(n,r,predicted,observed)
            assert sum(p[0])==1
            assert all(p[i][j]==p[(i+1)%n][(j+1)%n] for i in range(n) for j in range(n))
            assert abs(float(p[0][0])-spectral_return(n,float(r)))<2e-12
            if n>=4 and 0<r<F(1,3):
                assert p[0][2]<0
            if n>=4 and r>=F(1,3):
                assert all(p[0][j]>=0 for j in range(1,n))
            cases+=1
    for n,rho in rows:
        print('n=%2d, upper_r=%.12f' % (n,rho))
    print('exact-rational matrices:',cases,'; limit=',format(rinfty,'.15f'))

if __name__ == '__main__':
    test()
