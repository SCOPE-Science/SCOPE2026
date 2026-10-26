#!/usr/bin/env python3
"""Separate exact-arithmetic checks for correlated-switching active dimer formulas.

Python >= 3.9, standard library only. Each calculation is for finite, named
parameter choices; the associated proof establishes the general statements.
"""
from fractions import Fraction as F
from math import exp


def matrices(k, rate, c, chi):
    one = F(1)
    delta = one-chi
    mono = [[-2, 1, 0, 1], [1, -2, 1, 0],
            [0, 1, -2, 1], [1, 0, 1, -2]]
    bi = [[-1, 0, 1, 0], [0, -1, 0, 1],
          [1, 0, -1, 0], [0, 1, 0, -1]]
    m = [[rate*(delta*mono[i][j]+chi*bi[i][j])
          for j in range(4)] for i in range(4)]
    a = [2*(k+c), 2*k, 2*(k-c), 2*k]
    psi = [F(0), 2*c, F(0), -2*c]
    q = [[(2*a[i] if i==j else F(0))-m[i][j]
          for j in range(4)] for i in range(4)]
    return m, a, psi, q


def solve(mat, rhs):
    a = [list(row)+[rhs[i]] for i, row in enumerate(mat)]
    n = len(a)
    for i in range(n):
        pivot = next((j for j in range(i,n) if a[j][i]), None)
        assert pivot is not None
        a[i], a[pivot] = a[pivot], a[i]
        mult = a[i][i]
        a[i] = [v/mult for v in a[i]]
        for j in range(n):
            if j==i: continue
            mult = a[j][i]
            a[j] = [a[j][r]-mult*a[i][r] for r in range(n+1)]
    return [row[-1] for row in a]


def determinant(mat):
    a = [list(row) for row in mat]
    n = len(a)
    prod = F(1)
    for i in range(n):
        pivot = next((j for j in range(i,n) if a[j][i]), None)
        if pivot is None: return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            prod = -prod
        p = a[i][i]; prod *= p
        for j in range(i+1,n):
            mult = a[j][i]/p
            for r in range(i,n):
                a[j][r] -= mult*a[i][r]
    return prod


def mm(a,b):
    n=len(a); p=len(b); m=len(b[0])
    return [[sum(a[i][j]*b[j][k] for j in range(p)) for k in range(m)]
            for i in range(n)]


def expmat(m,t):
    # Scaling and squaring with a conventional Taylor series; 4 by 4 only.
    n=len(m)
    a=[[float(m[i][j])*t for j in range(n)] for i in range(n)]
    norm=max(sum(abs(v) for v in row) for row in a)
    s=0
    while norm > F(1,4):
        norm /= 2.0; s += 1
    a=[[v/(2**s) for v in row] for row in a]
    eye=[[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    result=[row[:] for row in eye]
    term=[row[:] for row in eye]
    for j in range(1,65):
        term=mm(term,a)
        term=[[v/j for v in row] for row in term]
        result=[[result[i][k]+term[i][k] for k in range(n)] for i in range(n)]
    for _ in range(s): result=mm(result,result)
    return result


def assert_close(x,y,rtol=1e-10):
    assert abs(x-y)<rtol*max(1,abs(x),abs(y)), (x,y)


def check(k,rate,c,dx,chi):
    m,a,psi,q=matrices(k,rate,c,chi)
    delta=1-chi
    num=(k+rate*delta)*(2*k+rate)-2*c*c
    den=k*(k+rate*delta)*(2*k+rate)-c*c*(2*k+rate*delta)
    assert den>0, (k,rate,c,chi)
    g=solve(q,[dx]*4)
    h=dx*num/(4*den)
    assert g[1]==g[3]==h
    assert min(g)>0
    assert determinant(q)==64*(2*k+rate)*den
    assert [sum(m[i][j]*psi[j] for j in range(4)) for i in range(4)]==[-2*rate*v for v in psi]
    assert all(a[i]*psi[i]==2*k*psi[i] for i in range(4))
    dactive=c*c*h/(k+rate)
    vv0=2*c*c*h
    for t in [F(1,7),F(2,3),F(3,2)]:
        mat=[[m[i][j] - (a[i] if i==j else 0) for j in range(4)] for i in range(4)]
        e=expmat(mat,float(t))
        z=[float(psi[j]*g[j]) for j in range(4)]
        exact_dot=sum(float(psi[i])*sum(e[i][j]*z[j] for j in range(4)) for i in range(4))/4
        formula=float(vv0)*exp(-2*float(k+rate)*float(t))
        assert_close(exact_dot,formula,1e-9)
        # independently integrate the single exponential covariance
        tt=float(t); R=2*float(k+rate)
        msd=float(dx)*tt+2*float(vv0)*(tt/R+(exp(-R*tt)-1)/(R*R))
        closed=float(dx)*tt+2*float(c*c*h/(k+rate))*tt-float(c*c*h/(k+rate)**2)*(1-exp(-R*tt))
        assert_close(msd,closed)
    assert dactive>0
    return h,dactive


def main():
    # Stable low-coupling regimes, including the unsynchronized endpoint chi=0.
    for chi in [F(0),F(1,5),F(1,2),F(9,10),F(99,100)]:
        for c in [F(1,5),F(1),F(11,10)]:
            check(F(1),F(2),c,F(3,2),chi)
    # Nonmonotone amplitude response and stabilization for strong fluctuations.
    h1,_=check(F(1),F(2),F(3,2),F(1),F(0))
    h2,_=check(F(1),F(2),F(3,2),F(1),F(1,2))
    assert h1 < h2
    # At the exceptional amplitude k=1, lambda=6, c=2, h=Dx/(2k).
    for chi in [F(0),F(1,2),F(99,100)]:
        h,_=check(F(1),F(6),F(2),F(1),chi)
        assert h==F(1,2)
    # Exact threshold with k=1, lambda=2, c=3/2: delta_crit=1/7.
    k,rate,c=F(1),F(2),F(3,2)
    assert (2*k*c*c-k*k*(2*k+rate))/(rate*(k*(2*k+rate)-c*c))==F(1,7)
    print('PASS: rational 4-state moments/determinants, covariance eigenmode, finite-lag semigroup,')
    print('      exact MSD, stable strong-coupling branch, critical flat law, boundary value.')

if __name__=='__main__': main()
