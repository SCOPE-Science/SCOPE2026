"""Exact finite checks for chronological cyclic transmission; Python standard library.

This is a reproducibility cross-check, not a proof for all dimensions.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb


def matmul(a,b):
    n=len(a)
    return [[sum(a[i][m]*b[m][j] for m in range(n)) for j in range(n)] for i in range(n)]


def diag(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]


def monodromy(n,aa,order):
    q=diag(n)
    for i in order:
        f=diag(n)
        f[(i+1)%n][i]+=aa[i]
        q=matmul(f,q)
    return q


def poly_coeff(q):
    n=len(q)
    b=diag(n)
    result=[F(1)]
    for j in range(1,n+1):
        qb=matmul(q,b)
        c=-sum(qb[i][i] for i in range(n))/j
        result.append(c)
        b=[[qb[i][k]+(c if i==k else 0) for k in range(n)] for i in range(n)]
    return result


def cyclic_ascents(order):
    n=len(order)
    pos={a:p for p,a in enumerate(order)}
    return sum(pos[i]<pos[(i+1)%n] for i in range(n))


def exact_checks():
    tested=0
    for n in range(2,6):
        aa=[F(i+2,i+3) for i in range(n)]
        prod=F(1)
        for a in aa: prod*=a
        for order in permutations(range(n)):
            k=cyclic_ascents(order)
            actual=poly_coeff(monodromy(n,aa,order))
            expected=[F((-1)**j*comb(n,j)) for j in range(n+1)]
            expected[n-k]-=prod
            assert actual==expected,(n,order,k,actual,expected)
            tested+=1
    assert tested==152
    n=3
    aa=[F(2,3)]*3
    p=F(8,27)
    assert cyclic_ascents((0,1,2))==2
    assert cyclic_ascents((2,1,0))==1
    assert p>F(1,4) and p<F(1,2)
    from math import log
    assert log(2)>2/3  # analytic inequality is proved in RESULT.md
    print('PASS: 152 exact permutation characteristic-polynomial checks, n=2..5')
    print('PASS: 3-season example, P=8/27 between 1/4 and 1/2')

if __name__=='__main__': exact_checks()
