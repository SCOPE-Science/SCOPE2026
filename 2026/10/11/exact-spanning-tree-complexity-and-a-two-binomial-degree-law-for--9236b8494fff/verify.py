"""Reproduce exact spanning-tree identities for a punctured ternary grid.

Python 3 standard library only.  This is finite corroboration of a general proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def determinant(a):
    """Fraction-free exact Bareiss determinant of an integer matrix."""
    a = [row[:] for row in a]
    n = len(a)
    if n == 0:
        return 1
    last, sign = 1, 1
    for k in range(n-1):
        if not a[k][k]:
            p = next((p for p in range(k+1,n) if a[p][k]), None)
            if p is None:
                return 0
            a[p],a[k] = a[k],a[p]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            x = a[i][k]
            for j in range(k+1,n):
                numerator = pivot*a[i][j]-x*a[k][j]
                quotient,remainder = divmod(numerator,last)
                assert remainder == 0
                a[i][j] = quotient
            a[i][k] = 0
        last = pivot
    return sign*a[-1][-1]


def base_trees(m):
    p = 1
    for a in range(m+1):
        for b in range(m-a+1):
            if a+b:
                exponent = factorial(m)//(factorial(a)*factorial(b)*factorial(m-a-b))
                p *= (a+3*b)**exponent
    assert p%(3**m) == 0
    return p//(3**m)


def alpha(m):
    return sum((Fraction(comb(m-1,k)*2**k,3**(m-1)*(3*k+1))
                for k in range(m)), Fraction(0))


def beta(m):
    return (1-Fraction(1,3**(m-1)))/ (2*(m-1))


def weighted_prediction(m,t):
    a,b=alpha(m),beta(m)
    z=Fraction(base_trees(m))*t*(1-a+a*t)**m*(1-b+b*t)**(m-1)
    assert z.denominator==1
    return z.numerator


def punctured_prediction(m):
    a,b=alpha(m),beta(m)
    z=Fraction(base_trees(m),2*m)*(1-a)**m*(1-b)**(m-1)
    assert z.denominator==1
    return z.numerator


def graph(m):
    vv=[s for s in product((-1,0,1),repeat=m) if any(s)]
    ix={v:i for i,v in enumerate(vv)}
    es=[]
    for i,u in enumerate(vv):
        for j in range(m):
            for q in (-1,0,1):
                if abs(u[j]-q)==1:
                    v=list(u);v[j]=q;v=tuple(v)
                    if v in ix and i<ix[v]:
                        es.append((i,ix[v]))
    return vv,es


def reduced_laplacian(m, center_edge_weight=None):
    """Ground first nonzero vertex (punctured graph) or deleted center (full graph).

    For center_edge_weight=t, connect all 2m unit vectors to the central
    grounded vertex with weight t. For None, use punctured graph and
    delete the last nonzero vertex for an independent Kirchhoff minor.
    """
    vv,es=graph(m)
    n=len(vv)
    size=n if center_edge_weight is not None else n-1
    a=[[0]*size for _ in range(size)]
    for i,j in es:
        if i<size: a[i][i]+=1
        if j<size: a[j][j]+=1
        if i<size and j<size:
            a[i][j]-=1
            a[j][i]-=1
    if center_edge_weight is not None:
        for i,v in enumerate(vv):
            if sum(x!=0 for x in v)==1:
                a[i][i]+=center_edge_weight
    return a,len(es)


def check():
    for m in range(2,5):
        matrix,edges=reduced_laplacian(m)
        direct=determinant(matrix)
        assert direct==punctured_prediction(m)
        print(f'm={m} |V|={3**m-1} |E|={edges} alpha={alpha(m)} beta={beta(m)} punctured_trees={direct}')
        for t in range(0,2*m+2):
            matrix,_=reduced_laplacian(m,t)
            direct_weighted=determinant(matrix)
            assert direct_weighted==weighted_prediction(m,t), (m,t)
        print(f'  UST central-degree polynomial agrees with weighted cofactors for t=0,...,{2*m+1}')
    print('VERIFY_OK exact Bareiss minors, all stated sample values, and weighted tree polynomials')

if __name__=='__main__':
    check()
