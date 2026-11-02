"""Finite exact and reproducible numerical checks for a random-knot P1 Poisson benchmark.

The infinite-dimensional limits and moment thresholds require the analytic arguments
in RESULT.md; these checks are deliberately not treated as proofs of limit laws.
"""
from fractions import Fraction as F
from math import factorial, pi
from random import Random


def dot(A, x):
    return [sum(row[j]*x[j] for j in range(len(x))) for row in A]


def trial(knots):
    n=len(knots)-1
    h=[knots[i+1]-knots[i] for i in range(n)]
    A=[[F(0) for _ in range(n-1)] for _ in range(n-1)]
    for j in range(n-1):
        A[j][j]=1/h[j]+1/h[j+1]
        if j+1<n-1:
            A[j][j+1]=A[j+1][j]=-1/h[j+1]
    rhs=[(h[j]+h[j+1])/2 for j in range(n-1)]
    u=[knots[j]*(1-knots[j])/2 for j in range(1,n)]
    assert dot(A,u)==rhs
    err=sum(a**3 for a in h)/12
    assert err>=0
    return err


def moment_check(n):
    # Dirichlet(1,...,1) mixed moments, from the beta-function formula.
    rise=1
    for j in range(6): rise*=n+j
    mom3=F(6,(n+1)*(n+2))
    momsq=F(36*n*(n+19),rise)
    var1=(momsq-mom3*mom3)/144
    var2=F((n-1)*(5*n+11),2*(n+1)**2*(n+2)**2*(n+3)*(n+4)*(n+5))
    assert var1==var2, (n,var1,var2)
    assert mom3/12==F(1,2*(n+1)*(n+2))


def numerical_limit_probe():
    try:
        import numpy as np
        from scipy.linalg import eigh_tridiagonal
    except ImportError:
        print('SCIPY_OPTIONAL_CHECK_SKIPPED')
        return
    rng=np.random.default_rng(31015)
    n=250
    values=[]
    for _ in range(100):
        e=rng.exponential(size=n)
        w=e.sum()/e
        d=w[:-1]+w[1:]
        o=-w[1:-1]
        a=eigh_tridiagonal(d,o,select='i',select_range=(0,0),eigvals_only=True)[0]
        b=eigh_tridiagonal(d,o,select='i',select_range=(n-2,n-2),eigvals_only=True)[0]
        values.append((n*a, b/n**2, (b/a)/n**3, n**2*sum((e/e.sum())**3)/12))
    med=np.median(np.array(values),axis=0)
    assert 8.5<med[0]<11.5
    assert 1.<med[1]<8.
    assert .09<med[2]<.85
    assert .42<med[3]<.56
    print('NUMERICAL_MEDIANS', ','.join(f'{v:.8g}' for v in med))
    print('TARGETS', pi*pi, 2/np.log(2), 2/(pi*pi*np.log(2)), .5)


def main():
    r=Random(51509)
    ct=0
    for n in range(2,13):
        for _ in range(50):
            interior=sorted(r.sample(range(1,997),n-1))
            knots=[F(0)]+[F(j,997) for j in interior]+[F(1)]
            trial(knots)
            ct+=1
    for n in range(1,151):
        moment_check(n)
    # One-cell and one-interior-node boundary cases.
    assert trial([F(0),F(1)]) == F(1,12)
    assert trial([F(0),F(1,2),F(1)]) == F(1,48)
    numerical_limit_probe()
    print('CHECK_OK',ct,'exact Galerkin systems;',150,'exact Dirichlet moment identities')

if __name__=='__main__':
    main()
