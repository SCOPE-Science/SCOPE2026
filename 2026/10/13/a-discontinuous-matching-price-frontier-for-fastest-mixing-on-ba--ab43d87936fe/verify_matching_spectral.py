"""Exact rational checks for the matching-price algebraic-connectivity theorem.

All matrix and bound calculations use Python's standard-library Fraction.
Finite cases are checks, not a replacement for the quantified proof.
"""
from fractions import Fraction as F
from random import Random


def graph_laplacian(weights):
    n = len(weights)
    z = [[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            w = weights[i][j]
            z[i][i] += w
            z[n+j][n+j] += w
            z[i][n+j] -= w
            z[n+j][i] -= w
    return z


def matvec(mat, vec):
    return [sum(x*y for x,y in zip(row,vec)) for row in mat]


def check_eigen(mat, vec, lam):
    assert matvec(mat,vec) == [lam*v for v in vec]


def spectrum_test(n, a, b):
    assert n >= 3 and a >= 0 and b > 0
    weights = [[a if i==j else b for j in range(n)] for i in range(n)]
    L = graph_laplacian(weights)
    s = a+(n-1)*b
    ones = [F(1)]*(2*n)
    check_eigen(L, ones, F(0))
    check_eigen(L, [F(1)]*n+[-F(1)]*n, 2*s)
    for k in range(n-1):
        x = [F(0)]*n
        x[k]=F(1);x[k+1]=F(-1)
        check_eigen(L, x+x, n*b)
        check_eigen(L, x+[-v for v in x], 2*a+(n-2)*b)
    assert sum(L[i][i] for i in range(2*n)) == 2*s*n
    return 2*n-1


def upper_bounds(weights):
    n = len(weights)
    A = sum(weights[i][i] for i in range(n))
    B = sum(weights[i][j] for i in range(n) for j in range(n) if i!=j)
    fplus = B/F(n-1)
    fminus = (2*(n-1)*A+(n-2)*B)/F(n*(n-1))
    return A,B,fplus,fminus


def opt(n,t):
    critical = F(2*(n-1),n-2)
    if t < critical:
        v = F(1,n*(t+n-1))
        return v,v,F(1,t+n-1)
    if t > critical:
        return F(0),F(1,n*(n-1)),F(n-2,n*(n-1))
    return F(0),F(1,n*(n-1)),F(n-2,n*(n-1))


def run():
    rng = Random(2027)
    exact_spectra = 0
    exact_rayleigh = 0
    exact_feasible = 0
    critical_cases = 0
    for n in range(3,10):
        critical = F(2*(n-1),n-2)
        ts = [F(1,4),F(1),F(3,2),F(2),critical-F(1,9),
              critical,critical+F(1,9),F(5),F(8)]
        for t in ts:
            a,b,value = opt(n,t)
            assert n*t*a+n*(n-1)*b == 1
            assert min(n*b,2*a+(n-2)*b) == value
            exact_spectra += spectrum_test(n,a,b)
            W = [[a if i==j else b for j in range(n)] for i in range(n)]
            AA,BB,fp,fm=upper_bounds(W)
            assert min(fp,fm)==value
            exact_rayleigh += 2
            if t==critical:
                for r in [F(0),F(1,5),F(1,2),F(1)]:
                    bx=F(1,n*(t*r+n-1));ax=r*bx
                    assert n*t*ax+n*(n-1)*bx==1
                    assert min(n*bx,2*ax+(n-2)*bx)==value
                    spectrum_test(n,ax,bx)
                    critical_cases += 1
            for _ in range(20):
                W = [[F(rng.randint(1,23)) for j in range(n)] for i in range(n)]
                budget=sum((t if i==j else 1)*W[i][j] for i in range(n) for j in range(n))
                W=[[v/budget for v in row] for row in W]
                AA,BB,fp,fm=upper_bounds(W)
                assert t*AA+BB==1
                assert min(fp,fm)<=value
                exact_feasible+=1
    n=3;t=F(3)
    a,b,l=opt(n,t)
    assert (a,b,l)==(F(1,15),F(1,15),F(1,5))
    assert F(1,5)>F(1,6)
    print('VERIFY_OK',exact_spectra,'exact eigenvector equations;',
          exact_rayleigh,'projector bounds;',
          exact_feasible,'feasible-allocation certificates;',
          critical_cases,'critical-family spectra')


if __name__=='__main__':
    run()
