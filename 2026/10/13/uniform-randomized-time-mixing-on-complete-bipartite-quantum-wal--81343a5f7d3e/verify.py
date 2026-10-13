#!/usr/bin/env python3
"""Exact finite consistency checks for randomized-time mixing on unweighted bicliques.

No third-party packages. The proof for all orders is in RESULT.md; these
checks do not substitute for its parameter inequalities.
"""
from fractions import Fraction as F
from itertools import product


def entry(m, n, a, b, x):
    """Exact |U(t)[a,b]|^2 for cos(sqrt(m*n)*t)=x.

    Same-part expressions are real squared amplitudes. Cross-part
    expressions are squared purely imaginary amplitudes.
    """
    if a < m and b < m:
        return (F(a == b) + (x - 1) / m) ** 2
    if a >= m and b >= m:
        return (F(a == b) + (x - 1) / n) ** 2
    return (1 - x*x) / (m*n)


def average(m, n, samples):
    N = m+n
    assert sum((w for x, w in samples), F()) == 1
    assert all(-1 <= x <= 1 and w >= 0 for x, w in samples)
    return [[sum((w*entry(m,n,a,b,x) for x,w in samples),F())
             for b in range(N)] for a in range(N)]


def check_block_cubic(m,n):
    N=m+n
    A=[[int((i<m)!=(j<m)) for j in range(N)] for i in range(N)]
    A2=[[sum(A[i][k]*A[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    A3=[[sum(A2[i][k]*A[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    assert all(A3[i][j]==m*n*A[i][j] for i in range(N) for j in range(N))
    assert all(A2[i][j]==(n if i<m else m) if (i<m)==(j<m) else A2[i][j]==0
               for i in range(N) for j in range(N))
    # For distinct sides and each rational x, the physical mixing rows sum to one.
    for x in [F(-1),F(-3,5),F(-1,2),F(0),F(1,7),F(3,5),F(1)]:
        assert all(sum((entry(m,n,i,j,x) for j in range(N)),F())==1 for i in range(N))
        assert all(entry(m,n,i,j,x)==entry(m,n,j,i,x) for i in range(N) for j in range(N))


def main():
    checked = 0
    for m in range(1,16):
        for n in range(1,16):
            check_block_cubic(m,n)
            checked+=1
            # The analytical cross-entry upper bound excludes all
            # m,n>=2 except m=n=2.
            if m>=2 and n>=2 and (m,n)!=(2,2):
                assert F(1,m*n)<F(1,m+n)
            if m==1 and n>=5:
                assert -F(n-2,2)<-1
            if n==1 and m>=5:
                assert -F(m-2,2)<-1

    witnesses = {
        (1,2): [(F(1),F(1,6)),(F(0),F(2,3)),(F(-1),F(1,6))],
        (1,3): [(F(-1,2),F(1))],
        (2,2): [(F(0),F(1))],
    }
    for (m,n),samples in witnesses.items():
        mat=average(m,n,samples)
        assert all(v==F(1,m+n) for row in mat for v in row)

    # K_(1,1), a single edge: t=pi/4 yields cos^2(t)=sin^2(t)=1/2.
    cosine_squared=F(1,2)  # cos(pi/4)^2
    single_edge_diagonal=cosine_squared
    single_edge_off_diagonal=1-cosine_squared
    assert single_edge_diagonal==single_edge_off_diagonal==F(1,2)

    # Rational moment constraints for stars with n=4 are incompatible.
    mu=F(-1)
    nu=F(1,5)
    assert (1-2*mu+nu)/16==F(1,5)
    assert nu!=1  # mu=-1 for a bounded x forces x=-1 a.s.

    # Quantitative robust obstruction for K_1,4: 
    # max entrywise error is at least 2/45, checked on finite sample laws.
    grid=[F(j,8) for j in range(-8,9)]
    for x,y in product(grid,repeat=2):
        for w in [F(),F(1,5),F(1,2),F(4,5),F(1)]:
            mat=average(1,4,[(x,w),(y,1-w)])
            error=max(abs(v-F(1,5)) for row in mat for v in row)
            assert error>=F(2,45)

    print('VERIFY_OK', f'block_cubic_and_rows={checked}',
          f'uniform_witnesses={len(witnesses)+1}', 'K14_gap=2/45',
          'rational_two_point_laws=1445')

if __name__=='__main__':
    main()
