"""Exact integer verification of the Laplacian factorization for uniform clique bouquets.
Python 3.8+, standard library only. Run: python3 verify_laplacian.py
"""
from itertools import combinations, product
from math import comb


def bases(r, m):
    # -1 is the shared vertex; other parts consist of consecutive labels.
    parts = [(-1,)] + [tuple(i*m+j for j in range(m)) for i in range(r)]
    return [frozenset(x) for I in combinations(range(r+1), r)
            for x in product(*(parts[i] for i in I))]


def laplacian(r, m):
    bs = bases(r, m)
    n = len(bs)
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if len(bs[i].intersection(bs[j])) == r-1:
                a[i][j] = a[j][i] = -1
    for i in range(n):
        a[i][i] = -sum(a[i])
    return a


def bareiss(mat):
    # Exact fraction-free Gaussian elimination; pivoting is sign-aware.
    a = [row[:] for row in mat]
    n = len(a)
    if n == 0:
        return 1
    den = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k+1,n) if a[i][k] != 0), None)
            if pivot is None:
                return 0
            a[k],a[pivot] = a[pivot],a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k+1,n):
            ik = a[i][k]
            for j in range(k+1,n):
                numer = a[i][j]*p-ik*a[k][j]
                assert numer % den == 0
                a[i][j] = numer // den
            a[i][k] = 0
        den = p
    return sign*a[-1][-1]


def predicted_det_shift(r,m,u):
    # det(L+u I), including the zero mode u.
    val = u*(u+r+m)*((u+(r+1)*m)**(r-1))
    for t in range(1,r):
        multiplicity = comb(r,t)*(m-1)**t
        q = u*u+(r+(3*t+1)*m)*u + m*t*(2*r+1+(2*t+1)*m)
        val *= q**multiplicity
        val *= ((u+(r+t+1)*m)**(multiplicity*(r-t-1)))
    val *= (u+r*(m+1))**((m-1)**r)
    return val


def predicted_trees(r,m):
    value=(r+1)**(r-1)*(r*(m+1))**((m-1)**r)
    for t in range(1,r):
        mult=comb(r,t)*(m-1)**t
        value *= (m*t*(2*r+1+(2*t+1)*m))**mult
        value *= ((r+t+1)*m)**(mult*(r-t-1))
    return value


def check(r,m):
    L=laplacian(r,m)
    n=len(L)
    assert n == m**(r-1)*(m+r)
    assert all(sum(row)==0 for row in L)
    assert all(L[i][j]==L[j][i] for i in range(n) for j in range(n))
    for u in (1,2,5):
        actual=bareiss([[L[i][j]+(u if i==j else 0) for j in range(n)]
                        for i in range(n)])
        expect=predicted_det_shift(r,m,u)
        assert actual==expect,(r,m,u,actual,expect)
    actual_tree=bareiss([row[:-1] for row in L[:-1]])
    expect_tree=predicted_trees(r,m)
    assert actual_tree==expect_tree,(r,m,actual_tree,expect_tree)
    print('OK r={} m={} vertices={} determinant_tests=3 spanning_tree_digits={}'.format(
          r,m,n,len(str(actual_tree))))


if __name__=='__main__':
    for rm in ((2,2),(2,3),(3,2),(3,3),(4,2)):
        check(*rm)
    print('LAPLACIAN_VERIFICATION_OK')
