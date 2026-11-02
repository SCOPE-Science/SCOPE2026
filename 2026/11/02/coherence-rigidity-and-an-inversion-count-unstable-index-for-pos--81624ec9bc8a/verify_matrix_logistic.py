#!/usr/bin/env python3
"""Exact rational witnesses for fixed points and Hermitian linearizations of a positive matrix logistic map.

Runs with Python 3 standard library only.  Infinite-dimensional-parameter classification
and exact all-N index formula follow from the proof, not finite computations.
"""
from fractions import Fraction as F
from itertools import combinations


def zero(n):
    return [[F(0) for j in range(n)] for i in range(n)]


def eye(n):
    m = zero(n)
    for i in range(n): m[i][i] = F(1)
    return m


def add(a,b):
    return [[x+y for x,y in zip(row,other)] for row,other in zip(a,b)]


def neg(a):
    return [[-x for x in row] for row in a]


def sub(a,b):
    return add(a,neg(b))


def mul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]


def sc(c,a):
    return [[c*x for x in row] for row in a]


def tr(a):
    return [list(x) for x in zip(*a)]


def diag(xs):
    m=zero(len(xs))
    for i,x in enumerate(xs): m[i][i]=x
    return m


def conj(q,x):
    return mul(mul(q,x),tr(q))


def dyn(b,h):
    return mul(mul(b,mul(h,sub(eye(len(h)),h))),b)


def differential(b,h,e):
    return mul(mul(b,sub(e,add(mul(h,e),mul(e,h)))),b)


def principal_checks():
    n=3
    v=[F(1),F(2),F(2)]
    q=[[F(i==j)-F(2,9)*v[i]*v[j] for j in range(n)] for i in range(n)]
    assert mul(q,tr(q)) == eye(n)
    bs=[F(6,5), F(7,5), F(8,5)]
    a=[z*z for z in bs]
    assert all(F(1)<z<F(3) for z in a) and a==sorted(a) and len(set(a))==n
    b=conj(q,diag(bs))
    assert b == tr(b)
    cnt=0
    index_table=[]
    for bitmask in range(1<<n):
        selected={i for i in range(n) if (bitmask>>i)&1}
        h=[F(1)-1/a[i] if i in selected else F(0) for i in range(n)]
        H=conj(q,diag(h))
        assert dyn(b,H)==H, (selected,'fixed_point')
        assert mul(b,H)==mul(H,b)
        multipliers=[]
        for i in range(n):
            e=zero(n);e[i][i]=1
            E=conj(q,e)
            lam=a[i]*(1-2*h[i])
            assert differential(b,H,E)==sc(lam,E),(selected,'diag',i)
            multipliers.append(lam)
        for i,j in combinations(range(n),2):
            lam=bs[i]*bs[j]*(1-h[i]-h[j])
            for sign in (1,-1):
                e=zero(n);e[i][j]=1;e[j][i]=sign
                E=conj(q,e)
                assert differential(b,H,E)==sc(lam,E),(selected,'offdiag',i,j,sign)
                multipliers.append(lam)
        assert len(multipliers)==n*n
        assert all(abs(lam)!=1 for lam in multipliers)
        unstable=sum(abs(lam)>1 for lam in multipliers)
        missing=[j for j in range(n) if j not in selected]
        inversions=sum(a[j]>a[i] for i in selected for j in missing)
        predicted=len(missing)**2+2*inversions
        assert unstable==predicted, (selected,unstable,predicted)
        index_table.append((bitmask,unstable))
        cnt+=1
    assert dict(index_table)=={0:9,1:8,2:6,3:5,4:4,5:3,6:1,7:0},index_table
    print('PASS exact rational checks for all',cnt,'isolated equilibria in N=3; 8 x 9 real Hermitian mode checks; index values',index_table)


def degeneracy_checks():
    # An off-diagonal rank-one projector in a repeated-eigenvalue block.
    beta=[F(3,2),F(3,2),F(5,4)]
    b=diag(beta)
    p=zero(3)
    p[0][0]=F(9,25);p[0][1]=F(12,25)
    p[1][0]=F(12,25);p[1][1]=F(16,25)
    assert mul(p,p)==p
    h=sc(F(5,9),p)
    assert h[0][1] != 0
    assert dyn(b,h)==h
    assert mul(b,h)==mul(h,b)
    print('PASS exact degenerate-eigenspace Grassmannian projection witness')


def mixed_spectral_checks():
    # The spectral sink works across the activation threshold beta^2=1.
    for beta in ([F(4,5), F(6,5), F(8,5)],
                 [F(2,3), F(3,4), F(6,5)]):
        a=[t*t for t in beta]
        hs=[(F(1)-1/z if z>1 else F(0)) for z in a]
        b=diag(beta);h=diag(hs); n=len(beta)
        assert dyn(b,h)==h
        weights=[]
        for i in range(n):
            weights.append(a[i]*(1-2*hs[i]))
            for j in range(i+1,n):
                weights.extend([beta[i]*beta[j]*(1-hs[i]-hs[j])]*2)
        assert len(weights)==n*n
        assert max(abs(z) for z in weights)<1,weights
    # Any gain beta^2>3 forbids a linearly attracting equilibrium:
    # activation has multiplier 2-beta^2, and omission has beta^2.
    for beta in [F(2),F(5,2)]:
        a=beta*beta
        assert a>3 and (abs(a)>1 and abs(2-a)>1)
    # At beta^2=1 the eigenmode has multiplier exactly +1.
    assert F(1)*(1-2*F(0))==1
    print('PASS mixed subcritical-gain sinks and exact gain-boundary multipliers')


if __name__=='__main__':
    principal_checks()
    degeneracy_checks()
    mixed_spectral_checks()
    print('All exact rational checks passed.')
