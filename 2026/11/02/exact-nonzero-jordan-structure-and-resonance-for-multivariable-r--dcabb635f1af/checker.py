"""Exact finite-dimensional tests of resonant Rhaly Jordan blocks."""
from fractions import Fraction
from math import comb
from itertools import product


def monomials(d, degree):
    if d == 1:
        return [(degree,)]
    return [(i,) + t for i in range(degree + 1)
            for t in monomials(d - 1, degree - i)]


def matrix(d, cutoff, q):
    import sympy as sp
    basis = [x for n in range(cutoff + 1) for x in monomials(d, n)]
    pos = {x: i for i, x in enumerate(basis)}
    A = sp.zeros(len(basis))
    for k, a in enumerate(basis):
        for n in range(sum(a), cutoff + 1):
            b = (a[0] + n - sum(a),) + a[1:]
            A[pos[b], k] = (n + 1)*sp.Rational(q.numerator,q.denominator)**n
    return A


def check():
    import sympy as sp
    cases = [(sp.Rational(1,2),0,1), (sp.Rational(2,3),1,2),
             (sp.Rational(3,4),2,3)]
    count = 0
    for d in (2,3):
        for q, n, m in cases:
            cut = m+1 if d==3 else m+2
            A=matrix(d,cut,q)
            lam=(n+1)*q**n
            N=A-lam*sp.eye(A.rows)
            geo=A.rows-N.rank()
            root2=A.rows-(N*N).rank()
            predgeo=comb(m+d-1,d-1)
            predalg=comb(n+d-1,d-1)+comb(m+d-1,d-1)
            assert geo==predgeo,(d,q,geo,predgeo)
            assert root2==predalg,(d,q,root2,predalg)
            count+=2
    # Three coincident diagonal levels, with non-monotone intervening entries.
    # The resulting Jordan sizes on transverse lines are 3, 2, 2, 1, 1.
    a=[2,3,2,4,2,sp.Rational(1,2),sp.Rational(1,4)]
    d=2; cutoff=6
    bs=[x for N in range(cutoff+1) for x in monomials(d,N)]
    idx={v:i for i,v in enumerate(bs)}
    T=sp.zeros(len(bs))
    for k, v in enumerate(bs):
        for N in range(sum(v),cutoff+1):
            w=(v[0]+N-sum(v),)+v[1:]
            T[idx[w],k]=a[N]
    B=T-2*sp.eye(T.rows)
    nulls=[T.rows-(B**k).rank() for k in (1,2,3,4)]
    assert nulls==[5,8,9,9],nulls
    count+=4
    print('CHECK_OK finite rational Jordan assertions:',count)

if __name__ == '__main__':
    check()
